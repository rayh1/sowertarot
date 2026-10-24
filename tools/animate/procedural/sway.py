#!/usr/bin/env python3
"""Animate plants swaying on a card in code: a displacement warp inside a mask, rooted at the bottom.

  sway.py --art ../batch/the-bramble/art.png --title "The Bramble" --out bramble_sway_v1 \
          --mask bramble_thicket.png --still bramble_still.png

The masked plants are shifted sideways; the shift is zero at each column's lowest masked row (the
roots) and grows towards the top of the mask (tips move most). Two travelling waves - a broad gust
and a finer ripple - make neighbouring parts move out of step. The shift fades to zero near the
--still mask (figures, animals), so they are never smeared. Where a tip moves away, the sky or field
behind it is filled along each row (--fill rows) or by diffusion. --depth shrinks the sway towards the horizon
(perspective), so far grass moves less than near grass. Waves run whole cycles per clip, so the loop is seamless.
"""
import argparse, os, subprocess, sys, tempfile
import numpy as np
from PIL import Image
from scipy import ndimage as nd

SKILL = os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../../skills/tarot-card-generator/scripts"))
sys.path.insert(0, SKILL)
from frame_card import cover_resize  # noqa: E402
from animate_compose import FRAME_FLAGS  # noqa: E402
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flicker import diffuse_fill  # noqa: E402
from flow_strokes import star_twinkle  # noqa: E402


def row_fill(img, hole):
    """Fill hole pixels along each row from the nearest known pixels left and right; keeps horizontal
    texture (field furrows, water lines) that a diffusion fill would blur away."""
    out = img.copy()
    cols = np.arange(img.shape[1])
    for y in np.nonzero(hole.any(1))[0]:
        k = ~hole[y]
        if k.sum() < 2:
            continue
        for c in range(3):
            out[y, hole[y], c] = np.interp(cols[hole[y]], cols[k], img[y, k, c])
    return out


