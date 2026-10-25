"""Score composed Ember clips: motion (check.py's d4: mean pixel change between frames 4 apart inside the mask), median and
largest frame step, loop jump (last frame to first), share of near-white pixels, and painted-smoke stillness (the
share of the card's pale painted-smoke pixels that never leave the card's colour). Writes a frame sheet per clip.
  python3 ember_clip_score.py <art.png> <mask.png> <smoke_drawn.png> <sheet dir> <clip.mp4> ...
"""
import subprocess, sys, os
import numpy as np
from PIL import Image, ImageDraw
sys.path.insert(0, '/workspace/sowertarot/skills/tarot-card-generator/scripts')
from animate_compose import cover_resize

W, H = 1024, 1792
art, mask, drawn, sheets, clips = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5:]
margin = round(W * 0.020); border = max(2, round(W * 0.008)); bh = round(H * 0.085)
il, it, ir, ib = margin + border, margin + border, W - margin - border, H - margin - border; bt = ib - bh


def place(img, mode):
    full = Image.new(mode, (W, H), 0); full.paste(cover_resize(img, ir - il, ib - it).crop((0, 0, ir - il, bt - it)), (il, it)); return full


reg = np.array(place(Image.open(mask).convert('L'), 'L')) > 128
smoke = np.array(place(Image.open(drawn).convert('L'), 'L')) > 127
orig = np.array(place(Image.open(art).convert('RGB'), 'RGB')).astype(np.int16)
smoke &= orig.mean(-1) > 90                                              # the pale strokes, not the dark border
ys, xs = np.nonzero(reg); y0, y1, x0, x1 = ys.min() - 20, ys.max() + 40, xs.min() - 20, xs.max() + 20
for p in clips:
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
    c = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3); f = c.astype(np.int16); n = len(f)
    d4 = np.abs(f[4:] - f[:-4]).mean(-1)[:, reg].mean()
    d1 = np.abs(f[1:] - f[:-1]).mean(-1)[:, reg].mean(1)
    jump = np.abs(f[0] - f[-1]).mean(-1)[reg].mean()
    white = (c.min(-1) > 240)[:, reg].mean(1).max()
    sm = np.abs(f[0] - f[n // 2]).mean(-1)[smoke].mean()                 # painted smoke, first vs middle frame
    still = (np.abs(f - orig).mean(-1)[:, smoke].max(0) < 12).mean()     # painted-smoke pixels that never leave the card
    print(f'{os.path.basename(p)}: frames {n}, motion {d4:.1f}, step median {np.median(d1):.2f} max {d1.max():.2f}, '
          f'jump {jump:.2f}, white max {white:.3f}, smoke first-vs-mid {sm:.1f}, smoke never changes {still:.1%}')
    idx = [0, n // 4, n // 2, 3 * n // 4, n - 1]
    tw = x1 - x0; th = y1 - y0
    sh = Image.new('RGB', ((tw + 10) * (len(idx) + 1), th + 20), 'white'); d = ImageDraw.Draw(sh)
    sh.paste(Image.fromarray(orig[y0:y1, x0:x1].astype(np.uint8)), (0, 20)); d.text((3, 3), 'CARD', fill='black')
    for k, i in enumerate(idx, 1):
        sh.paste(Image.fromarray(c[i, y0:y1, x0:x1]), (k * (tw + 10), 20)); d.text((k * (tw + 10) + 3, 3), f'f{i}', fill='black')
    sh.save(os.path.join(sheets, os.path.basename(p).replace('.mp4', '_sheet.png')))
