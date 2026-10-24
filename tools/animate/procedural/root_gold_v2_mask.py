"""Mask for The Root clip v2 (2026-10-24): the glowing gold roots, cut from the card's own art by colour.
Gold = saturated yellow (B < 100, R - B > 120) plus the pale core line next to it; only the group linked to
the main gold body is kept, so lit tan roots stay out. Run in tools/animate/procedural; writes root_gold_v2.png."""
import numpy as np
from PIL import Image
from scipy import ndimage as nd

A = np.asarray(Image.open("../batch/the-root/art.png").convert("RGB"), float)
R, G, B = A[..., 0], A[..., 1], A[..., 2]
reg = np.zeros(R.shape, bool); reg[880:1792, 150:900] = True          # below ground, round the gold roots
gold = (R > 170) & (G > 130) & (B < 100) & (R - B > 120) & reg
bright = (R > 235) & (G > 225) & reg                                   # the pale core line
cand = gold | (bright & nd.binary_dilation(gold, iterations=4))
lab, n = nd.label(nd.binary_dilation(cand, iterations=2), structure=np.ones((3, 3)))
big = np.argmax(nd.sum(np.ones_like(lab), lab, range(1, n + 1))) + 1
g = cand & (lab == big)
g = nd.binary_closing(g, iterations=1) | g
Image.fromarray((g * 255).astype(np.uint8)).save("root_gold_v2.png")