def side_copy_fill(img, hole):
    """Fill each row's hole with the strip of the same width just left of it (right if there is no room);
    keeps fine texture such as stippled sky that interpolation would smooth away."""
    out = img.copy()
    W = img.shape[1]
    for y in np.nonzero(hole.any(1))[0]:
        xs = np.nonzero(hole[y])[0]
        for run in np.split(xs, np.nonzero(np.diff(xs) > 1)[0] + 1):
            x0, x1 = run[0], run[-1] + 1; w = x1 - x0
            src = x0 - w if x0 - w >= 0 else x1
            if src + w <= W:
                out[y, x0:x1] = img[y, src:src + w]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--art", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--mask", required=True, help="white = plants that sway")
    ap.add_argument("--still", help="white = things that must not move (sway fades out near them)")
    ap.add_argument("--frames", type=int, default=96)
    ap.add_argument("--fps", type=float, default=24)
    ap.add_argument("--amp", type=float, default=10, help="sideways shift in px at the tips")
    ap.add_argument("--gust", type=float, default=520, help="wavelength in px of the broad gust")
    ap.add_argument("--ripple", type=float, default=150, help="wavelength in px of the finer ripple")
    ap.add_argument("--pin", type=float, default=60, help="px over which the sway fades out near --still")
    ap.add_argument("--depth", help="far_y,near_y,share: perspective - the sway shrinks to `share` of --amp at row far_y "
                                    "(the horizon) and is full from row near_y down")
    ap.add_argument("--fill", choices=("rows", "diffuse", "copy"), default="rows",
                    help="how to fill behind moving plants: along rows (keeps horizontal texture) or diffusion")
    ap.add_argument("--star", help="x0,y0,x1,y1: box around a gold star on a smooth sky; makes it twinkle")
    ap.add_argument("--parts", action="store_true",
                    help="root each connected part of the mask (a blade, tuft or twig) at its own lowest pixel, "
                         "instead of each column at the mask's lowest row")
    ap.add_argument("--part-bend", type=float, default=0.35,
                    help="with --parts: max tip shift as a fraction of the part's height (short blades bend less)")
    ap.add_argument("--part-join", type=int, default=0,
                    help="with --parts: treat pieces within this many px of each other as one part (twig fragments)")
    ap.add_argument("--keep-rooted", action="store_true",
                    help="keep the original pixels under the plants where the sway is ~0 (no fill seam at a cut root)")
    ap.add_argument("--pivot", help="x,y: pendulum mode - the masked thing hangs from this point and swings about it "
                                    "(instead of plants rooted at the bottom)")
    ap.add_argument("--clear", type=int, default=4, help="--fill copy: px around the mask also refilled (a pale glow)")
    ap.add_argument("--swing", type=float, default=3.0, help="pendulum: swing amplitude in degrees")
    ap.add_argument("--lag", type=float, default=0.25,
                    help="pendulum: phase lag in radians from pivot to lowest point, so the thread bends slightly")
    a = ap.parse_args()
    T = a.frames

    art = Image.open(a.art).convert("RGB")
    W, H = art.size
    px = np.array(art).astype(float)
    mask = np.array(Image.open(a.mask).convert("L")) > 128
    Y, X = np.mgrid[0:H, 0:W].astype(float)

    if a.parts:
        # height factor per connected part: 0 at its lowest pixel, 1 at its top, capped for short parts;
        # spread to the empty pixels around each part so a moving tip can land there
        grp = nd.binary_dilation(mask, iterations=a.part_join) if a.part_join else mask
        lab, n = nd.label(grp, structure=np.ones((3, 3)))
        lab = lab * mask
        idx = np.arange(1, n + 1)
        ptop = np.r_[0, nd.minimum(Y, lab, idx)]; pbot = np.r_[0, nd.maximum(Y, lab, idx)]
        ph = np.maximum(pbot - ptop, 1)
        cap = np.minimum(1.0, a.part_bend * ph / a.amp)
        hf = np.where(mask, np.clip((pbot[lab] - Y) / ph[lab], 0, 1) ** 1.5 * cap[lab], 0)
        near = nd.distance_transform_edt(~mask, return_distances=False, return_indices=True)
        hf = hf[near[0], near[1]]
    else:
        # height factor: 0 at each column's lowest masked row, 1 at its top, smoothed across columns
        has = mask.any(0)
        cols = np.arange(W)
        top = np.interp(cols, cols[has], mask.argmax(0)[has])               # columns without plants borrow
        bot = np.interp(cols, cols[has], (H - 1 - mask[::-1].argmax(0))[has])  # from their neighbours
        top = nd.gaussian_filter1d(top, 25); bot = nd.gaussian_filter1d(bot, 25)
        hf = np.clip((bot[None, :] - Y) / np.maximum(bot - top, 1)[None, :], 0, 1) ** 1.5
    pin = np.ones((H, W))
    if a.still:
        still = np.array(Image.open(a.still).convert("L")) > 128
        dd = nd.distance_transform_edt(~still)
        u = np.clip(dd / a.pin, 0, 1); pin = u * u * (3 - 2 * u)
    reach = nd.binary_dilation(mask, iterations=int(a.amp) + 4)       # where the warp can change pixels
    if a.pivot:
        pvx, pvy = [float(v) for v in a.pivot.split(",")]
        rad = np.hypot(X - pvx, Y - pvy)
        Lmax = rad[mask].max()
        reach = nd.binary_dilation(mask, iterations=int(np.radians(a.swing) * Lmax) + 4)
    depth = np.ones((H, W))
    if a.depth:                                                         # far plants sway less
        fy, ny, share = [float(v) for v in a.depth.split(",")]
        depth = share + (1 - share) * np.clip((Y - fy) / max(1.0, ny - fy), 0, 1)
    amp = nd.gaussian_filter(a.amp * hf * pin * depth, 3)

    hole = nd.binary_dilation(mask, iterations=2)
    if a.fill == "copy":
        bg = side_copy_fill(px, nd.binary_dilation(mask, iterations=a.clear))   # also clears a glow around it
    else:
        bg = row_fill(px, hole) if a.fill == "rows" else diffuse_fill(px, hole, iters=250)
    if a.keep_rooted:
        bg = np.where((amp < 0.3)[..., None], px, bg)
    soft = nd.gaussian_filter(mask.astype(float), 0.7)
    ys = slice(int(np.nonzero(reach.any(1))[0].min()), H)

    work = tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(a.out)) or ".")
    static = os.path.join(work, "static.png")
    subprocess.run([sys.executable, f"{SKILL}/frame_card.py", "--art", a.art, "--title", a.title, "--out", static,
                    *FRAME_FLAGS], check=True)
    card = Image.open(static).convert("RGB")
    margin = round(W * 0.020); border = max(2, round(W * 0.008)); banner_h = round(H * 0.085)
    il, it, ir, ib = margin + border, margin + border, W - margin - border, H - margin - border
    banner_top = ib - banner_h
    twinkle = star_twinkle(art, [int(v) for v in a.star.split(",")], T) if a.star else None

    Ys, Xs = Y[ys], X[ys]
    for f in range(T):
        t = f / T
        wave = (0.7 * np.sin(2 * np.pi * (2 * t - Xs / a.gust - Ys / (3 * a.gust)))
                + 0.3 * np.sin(2 * np.pi * (5 * t - Xs / a.ripple + Ys / (2 * a.ripple)) + 1.1))
        if a.pivot:                                                     # rotate back about the pivot
            th = np.radians(a.swing) * np.sin(2 * np.pi * t - a.lag * rad[ys] / Lmax)
            c, sn = np.cos(th), np.sin(th)
            ox, oy = Xs - pvx, Ys - pvy
            coords = [pvy - sn * ox + c * oy, pvx + c * ox + sn * oy]
        else:
            dx = amp[ys] * wave
            coords = [Ys, Xs - dx]                                      # output shows the plant from here
        al = nd.map_coordinates(soft, coords, order=1)[..., None]
        col = np.stack([nd.map_coordinates(px[..., c], coords, order=1) for c in range(3)], -1)
        base = np.array(twinkle(f, art)).astype(float) if twinkle else px
        out = base.copy()
        region = reach[ys][..., None]
        out[ys] = np.where(region, bg[ys] * (1 - al) + col * al, base[ys])
        frame = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))
        interior = cover_resize(frame, ir - il, ib - it).crop((0, 0, ir - il, banner_top - it))
        o = card.copy(); o.paste(interior, (il, it))
        o.save(os.path.join(work, f"f{f:04d}.png"))
    pat = os.path.join(work, "f%04d.png")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", pat, "-c:v", "libx264",
                    "-pix_fmt", "yuv420p", "-crf", "16", "-movflags", "+faststart", a.out + ".mp4"], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", pat, "-vf", "scale=512:-1",
                    "-c:v", "libwebp", "-loop", "0", "-quality", "85", a.out + ".webp"], check=True)
    print(a.out + ".mp4", T, "frames; work dir", work)


if __name__ == "__main__":
    main()
