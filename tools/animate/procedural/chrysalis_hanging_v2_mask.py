#!/usr/bin/env python3
"""Mask for The Chrysalis clip v2: the silk thread and the chrysalis that hangs from it (white = swings).

Cut from the art itself: dark ink below the branch, plus everything far from the cream sky below y 560,
kept only where connected to the chrysalis, holes filled, widened 4 px.
  python3 chrysalis_hanging_v2_mask.py ../batch/the-chrysalis/art.png chrysalis_hanging_v2.png
"""
import sys

import numpy as np
from PIL import Image
from scipy import ndimage

art, out = sys.argv[1:3]
a = np.asarray(Image.open(art).convert("RGB")).astype(float)
H, W, _ = a.shape
region = np.zeros((H, W), bool)
region[392:1100, 560:800] = True                                  # below the pivot (662,388), round the thread
sky = np.median(a[700:1000, 740:800].reshape(-1, 3), 0)          # plain cream sky right of the chrysalis
far = np.abs(a - sky).sum(2) > 45
cand = region & ((a.mean(2) < 110) | (far & (np.arange(H)[:, None] > 560)))
lab, _ = ndimage.label(cand)
mask = np.isin(lab, list({lab[800, 660], lab[450, 662]} - {0}))  # chrysalis body and thread
mask = ndimage.binary_dilation(ndimage.binary_fill_holes(mask), iterations=4)
Image.fromarray((mask * 255).astype(np.uint8)).save(out)
