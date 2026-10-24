#!/usr/bin/env python3
"""Two repairs that do not show as a patch, shared by edit_card.py, fill_disc.py and
render_card.py --from-note (which must replay them exactly).

tone_match  — Qwen Image 2.1 returns its whole edit a few levels lighter or darker than the
              original (measured 4–16 levels on the 2026-10-03 sun removals), so a pasted box
              shows as a rectangle on flat areas. The offset is measured on a band just inside
              the box's solid part, where the edit should equal the original (pixels the edit
              really changed are skipped), spread over the box by Laplace interpolation (so
              clouds keep their own shading) and applied in exact proportion to the paste weight.
fill_disc   — removes a sun/moon disc from a FLAT sky with no AI edit: the disc is found in the
              art itself, filled by Laplace interpolation from the sky around it (dark linework
              and very light drawn detail are walls that give no colour), plus random grain
              sampled from that sky. Deterministic: the same art and parameters give the same
              pixels.
fill_halo   — removes a light rim (halo) round dark linework on a FLAT sky with no AI edit: the
              rim is what differs from the sky next to the ink, outside the drawn shape; it is
              filled the same way. Qwen either deletes the whole figure or widens the rim (The
              Anchor's gull, 2026-10-24). Deterministic.
"""
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy import ndimage
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve


def paste_weight(size, box, feather):
    """The exact weight render_card.paste_back gives the edit at each pixel (0..1)."""
    m = Image.new("L", size, 0)
    ImageDraw.Draw(m).rectangle(tuple(box), fill=255)
    return np.asarray(m.filter(ImageFilter.GaussianBlur(feather / 2))).astype(float) / 255


def _laplace(known, unknown, values, walls=None):
    """Solve the 4-neighbour Laplace equation on `unknown` pixels; neighbours that are known
    contribute `values`, walls contribute nothing. Returns the solved (n, 3) array."""
    H, W = unknown.shape
    ys, xs = np.nonzero(unknown)
    idx = -np.ones((H, W), int); idx[ys, xs] = np.arange(len(ys))
    A = lil_matrix((len(ys), len(ys))); rhs = np.zeros((len(ys), 3))
    for k, (y, x) in enumerate(zip(ys, xs)):
        n = 0
        for yy, xx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
            j = idx[yy, xx]
            if j >= 0:
                A[k, j] = -1; n += 1
            elif walls is not None and walls[yy, xx]:
                continue
            elif known[yy, xx]:
                rhs[k] += values[yy, xx]; n += 1
        A[k, k] = max(n, 1)
    return ys, xs, spsolve(A.tocsr(), rhs)


def tone_match(orig, pasted, box, feather):
    """Return (corrected PIL image, median offset per channel). orig/pasted: PIL RGB, same size."""
    o = np.asarray(orig.convert("RGB")).astype(float)
    p = np.asarray(pasted.convert("RGB")).astype(float)
    H, W, _ = o.shape
    w = paste_weight((W, H), box, feather)
    solid = w > 0.98
    band = solid & ~ndimage.binary_erosion(solid, iterations=10)
    d = ndimage.gaussian_filter(o - p, (3, 3, 0))
    med = np.median(d[band], 0)
    ok = band & (np.abs(d - med).sum(2) < 6)       # skip where the edit really changed the picture
    if ok.sum() < 500:
        return pasted, med                          # nothing reliable to measure on: leave as pasted
    ys, xs, sol = _laplace(ok, solid & ~ok, d, walls=~solid)
    c = np.zeros_like(o); c[ok] = d[ok]; c[ys, xs] = sol
    _, (iy, ix) = ndimage.distance_transform_edt(~solid, return_indices=True)
    c = c[iy, ix]                                   # carry the edge values out into the soft edge
    out = np.clip(p + w[..., None] * c, 0, 255).astype(np.uint8)
    return Image.fromarray(out), med


