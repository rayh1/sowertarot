#!/usr/bin/env python3
"""Animate thin drifting mist on a card in code: pale horizontal ribbons drift sideways inside a region.

  drifting_fog.py --art ../batch/the-threshold/art.png --title "The Threshold" --out threshold_fog_v1 \
                  --box 205,640,690,1150 --dense 900,1120

The mist is added over the art inside --box (soft edges), thickest between the --dense rows and thinning
above them. Ribbons come from smooth noise stretched sideways, cut with a soft threshold so they read as
flat bands. Two noise layers drift at different speeds and directions, so the ribbons drift and change
shape, and the whole mist slowly rises and sinks (--bob). Loop: each layer is a blend of the field at
offset v*t and at v*(t-T), so frame T equals frame 0.

--plume x,y switches to a smoke plume from a chimney instead (see plume_main); --box and --dense are
then not used.
"""
import argparse, os, subprocess, sys, tempfile
import numpy as np
from PIL import Image
from scipy import ndimage as nd

SKILL = os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../../skills/tarot-card-generator/scripts"))
sys.path.insert(0, SKILL)
from frame_card import cover_resize  # noqa: E402
from animate_compose import FRAME_FLAGS  # noqa: E402


def noise(rng, h, w, sy, sx):
    """Smooth zero-mean, unit-variance noise, periodic in x (so it can be shifted around)."""
    n = nd.gaussian_filter(rng.standard_normal((h, w)), (sy, sx), mode=("nearest", "wrap"))
    return (n - n.mean()) / n.std()


def drifted(n, shift):
    """n shifted right by a fractional number of px, wrapping around."""
    i = int(np.floor(shift)); fr = shift - i
    return (1 - fr) * np.roll(n, i, 1) + fr * np.roll(n, i + 1, 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--art", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--box", help="x0,y0,x1,y1 where mist may appear (fog mode; required unless --plume)")
    ap.add_argument("--dense", help="y0,y1: rows where the mist is thickest (fog mode; required unless --plume)")
    ap.add_argument("--frames", type=int, default=96)
    ap.add_argument("--fps", type=float, default=24)
    ap.add_argument("--speed", type=float, default=3.0, help="px per frame of the main wisps")
    ap.add_argument("--length", type=float, default=26, help="wisp length scale in px (short wisps show their drift)")
    ap.add_argument("--bob", type=float, default=8, help="px the mist rises and sinks, once per clip")
    ap.add_argument("--opacity", type=float, default=0.55, help="opacity of the thickest mist")
    ap.add_argument("--cover", type=float, default=0.45, help="share of the region covered by ribbons (0-1)")
    ap.add_argument("--colour", default="226,234,222")
    ap.add_argument("--feather", type=float, default=30, help="soft edge of the box in px")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--plume", help="x,y: smoke plume mode - wisps leave this point (a chimney) and drift on the wind")
    ap.add_argument("--wind", default="3.0,0.5", help="plume: px per frame the wisps travel (x,y)")
    ap.add_argument("--puffs", type=int, default=36, help="plume: wisps alive at any time")
    ap.add_argument("--grow", default="10,46", help="plume: wisp radius in px at birth and at the end of its life")
    ap.add_argument("--wave", type=float, default=14, help="plume: px the plume waves sideways at its far end")
    ap.add_argument("--plume-colour", default="214,218,212")
    ap.add_argument("--ribbon", type=float, default=0,
                    help="plume: draw one smooth ribbon this many px tall instead of wisps (incense-style smoke); "
                         "its bends travel upward, whole cycles per clip")
    ap.add_argument("--ribbon-strands", type=int, default=2, choices=(2, 3),
                    help="plume ribbon: 2 = main strand + one peeling off; 3 adds a third strand on the other side")
    ap.add_argument("--ribbon-fade", type=float, default=0.55, help="plume ribbon: height fraction where it starts to fade")
    ap.add_argument("--ribbon-spread", type=float, default=12, help="plume ribbon: px the side strands drift away")
    ap.add_argument("--ribbon-width", default="5,16", help="plume ribbon: width in px at the source and at the top")
    ap.add_argument("--plume-clear", help="plume: mask (white) of drawn smoke to paint out first, so only the moving plume shows")
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)
    T = a.frames
    if a.plume:
        return plume_main(a, rng, T)
    if not (a.box and a.dense):
        ap.error("--box and --dense are required unless --plume is given")

    art = Image.open(a.art).convert("RGB")
    W, H = art.size
    px = np.array(art).astype(float)
    x0, y0, x1, y1 = [int(v) for v in a.box.split(",")]
    d0, d1 = [int(v) for v in a.dense.split(",")]
    colour = np.array([float(v) for v in a.colour.split(",")])
    h = y1 - y0

    # where the mist may be, and how thick: soft box times a vertical profile
    box = np.zeros((H, W)); box[y0:y1, x0:x1] = 1
    box = nd.gaussian_filter(box, a.feather / 2)[y0:y1]
    rows = np.arange(y0, y1)
    prof = np.where(rows < d0, np.clip(1 - (d0 - rows) / max(1, d0 - y0), 0, 1) ** 1.5 * 0.85 + 0.15,
                    np.where(rows > d1, np.clip(1 - (rows - d1) / max(1, y1 - d1), 0, 1), 1.0))
    weight = box * prof[:, None]

    # two wisp layers: larger ones drifting left, finer ones drifting right
    PAD = int(a.bob) + 4                                                # spare rows for the up-and-down roll
    layers = [(noise(rng, h + 2 * PAD, W, 6, a.length), -a.speed),
              (noise(rng, h + 2 * PAD, W, 4, a.length * 0.6), a.speed * 0.6)]
    thr = np.quantile(layers[0][0], 1 - a.cover)

    work = tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(a.out)) or ".")
    static = os.path.join(work, "static.png")
    subprocess.run([sys.executable, f"{SKILL}/frame_card.py", "--art", a.art, "--title", a.title, "--out", static,
                    *FRAME_FLAGS], check=True)
    card = Image.open(static).convert("RGB")
    margin = round(W * 0.020); border = max(2, round(W * 0.008)); banner_h = round(H * 0.085)
    il, it, ir, ib = margin + border, margin + border, W - margin - border, H - margin - border
    banner_top = ib - banner_h

    for f in range(T):
        u = f / T
        c1, c2 = np.cos(np.pi / 2 * u), np.sin(np.pi / 2 * u)        # keeps the noise variance constant
        field = 0
        for n, v in layers:
            fld = c1 * drifted(n, v * f) + c2 * drifted(n, v * (f - T))
            field = field + (0.75 if v < 0 else 0.45) * fld
        field /= np.hypot(0.75, 0.45)
        dy = PAD + a.bob * np.sin(2 * np.pi * u); i = int(dy); fr = dy - i
        field = (1 - fr) * field[i:i + h] + fr * field[i + 1:i + 1 + h]
        mist = np.clip((field - thr) / 0.6, 0, 1) ** 0.8                # soft-edged flat bands
        al = (mist * weight * a.opacity)[..., None]
        out = px.copy()
        out[y0:y1] = out[y0:y1] * (1 - al) + colour * al
        frame = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))
        interior = cover_resize(frame, ir - il, ib - it).crop((0, 0, ir - il, banner_top - it))
        o = card.copy(); o.paste(interior, (il, it))
        o.save(os.path.join(work, f"f{f:04d}.png"))
    pat = os.path.join(work, "f%04d.png")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", pat, "-c:v", "libx264",
                    "-pix_fmt", "yuv420p", "-crf", "16", "-movflags", "+faststart", a.out + ".mp4"], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", pat, "-vf", "scale=512:-1",
                    "-c:v", "libwebp", "-loop", "0", "-quality", "85", a.out + ".webp"], check=True)
    print(a.out + ".mp4", T, "frames; work dir", work)


