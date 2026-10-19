#!/usr/bin/env python3
"""Animate lights on a card in code: twinkling stars, a pulsing light, a glow travelling along a light.

  glow.py --art ../batch/the-oracle/art.png --title "The Oracle" --out oracle_twinkle_v1 --twinkle 260,20,770,800
  glow.py --art ../batch/the-root/art.png --title "The Root" --out root_glow_v1 --light root_gold.png \
          --travel-from 512,950 --wavelength 300

Lights never move. --twinkle finds stars in a box (bright specks on a dark sky, or with --twinkle-dark dark
specks on a light ground), cuts them out, fills the sky behind, and redraws each star every frame with its
own rhythm: size, brightness, a soft halo, and four thin rays at its peaks. --light takes a mask of a light
(beams, glowing roots): with --pulse the whole light brightens and dims; with --travel-from or
--travel-down bright bands run outward along it. Both add a soft outer glow. Every rhythm runs whole
cycles per clip, so the loop is seamless.
"""
import argparse, os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage as nd

SKILL = os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../../skills/tarot-card-generator/scripts"))
sys.path.insert(0, SKILL)
from frame_card import cover_resize  # noqa: E402
from animate_compose import FRAME_FLAGS  # noqa: E402


def rhythm(rng, T, slow, fast):
    """Irregular wave in [-1, 1] that repeats exactly every T frames."""
    t = np.arange(T) / T
    w = (0.65 * np.sin(2 * np.pi * rng.choice(slow) * t + rng.uniform(0, 6.3))
         + 0.35 * np.sin(2 * np.pi * rng.choice(fast) * t + rng.uniform(0, 6.3)))
    return w / np.abs(w).max()


