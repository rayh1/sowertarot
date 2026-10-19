#!/usr/bin/env python3
"""Paste Wan output frames into a card inside a mask, frame it, write MP4 + WebP.

  animate_compose.py --frames-prefix <ComfyUI output prefix> --count N --fps F --art forge_art.png
             --mask forge_mask.png --title "The Forge" --out forge_14b [--crossfade 0.5] [--crop x0,y0,x1,y1]

Outside the mask every frame is the original art, so linework stays exact. The frame and title
banner are rendered once (frame_card.py) and reused, so the paper texture does not flicker.
--crossfade S blends the last S seconds into the first for start-image-only models.
--slow N plays the clip N times slower by inserting motion-interpolated frames (ffmpeg minterpolate).
--pingpong loops by playing the clip forward then backward instead of a crossfade.
--crop: the model was given only this box of the art (art pixels); its frames are pasted back there.
"""
import argparse, http.client, io, os, subprocess, sys, tempfile, time, urllib.request
from PIL import Image

SKILL = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SKILL)
from frame_card import cover_resize  # noqa: E402

HOST = os.environ.get("COMFY_LOCAL_URL", "http://127.0.0.1:8188").rstrip("/")  # set by with-comfy
FRAME_FLAGS = ["--paper", "216,199,158", "--ink", "26,22,18", "--margin-frac", "0.020",
               "--border-frac", "0.008", "--banner-frac", "0.085"]


def fetch(name, tries=5):
    for t in range(tries):
        try:
            return Image.open(io.BytesIO(urllib.request.urlopen(f"{HOST}/view?filename={name}&type=output", timeout=60).read())).convert("RGB")
        except (OSError, http.client.HTTPException):
            if t == tries - 1:
                raise
            time.sleep(2 * (t + 1))


def interpolate(frames, fps, slow):
    """Motion-interpolate to fps*slow frames per second; played back at fps that is `slow` times slower."""
    d = tempfile.mkdtemp()
    for i, f in enumerate(frames):
        f.save(os.path.join(d, f"r{i:04d}.png"))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(fps), "-i", os.path.join(d, "r%04d.png"),
                    "-vf", f"minterpolate=fps={fps * slow}:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1",
                    os.path.join(d, "i%05d.png")], check=True)
    out = [Image.open(os.path.join(d, n)).convert("RGB") for n in sorted(os.listdir(d)) if n.startswith("i")]
    subprocess.run(["rm", "-rf", d])
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--frames-prefix", required=True)
    ap.add_argument("--count", type=int, required=True)
    ap.add_argument("--fps", type=float, required=True)
    ap.add_argument("--art", required=True)
    ap.add_argument("--mask", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--crossfade", type=float, default=0.0)
    ap.add_argument("--start", type=int, default=1, help="ComfyUI counter of the first frame")
    ap.add_argument("--slow", type=float, default=1.0, help="play N times slower via motion interpolation")
    ap.add_argument("--pingpong", action="store_true", help="loop forward+backward instead of a crossfade")
    ap.add_argument("--crop", help="x0,y0,x1,y1 in art pixels: the box the model was given")
    a = ap.parse_args()

    art = Image.open(a.art).convert("RGB")
    mask = Image.open(a.mask).convert("L")
    W, H = art.size
    if a.crop:
        x0, y0, x1, y1 = (int(v) for v in a.crop.split(","))
        def place(f):
            full = art.copy(); full.paste(f.resize((x1 - x0, y1 - y0), Image.LANCZOS), (x0, y0)); return full
    else:
        def place(f):
            return f.resize((W, H), Image.LANCZOS)
    raw = [fetch(f"{a.frames_prefix}_{a.start + i:05d}_.png") for i in range(a.count)]
    if a.slow > 1:
        raw = interpolate(raw, a.fps, a.slow)
    frames = [place(f) for f in raw]
    if a.pingpong:
        frames = frames + frames[-2:0:-1]
    # Wan's first-last-frame output repeats the start image as its final frame; drop it so the loop doesn't stutter
    if (a.crossfade == 0) and not a.pingpong and len(frames) > 1:
        frames = frames[:-1]
    if a.crossfade > 0:
        # out[i] for i < n fades from the clip's last n frames into its first n; the loop then wraps
        # from frame N-n-1 back to out[0] (mostly frame N-n), so there is no jump
        n, N = round(a.crossfade * a.fps), len(frames)
        frames = [Image.blend(frames[N - n + i], frames[i], (i + 1) / (n + 1)) if i < n else frames[i] for i in range(N - n)]
    work = tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(a.out)) or ".")
    static = os.path.join(work, "static.png")
    subprocess.run([sys.executable, f"{SKILL}/frame_card.py", "--art", a.art, "--title", a.title, "--out", static, *FRAME_FLAGS], check=True)
    card = Image.open(static).convert("RGB")
    margin = round(W * 0.020); border = max(2, round(W * 0.008)); banner_h = round(H * 0.085)
    il, it, ir, ib = margin + border, margin + border, W - margin - border, H - margin - border
    banner_top = ib - banner_h
    for i, f in enumerate(frames):
        art_i = Image.composite(f, art, mask)
        interior = cover_resize(art_i, ir - il, ib - it).crop((0, 0, ir - il, banner_top - it))
        out = card.copy(); out.paste(interior, (il, it))
        out.save(os.path.join(work, f"f{i:04d}.png"))
    pat = os.path.join(work, "f%04d.png")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", pat, "-c:v", "libx264",
                    "-pix_fmt", "yuv420p", "-crf", "16", "-movflags", "+faststart", a.out + ".mp4"], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", pat, "-vf", "scale=512:-1",
                    "-c:v", "libwebp", "-loop", "0", "-quality", "85", a.out + ".webp"], check=True)
    print(a.out + ".mp4", len(frames), "frames;", "work dir", work)


if __name__ == "__main__":
    main()
