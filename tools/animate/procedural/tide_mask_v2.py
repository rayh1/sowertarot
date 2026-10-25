"""The Tide clip v2 mask: all the sea and surf, the woman, bowl and stream cut out tightly.

Sea = teal water plus the foam it encloses, found on the figure-free copy (nowoman_art.png).
Woman = her blue dress (B > G) and her hair and skin (R > G) on art.png, in the box Qwen cleared;
bowl, stream and the lit neck are white like the foam, so they are hand-drawn polygons.
Run from tools/animate/batch/the-tide/ (art.png = the repaired art trimmed as frame_card.py does, nowoman_art.png =
the same with the woman removed by Qwen); writes mask.png and a pink preview.png:
  python3 ../../procedural/tide_mask_v2.py
"""
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy import ndimage as nd

art = np.asarray(Image.open('art.png').convert('RGB')).astype(int)
nw = np.asarray(Image.open('nowoman_art.png').convert('RGB')).astype(int)
H, W = art.shape[:2]
yy = np.arange(H)[:, None]


def close(m, k):
    # pad with the edge first: scipy treats the outside as empty and would trim the sea at the card edge
    p = np.pad(m, k, mode='edge')
    return nd.binary_closing(p, structure=np.ones((k, k)))[k:-k, k:-k]


R, G, B = nw[..., 0], nw[..., 1], nw[..., 2]
sea = (G - R > 12) & (yy > 630)
sea = nd.binary_fill_holes(close(sea, 21))
lab, k = nd.label(sea)
sizes = nd.sum(sea, lab, range(1, k + 1))
sea = np.isin(lab, 1 + np.where(sizes > 20000)[0])
# the white surf on the wet sand: grow the sea into foam-white pixels (sand is far warmer, R - B ~ 88)
foam = (nw.sum(2) > 540) & (R - B < 55) & (yy > 630)
sea = nd.binary_dilation(sea, iterations=40, mask=sea | foam)
sea = nd.binary_fill_holes(close(sea, 7))

R, G, B = art[..., 0], art[..., 1], art[..., 2]
near = np.zeros_like(sea)
near[520:1480, 230:740] = True  # the box Qwen cleared, in clip-art pixels
fig = ((B - G > 6) | (R - G > 15)) & near
fig = nd.binary_opening(fig, structure=np.ones((3, 3)))
fig = nd.binary_fill_holes(nd.binary_closing(fig, structure=np.ones((9, 9))))
lab, k = nd.label(fig)
sizes = nd.sum(fig, lab, range(1, k + 1))
fig = lab == 1 + np.argmax(sizes)
poly = Image.new('L', (W, H), 0)
ImageDraw.Draw(poly).polygon([(548, 822), (600, 812), (650, 822), (684, 845), (682, 868), (668, 895),
                              (664, 960), (662, 1040), (660, 1088), (636, 1088), (637, 1000), (636, 940),
                              (612, 900), (570, 880), (548, 850)], fill=255)
# her neck and arms: the lit skin has the colour of the foam
ImageDraw.Draw(poly).polygon([(418, 640), (484, 640), (482, 652), (476, 663), (452, 668), (456, 705), (455, 735), (420, 740)], fill=255)
ImageDraw.Draw(poly).polygon([(400, 795), (440, 798), (500, 812), (545, 820), (560, 840), (580, 850),
                              (590, 870), (560, 875), (500, 875), (430, 872), (400, 860)], fill=255)
fig |= np.asarray(poly) > 0
fig = nd.binary_dilation(fig, iterations=3)

hard = np.pad(((sea & ~fig) * 255).astype('uint8'), 8, mode='edge')
m = Image.fromarray(hard).filter(ImageFilter.GaussianBlur(2)).crop((8, 8, W + 8, H + 8))
m.save('mask.png')
p = art.astype(float)
w = np.asarray(m)[..., None] / 255
p = p * (1 - 0.55 * w) + np.array([255, 0, 200]) * 0.55 * w
Image.fromarray(p.astype('uint8')).save('preview.png')
