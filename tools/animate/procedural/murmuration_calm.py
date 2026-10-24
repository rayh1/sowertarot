"""Calm water for The Murmuration clip (2026-10-24): the painted ink ripples on the stream are filled from the
pale water round them, so only the moving strokes of flow_strokes.py show ripples (with the painted ones left
in, the moving strokes were lost among them). Only flat little dashes (at most 7 px high, at most 250 px, wholly at least 8 px inside the mask) are
filled, so the banks, their shadows and the overhanging grass stay. Run in tools/animate/procedural; reads ../batch/the-murmuration/art.png and murmuration_water.png,
writes ../batch/the-murmuration/art_calm.png."""
import numpy as np
from PIL import Image
from scipy import ndimage as nd
from flicker import diffuse_fill

A = np.asarray(Image.open("../batch/the-murmuration/art.png").convert("RGB"), float)
water = np.asarray(Image.open("murmuration_water.png").convert("L")) > 128
inner = nd.binary_erosion(water, iterations=8)
ink = water & (A.mean(-1) < 170)
lab, n = nd.label(ink, structure=np.ones((3, 3)))
dash = np.zeros(n + 1, bool)                                    # flat little dashes well inside the water
for i, o in enumerate(nd.find_objects(lab), 1):
    h, w = o[0].stop - o[0].start, o[1].stop - o[1].start
    part = lab[o] == i
    dash[i] = h <= 7 and w >= h and part.sum() <= 250 and inner[o][part].all()
hole = nd.binary_dilation(dash[lab], iterations=2) & water
out = diffuse_fill(A, hole, iters=300)
Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save("../batch/the-murmuration/art_calm.png")
