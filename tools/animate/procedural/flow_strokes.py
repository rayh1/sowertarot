#!/usr/bin/env python3
"""Animate flowing water on a card in code: ripple strokes drift downstream inside a water mask.

  flow_strokes.py --art compass_art.png --water compass_water2.png --title "The Compass Rose" --out compass_flow

The art outside the strokes is untouched. Strokes drift down the river: their path is the gradient
of the distance travelled inside the mask from its top end, and they grow and speed up towards the
bottom of the card (perspective). Every stroke repeats exactly once per clip, so the loop is seamless.
"""
import argparse, os, subprocess, sys, tempfile
from collections import deque
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy import ndimage as nd

SKILL = os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../../skills/tarot-card-generator/scripts"))
sys.path.insert(0, SKILL)
from frame_card import cover_resize  # noqa: E402
from animate_compose import FRAME_FLAGS  # noqa: E402


def geodesic_from_top(mask):
    """Steps inside the mask from its topmost row (BFS, 8-connected)."""
    H, W = mask.shape
    d = np.full((H, W), -1.0)
    ys, xs = np.nonzero(mask)
    top = ys.min()
    q = deque()
    for y, x in zip(ys, xs):
        if y <= top + 2:
            d[y, x] = 0; q.append((y, x))
    while q:
        y, x = q.popleft()
        for dy, dx, c in ((1, 0, 1), (-1, 0, 1), (0, 1, 1), (0, -1, 1), (1, 1, 1.41), (1, -1, 1.41), (-1, 1, 1.41), (-1, -1, 1.41)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < H and 0 <= nx < W and mask[ny, nx] and d[ny, nx] < 0:
                d[ny, nx] = d[y, x] + c; q.append((ny, nx))
    return d


def star_twinkle(art, box, T):
    """Return f(frame) -> art with the star in box pulsing in size, brightness and glow, period T."""
    x0, y0, x1, y1 = box
    a = np.array(art).astype(float)
    sub = a[y0:y1, x0:x1]
    R, G, B = sub[..., 0], sub[..., 1], sub[..., 2]
    star = nd.binary_dilation((R > 170) & (G > 130) & (R - B > 50), iterations=2)
    # sky without the star: a plane fitted to the sky pixels of the box
    yy, xx = np.mgrid[0:y1 - y0, 0:x1 - x0]
    A = np.c_[xx[~star], yy[~star], np.ones((~star).sum())]
    sky = np.stack([(np.c_[xx.ravel(), yy.ravel(), np.ones(xx.size)] @ np.linalg.lstsq(A, sub[..., c][~star], rcond=None)[0])
                    .reshape(star.shape) for c in range(3)], -1)
    sky = np.where(star[..., None], sky, sub)
    cy, cx = [v.mean() for v in np.nonzero(star)]
    sprite = Image.fromarray(sub.astype(np.uint8))
    alpha = Image.fromarray((star * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8))
    glow_base = nd.gaussian_filter(star.astype(float), 9)
    glow_base /= glow_base.max()
    t = np.arange(T) / T
    w = 0.6 * np.sin(2 * np.pi * 2 * t) + 0.4 * np.sin(2 * np.pi * 5 * t + 1.3)   # irregular, exact period T
    w = np.sign(w) * np.abs(w) ** 0.7 / np.abs(w).max() ** 0.7

    def frame(f, base):
        k = w[f]
        sx, sy = 1 + 0.05 * k, 1 + 0.11 * k          # the long rays stretch more than the body
        nw, nh = round(sprite.width * sx), round(sprite.height * sy)
        sp = sprite.resize((nw, nh), Image.LANCZOS); al = alpha.resize((nw, nh), Image.LANCZOS)
        lift = max(0.0, k) * 0.45                     # brighten towards a pale gold at the peaks
        sp = Image.blend(sp, Image.new("RGB", sp.size, (255, 244, 200)), lift)
        canvas = Image.fromarray(sky.astype(np.uint8))
        g = (glow_base * 0.55 * max(0.0, k))[..., None]
        canvas = Image.fromarray((np.array(canvas) * (1 - g) + np.array([255, 236, 170]) * g).astype(np.uint8))
        canvas.paste(sp, (round(cx - cx * sx), round(cy - cy * sy)), al)
        out = base.copy(); out.paste(canvas, (x0, y0))
        return out
    return frame


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--art", required=True)
    ap.add_argument("--water", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--frames", type=int, default=96)
    ap.add_argument("--fps", type=float, default=24)
    ap.add_argument("--count", type=int, default=200, help="number of strokes")
    ap.add_argument("--speed", type=float, default=2.4, help="px per frame at the bottom of the river")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--dark", type=float, default=0.5, help="ripple colour = water colour x this")
    ap.add_argument("--star", help="x0,y0,x1,y1: box around a gold star on a smooth sky; makes it twinkle")
    # opt-in options (2026-10-08); the defaults reproduce the earlier behaviour exactly
    ap.add_argument("--warp", type=float, default=0, help="move the water itself: wave amplitude in px near the viewer")
    ap.add_argument("--warp-length", type=float, default=140, help="wavelength in px of the warp near the viewer")
    ap.add_argument("--warp-waves", type=int, default=3, help="wave fronts passing per clip (whole number: loop-exact)")
    ap.add_argument("--warp-slant", type=float, default=0.15, help="sideways tilt of the wave fronts")
    ap.add_argument("--shimmer", type=float, default=0, help="share of the drawn light flecks hidden at a time (0-1): flecks blink and the pattern drifts downstream")
    ap.add_argument("--shimmer-lum", type=float, default=200, help="brightness above which a water pixel counts as a light fleck")
    ap.add_argument("--shimmer-size", type=float, default=7, help="size in px of the blinking patches")
    ap.add_argument("--shimmer-speed", type=float, default=3, help="px per frame the blink pattern drifts")
    ap.add_argument("--shimmer-thin", type=int, help="only flecks thinner than about 2N px blink; solid bright areas (a moon band) stay")
    ap.add_argument("--fleck-morph", type=float, default=0, help="with --shimmer: px the light flecks stretch and shift sideways (they lengthen, break up and rejoin)")
    ap.add_argument("--fleck-morph-size", type=float, default=16, help="horizontal size in px of the stretching cells")
    ap.add_argument("--shimmer-local", type=float, help="a light fleck is a water pixel this much brighter than the water around it (instead of --shimmer-lum)")
    ap.add_argument("--shimmer-box", help="x0,y0,x1,y1: only flecks inside this box shimmer (e.g. a sun path)")
    ap.add_argument("--shimmer-depth", type=float, help="shimmer and sparkles at the far end of the water, as a share of the near end (e.g. 0.25): calmer, slower and fewer far away")
    ap.add_argument("--save-raw", help="also save each unframed frame (art size) as DIR/f%%04d.png")
    ap.add_argument("--flow-mask", help="mask that steers the flow (may bridge gaps); strokes stay on --water")
    ap.add_argument("--dir", help="dx,dy: one fixed drift direction for all strokes (sea, lake) instead of downstream")
    ap.add_argument("--orient", choices=("across", "horizontal", "along"), default="across",
                    help="stroke direction: across the current (river) or always horizontal (sea, lake)")
    ap.add_argument("--dark-rgb", help="r,g,b of the ripple strokes (default: water colour x --dark)")
    ap.add_argument("--light-frac", type=float, help="share of pale strokes (default 0.3)")
    ap.add_argument("--light", help="r,g,b of the pale strokes (default 244,242,214)")
    ap.add_argument("--stroke-scale", type=float, default=1.0, help="multiplies stroke length and width")
    ap.add_argument("--glints", type=int, default=0, help="sparkles on the water, each flashes once per clip")
    ap.add_argument("--glint-box", help="x0,y0,x1,y1: put the sparkles only here (e.g. the sun's path)")
    ap.add_argument("--glint-rgb", help="r,g,b of the sparkles (default: the pale stroke colour)")
    ap.add_argument("--glint-outline", help="r,g,b of a thin outline around each sparkle (default: none)")
    ap.add_argument("--glint-size", type=float, default=9, help="ray length in px of the sparkles near the viewer")
    ap.add_argument("--cycles", type=int, default=1, help="each stroke lives this many short lives per clip (short streams)")
    ap.add_argument("--stroke-mask", help="draw strokes only inside this mask (e.g. a falling stream); default: --water")
    ap.add_argument("--warp-mask", help="warp only inside this mask (e.g. a pool); default: --water")
    ap.add_argument("--roll", type=float, default=0, help="with --warp: waves travel shoreward by this share of the wave spacing per roll cycle (flow-map, two layers)")
    ap.add_argument("--roll-cycles", type=int, default=2, help="roll cycles per clip (whole number: loop-exact)")
    ap.add_argument("--roll-sharp", type=float, default=1.0, help="above 1: one roll layer dominates longer (less doubling)")
    ap.add_argument("--roll-jitter", type=float, default=0.5, help="share of a cycle by which the roll timing varies across the width")
    ap.add_argument("--warp-radial", help="x,y: warp wave fronts are rings spreading out from this point")
    ap.add_argument("--warp-squash", type=float, default=0.35, help="with --warp-radial: ring height / width (perspective)")
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)

    art = Image.open(a.art).convert("RGB")
    W, H = art.size
    water = np.array(Image.open(a.water).convert("L")) > 128
    smask = np.array(Image.open(a.stroke_mask).convert("L")) > 128 if a.stroke_mask else water
    inner = nd.binary_erosion(smask, iterations=3)
    flow = np.array(Image.open(a.flow_mask).convert("L")) > 128 if a.flow_mask else water
    d = geodesic_from_top(flow)
    d[d < 0] = 0
    # smooth the distance field inside the mask, then its gradient is the downstream direction
    ds = nd.gaussian_filter(d, 6) / np.maximum(nd.gaussian_filter(flow.astype(float), 6), 1e-3)
    gy, gx = np.gradient(ds)
    n = np.hypot(gx, gy) + 1e-6
    gx, gy = gx / n, gy / n
    if a.dir:
        dx_, dy_ = [float(v) for v in a.dir.split(",")]
        nn_ = np.hypot(dx_, dy_)
        gx, gy = np.full_like(gx, dx_ / nn_), np.full_like(gy, dy_ / nn_)
    ys, xs = np.nonzero(inner)
    y_top, y_bot = ys.min(), ys.max()

    def scale(y):  # perspective: far water small and slow, near water large and fast
        return 0.35 + 0.65 * np.clip((y - y_top) / (y_bot - y_top), 0, 1)

    def sample(f, x, y):
        return f[int(np.clip(round(y), 0, H - 1)), int(np.clip(round(x), 0, W - 1))]

    # each stroke: a track of T positions starting at a random water point (more strokes near the viewer)
    T = a.frames
    wts = scale(ys) ** 1.5; wts /= wts.sum()
    strokes = []
    for k in rng.choice(len(ys), a.count, p=wts):
        x, y = float(xs[k]), float(ys[k])
        tr = []
        for _ in range(T):
            tr.append((x, y, sample(gx, x, y), sample(gy, x, y)))
            s = a.speed * scale(y)
            x += s * sample(gx, x, y); y += s * sample(gy, x, y)
        dark = rng.random() < (0.7 if a.light_frac is None else 1 - a.light_frac)
        strokes.append(dict(track=tr, phase=int(rng.integers(T)), dark=dark,
                            length=rng.uniform(14, 34), width=rng.uniform(1.9, 3.2)))

    water_rgb = np.median(np.array(art)[water], 0)
    dark_rgb = tuple(int(v) for v in water_rgb * a.dark)          # ink-like ripple line in the water's hue
    light_rgb = (244, 242, 214)                                   # pale glint, as in the sunlit lake
    if a.dark_rgb:
        dark_rgb = tuple(int(v) for v in a.dark_rgb.split(","))
    if a.light:
        light_rgb = tuple(int(v) for v in a.light.split(","))
    glints = []
    if a.glints:
        grng = np.random.default_rng(a.seed + 1000)                  # own generator: strokes stay unchanged
        gm = inner.copy()
        if a.glint_box:
            bx0, by0, bx1, by1 = [int(v) for v in a.glint_box.split(",")]
            box_ = np.zeros_like(gm); box_[by0:by1, bx0:bx1] = True; gm &= box_
        gys, gxs = np.nonzero(gm)
        for k in grng.choice(len(gys), a.glints, replace=False):
            glints.append((gxs[k], gys[k], int(grng.integers(T)), grng.uniform(0.6, 1.0)))
        if a.shimmer_depth is not None:                                # fewer sparkles far away
            ty0, ty1 = gys.min(), gys.max()
            keep_p = lambda yv: a.shimmer_depth + (1 - a.shimmer_depth) * ((yv - ty0) / max(1, ty1 - ty0)) ** 0.8
            drng = np.random.default_rng(a.seed + 3000)
            glints = [g_ for g_ in glints if drng.random() < keep_p(g_[1])]
        gdur = max(6, T // 8)
        glint_rgb = tuple(int(v) for v in a.glint_rgb.split(",")) if a.glint_rgb else light_rgb
        glint_outline = tuple(int(v) for v in a.glint_outline.split(",")) if a.glint_outline else None
    clip = Image.fromarray((nd.binary_erosion(smask, iterations=2) * 255).astype(np.uint8))

    work = tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(a.out)) or ".")
    static = os.path.join(work, "static.png")
    subprocess.run([sys.executable, f"{SKILL}/frame_card.py", "--art", a.art, "--title", a.title, "--out", static,
                    *FRAME_FLAGS], check=True)
    card = Image.open(static).convert("RGB")
    margin = round(W * 0.020); border = max(2, round(W * 0.008)); banner_h = round(H * 0.085)
    il, it, ir, ib = margin + border, margin + border, W - margin - border, H - margin - border
    banner_top = ib - banner_h

    twinkle = star_twinkle(art, [int(v) for v in a.star.split(",")], T) if a.star else None
    if a.shimmer:
        # light flecks: bright pixels in the water; behind them, the water colour around them
        apx = np.array(art).astype(float)
        if a.shimmer_local is not None:
            lum_ = apx.mean(-1)
            wl_ = np.where(water, lum_, np.nan)
            num_ = nd.uniform_filter(np.nan_to_num(wl_), 31); den_ = nd.uniform_filter(water.astype(float), 31)
            local_ = num_ / np.maximum(den_, 1e-3)
            fleck = water & (lum_ > local_ + a.shimmer_local)
        else:
            fleck = water & (apx.mean(-1) > a.shimmer_lum)
        if a.shimmer_box:
            bx0_, by0_, bx1_, by1_ = [int(v) for v in a.shimmer_box.split(",")]
            bb_ = np.zeros_like(fleck); bb_[by0_:by1_, bx0_:bx1_] = True; fleck &= bb_
        fleck = nd.binary_dilation(fleck, iterations=1) & water
        core = np.zeros_like(fleck)
        if a.shimmer_thin:
            core = nd.binary_opening(fleck, iterations=a.shimmer_thin)
            fleck &= ~nd.binary_dilation(core, iterations=2)
        calm = water & ~fleck
        num = np.stack([nd.gaussian_filter(apx[..., c] * calm, 5) for c in range(3)], -1)
        den = nd.gaussian_filter(calm.astype(float), 5)[..., None]
        under = np.where(den > 1e-3, num / np.maximum(den, 1e-3), apx)
        fl_soft = nd.gaussian_filter(fleck.astype(float), 0.7)[..., None]
        fl_box = nd.binary_dilation(fleck, iterations=40) & nd.binary_dilation(water, iterations=2)
        srng = np.random.default_rng(a.seed + 2000)
        sh_n = nd.gaussian_filter(srng.standard_normal((H, W)), a.shimmer_size, mode=("wrap", "nearest"))
        sh_n = (sh_n - sh_n.mean()) / sh_n.std()
        sh_thr = np.quantile(sh_n, a.shimmer)
        if a.fleck_morph:
            mrng = np.random.default_rng(a.seed + 4000)
            mo_n = nd.gaussian_filter(mrng.standard_normal((H, W)), (2.5, a.fleck_morph_size), mode=("wrap", "wrap"))
            mo_n = (mo_n - mo_n.mean()) / mo_n.std()
            wsoft_all = nd.gaussian_filter(water.astype(float), 1.0)
            halo = nd.binary_dilation(fleck, iterations=3) & water            # fleck plus its soft edge
            halo &= ~nd.binary_dilation(core, iterations=6)                 # never next to a solid bright core
            calm_h = water & ~halo
            num_h = np.stack([nd.gaussian_filter(apx[..., c] * calm_h, 6) for c in range(3)], -1)
            den_h = nd.gaussian_filter(calm_h.astype(float), 6)[..., None]
            under_h = np.where(den_h > 1e-3, num_h / np.maximum(den_h, 1e-3), apx)
            halo_soft = nd.gaussian_filter(halo.astype(float), 1.0)[..., None]
            YY, XX = np.mgrid[0:H, 0:W].astype(float)
        if a.shimmer_depth is not None:
            # depth weight per row: shimmer_depth at the far (top) end of the water, 1 at the near end
            fy_ = np.nonzero(water.any(1))[0]
            tt_ = np.clip((np.arange(H) - fy_[0]) / max(1, fy_[-1] - fy_[0]), 0, 1)
            sh_g = (a.shimmer_depth + (1 - a.shimmer_depth) * tt_ ** 0.8)[:, None]

    def shimmered(img, f):
        """Hide the flecks where a downstream-drifting noise is low; loop-exact blend of two offsets."""
        u_ = f / T
        sh_ = a.shimmer_speed
        def off_n(n_, k):
            i_ = int(np.floor(k)); fr_ = k - i_
            return (1 - fr_) * np.roll(n_, i_, 0) + fr_ * np.roll(n_, i_ + 1, 0)

        def off(k):
            return off_n(sh_n, k)
        fld = np.cos(np.pi / 2 * u_) * off(sh_ * f) + np.sin(np.pi / 2 * u_) * off(sh_ * (f - T))
        vis = np.clip((fld - sh_thr) / 0.35 + 0.5, 0, 1)
        if a.shimmer_depth is not None:
            # far away the pattern drifts slower (blend with a field moving at shimmer_depth x speed)
            # and fewer flecks blink (visibility pulled toward 1)
            sl_ = sh_ * a.shimmer_depth
            slow = np.cos(np.pi / 2 * u_) * off(sl_ * f) + np.sin(np.pi / 2 * u_) * off(sl_ * (f - T))
            mix = (sh_g * fld + (1 - sh_g) * slow) / np.sqrt(sh_g ** 2 + (1 - sh_g) ** 2)
            vis = 1 - sh_g * (1 - np.clip((mix - sh_thr) / 0.35 + 0.5, 0, 1))
        vis = vis[..., None]
        px_ = np.array(img).astype(float)
        if a.fleck_morph:
            # the flecks are lifted off and redrawn through a horizontal displacement that drifts
            # downstream: where it varies along a row a fleck stretches or shrinks, pieces split and join
            mo = np.cos(np.pi / 2 * u_) * off_n(mo_n, sh_ * f) + np.sin(np.pi / 2 * u_) * off_n(mo_n, sh_ * (f - T))
            amp_ = a.fleck_morph * (sh_g if a.shimmer_depth is not None else 1.0)
            ys_, xs_ = np.nonzero(fl_box)
            y0_, y1_, x0_, x1_ = ys_.min(), ys_.max() + 1, xs_.min(), xs_.max() + 1
            dxm = amp_ * mo if np.ndim(amp_) == 0 else amp_ * mo
            cy_ = YY[y0_:y1_, x0_:x1_]; cx_ = XX[y0_:y1_, x0_:x1_] - dxm[y0_:y1_, x0_:x1_]
            fm = nd.map_coordinates(halo_soft[..., 0], [cy_, cx_], order=1)   # fleck with its soft edge
            fc = np.stack([nd.map_coordinates(apx[..., c], [cy_, cx_], order=1) for c in range(3)], -1)
            out_ = px_ * (1 - halo_soft) + under_h * halo_soft               # water without its flecks
            fmw = (fm * wsoft_all[y0_:y1_, x0_:x1_])[..., None] * vis[y0_:y1_, x0_:x1_]
            out_[y0_:y1_, x0_:x1_] = out_[y0_:y1_, x0_:x1_] * (1 - fmw) + fc * fmw
            return out_
        out_ = px_ * (1 - fl_soft) + (under + vis * (px_ - under)) * fl_soft
        return out_

    if a.warp:
        # sea-only source: pixels outside the water are filled along each row from the water, so the warp
        # never pulls figures or sand into the sea
        art_px = np.array(art).astype(float)
        src = art_px.copy()
        cols = np.arange(W)
        for yy_ in np.nonzero(water.any(1))[0]:
            k_ = water[yy_]
            if k_.sum() >= 2:
                for c_ in range(3):
                    src[yy_, ~k_, c_] = np.interp(cols[~k_], cols[k_], art_px[yy_, k_, c_])
        wy0, wy1 = np.nonzero(water.any(1))[0][[0, -1]]
        wy1 += 1
        rows = np.arange(wy0, wy1).astype(float)
        sc_r = scale(rows)
        u = np.cumsum(1.0 / (a.warp_length * sc_r))                    # wave count from the horizon down
        WY, WX = np.mgrid[wy0:wy1, 0:W].astype(float)
        amp = (a.warp * sc_r ** 2)[:, None]
        wmask_ = np.array(Image.open(a.warp_mask).convert("L")) > 128 if a.warp_mask else water
        wsoft = nd.gaussian_filter(wmask_.astype(float), 1.0)[wy0:wy1, :, None]
        if a.roll:
            jr_ = np.random.default_rng(a.seed + 5000)
            jit = nd.gaussian_filter1d(jr_.standard_normal(W), 60, mode="wrap")
            jit = (jit - jit.min()) / (jit.max() - jit.min() + 1e-9) * a.roll_jitter       # per-column phase offset
            spacing = (a.warp_length * sc_r)[:, None]                                         # wave spacing per row
        if a.warp_radial:
            rcx, rcy = [float(v) for v in a.warp_radial.split(",")]
            RX, RY = WX - rcx, (WY - rcy) / a.warp_squash
            RR = np.hypot(RX, RY) + 1e-6

    def warped(img, f, source=None):
        """The water region of img displaced by a wave travelling toward the viewer (period T/warp_waves)."""
        if a.warp_radial:                                               # rings spread out from the centre
            ph = 2 * np.pi * (a.warp_waves * f / T - RR / a.warp_length)
            dx = a.warp * np.sin(ph) * RX / RR
            dy = a.warp * np.sin(ph) * RY / RR * a.warp_squash
        else:
            ph = 2 * np.pi * (a.warp_waves * f / T - u[:, None] - a.warp_slant * WX / a.warp_length)
            dy, dx = amp * np.sin(ph), 0.4 * amp * np.cos(ph)              # crests bob and roll
        coords = [np.clip(WY - dy, 0, H - 1), np.clip(WX - dx, 0, W - 1)]
        sv = src if source is None else source
        if a.roll:
            # two layers slide shoreward; each fades out before it jumps back (triangle weights)
            mv = 0
            phs = [(a.roll_cycles * f / T + half + jit[None, :]) % 1.0 for half in (0.0, 0.5)]
            wts = [(1 - np.abs(2 * p_ - 1)) ** a.roll_sharp for p_ in phs]
            wsum = wts[0] + wts[1]
            for ph_, wgt in zip(phs, wts):
                wgt = wgt / wsum
                ry = coords[0] - a.roll * spacing * ph_
                lay = np.stack([nd.map_coordinates(sv[..., c], [np.clip(ry, 0, H - 1), coords[1]], order=1)
                                for c in range(3)], -1)
                mv = mv + wgt[..., None] * lay
        else:
            mv = np.stack([nd.map_coordinates(sv[..., c], coords, order=1) for c in range(3)], -1)
        out = np.array(img).astype(float)
        out[wy0:wy1] = out[wy0:wy1] * (1 - wsoft) + mv * wsoft
        return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))
    SS = 2  # draw at 2x and downsample for clean anti-aliased lines
    for f in range(T):
        col = Image.new("RGB", (W * SS, H * SS)); alp = Image.new("L", (W * SS, H * SS), 0)
        dc, da = ImageDraw.Draw(col), ImageDraw.Draw(alp)
        for st in strokes:
            age = (f + st["phase"]) % T if a.cycles == 1 else ((f + st["phase"]) * a.cycles) % T
            x, y, ux, uy = st["track"][age]
            if not inner[int(min(H - 1, y)), int(min(W - 1, x))]:
                continue
            env = np.sin(np.pi * age / T) ** 2                     # fade in and out over the stroke's life
            sc = scale(y); L = st["length"] * sc * a.stroke_scale; w = max(1, st["width"] * sc * a.stroke_scale)
            # ripple dashes lie across the current, flattened towards horizontal by the viewing angle
            px, py = -uy, ux
            if px < 0: px, py = -px, -py
            if a.orient == "along":
                px, py = ux, uy                                            # streaks along the flow
            ux, uy = (0.45 * px + 0.55, 0.45 * py) if a.orient == "across" else (px, py) if a.orient == "along" else (1.0, 0.0)
            nn = np.hypot(ux, uy); ux, uy = ux / nn, uy / nn
            p0 = ((x - ux * L / 2) * SS, (y - uy * L / 2) * SS); p1 = ((x + ux * L / 2) * SS, (y + uy * L / 2) * SS)
            dc.line([p0, p1], fill=dark_rgb if st["dark"] else light_rgb, width=round(w * SS))
            da.line([p0, p1], fill=int(255 * env), width=round(w * SS))
        for gx_, gy_, g0, gs in glints:                               # four-pointed sparkle, flashes once
            age = (f - g0) % T
            if age >= gdur:
                continue
            k = np.sin(np.pi * (age + 0.5) / gdur)
            L = a.glint_size * gs * scale(gy_) * (0.4 + 0.6 * k) * SS
            cx, cy = gx_ * SS, gy_ * SS
            if a.glint_outline:                                        # dark rim so a glint shows on pale water
                o = 2.0 * SS
                for vx, vy in ((L + o, 0), (0, L * 0.7 + o)):
                    poly = [(cx - vx, cy - vy), (cx - vy * 0.26, cy + vx * 0.26), (cx + vx, cy + vy), (cx + vy * 0.26, cy - vx * 0.26)]
                    dc.polygon(poly, fill=glint_outline); da.polygon(poly, fill=int(255 * k))
            for vx, vy in ((L, 0), (0, L * 0.7)):
                poly = [(cx - vx, cy - vy), (cx - vy * 0.12, cy + vx * 0.12), (cx + vx, cy + vy), (cx + vy * 0.12, cy - vx * 0.12)]
                dc.polygon(poly, fill=glint_rgb); da.polygon(poly, fill=int(255 * k))
        col = col.resize((W, H), Image.LANCZOS); alp = alp.resize((W, H), Image.LANCZOS)
        alp = Image.fromarray((np.array(alp).astype(float) * (np.array(clip) / 255)).astype(np.uint8))
        base = twinkle(f, art) if a.star else art
        if a.shimmer:
            shf = shimmered(base, f)
            if a.warp:
                srcf = shf.copy()
                srcf[water] = shf[water]
                srcf[~water] = src[~water]
                base = warped(base, f, srcf)
            else:
                base = Image.fromarray(np.clip(shf, 0, 255).astype(np.uint8))
        elif a.warp:
            base = warped(base, f)
        frame = Image.composite(col, base, alp)
        if a.save_raw:
            os.makedirs(a.save_raw, exist_ok=True)
            frame.save(os.path.join(a.save_raw, f"f{f:04d}.png"))
        interior = cover_resize(frame, ir - il, ib - it).crop((0, 0, ir - il, banner_top - it))
        out = card.copy(); out.paste(interior, (il, it))
        out.save(os.path.join(work, f"f{f:04d}.png"))
    pat = os.path.join(work, "f%04d.png")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", pat, "-c:v", "libx264",
                    "-pix_fmt", "yuv420p", "-crf", "16", "-movflags", "+faststart", a.out + ".mp4"], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", pat, "-vf", "scale=512:-1",
                    "-c:v", "libwebp", "-loop", "0", "-quality", "85", a.out + ".webp"], check=True)
    print(a.out + ".mp4", T, "frames; work dir", work)


if __name__ == "__main__":
    main()
