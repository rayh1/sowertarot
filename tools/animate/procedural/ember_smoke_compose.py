#!/usr/bin/env python3
"""Compose The Ember's AI-route clip so the smoke passes in front of the window instead of being cut off.

Wan is given the crop box with the window painted out (ember_smoke_v3_input.py), so it draws its smoke on plain
black; with the window in its input it moved and faded the stone, and its moved stone could not be told from
smoke by colour. Per frame:
  1. inside the mask (ember_smoke_v3.png: the painted smoke and the dark air round it) Wan's pixels, as
     animate_compose.py does, so no painted smoke stays still;
  2. elsewhere in the crop box (figure, bowl and ember excluded) Wan's smoke laid over the card as a see-through
     layer: on its black background a Wan pixel's brightness is the smoke itself, so it is added to the card,
     which shows through by one minus the smoke's opacity (brightness above black / 170). The smoke so passes
     in front of the card's own pillar, sill and view.
Options as animate_compose.py, without --start and --pingpong (--crop required); run through with-comfy, from the
card's batch folder:
  python3 ember_smoke_compose.py --frames-prefix ember_v4_s6 --count 121 --fps 24 --art art.png --mask mask.png
      --title "The Ember" --out the-ember_s6_v5 --slow 2 --crossfade 0.5 --crop 360,620,760,1331
"""
import argparse, os, subprocess, sys, tempfile

import numpy as np
from PIL import Image
from scipy import ndimage

sys.path.insert(0, "/workspace/sowertarot/skills/tarot-card-generator/scripts")
from animate_compose import FRAME_FLAGS, SKILL, cover_resize, fetch, interpolate  # noqa: E402


def overlay_region(art, box):
    """Where Wan's smoke may lie over the card: the crop box above the floor minus the figure, soft at the edges."""
    a = np.asarray(art).astype(int); H, W, _ = a.shape
    x0, y0, x1, y1 = box
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    figure = np.zeros((H, W), bool)
    figure[600:1300, 300:560] = ((r > 140) & (r - b > 60) & (g > 60))[600:1300, 300:560]            # robe
    figure[1080:1240, 380:530] |= ((a.mean(2) > 170) & (np.abs(r - b) < 50))[1080:1240, 380:530]   # hand
    figure = ndimage.binary_dilation(ndimage.binary_fill_holes(ndimage.binary_closing(figure, iterations=3)), iterations=35)
    reg = np.zeros((H, W)); reg[y0:y1, x0:x1] = 1
    yy, xx = np.mgrid[0:H, 0:W]
    edge = np.minimum.reduce([xx - x0, x1 - 1 - xx, yy - y0, y1 - 1 - yy]).astype(float)
    reg *= np.clip(edge / 40, 0, 1)
    reg[figure] = 0
    reg[1150:] = 0                       # Wan's input still holds the floor tiles and bowl; the mask covers the smoke there
    return ndimage.gaussian_filter(reg, 6)


def main():
    ap = argparse.ArgumentParser()
    for k in ("--frames-prefix", "--art", "--mask", "--title", "--out", "--crop"):
        ap.add_argument(k, required=True)
    ap.add_argument("--count", type=int, required=True)
    ap.add_argument("--fps", type=float, required=True)
    ap.add_argument("--crossfade", type=float, default=0.0)
    ap.add_argument("--slow", type=float, default=1.0)
    a = ap.parse_args()

    art = Image.open(a.art).convert("RGB"); W, H = art.size
    C = np.asarray(art).astype(float)
    M = np.asarray(Image.open(a.mask).convert("L")).astype(float)[..., None] / 255
    box = [int(v) for v in a.crop.split(",")]
    R = overlay_region(art, box)
    raw = [fetch(f"{a.frames_prefix}_{1 + i:05d}_.png") for i in range(a.count)]
    if a.slow > 1:
        raw = interpolate(raw, a.fps, a.slow)

    def compose(f):
        full = art.copy(); full.paste(f.resize((box[2] - box[0], box[3] - box[1]), Image.LANCZOS), box[:2])
        F = np.asarray(full).astype(float)
        al = np.clip((F.mean(2) - 18) / 170, 0, 1)[..., None]               # smoke opacity on Wan's black
        over = np.clip(C * (1 - al) + np.clip(F - 8, 0, None), 0, 255)       # the smoke laid over the card
        Rm = R[..., None] * (1 - M)
        return Image.fromarray((F * M + over * Rm + C * (1 - M - Rm)).round().astype(np.uint8))

    frames = [compose(f) for f in raw]
    if a.crossfade > 0:
        n, N = round(a.crossfade * a.fps), len(frames)
        frames = [Image.blend(frames[N - n + i], frames[i], (i + 1) / (n + 1)) if i < n else frames[i] for i in range(N - n)]
    else:
        frames = frames[:-1]
    work = tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(a.out)) or ".")
    static = os.path.join(work, "static.png")
    subprocess.run([sys.executable, f"{SKILL}/frame_card.py", "--art", a.art, "--title", a.title, "--out", static, *FRAME_FLAGS], check=True)
    card = Image.open(static).convert("RGB")
    margin = round(W * 0.020); border = max(2, round(W * 0.008)); banner_h = round(H * 0.085)
    il, it, ir, ib = margin + border, margin + border, W - margin - border, H - margin - border
    for i, f in enumerate(frames):
        interior = cover_resize(f, ir - il, ib - it).crop((0, 0, ir - il, ib - banner_h - it))
        out = card.copy(); out.paste(interior, (il, it)); out.save(os.path.join(work, f"f{i:04d}.png"))
    pat = os.path.join(work, "f%04d.png")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", pat, "-c:v", "libx264",
                    "-pix_fmt", "yuv420p", "-crf", "16", "-movflags", "+faststart", a.out + ".mp4"], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", pat, "-vf", "scale=512:-1",
                    "-c:v", "libwebp", "-loop", "0", "-quality", "85", a.out + ".webp"], check=True)
    print(a.out + ".mp4", len(frames), "frames; work dir", work)


if __name__ == "__main__":
    main()
