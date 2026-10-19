#!/usr/bin/env python3
"""Animate hanging ribbons (or tassels, cords) on a card in code: each ribbon bends sideways row by row.

  ribbon.py --art ../batch/the-mask/art.png --title "The Mask" --out mask_ribbons_v1 \
            --mask mask_ribbons.png

Each connected part of the mask is one ribbon, fixed at its top row. A row's sideways shift grows
from zero at the top to --amp px at the tip (power --curve), and a wave runs down the ribbon so the
tip trails the middle, like cloth in a light breeze. Ribbons get staggered phases. Behind a moving
ribbon the background is filled along each row from the pixels either side, which suits a plain sky.
Whole cycles per clip (--cycles), so the loop is seamless.
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


def light_row_fill(img, hole, light):
    """Fill hole pixels along each row from the nearest light (background) pixels left and right, so
    dark linework next to the hole (a hand, a knot) never bleeds into the fill."""
    out = img.copy()
    cols = np.arange(img.shape[1])
    for y in np.nonzero(hole.any(1))[0]:
        k = ~hole[y] & light[y]
        if k.sum() < 2:
            continue
        for c in range(3):
            out[y, hole[y], c] = np.interp(cols[hole[y]], cols[k], img[y, k, c])
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--art", required=True); p.add_argument("--title", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--mask", required=True, help="white = ribbons; each connected part is one ribbon")
    p.add_argument("--frames", type=int, default=96); p.add_argument("--fps", type=int, default=24)
    p.add_argument("--amp", type=float, default=7, help="sideways shift in px at the tip")
    p.add_argument("--curve", type=float, default=1.5, help="how the shift grows from top to tip")
    p.add_argument("--cycles", type=int, default=2, help="swings per clip")
    p.add_argument("--wave", type=float, default=1.6, help="phase lag in radians from top to tip")
    p.add_argument("--grow", type=int, default=3, help="px the fill hole extends past the mask")
    p.add_argument("--cloth", help="white = a hanging cloth whose folds ripple in place (outline kept still)")
    p.add_argument("--cloth-amp", type=float, default=4, help="sideways ripple in px at the cloth's hem")
    p.add_argument("--cloth-wave", type=float, default=140, help="wavelength in px of the ripple across the cloth")
    p.add_argument("--cloth-edge", type=float, default=14, help="px over which the ripple fades out at the outline")
    p.add_argument("--save-raw", help="also write the unframed frames to this folder")
    p.add_argument("--light", type=float, default=40, help="max colour distance from the paper for a fill source pixel")
    a = p.parse_args()

    art = Image.open(a.art).convert("RGB"); W, H = art.size
    px = np.asarray(art).astype(float)
    mask = np.asarray(Image.open(a.mask).convert("L").resize((W, H))) > 128
    lab, n = nd.label(mask)
    near = lab[tuple(nd.distance_transform_edt(lab == 0, return_distances=False, return_indices=True))]  # nearest ribbon
    Y, X = np.mgrid[0:H, 0:W].astype(float)
    amp = np.zeros((H, W)); phase = np.zeros((H, W))
    for i in range(1, n + 1):
        ys = np.nonzero((lab == i).any(1))[0]
        top, L = ys.min(), max(1, ys.max() - ys.min())
        s = np.clip((Y - top) / L, 0, 1)
        part = nd.binary_dilation(lab == i, iterations=int(a.amp + a.grow + 2)) & (near == i)
        amp = np.where(part, a.amp * s ** a.curve, amp)
        phase = np.where(part, -a.wave * s + 2.1 * (i - 1), phase)
    hole = nd.binary_dilation(mask, iterations=a.grow)
    ring = nd.binary_dilation(mask, iterations=20) & ~nd.binary_dilation(mask, iterations=8)
    paper = np.median(px[ring], axis=0)                                # the background colour round the ribbons
    light = np.abs(px - paper).sum(2) < a.light
    light &= ~nd.binary_dilation(hole, iterations=3)                    # skip the pale halo round the ink
    bg = light_row_fill(px, hole, light)
    softs = [nd.gaussian_filter((lab == i).astype(float), 0.7) for i in range(1, n + 1)]
    reach = amp > 0
    ys = slice(int(np.nonzero(reach.any(1))[0].min()), int(np.nonzero(reach.any(1))[0].max()) + 1)

    work = tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(a.out)) or ".")
    static = os.path.join(work, "static.png")
    subprocess.run([sys.executable, f"{SKILL}/frame_card.py", "--art", a.art, "--title", a.title, "--out", static,
                    *FRAME_FLAGS], check=True)
    card = Image.open(static).convert("RGB")
    margin = round(W * 0.020); border = max(2, round(W * 0.008)); banner_h = round(H * 0.085)
    il, it, ir, ib = margin + border, margin + border, W - margin - border, H - margin - border
    banner_top = ib - banner_h

    if a.cloth:                                                         # ripple inside the cloth, zero at its outline
        cm = np.asarray(Image.open(a.cloth).convert("L").resize((W, H))) > 128
        cy = np.nonzero(cm.any(1))[0]
        fade = np.clip(nd.distance_transform_edt(cm) / a.cloth_edge, 0, 1)
        cs = slice(cy.min(), cy.max() + 1)
        camp = (a.cloth_amp * fade * np.clip((Y - cy.min()) / (cy.max() - cy.min()), 0, 1))[cs]
    Ys, Xs = Y[ys], X[ys]
    for f in range(a.frames):
        t = f / a.frames
        dx = amp[ys] * np.sin(2 * np.pi * a.cycles * t + phase[ys])
        coords = [Ys, Xs - dx]                                          # output shows the ribbon from here
        al = sum(np.where(near[ys] == i, nd.map_coordinates(softs[i - 1], coords, order=1), 0)
                 for i in range(1, n + 1))[..., None]               # each pixel shows only its own ribbon
        col = np.stack([nd.map_coordinates(px[..., c], coords, order=1) for c in range(3)], -1)
        out = px.copy()
        if a.cloth:
            cdx = camp * np.sin(2 * np.pi * (a.cycles * t - X[cs] / a.cloth_wave))
            out[cs] = np.stack([nd.map_coordinates(px[..., c],
                                                   [Y[cs], X[cs] - cdx], order=1) for c in range(3)], -1)
        region = (reach[ys] & (hole[ys] | (al[..., 0] > 0)))[..., None]
        out[ys] = np.where(region, bg[ys] * (1 - al) + col * al, out[ys])
        frame = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))
        if a.save_raw:
            os.makedirs(a.save_raw, exist_ok=True); frame.save(os.path.join(a.save_raw, f"r{f:04d}.png"))
        interior = cover_resize(frame, ir - il, ib - it).crop((0, 0, ir - il, banner_top - it))
        o = card.copy(); o.paste(interior, (il, it))
        o.save(os.path.join(work, f"f{f:04d}.png"))
    pat = os.path.join(work, "f%04d.png")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", pat, "-c:v", "libx264",
                    "-pix_fmt", "yuv420p", "-crf", "16", "-movflags", "+faststart", a.out + ".mp4"], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", pat, "-vf", "scale=512:-1",
                    "-c:v", "libwebp", "-loop", "0", "-quality", "85", a.out + ".webp"], check=True)
    print(a.out + ".mp4", a.frames, "frames; work dir", work)


if __name__ == "__main__":
    main()