def plume_main(a, rng, T):
    """Smoke plume: textured wisps are born at --plume, travel with --wind, grow, wave sideways and fade.
    Each wisp lives exactly one clip and they are evenly staggered, so the plume is continuous and loops."""
    art = Image.open(a.art).convert("RGB")
    W, H = art.size
    px = np.array(art).astype(float)
    if a.plume_clear:                                                   # paint out the drawn smoke
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from flicker import diffuse_fill
        px = diffuse_fill(px, np.array(Image.open(a.plume_clear).convert("L")) > 128)
    ex, ey = [float(v) for v in a.plume.split(",")]
    vx, vy = [float(v) for v in a.wind.split(",")]
    r0, r1 = [float(v) for v in a.grow.split(",")]
    colour = np.array([float(v) for v in a.plume_colour.split(",")])
    sp = np.hypot(vx, vy); nx_, ny_ = -vy / sp, vx / sp                    # sideways to the wind

    # a few wisp sprites: soft round envelope times smooth noise, cut with a soft threshold (flat wisps)
    S = 96
    yy, xx = np.mgrid[0:S, 0:S] / (S - 1) * 2 - 1
    env = np.clip(1 - (xx ** 2 + yy ** 2), 0, 1) ** 1.2
    sprites = []
    for _ in range(6):
        n = nd.gaussian_filter(rng.standard_normal((S, S)), 7, mode="wrap"); n = (n - n.mean()) / n.std()
        sprites.append(np.clip((env * (1 + 0.6 * n) - 0.35) / 0.25, 0, 1))
    puffs = [dict(ph=(k + rng.uniform(-0.3, 0.3)) * T / a.puffs, spr=int(rng.integers(6)),
                  jit=rng.normal(0, 3, 2), k=rng.uniform(0.8, 1.2)) for k in range(a.puffs)]

    work = tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(a.out)) or ".")
    static = os.path.join(work, "static.png")
    subprocess.run([sys.executable, f"{SKILL}/frame_card.py", "--art", a.art, "--title", a.title, "--out", static,
                    *FRAME_FLAGS], check=True)
    card = Image.open(static).convert("RGB")
    margin = round(W * 0.020); border = max(2, round(W * 0.008)); banner_h = round(H * 0.085)
    il, it, ir, ib = margin + border, margin + border, W - margin - border, H - margin - border
    banner_top = ib - banner_h

    for f in range(T):
        if a.ribbon:
            alpha = ribbon_alpha(a, W, H, ex, ey, vx, vy, f, T)
            puffs_now = []
        else:
            alpha = np.zeros((H, W)); puffs_now = puffs
        for p in puffs_now:
            age = ((f + p["ph"]) % T) / T                                     # 0 at the chimney, 1 at the end
            dist = age * T
            wave = a.wave * age * np.sin(2 * np.pi * (2 * f / T - 1.5 * age))   # travelling sideways wave
            cx = ex + vx * dist + nx_ * wave + p["jit"][0] * age
            cy = ey + vy * dist + ny_ * wave + p["jit"][1] * age
            r = (r0 + (r1 - r0) * age) * p["k"]
            op = min(1.0, age / 0.06) * (1 - max(0.0, (age - 0.45) / 0.55)) ** 1.3
            if op <= 0:
                continue
            size = max(4, int(round(2 * r)))
            spr = np.array(Image.fromarray((sprites[p["spr"]] * 255).astype(np.uint8)).resize((size, size),
                                                                                              Image.BILINEAR)) / 255.0
            xa, ya = int(round(cx - size / 2)), int(round(cy - size / 2))
            xs0, ys0 = max(0, xa), max(0, ya); xs1, ys1 = min(W, xa + size), min(H, ya + size)
            if xs1 <= xs0 or ys1 <= ys0:
                continue
            sub = spr[ys0 - ya:ys1 - ya, xs0 - xa:xs1 - xa] * op
            reg = alpha[ys0:ys1, xs0:xs1]
            alpha[ys0:ys1, xs0:xs1] = 1 - (1 - reg) * (1 - sub)               # wisps add up like layers of gauze
        al = (alpha * a.opacity)[..., None]
        out = px * (1 - al) + colour * al
        frame = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))
        interior = cover_resize(frame, ir - il, ib - it).crop((0, 0, ir - il, banner_top - it))
        o = card.copy(); o.paste(interior, (il, it))
        o.save(os.path.join(work, f"f{f:04d}.png"))
    pat = os.path.join(work, "f%04d.png")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", pat, "-c:v", "libx264",
                    "-pix_fmt", "yuv420p", "-crf", "16", "-movflags", "+faststart", a.out + ".mp4"], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", pat, "-vf", "scale=512:-1",
                    "-c:v", "libwebp", "-loop", "0", "-quality", "85", a.out + ".webp"], check=True)
    print(a.out + ".mp4", T, "frames; work dir", work)