def find_stars(px, box, dark, min_px, contrast, sky_max=255.0):
    """Star components inside box: specks that differ from the local background by `contrast`."""
    x0, y0, x1, y1 = box
    lum = px[y0:y1, x0:x1].mean(-1)
    bgl = nd.median_filter(lum, 25)
    spot = (bgl - lum > contrast) if dark else (lum - bgl > contrast)
    lab, n = nd.label(nd.binary_closing(spot, iterations=1))
    out = []
    for i, sl in enumerate(nd.find_objects(lab)):
        m = lab[sl] == i + 1
        if m.sum() < min_px or max(m.shape) > 60:
            continue
        if min(sl[0].start + y0, sl[1].start + x0) < 6 or sl[0].stop + y0 > px.shape[0] - 6 or sl[1].stop + x0 > px.shape[1] - 6:
            continue                                                    # too close to the edge (under the frame)
        ys, xs = np.nonzero(m)
        if bgl[int(ys.mean()) + sl[0].start, int(xs.mean()) + sl[1].start] > sky_max:
            continue                                                    # not on the sky (e.g. a curtain)
        out.append(dict(y0=sl[0].start + y0, x0=sl[1].start + x0, m=m,
                        cy=ys.mean() + sl[0].start + y0, cx=xs.mean() + sl[1].start + x0,
                        r=np.sqrt(m.sum() / np.pi)))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--art", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--frames", type=int, default=96)
    ap.add_argument("--fps", type=float, default=24)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--base-frames", help="dir of f0000.png... (unframed art, already animated) used as each "
                                         "frame's background instead of the static art; star holes refilled per frame")
    # stars
    ap.add_argument("--twinkle", action="append", default=[], help="x0,y0,x1,y1 box to find stars in (repeatable)")
    ap.add_argument("--twinkle-dark", action="store_true", help="stars are dark specks on a light ground")
    ap.add_argument("--star-colour", default="255,250,225", help="colour of halo and rays")
    ap.add_argument("--star-min", type=int, default=3, help="smallest star in pixels")
    ap.add_argument("--twinkle-count", type=int, default=0, help="only the N largest stars twinkle (0 = all)")
    ap.add_argument("--flash", type=float, default=0, help="each star flashes once per clip; width as a fraction "
                    "of the clip (e.g. 0.06), flashes spread evenly; 0 = continuous twinkle")
    ap.add_argument("--twinkle-zone", help="mask PNG: keep only stars whose centre lies in it")
    ap.add_argument("--star-mask", help="mask PNG whose white blobs are the stars (e.g. gold flecks picked by "
                                        "colour), added to any --twinkle stars")
    ap.add_argument("--contrast", type=float, default=60)
    ap.add_argument("--sky-max", type=float, default=255, help="only stars whose local background is darker than this")
    ap.add_argument("--halo", type=float, default=0.9, help="halo strength at a star's peak")
    ap.add_argument("--rays", type=float, default=4.0, help="ray length per px of star radius at its peak")
    ap.add_argument("--ray-max", type=float, default=45, help="longest ray in px")
    ap.add_argument("--grow", type=float, default=0.3, help="star size change (fraction)")
    # light area
    ap.add_argument("--light", help="mask PNG of a light (white = light)")
    ap.add_argument("--tint", default="255,246,205", help="colour the light brightens towards")
    ap.add_argument("--pulse", type=int, default=0, help="whole-light pulses per clip")
    ap.add_argument("--travel-from", help="x,y: bright bands run outward from this point")
    ap.add_argument("--travel-down", action="store_true", help="bright bands run down the card")
    ap.add_argument("--wavelength", type=float, default=300, help="px between travelling bands")
    ap.add_argument("--cycles", type=int, default=2, help="bands passing a point per clip")
    ap.add_argument("--bright", type=float, default=0.55, help="how far the light moves towards --tint at a peak")
    ap.add_argument("--dim", type=float, default=0.3, help="how much the light darkens in a trough")
    ap.add_argument("--dim-mult", help="r,g,b multipliers in a trough (overrides --dim), e.g. 0.82,0.66,0.45 = deeper amber")
    ap.add_argument("--fade-to", help="r,g,b: in a trough the light fades towards this colour by --dim (e.g. the sky)")
    ap.add_argument("--light-also", help="mask PNG of a second light that brightens with the bands but never fades")
    ap.add_argument("--outer", type=float, default=0.35, help="strength of the soft glow outside the light")
    ap.add_argument("--outer-size", type=float, default=14, help="blur radius of the outer glow in px")
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)
    T = a.frames

    art = Image.open(a.art).convert("RGB")
    W, H = art.size
    px = np.array(art).astype(float)
    bg = px.copy()

    stars = []
    for b in a.twinkle:
        stars += find_stars(px, [int(v) for v in b.split(",")], a.twinkle_dark, a.star_min, a.contrast, a.sky_max)
    if a.twinkle_zone:
        zone = np.array(Image.open(a.twinkle_zone).convert("L")) > 128
        stars = [s for s in stars if zone[int(round(s["cy"])), int(round(s["cx"]))]]
    if a.star_mask:
        sm = np.array(Image.open(a.star_mask).convert("L")) > 128
        lab, _ = nd.label(sm)
        for i, sl in enumerate(nd.find_objects(lab)):
            m = lab[sl] == i + 1
            ys, xs = np.nonzero(m)
            stars.append(dict(y0=sl[0].start, x0=sl[1].start, m=m, cy=ys.mean() + sl[0].start,
                              cx=xs.mean() + sl[1].start, r=np.sqrt(m.sum() / np.pi)))
    if a.twinkle_count:                                                 # only the largest stars twinkle;
        stars = sorted(stars, key=lambda s: -s["r"])[:a.twinkle_count]  # the rest stay as drawn
    scol = np.array([float(v) for v in a.star_colour.split(",")])
    for s in stars:
        m = np.pad(s["m"], 3); y0, x0 = s["y0"] - 3, s["x0"] - 3
        hole = nd.binary_dilation(m, iterations=2)
        h, w = m.shape
        ring = nd.binary_dilation(hole, iterations=3) & ~hole
        reg = px[y0:y0 + h, x0:x0 + w]
        sky = np.median(reg[ring], 0)
        bg[y0:y0 + h, x0:x0 + w][hole] = sky
        alpha = nd.gaussian_filter(nd.binary_dilation(m, iterations=1).astype(float), 0.6)
        s.update(hole=hole, ring=ring, y0=y0, x0=x0, sprite=Image.fromarray(np.dstack([reg, alpha * 255]).astype(np.uint8), "RGBA"),
                 k=rhythm(rng, T, (2, 3, 4), (5, 7, 9)))
    if a.flash and stars:                                               # one brief flash per star per clip,
        starts = rng.permutation(len(stars)) / len(stars)               # spread evenly so few peak at once
        tt = np.arange(T) / T
        for s, t0 in zip(stars, starts):
            dt = (tt - t0 + 0.5) % 1 - 0.5
            s["k"] = np.exp(-(dt / a.flash) ** 2)
    if stars:
        print(len(stars), "stars found")

    light = None
    if a.light:
        light = nd.gaussian_filter((np.array(Image.open(a.light).convert("L")) > 128).astype(float), 1.2)
        Y, X = np.mgrid[0:H, 0:W].astype(float)
        if a.travel_from:
            fx, fy = [float(v) for v in a.travel_from.split(",")]
            dist = np.hypot(X - fx, Y - fy)
        elif a.travel_down:
            dist = Y
        else:
            dist = None
        tint = np.array([float(v) for v in a.tint.split(",")])
        fade = np.array([float(v) for v in a.fade_to.split(",")]) if a.fade_to else None
        also = nd.gaussian_filter((np.array(Image.open(a.light_also).convert("L")) > 128).astype(float), 1.2) \
            if a.light_also else None
        dmul = np.array([float(v) for v in a.dim_mult.split(",")]) if a.dim_mult else np.full(3, 1 - a.dim)

    work = tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(a.out)) or ".")
    static = os.path.join(work, "static.png")
    subprocess.run([sys.executable, f"{SKILL}/frame_card.py", "--art", a.art, "--title", a.title, "--out", static,
                    *FRAME_FLAGS], check=True)
    card = Image.open(static).convert("RGB")
    margin = round(W * 0.020); border = max(2, round(W * 0.008)); banner_h = round(H * 0.085)
    il, it, ir, ib = margin + border, margin + border, W - margin - border, H - margin - border
    banner_top = ib - banner_h

    SS = 3
    for f in range(T):
        t = f / T
        if a.base_frames:                                                       # animated background: fill each
            out = np.array(Image.open(os.path.join(a.base_frames, f"f{f:04d}.png")).convert("RGB")).astype(float)
            for s in stars:                                                     # star hole from this frame's ring
                h, w = s["hole"].shape
                reg = out[s["y0"]:s["y0"] + h, s["x0"]:s["x0"] + w]
                reg[s["hole"]] = np.median(reg[s["ring"]], 0)
        else:
            out = bg.copy()
        if light is not None:
            if dist is not None:
                band = (0.5 + 0.5 * np.cos(2 * np.pi * (dist / a.wavelength - a.cycles * t))) ** 2
            else:
                band = np.full((H, W), 0.5 + 0.5 * np.cos(2 * np.pi * a.pulse * t))
            lb = (light * band)[..., None]
            trough = (light[..., None] - lb)                                    # light that is between bands
            if fade is not None:                                                # troughs fade into the sky
                out = out + (fade - out) * trough * a.dim
            else:
                out = out * (1 - trough * (1 - dmul))
            out = out + (tint - out) * a.bright * lb
            if also is not None:                                                # e.g. a lamp: brightens only
                out = out + (tint - out) * a.bright * (also * band)[..., None]
            g = nd.gaussian_filter((light if also is None else np.maximum(light, also)) * band, a.outer_size)[..., None] * a.outer
            out = 255 - (255 - out) * (1 - g * tint / 255)                      # screen-blend the outer glow
        frame = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))
        if stars:
            arr = np.array(frame).astype(float)
            for s in stars:                                                     # halo first (numpy)
                k = max(0.0, s["k"][f])
                sig = min(18.0, max(4.0, 2.2 * s["r"]))
                R = int(3 * sig)                                                # window wide enough: no square edge
                cy, cx = int(round(s["cy"])), int(round(s["cx"]))
                ys, xs = slice(max(0, cy - R), cy + R + 1), slice(max(0, cx - R), cx + R + 1)
                yy, xx = np.mgrid[ys, xs]
                g = (a.halo * k ** 1.5 * np.exp(-((yy - s["cy"]) ** 2 + (xx - s["cx"]) ** 2) / (2 * sig ** 2)))[..., None]
                arr[ys, xs] = 255 - (255 - arr[ys, xs]) * (1 - g * scol / 255)
            frame = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
            for s in stars:                                                     # the star itself, resized
                k = s["k"][f]
                sc = 1 + a.grow * k
                sp = s["sprite"]
                nw, nh = max(1, round(sp.width * sc)), max(1, round(sp.height * sc))
                spr = sp.resize((nw, nh), Image.LANCZOS)
                lift = max(0.0, k) * 0.5
                rgb = np.array(spr)[..., :3].astype(float)
                rgb = rgb + (scol - rgb) * lift
                spr = Image.fromarray(np.dstack([rgb, np.array(spr)[..., 3]]).astype(np.uint8), "RGBA")
                frame.paste(spr, (round(s["cx"] - nw / 2), round(s["cy"] - nh / 2)), spr)
            lay = Image.new("RGBA", (W * SS, H * SS), (0, 0, 0, 0))
            d = ImageDraw.Draw(lay)
            for s in stars:                                                     # rays at the peaks
                k = max(0.0, s["k"][f])
                L = min(a.rays * max(1.2, s["r"]), a.ray_max) * k ** 2 * SS
                if L < 2 * SS:
                    continue
                cx, cy, wd = s["cx"] * SS, s["cy"] * SS, max(1.0, 0.35 * s["r"]) * SS
                al = int(255 * min(1.0, 1.3 * k))
                for ux, uy in ((1, 0), (0, 1)):
                    d.polygon([(cx - ux * L, cy - uy * L), (cx - uy * wd, cy + ux * wd), (cx + ux * L, cy + uy * L),
                               (cx + uy * wd, cy - ux * wd)], fill=tuple(int(v) for v in scol) + (al,))
            lay = lay.resize((W, H), Image.LANCZOS)
            frame.paste(lay, (0, 0), lay)
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
