"""anchor_water_v6.png: The Anchor's water mask fitted to the repaired art (2026-10-24). The old
mask (anchor_water.png) was drawn round a re-rendered anchor with a chain looped over the sea;
the deck picture has no chain. Old mask + the sea round the anchor's top (right of the man's cuff)
+ the foam down to the shore ink line (found per column) - the real anchor, stock, ring, hand,
vine and right fluke tip (polygons in trimmed-art pixels, ~8 px margin). Binary, like the old mask.
    python3 anchor_water_v6_mask.py anchor_water.png anchor_water_v6.png ../batch/the-anchor/art.png"""
import sys
import numpy as np
from PIL import Image, ImageDraw
oldmask, out, art = sys.argv[1:4]
m = Image.open(oldmask).convert('L').point(lambda v: 255 if v > 128 else 0)
ImageDraw.Draw(m).polygon([(505, 660), (830, 660), (830, 1215), (640, 1215), (560, 1100), (440, 860),
                           (430, 790), (470, 770), (505, 765)], fill=255)          # sea round the anchor's top
a = np.asarray(Image.open(art).convert('RGB')).astype(int)
mm = np.array(m)
for x in range(405, a.shape[1]):                                                   # foam down to the shore line
    col = a[1120:1280, x]; lum = col.mean(1)
    sand = (col[:, 0] > 180) & (col[:, 2] < 150) & (col[:, 0] - col[:, 2] > 50)
    for i in range(len(col) - 8):
        if lum[i] < 90 and sand[i + 4:i + 8].all():                                # ink line with sand under it
            top = np.nonzero(mm[:1120 + i, x])[0]
            if len(top) and 1120 + i - top[-1] < 60:
                mm[top[-1]:1120 + i - 1, x] = 255
            break
m = Image.fromarray(mm)
d = ImageDraw.Draw(m)
for poly in ([(490, 682), (530, 688), (575, 705), (600, 722), (622, 738), (650, 745), (675, 736),
              (705, 734), (717, 748), (720, 790), (702, 802), (665, 808), (662, 840), (658, 876),
              (692, 905), (692, 1030), (728, 1052), (737, 1130), (732, 1160), (712, 1185), (712, 1235),
              (728, 1290), (570, 1290), (590, 1235), (612, 1190), (612, 1150), (607, 1120), (598, 1088), (590, 1060), (566, 1010), (545, 962),
              (528, 935), (527, 895), (530, 860), (480, 860), (438, 856), (430, 840), (430, 798),
              (445, 786), (470, 782), (492, 758), (486, 700)],                     # hand, ring, stock, shank, vine
             [(898, 1148), (918, 1148), (955, 1205), (980, 1245), (985, 1260), (898, 1260)]):  # right fluke tip
    d.polygon(poly, fill=0)
m.save(out)
