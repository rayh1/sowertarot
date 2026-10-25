#!/usr/bin/env python3
"""Make the stream pouring from The Tide's bowl flow, on top of an already composed clip.

The AI-route clip (animate_compose.py) keeps the stream still: it is cut out of the sea mask, because Wan was given
the art with the woman, bowl and stream painted out. Here soft light dashes run down the stream's white strands
(--mode light), or short see-through gaps of sea colour, which show better on the near-white strands (--mode gap):
each 3 px column of the stream gets its own phase, a dash changes only the light pixels (the ink lines stay), and
the dashes fade in below the bowl's rim and out above the splash. --wobble sways the strands sideways in ripples
that run down the stream at the dashes' speed. They move --cycles periods per clip, so the clip
still loops exactly.
Input is the composed clip's frames (the f%04d.png files left in animate_compose.py's work folder); the stream is
drawn in clip-art pixels (art.png) and mapped into the card as animate_compose.py maps its frames. From the card's
batch folder:
  python3 ../../procedural/tide_stream_flow.py --frames-dir tmp2ebwqqjf --art art.png --title "The Tide"
      --out the-tide_s2_v8 --fps 24
"""
import argparse, glob, os, subprocess, sys, tempfile

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy import ndimage

sys.path.insert(0, "/workspace/sowertarot/skills/tarot-card-generator/scripts")
from animate_compose import cover_resize  # noqa: E402

# the stream below the bowl's front rim, in clip-art pixels (tools/animate/batch/the-tide/art.png)
STREAM = [(628, 885), (668, 875), (671, 900), (671, 1078), (640, 1078), (637, 1000), (632, 940), (628, 905)]
TOP, BOTTOM = 880, 1078


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--frames-dir", required=True)
    ap.add_argument("--art", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--fps", type=int, default=24)
    ap.add_argument("--period", type=float, default=60, help="px between dashes along a strand")
    ap.add_argument("--cycles", type=int, default=8, help="periods the dashes move per clip (whole: loop-exact)")
    ap.add_argument("--mode", choices=["light", "gap"], default="gap")
    ap.add_argument("--amp", type=float, default=0.45, help="dash strength: share of the way to white (light) or to --sea (gap)")
    ap.add_argument("--sea", default="110,136,118", help="RGB a gap fades towards")
    ap.add_argument("--wobble", type=float, default=0, help="sideways sway of the strands in px")
    ap.add_argument("--wobble-period", type=float, default=0, help="px between sway ripples (default: --period)")
    ap.add_argument("--dash", type=float, default=0.14, help="dash length as a share of the period")
    a = ap.parse_args()

    art = Image.open(a.art).convert("RGB")
    W, H = art.size
    m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).polygon(STREAM, fill=255)
    m = np.asarray(m.filter(ImageFilter.GaussianBlur(1.2))) / 255.0
    ys = np.arange(H)[:, None].astype(float)
    xs = np.arange(W)[None, :]
    fade = np.clip((ys - TOP) / 18, 0, 1) * np.clip((BOTTOM - ys) / 12, 0, 1)
    rng = np.random.default_rng(3)
    phase = rng.random(W // 3 + 1)[xs // 3]
    A = np.asarray(art).astype(float)
    light = np.clip((A.mean(2) - 90) / 140, 0, 1)  # ink lines and dark gaps stay as drawn
    weight = (m * fade * light)[..., None]

    # animate_compose.py's placement of the art inside the frame
    margin = round(W * 0.020); border = max(2, round(W * 0.008)); banner_h = round(H * 0.085)
    il, it, ir, ib = margin + border, margin + border, W - margin - border, H - margin - border
    banner_top = ib - banner_h

    def place(img):
        return cover_resize(img, ir - il, ib - it).crop((0, 0, ir - il, banner_top - it))

    pm = place(Image.fromarray((m * fade * 255).astype("uint8")))
    frames = sorted(glob.glob(os.path.join(a.frames_dir, "f[0-9][0-9][0-9][0-9].png")))
    N = len(frames)
    work = tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(a.out)) or ".")
    for i, f in enumerate(frames):
        shift = a.cycles * a.period * i / N
        p = ((ys - shift) / a.period + phase) % 1.0
        d = np.exp(-((p - 0.5) / a.dash) ** 2)[..., None]
        T = 255.0 if a.mode == "light" else np.array([float(v) for v in a.sea.split(",")])
        S = A + (T - A) * a.amp * d * weight
        if a.wobble:
            wp = a.wobble_period or a.period
            dx = a.wobble * np.sin(2 * np.pi * (ys[:, 0] - shift) / wp) * fade[:, 0]
            moved = np.stack([ndimage.map_coordinates(S[..., c], [np.broadcast_to(ys, (H, W)),
                              xs + dx[:, None] + 0 * ys], order=1, mode="nearest") for c in range(3)], -1)
            S = S + (moved - S) * m[..., None]
        layer = place(Image.fromarray(np.clip(S, 0, 255).astype("uint8")))
        out = Image.open(f).convert("RGB")
        interior = out.crop((il, it, ir, banner_top))
        out.paste(Image.composite(layer, interior, pm), (il, it))
        out.save(os.path.join(work, f"f{i:04d}.png"))
    pat = os.path.join(work, "f%04d.png")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", pat, "-c:v", "libx264",
                    "-pix_fmt", "yuv420p", "-crf", "16", "-movflags", "+faststart", a.out + ".mp4"], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", pat, "-vf", "scale=512:-1",
                    "-c:v", "libwebp", "-loop", "0", "-quality", "85", a.out + ".webp"], check=True)
    print(f"{a.out}.mp4 {N} frames; work dir {work}")


if __name__ == "__main__":
    main()
