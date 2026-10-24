"""Mask for The Oracle clip v2 (2026-10-24): the crystal orb in her hands, cut from the card's own art.
Orb = the near-white pixels (all channels > 200) in a box round the orb, the group linked to the brightest
centre, holes filled so the inked hatching inside pulses with it; the pale hands stay out (they are cream,
B well below R). Run in tools/animate/procedural; writes oracle_orb_v2.png."""
import numpy as np
from PIL import Image
from scipy import ndimage as nd

A = np.asarray(Image.open("../batch/the-oracle/art.png").convert("RGB"), float)
R, G, B = A[..., 0], A[..., 1], A[..., 2]
reg = np.zeros(R.shape, bool); reg[1100:1320, 420:640] = True          # round the orb
white = (R > 200) & (G > 200) & (B > 200) & (B > R - 25) & reg
lab, n = nd.label(nd.binary_dilation(white, iterations=2))
big = np.argmax(nd.sum(np.ones_like(lab), lab, range(1, n + 1))) + 1
g = nd.binary_fill_holes(nd.binary_closing(lab == big, iterations=3)) & reg
Image.fromarray((g * 255).astype(np.uint8)).save("oracle_orb_v2.png")
ys, xs = np.nonzero(g); print("orb box", xs.min(), ys.min(), xs.max(), ys.max(), "px", g.sum())
