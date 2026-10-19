#!/usr/bin/env python3
"""Animate candle flames on a card in code: each flame stretches, sways at the tip and glows.

  flicker.py --art ../batch/the-candelabra/art.png --title "The Candelabra" --out candelabra_flicker_v1 \
             --box 140,320,500,520

Flames are found by colour (bright yellow-orange) inside --box; each flame's mask is widened to take in
its ink outline and tip, cut out, and the sky behind it filled by diffusion. Every frame the flame is
redrawn from the original pixels, pinned at the wick: height pulses, the tip sways (bending grows with
height), brightness and a warm glow breathe. Each flame has its own rhythm built from whole cycles per
clip, so the loop is seamless. The art outside the flames is untouched.
"""
import argparse, os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage as nd

SKILL = os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../../skills/tarot-card-generator/scripts"))
sys.path.insert(0, SKILL)
from frame_card import cover_resize  # noqa: E402
from animate_compose import FRAME_FLAGS  # noqa: E402


def diffuse_fill(img, hole, iters=400):
    """Fill hole pixels by repeated local averaging from their surroundings (a simple inpaint)."""
    out = img.copy()
    known = ~hole
    out[hole] = 0
    for _ in range(iters):
        blur = np.stack([nd.uniform_filter(out[..., c], 5) for c in range(3)], -1)
        out[hole] = blur[hole]
    out[known] = img[known]
    return out


def rhythm(rng, T, slow, fast):
    """Irregular wave in [-1, 1] that repeats exactly every T frames."""
    t = np.arange(T) / T
    n1, n2 = rng.choice(slow), rng.choice(fast)
    w = 0.65 * np.sin(2 * np.pi * n1 * t + rng.uniform(0, 6.3)) + 0.35 * np.sin(2 * np.pi * n2 * t + rng.uniform(0, 6.3))
    return w / np.abs(w).max()


def write_clip(a, frames_fn, art, W, H):
    """Frame each unframed frame with the deck frame and write the MP4 and WebP."""
    work = tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(a.out)) or ".")
    static = os.path.join(work, "static.png")
    subprocess.run([sys.executable, f"{SKILL}/frame_card.py", "--art", a.art, "--title", a.title, "--out", static,
                    *FRAME_FLAGS], check=True)
    card = Image.open(static).convert("RGB")
    margin = round(W * 0.020); border = max(2, round(W * 0.008)); banner_h = round(H * 0.085)
    il, it, ir, ib = margin + border, margin + border, W - margin - border, H - margin - border
    banner_top = ib - banner_h
    for f in range(a.frames):
        frame = frames_fn(f)
        interior = cover_resize(frame, ir - il, ib - it).crop((0, 0, ir - il, banner_top - it))
        o = card.copy(); o.paste(interior, (il, it))
        o.save(os.path.join(work, f"f{f:04d}.png"))
    pat = os.path.join(work, "f%04d.png")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", pat, "-c:v", "libx264",
                    "-pix_fmt", "yuv420p", "-crf", "16", "-movflags", "+faststart", a.out + ".mp4"], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", pat, "-vf", "scale=512:-1",
                    "-c:v", "libwebp", "-loop", "0", "-quality", "85", a.out + ".webp"], check=True)
    print(a.out + ".mp4", a.frames, "frames; work dir", work)


