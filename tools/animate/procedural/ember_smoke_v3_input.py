#!/usr/bin/env python3
"""Wan input for The Ember clip: the 9:16 crop box with the window (stone pillar, sill and the view) painted over
in the dark wall colour, so Wan draws its smoke on plain black and has no stone to redraw. With the window in its
input, Wan moved and faded the pillar and sill, and its moved stone could not be told from smoke by colour.
ember_smoke_compose.py lays the smoke back over the card's own window.
  python3 ember_smoke_v3_input.py ../batch/the-ember/art.png ember_smoke_drawn.png ../batch/the-ember/input_576x1024_nowindow.png
"""
import sys

import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

BOX = (360, 620, 760, 1331)                                       # crop.txt
art, drawn, out = sys.argv[1:4]
a = Image.open(art).convert("RGB")
W, H = a.size
smoke = ndimage.binary_dilation(np.asarray(Image.open(drawn).convert("L")) > 127, iterations=4)
window = np.zeros((H, W), bool)
window[600:966, 548:] = True                                      # pillar, sill and view, right of the smoke
window &= ~smoke
m = Image.fromarray((window * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(3))
wall = Image.new("RGB", (W, H), (4, 9, 10))                       # the dark wall left of the pillar
Image.composite(wall, a, m).crop(BOX).resize((576, 1024), Image.LANCZOS).save(out)