def fill_disc(art, box, grow=14, thresh=18):
    """Return (filled PIL image, disc pixel count). art: PIL RGB unframed art.
    grow: pixels the disc mask is widened by (24 when a faint glow or rim remains);
    thresh: colour distance from the box-edge sky that counts as disc (raise to ~40 on a
    graded sky, where a low value catches the gradient)."""
    x0, y0, x1, y1 = box
    o = np.asarray(art.convert("RGB")).astype(float); H, W, _ = o.shape
    edge = np.concatenate([o[y0:y0 + 6, x0:x1].reshape(-1, 3), o[y1 - 6:y1, x0:x1].reshape(-1, 3),
                           o[y0:y1, x0:x0 + 6].reshape(-1, 3), o[y0:y1, x1 - 6:x1].reshape(-1, 3)])
    sky = np.median(edge, 0)
    box_m = np.zeros((H, W), bool); box_m[y0:y1, x0:x1] = True
    lum = o.mean(2)
    dark = lum < 90
    dl, dn = ndimage.label(dark)
    if dn:                                          # stipple dots are not linework
        dark = np.isin(dl, 1 + np.nonzero(ndimage.sum(dark, dl, range(1, dn + 1)) >= 40)[0])
    ink = ndimage.binary_dilation(dark, iterations=2) & box_m
    holes, nh = ndimage.label(ndimage.binary_fill_holes(ink) & ~ink)   # what linework encloses (gull bodies)
    if nh:
        hs = ndimage.sum(np.ones_like(holes), holes, range(1, nh + 1))
        ink |= np.isin(holes, 1 + np.nonzero(hs < 3000)[0])
    so = ndimage.gaussian_filter(o, (3, 3, 0))      # grain-free, so a soft glow counts too
    disc = (np.abs(so - sky).sum(2) > thresh) & box_m & ~ink
    lab, n = ndimage.label(disc)
    if not n:
        raise SystemExit("fill_disc: no disc found in the box")
    sizes = ndimage.sum(disc, lab, range(1, n + 1))
    disc = np.isin(lab, 1 + np.nonzero(sizes >= 150)[0])   # every disc piece (a gull may split it)
    disc = ndimage.binary_fill_holes(disc)
    disc = ndimage.binary_dilation(disc, iterations=grow) & ~ink & box_m
    halo = ndimage.binary_dilation(disc, iterations=25) & ~disc & ~ink & box_m
    speck = halo & (np.abs(o - ndimage.median_filter(o, size=(9, 9, 1))).sum(2) > 45)
    disc |= ndimage.binary_dilation(speck, iterations=3) & ~ink
    near = ndimage.binary_dilation(disc, iterations=12)
    ring = ndimage.binary_dilation(disc, iterations=55) & ~near & ~ink & box_m
    ring &= np.abs(so - sky).sum(2) < thresh
    ys, xs = np.nonzero(ring)
    if len(xs) < 1500:
        raise SystemExit(f"fill_disc: only {len(xs)} sky pixels around the disc; widen the box")
    grain = o - ndimage.gaussian_filter(o, (2, 2, 0))
    ink = ink | (ndimage.binary_dilation(lum > sky.mean() + 40, iterations=2) & ~disc & box_m)  # detail much lighter than the sky (frosted twigs) is a wall too
    skym = (~ink & ~disc).astype(float)
    num = ndimage.gaussian_filter(ndimage.median_filter(o, size=(5, 5, 1)) * skym[..., None], (4, 4, 0))
    base = num / np.maximum(ndimage.gaussian_filter(skym, 4)[..., None], 1e-6)
    dy, dx, sol = _laplace(~disc, disc, base, walls=ink)
    rng = np.random.default_rng(0)
    g = grain[ys, xs]; g = g[(np.abs(g) < 3 * g.std(0) + 1).all(1)]
    pick = g[rng.integers(0, len(g), len(dx))] * (grain[ys, xs].std(0) / g.std(0))
    out = o.copy(); out[dy, dx] = sol + pick
    m = ndimage.gaussian_filter(disc.astype(float), 1.5)[..., None]   # soften the seam
    res = np.clip(o * (1 - m) + out * m, 0, 255).astype(np.uint8)
    return Image.fromarray(res), int(disc.sum())


def fill_halo(art, box, grow=2):
    """Return (filled PIL image, rim pixel count). art: PIL RGB unframed art.
    grow: pixels the rim mask is widened by (2 cleared The Anchor's gull)."""
    x0, y0, x1, y1 = box
    o = np.asarray(art.convert("RGB")).astype(float)
    c = o[y0:y1, x0:x1]
    ink = c.mean(2) < 90
    lab, _ = ndimage.label(~ink)                    # outside = not enclosed by the linework
    border = set(np.unique(np.r_[lab[0], lab[-1], lab[:, 0], lab[:, -1]])) - {0}
    outside = np.isin(lab, list(border))
    sky = outside & ~ndimage.binary_dilation(ink, iterations=10)
    if sky.sum() < 1500:
        raise SystemExit(f"fill_halo: only {int(sky.sum())} sky pixels in the box; widen it")
    dev = np.abs(c - np.median(c[sky], 0)).sum(2)
    rim = outside & ndimage.binary_dilation(ink, iterations=8) & (dev > 14)
    rim = ndimage.binary_dilation(rim, iterations=grow) & outside & ~ink
    if not rim.any():
        raise SystemExit("fill_halo: no rim found in the box")
    ys, xs, sol = _laplace(sky | (outside & ~rim), rim, c, walls=ink)
    grain = c[sky] - ndimage.gaussian_filter(c, (4, 4, 0))[sky]
    rng = np.random.default_rng(0)
    res = c.copy(); res[ys, xs] = sol + grain[rng.integers(0, len(grain), len(ys))]
    out = o.copy(); out[y0:y1, x0:x1] = res
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)), int(rim.sum())