def ribbon_alpha(a, W, H, ex, ey, vx, vy, f, T):
    """Alpha of a smooth smoke ribbon rising from (ex, ey): it leans with the wind, its sideways bends travel
    upward (2 and 3 cycles per clip, so frame T = frame 0), it widens and fades towards the top, and a thin
    second strand peels off it halfway up."""
    from PIL import ImageDraw
    SS = 3
    L = a.ribbon
    w0, w1 = [float(v) for v in a.ribbon_width.split(",")]
    lean = vx / max(abs(vy), 1e-6)                                   # px sideways per px up
    t = f / T
    img = Image.new("L", (W * SS, H * SS), 0)
    d = ImageDraw.Draw(img)
    strands = [(0.0, 1.0, 0.0, 1.0, 1), (0.35, 0.45, 1.7, 0.6, 1)]     # (start s, width factor, phase, opacity, side)
    if a.ribbon_strands == 3:
        strands.append((0.2, 0.6, 3.6, 0.7, -1))
    for s0, wf, ph, opf, side in strands:
        s = np.linspace(s0, 1, 400)
        amp = a.wave * s ** 0.9 + (a.ribbon_spread * side * (s - s0) if s0 else 0)
        x = (ex + lean * L * s + amp * (0.7 * np.sin(2 * np.pi * (1.6 * s - 2 * t) + ph)
                                       + 0.3 * np.sin(2 * np.pi * (3.1 * s - 3 * t) + 0.8 + ph)))
        y = ey - L * s
        w = (w0 + (w1 - w0) * s) * wf
        op = np.clip((s - s0) / 0.05, 0, 1) * np.clip(1 - (s - a.ribbon_fade) / (1 - a.ribbon_fade), 0, 1) ** 1.4 * opf
        for i in range(len(s)):
            r = w[i] / 2 * SS
            d.ellipse([x[i] * SS - r, y[i] * SS - r, x[i] * SS + r, y[i] * SS + r], fill=int(255 * op[i]))
    img = img.resize((W, H), Image.LANCZOS)
    return nd.gaussian_filter(np.array(img) / 255.0, 0.8)


if __name__ == "__main__":
    main()
