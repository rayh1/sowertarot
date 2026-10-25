#!/usr/bin/env python3
"""Mask for The Ember clip v3 (AI route): the painted smoke and the dark air above it (white = moves).

The painted smoke (ember_smoke_drawn.png) widened 35 px, since the smoke drifts sideways, plus the dark air
above its top (x 400-580), fading out upward and to both sides so rising wisps dissolve; the robe and the open hand cut out by their
colours with a 35 px margin (Wan shifts the robe), the sill with 14 px; over the floor tiles (below
y 1150) only the smoke itself plus 12 px, since Wan darkens the tiles; nothing below the ember's top
(y 1272), so the coal stays the card's own. Blurred 10 px, then faded to nothing over the 20-70 px
before the window's stone pillar, so wisps dissolve instead of ending on a line.
  python3 ember_smoke_v3_mask.py ../batch/the-ember/art.png ember_smoke_drawn.png ember_smoke_v3.png
"""
import sys

import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

art, drawn, out = sys.argv[1:4]
a = np.asarray(Image.open(art).convert("RGB")).astype(int)
H, W, _ = a.shape
smoke = np.asarray(Image.open(drawn).convert("L")) > 127
yy, xx = np.ogrid[-35:36, -35:36]
mask = ndimage.binary_dilation(smoke, structure=xx**2 + yy**2 <= 35**2)
side = np.clip(np.minimum(np.arange(W) - 400, 580 - np.arange(W)) / 50, 0, 1)   # soft sides, no straight edge
air = np.zeros((H, W)); air[640:790] = np.linspace(0, 1, 150)[:, None] * side    # dark air above the smoke's top
r, g, b = a[..., 0], a[..., 1], a[..., 2]
robe = (r > 140) & (r - b > 60) & (g > 60)                       # orange habit
hand = (a.mean(2) > 170) & (np.abs(r - b) < 50)                  # pale hand; the smoke is pale too
figure = np.zeros((H, W), bool)
figure[600:1300, 300:560] = robe[600:1300, 300:560]
figure[1080:1240, 380:530] |= hand[1080:1240, 380:530]
figure = ndimage.binary_fill_holes(ndimage.binary_closing(figure, iterations=3))
mask &= ~ndimage.binary_dilation(figure, iterations=35)
lab, _ = ndimage.label(a.mean(2) > 140)
stone = np.zeros((H, W), bool)
for (y, x), grow in (((750, 640), 30), ((915, 700), 14)):         # window pillar (smoke fades before it), sill
    part = lab == lab[y, x]
    part[:600] = part[1000:] = False; part[:, :540] = part[:, 800:] = False
    part = ndimage.binary_dilation(ndimage.binary_fill_holes(ndimage.binary_closing(part, iterations=4)), iterations=grow)
    stone |= part
mask &= ~stone
floor = ndimage.binary_dilation(smoke, iterations=12)                # over the floor tiles only the smoke itself
mask[1150:] &= floor[1150:]
mask[1272:] = False
m = np.maximum(mask * 255.0, air * 255 * ~(ndimage.binary_dilation(figure, iterations=35) | stone))
m = np.asarray(Image.fromarray(m.astype(np.uint8)).filter(ImageFilter.GaussianBlur(10))).astype(float)
pillar = lab == lab[750, 640]; pillar[:600] = pillar[1000:] = False; pillar[:, :540] = pillar[:, 800:] = False
d = ndimage.distance_transform_edt(~ndimage.binary_fill_holes(ndimage.binary_closing(pillar, iterations=4)))
m *= np.clip((d - 20) / 50, 0, 1)                                 # wisps dissolve toward the pillar, no cut edge
Image.fromarray(m.astype(np.uint8)).save(out)