def fire_main(a):
    """Fire mode: a hearth fire licks upward (a displacement field rising through the fire mask, fading to zero
    at its edge so nothing outside is pulled in), the flames breathe brighter and dimmer, a warm glow on the
    surroundings breathes with them, and sparks fly up from --spark-from. Whole cycles per clip."""
    rng = np.random.default_rng(a.seed)
    T = a.frames
    art = Image.open(a.art).convert("RGB")
    W, H = art.size
    px = np.array(art).astype(float)
    fire = np.array(Image.open(a.fire_mask).convert("L")) > 128
    flames = (np.array(Image.open(a.flames_mask).convert("L")) > 128) if a.flames_mask else fire
    ys_, xs_ = np.nonzero(fire)
    y0, y1, x0, x1 = ys_.min(), ys_.max() + 1, xs_.min(), xs_.max() + 1
    sl = (slice(y0, y1), slice(x0, x1))
    h, w = y1 - y0, x1 - x0
    # warp strength: 0 at the fire's edge, full 25 px inside
    inside = np.clip(nd.distance_transform_edt(fire)[sl] / 25, 0, 1)
    inside = inside * inside * (3 - 2 * inside)
    # rising noise: periodic vertically over a tile of height P, scrolled up rise_cycles tiles per clip
    P = h
    def tile(sy, sx):
        n = nd.gaussian_filter(rng.standard_normal((P, w)), (sy, sx), mode="wrap")
        return n / n.std()
    nx, ny = tile(14, 6), tile(18, 10)
    Y, X = np.mgrid[0:h, 0:w].astype(float)
    taper = np.clip(1 - Y / h, 0.25, 1)                      # tips (top) waver more than the base
    br = rhythm(rng, T, (3, 4), (7, 9))                      # brightness breathing
    flm = nd.gaussian_filter(flames.astype(float), 1.5)[sl][..., None]
    glow = nd.gaussian_filter(fire.astype(float), 45)
    glow = (glow / glow.max())[..., None] * (1 - nd.gaussian_filter(fire.astype(float), 3)[..., None])
    warm = np.array([255, 170, 70])

    # sparks: each repeats k times per clip on its own phase; ballistic flight up and outward, fading
    sx0, sy0 = [float(v) for v in a.spark_from.split(",")]
    amin, amax = [np.radians(float(v)) for v in a.spark_angle.split(",")]
    sparks = [dict(ang=rng.uniform(amin, amax), d=a.spark_dist * rng.uniform(0.5, 1.2), ph=rng.uniform(0, 1),
                   k=int(rng.choice((2, 3))), r=a.spark_size * rng.uniform(0.7, 1.2), ox=rng.uniform(-14, 14), oy=rng.uniform(-8, 4))
              for _ in range(a.sparks)]

    def frame(f):
        t = f / T
        shift = (a.rise_cycles * P * t)
        i = int(np.floor(shift)); fr = shift - i
        def scroll(n):                                       # pattern moves UP: sample from below
            return (1 - fr) * np.roll(n, -i, 0) + fr * np.roll(n, -i - 1, 0)
        dx = a.rise * 0.6 * scroll(nx) * inside * taper
        dy = a.rise * scroll(ny) * inside * taper
        coords = [Y + y0 + dy, X + x0 + dx]
        out = px.copy()
        out[sl] = np.stack([nd.map_coordinates(px[..., c], coords, order=1, mode="nearest") for c in range(3)], -1)
        k = br[f]
        out[sl] = out[sl] + (np.array([255, 250, 225]) - out[sl]) * flm * max(0.0, k) * 0.35 \
            + (np.array([255, 150, 30]) - out[sl]) * flm * max(0.0, -k) * 0.3      # dim towards orange, not grey
        g = glow * a.fire_glow * (0.6 + 0.4 * k)
        out = 255 - (255 - out) * (1 - g * warm / 255)
        im = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))
        if sparks:
            SS = 3
            lay = Image.new("RGBA", (W * SS, H * SS), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
            for s in sparks:
                u = (s["k"] * t + s["ph"]) % 1                   # life 0..1
                prev = max(0.0, u - 0.05)
                def at(u):
                    dist = s["d"] * u
                    return (sx0 + s["ox"] + np.cos(s["ang"]) * dist,
                            sy0 + s["oy"] + np.sin(s["ang"]) * dist + 0.45 * s["d"] * u * u)   # gravity bends it
                (xa, ya), (xb, yb) = at(prev), at(u)
                fade = min(1.0, u / 0.08) * (1 - u) ** 1.2
                al = int(255 * fade)
                col = (255, int(235 - 90 * u), int(150 - 130 * u))
                rr = s["r"] * SS
                if a.spark_outline > 0:                          # ink outline: shows on pale fire as on dark wall
                    ro = rr + a.spark_outline * SS
                    d.line([(xa * SS, ya * SS), (xb * SS, yb * SS)], fill=(26, 22, 18, al),
                           width=round(2 * ro * 0.8))
                    d.ellipse([xb * SS - ro, yb * SS - ro, xb * SS + ro, yb * SS + ro], fill=(26, 22, 18, al))
                d.line([(xa * SS, ya * SS), (xb * SS, yb * SS)], fill=col + (al,), width=round(2 * rr * 0.8))
                d.ellipse([xb * SS - rr, yb * SS - rr, xb * SS + rr, yb * SS + rr], fill=(255, 250, 220, al))
            lay = lay.resize((W, H), Image.LANCZOS)
            im.paste(lay, (0, 0), lay)
        return im

    write_clip(a, frame, art, W, H)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--art", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--box", help="x0,y0,x1,y1 to search for flames (required unless --fire-mask)")
    ap.add_argument("--frames", type=int, default=96)
    ap.add_argument("--fps", type=float, default=24)
    ap.add_argument("--stretch", type=float, default=0.10, help="height change, fraction of flame height")
    ap.add_argument("--sway", type=float, default=0.12, help="tip sideways shift, fraction of flame height")
    ap.add_argument("--glow", type=float, default=0.35, help="strength of the breathing warm glow")
    ap.add_argument("--min-size", type=int, default=150, help="smallest flame in pixels")
    ap.add_argument("--core", default="190,120,70", help="flame colour: min red, min green, min red-blue")
    ap.add_argument("--widen", type=float, default=45, help="take in outline and tip: pixels near the flame that differ "
                    "from the surroundings by this much; 0 = no widening (flame on a bright halo)")
    ap.add_argument("--glow-mask", help="mask PNG of a lit area (e.g. a doorway) that brightens and dims with the flames")
    ap.add_argument("--glow-amp", type=float, default=0.18, help="brightness change of --glow-mask (fraction)")
    ap.add_argument("--glow-soft", action="store_true", help="read --glow-mask's grey levels as light strength "
                    "(e.g. a falloff from the flame) instead of a white/black area")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--save-raw", help="also save each unframed frame (art size) as DIR/f%%04d.png (candle mode)")
    ap.add_argument("--fire-mask", help="fire mode: mask PNG of a whole fire (hearth); warps it upward instead of "
                    "redrawing single candle flames")
    ap.add_argument("--flames-mask", help="fire mode: mask PNG of the brightest flame strokes (breathe most)")
    ap.add_argument("--rise", type=float, default=7.0, help="fire mode: warp amplitude in px")
    ap.add_argument("--rise-cycles", type=int, default=4, help="fire mode: times the warp pattern rises past per clip")
    ap.add_argument("--fire-glow", type=float, default=0.25, help="fire mode: breathing glow on the surroundings")
    ap.add_argument("--sparks", type=int, default=0, help="fire mode: number of sparks")
    ap.add_argument("--spark-from", default="560,1000", help="fire mode: x,y where sparks start")
    ap.add_argument("--spark-angle", default="-110,-30", help="fire mode: launch angles in degrees (-90 = straight up)")
    ap.add_argument("--spark-size", type=float, default=2.2, help="fire mode: spark radius in px")
    ap.add_argument("--spark-outline", type=float, default=0, help="fire mode: ink outline width in px (0 = none)")
    ap.add_argument("--spark-dist", type=float, default=230, help="fire mode: typical flight distance in px")
    a = ap.parse_args()
    if a.fire_mask:
        return fire_main(a)
    if not a.box:
        ap.error("--box is required unless --fire-mask is given")
    rng = np.random.default_rng(a.seed)
    T = a.frames

    art = Image.open(a.art).convert("RGB")
    W, H = art.size
    px = np.array(art).astype(float)
    R, G, B = px[..., 0], px[..., 1], px[..., 2]
    x0, y0, x1, y1 = [int(v) for v in a.box.split(",")]
    c0, c1, c2 = [float(v) for v in a.core.split(",")]
    core = (R > c0) & (G > c1) & (R - B > c2)
    inbox = np.zeros_like(core); inbox[y0:y1, x0:x1] = True
    core &= inbox
    lab, n = nd.label(core)
    sizes = nd.sum(core, lab, range(1, n + 1))

    flames, hole = [], np.zeros_like(core)
    for i, (sl, s) in enumerate(zip(nd.find_objects(lab), sizes)):
        if s < a.min_size:
            continue
        c = nd.binary_fill_holes(lab == i + 1)
        bottom = sl[0].stop - 1                                  # the wick: the flame is pinned here
        h = bottom - sl[0].start
        # widen: everything that differs from the local sky, near the flame and above the wick
        if a.widen > 0:
            near = nd.binary_dilation(c, iterations=7)
            near[: max(0, sl[0].start - h // 4)] = False
            ring = nd.binary_dilation(near, iterations=6) & ~near
            sky = np.median(px[ring], 0)
            m = near & (np.abs(px - sky).sum(-1) > a.widen)
            m = nd.binary_fill_holes(nd.binary_closing(m | c, iterations=2))
            lab2, _ = nd.label(m)
            m = lab2 == np.bincount(lab2[c]).argmax()               # keep the part connected to the flame
            m[bottom + 1:] = False
            m = nd.binary_dilation(m, iterations=1)
            m[bottom + 1:] = False
        else:                                                    # tight: the colour core plus 2 px
            m = nd.binary_dilation(c, iterations=2)
            m[bottom + 1:] = False
        cy, cx = [v.mean() for v in np.nonzero(c)]
        flames.append(dict(mask=m, base=(cx, bottom), h=h, cy=cy,
                           st=rhythm(rng, T, (3, 4, 5), (7, 9, 11)), sw=rhythm(rng, T, (2, 3), (5, 6)),
                           br=rhythm(rng, T, (4, 5, 6), (9, 11, 13))))
        hole |= m
    print(len(flames), "flames found")

    bg = diffuse_fill(px, nd.binary_dilation(hole, iterations=1))
    Y, X = np.mgrid[0:H, 0:W].astype(float)

    work = tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(a.out)) or ".")
    static = os.path.join(work, "static.png")
    subprocess.run([sys.executable, f"{SKILL}/frame_card.py", "--art", a.art, "--title", a.title, "--out", static,
                    *FRAME_FLAGS], check=True)
    card = Image.open(static).convert("RGB")
    margin = round(W * 0.020); border = max(2, round(W * 0.008)); banner_h = round(H * 0.085)
    il, it, ir, ib = margin + border, margin + border, W - margin - border, H - margin - border
    banner_top = ib - banner_h

    soft = [nd.gaussian_filter(fl["mask"].astype(float), 0.8) for fl in flames]
    glow_base = [nd.gaussian_filter(fl["mask"].astype(float), fl["h"] * 0.45) for fl in flames]
    glow_base = [g / g.max() for g in glow_base]
    if a.glow_mask:
        gm = np.array(Image.open(a.glow_mask).convert("L")).astype(float)
        lit = (gm / 255 if a.glow_soft else nd.gaussian_filter((gm > 128).astype(float), 4))[..., None]
        breath = np.mean([fl["br"] for fl in flames], 0)                # follows the flames' brightness
    for f in range(T):
        out = bg.copy()
        if a.glow_mask:
            out = out * (1 + a.glow_amp * breath[f] * lit)
        for fl, sm, gb in zip(flames, soft, glow_base):
            bx, by = fl["base"]
            s = 1 + a.stretch * fl["st"][f]
            hgt = np.clip((by - Y) / (fl["h"] * s), 0, 1.5)      # 0 at the wick, 1 at the tip
            shift = a.sway * fl["h"] * fl["sw"][f] * hgt ** 2
            # inverse map: the output pixel (X, Y) shows the source pixel at
            sx = X - shift
            sy = by - (by - Y) / s
            ys0, ys1 = int(by - fl["h"] * 1.6), int(by + 2)
            xs0, xs1 = int(bx - fl["h"]), int(bx + fl["h"])
            ys0, xs0 = max(0, ys0), max(0, xs0)
            cs = (slice(ys0, ys1), slice(xs0, min(W, xs1)))
            coords = [sy[cs], sx[cs]]
            al = nd.map_coordinates(sm, coords, order=1)[..., None]
            col = np.stack([nd.map_coordinates(px[..., c], coords, order=1) for c in range(3)], -1)
            k = fl["br"][f]
            col = col + (np.array([255, 236, 170]) - col) * max(0.0, k) * 0.25 * (col.sum(-1, keepdims=True) > 400)
            out[cs] = out[cs] * (1 - al) + col * al
            g = (gb * a.glow * (0.55 + 0.45 * k))[..., None]
            out = out + (np.array([255, 214, 120]) - out) * g * 0.35
        frame = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))
        if a.save_raw:
            os.makedirs(a.save_raw, exist_ok=True)
            frame.save(os.path.join(a.save_raw, f"f{f:04d}.png"))
        interior = cover_resize(frame, ir - il, ib - it).crop((0, 0, ir - il, banner_top - it))
        o = card.copy(); o.paste(interior, (il, it))
        o.save(os.path.join(work, f"f{f:04d}.png"))
    pat = os.path.join(work, "f%04d.png")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", pat, "-c:v", "libx264",
                    "-pix_fmt", "yuv420p", "-crf", "16", "-movflags", "+faststart", a.out + ".mp4"], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", pat, "-vf", "scale=512:-1",
                    "-c:v", "libwebp", "-loop", "0", "-quality", "85", a.out + ".webp"], check=True)
    print(a.out + ".mp4", T, "frames; work dir", work)


if __name__ == "__main__":
    main()
