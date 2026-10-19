#!/usr/bin/env python3
"""Check a flow_strokes clip: loop seam, motion outside the water, frame strip.
  wcheck.py WORKDIR MASK.png x0,y0,x1,y1 OUT.png   (box in art coordinates)"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage as nd
d, maskp, box, outp = sys.argv[1:5]
W, H = 1024, 1792
margin = round(W * 0.020); border = max(2, round(W * 0.008)); bh = round(H * 0.085)
il = it = margin + border; ir = W - margin - border; ib = H - margin - border; bt = ib - bh
fr = [np.array(Image.open(f"{d}/f{i:04d}.png")).astype(float)[it:bt, il:ir] for i in range(96)]
# interior = art resized to (ir-il) wide (cover) -> map mask the same way
iw, ih = ir - il, ib - it
s = max(iw / W, ih / H)
mm = Image.open(maskp).convert("L").resize((max(1, round(W * s)), max(1, round(H * s))))
left, top = (mm.width - iw) // 2, (mm.height - ih) // 2
m = np.array(mm.crop((left, top, left + iw, top + ih)))[:bt - it] > 128
out = ~nd.binary_dilation(m, iterations=6)
steps = [np.abs(fr[(i + 1) % 96] - fr[i]).mean() for i in range(96)]
print("seam 95->0 %.3f  typical %.3f" % (steps[95], np.mean(steps[:95])))
mx = max(np.abs(fr[i][out] - fr[0][out]).max() for i in range(0, 96, 8))
print("max change outside the water (dilated 6 px):", round(mx, 1))
x0, y0, x1, y1 = [int(v) for v in box.split(",")]
x0, x1 = [max(0, round(v * s) - left) for v in (x0, x1)]; y0, y1 = [max(0, round(v * s) - top) for v in (y0, y1)]
tiles = [Image.fromarray(fr[i][y0:y1, x0:x1].astype(np.uint8)) for i in (0, 8, 16)]
sh = Image.new("RGB", (tiles[0].width, 3 * tiles[0].height + 20), "white")
for j, t in enumerate(tiles):
    sh.paste(t, (0, j * (t.height + 10)))
sh.save(outp)
