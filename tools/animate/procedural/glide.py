#!/usr/bin/env python3
"""Animate birds gliding on a card in code: each bird is cut out and flown along a slow closed loop.

  glide.py --art ../batch/the-pilgrim/art.png --title "The Pilgrim" --out pilgrim_glide_v1 --box 130,140,900,310

Birds are found inside --box as everything that differs from a smooth sky (a quadratic surface fitted
to the box, refitted without outliers). The sky behind each bird is replaced by that fit plus faint
grain. Every frame each bird is redrawn with sub-pixel precision: it travels an ellipse (one lap per
clip, own size and phase), banks with its vertical motion, and beats its wings (a gentle vertical
squash, whole cycles per clip). The flock also drifts together slightly. The clip loops seamlessly,
and the number of birds never changes.
"""
import argparse, os, subprocess, sys, tempfile
import numpy as np
from PIL import Image
from scipy import ndimage as nd

SKILL = os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../../skills/tarot-card-generator/scripts"))
sys.path.insert(0, SKILL)
from frame_card import cover_resize  # noqa: E402
from animate_compose import FRAME_FLAGS  # noqa: E402


def fit_sky(sub, x0, y0):
    """Quadratic surface per channel fitted to the sky pixels of sub; returns fit and |residual| sum."""
    h, w = sub.shape[:2]
    yy, xx = np.mgrid[y0:y0 + h, x0:x0 + w]
    A = np.c_[np.ones(xx.size), xx.ravel(), yy.ravel(), xx.ravel() ** 2, yy.ravel() ** 2, (xx * yy).ravel()]
    A = A / np.array([1, 1e3, 1e3, 1e6, 1e6, 1e6])
    ok = np.ones(xx.size, bool)
    for _ in range(3):
        co = [np.linalg.lstsq(A[ok], sub[..., ch].ravel()[ok], rcond=None)[0] for ch in range(3)]
        fit = np.stack([(A @ k).reshape(h, w) for k in co], -1)
        res = np.abs(sub - fit).sum(-1)
        ok = (res < 25).ravel()
    return fit, res


def local_fill(px, hole, rng, grain):
    """Fill hole pixels by diffusion from their surroundings (local crop), then add sky-like grain:
    smoothed noise scaled to the std of the surrounding pixels' fine detail."""
    ys, xs = np.nonzero(hole)
    y0, y1 = max(0, ys.min() - 20), min(px.shape[0], ys.max() + 21)
    x0, x1 = max(0, xs.min() - 20), min(px.shape[1], xs.max() + 21)
    crop, h = px[y0:y1, x0:x1].copy(), hole[y0:y1, x0:x1]
    crop[h] = crop[~h].mean(0)
    for _ in range(600):
        blur = np.stack([nd.uniform_filter(crop[..., c], 5) for c in range(3)], -1)
        crop[h] = blur[h]
    if grain:
        ring = nd.binary_dilation(h, iterations=14) & ~nd.binary_dilation(h, iterations=3)
        orig = px[y0:y1, x0:x1]
        detail = orig - np.stack([nd.gaussian_filter(orig[..., c], 3) for c in range(3)], -1)
        sd = detail[ring].std(0)
        nz = np.stack([nd.gaussian_filter(rng.standard_normal(h.shape), 0.8) for _ in range(3)], -1)
        nz /= nz[h].std(0)
        crop[h] += (nz * sd)[h]
    out = px.copy(); out[y0:y1, x0:x1][h] = crop[h]
    return out


def find_insects(a, px, rng, T):
    """Insect mode: one creature per box. Returns the filled background, the creatures, and the patch margin.
    Sprites carry no background halo: alpha comes from how far each pixel differs from the sky behind it
    (estimated by a smooth fill of the hole), and edge pixels are un-mixed from that sky, so an insect
    keeps clean edges when it flies over sky of another colour."""
    H, W = px.shape[:2]
    boxes = [[int(v) for v in b.split(",")] for b in a.boxes.split(";")]
    kinds = a.kinds.split(",") if a.kinds else ["butterfly"] * len(boxes)
    shapes, hole_all = [], np.zeros((H, W), bool)
    for (x0, y0, x1, y1), kind in zip(boxes, kinds):
        X0, Y0, X1, Y1 = max(0, x0 - 40), max(0, y0 - 40), min(W, x1 + 40), min(H, y1 + 40)
        # the insect's own colours - dark ink, white wing, saturated body - so a sharp edge in the sky
        # (a cloud's outline) is never mistaken for part of the insect
        sub = px[Y0:Y1, X0:X1]
        lum, sat = sub.mean(-1), sub.max(-1) - sub.min(-1)
        found = (lum < 100) | (sub.min(-1) > 215) | (sat > 80)
        found = nd.binary_fill_holes(nd.binary_closing(found, iterations=2))
        found[:y0 - Y0] = False; found[y1 - Y0:] = False; found[:, :x0 - X0] = False; found[:, x1 - X0:] = False
        lab, _ = nd.label(found)
        sz = np.bincount(lab.ravel()); sz[0] = 0
        sl = nd.find_objects(lab)[sz.argmax() - 1]
        m = np.pad(lab[sl] == sz.argmax(), 4)
        bys, bxs = sl[0].start + Y0 - 4, sl[1].start + X0 - 4
        m = nd.binary_dilation(m, iterations=2)
        hole_all[bys:bys + m.shape[0], bxs:bxs + m.shape[1]] |= m
        shapes.append((m, bys, bxs, kind))
    hole_all = nd.binary_dilation(hole_all, iterations=2)
    lab, n = nd.label(hole_all)
    smooth, bg = px.copy(), px.copy()
    for i in range(1, n + 1):
        smooth = local_fill(smooth, lab == i, rng, grain=False)        # the sky behind, for un-mixing
        bg = local_fill(bg, lab == i, rng, grain=True)                 # the sky behind, as shown
    birds = []
    for m, bys, bxs, kind in shapes:
        hh, ww = m.shape
        rgb, sky = px[bys:bys + hh, bxs:bxs + ww], smooth[bys:bys + hh, bxs:bxs + ww]
        alpha = np.clip(np.abs(rgb - sky).sum(-1) / 90, 0, 1) * m        # how much of the pixel is insect
        alpha = np.maximum(alpha, nd.binary_erosion(nd.binary_fill_holes(m), iterations=3))  # solid inside
        alpha[alpha < 0.08] = 0
        col = np.clip(sky + (rgb - sky) / np.maximum(alpha, 0.08)[..., None], 0, 255)
        sprite = Image.fromarray(np.dstack([col, alpha * 255]).astype(np.uint8), "RGBA")
        bee, bird = kind == "bee", kind == "bird"
        r = a.radius * (0.5 if bee else 1.0) * rng.uniform(0.85, 1.15)
        birds.append(dict(sprite=sprite, x=bxs, y=bys, cx=ww / 2, cy=hh / 2, kind=kind,
                          rx=r, ry=r * (0.4 if bird else rng.uniform(0.5, 0.7)), ph=rng.uniform(0, 2 * np.pi),
                          laps=3 if bee else 1, dirn=rng.choice((-1, 1)), bank=a.bank * (1.6 if bee else 1.0),
                          beats=24 if bee else (3 if bird else 10), flap=0.18 if bee else (0.12 if bird else 0.42),
                          fph=rng.uniform(0, 2 * np.pi),
                          jit=[(rng.uniform(0, 6.3), rng.uniform(0, 6.3)) for _ in range(2)] if bee else None))
        print(kind, "at", (bxs, bys, bxs + ww, bys + hh), int(m.sum()), "px")
    P = int(a.radius * 1.6 + 40)
    return bg, birds, P


def insect_motion(b, t):
    """Offset, tilt and wing squash of one insect at clip time t (0..1); all terms whole cycles per clip."""
    ang = 2 * np.pi * b["laps"] * t * b["dirn"] + b["ph"]
    dx, dy = b["rx"] * np.cos(ang), b["ry"] * np.sin(ang)
    fl = np.sin(2 * np.pi * b["beats"] * t + b["fph"])
    if b["kind"] == "bird":                                            # gliding bird: slow lap, few slow wing beats
        th = np.radians(b["bank"] * np.cos(ang) * b["dirn"])
        return dx, dy, th, 1.0, 1 + b["flap"] * fl
    if b["jit"]:                                                       # bee: a small buzz on top of quick loops
        (p1, p2), (p3, p4) = b["jit"]
        dx += 2.5 * np.sin(2 * np.pi * 17 * t + p1) + 1.5 * np.sin(2 * np.pi * 29 * t + p2)
        dy += 2.0 * np.sin(2 * np.pi * 19 * t + p3) + 1.2 * np.sin(2 * np.pi * 31 * t + p4)
    else:                                                              # butterfly: lifts a little on each beat
        dy += -3.0 * max(0.0, fl)
    th = np.radians(b["bank"] * np.cos(ang) * b["dirn"])
    sx = 1 - b["flap"] * (0.5 + 0.5 * fl)                              # wings close sideways, never wider than drawn
    return dx, dy, th, sx, 1.0


def swirl(a, rng, T):
    """Twist the dark flock about a centre: angle = swing(r) * sin(2 pi t - r / 400) - inner coils twist more,
    the twist travels outward - plus a slight breathing of size. Fades out near the art's edges, so its
    border line stays put and nothing is pulled in from outside. Exposed sky is filled by diffusion + grain."""
    art = Image.open(a.art).convert("RGB")
    W, H = art.size
    px = np.array(art).astype(float)
    lum = px.mean(-1)
    flock = lum < a.flock_thr
    keep = np.zeros((H, W), bool); keep[:a.flock_maxy] = True
    if a.flock_extra:
        x0, y0, x1, y1 = [int(v) for v in a.flock_extra.split(",")]
        keep[y0:y1, x0:x1] = True
    edge = np.zeros((H, W), bool); edge[8:H - 8, 8:W - 8] = True       # the art's own border line stays
    flock = nd.binary_fill_holes(nd.binary_closing(flock & keep, iterations=2)) & edge
    print("flock px", int(flock.sum()))
    if a.base_frames:
        print("base frames: used below the flock only (rows below its reach)")
    bg = local_fill(px, nd.binary_dilation(flock, iterations=2), rng, grain=True)
    soft = nd.gaussian_filter(flock.astype(float), 0.7)
    cx, cy = [float(v) for v in a.centre.split(",")]
    rows = int(np.nonzero(nd.binary_dilation(flock, iterations=40).any(1))[0].max()) + 1
    Y, X = np.mgrid[0:rows, 0:W].astype(float)
    r = np.hypot(X - cx, Y - cy)
    amp = np.radians(a.swing) / (1 + (r / 300) ** 1.5)
    d_edge = np.minimum.reduce([X, Y, W - 1 - X, H - 1 - Y]) - 8
    u = np.clip(d_edge / 60, 0, 1); fade = u * u * (3 - 2 * u)

    work = tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(a.out)) or ".")
    static = os.path.join(work, "static.png")
    subprocess.run([sys.executable, f"{SKILL}/frame_card.py", "--art", a.art, "--title", a.title, "--out", static,
                    *FRAME_FLAGS], check=True)
    card = Image.open(static).convert("RGB")
    margin = round(W * 0.020); border = max(2, round(W * 0.008)); banner_h = round(H * 0.085)
    il, it, ir, ib = margin + border, margin + border, W - margin - border, H - margin - border
    banner_top = ib - banner_h
    for f in range(T):
        t = f / T
        th = amp * np.sin(2 * np.pi * t - r / 400)
        sc = 1 + a.breathe * np.sin(2 * np.pi * t + 1.0)
        c, s_ = np.cos(-th), np.sin(-th)                                 # output -> source: undo the twist
        qx = cx + (c * (X - cx) - s_ * (Y - cy)) / sc
        qy = cy + (s_ * (X - cx) + c * (Y - cy)) / sc
        sx, sy = X + fade * (qx - X), Y + fade * (qy - Y)
        al = nd.map_coordinates(soft, [sy, sx], order=1, mode="nearest")[..., None]
        col = np.stack([nd.map_coordinates(px[..., ch], [sy, sx], order=1, mode="nearest") for ch in range(3)], -1)
        out = bg.copy()
        if a.base_frames:                                               # below the flock: the other animation
            raw = np.array(Image.open(os.path.join(a.base_frames, f"f{f:04d}.png")).convert("RGB")).astype(float)
            out[rows:] = raw[rows:]
        out[:rows] = bg[:rows] * (1 - al) + col * al
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--art", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--box", help="x0,y0,x1,y1 of the sky band holding the birds")
    ap.add_argument("--boxes", help="insect mode: 'x0,y0,x1,y1;...' one box per creature (largest shape in it); "
                                    "background filled by local diffusion plus grain instead of the sky fit")
    ap.add_argument("--mode", choices=("glide", "swirl"), default="glide",
                    help="swirl: the whole dark flock twists back and forth about --centre (a turning wave)")
    ap.add_argument("--centre", help="swirl: x,y of the spiral's centre")
    ap.add_argument("--swing", type=float, default=9, help="swirl: twist in degrees near the centre")
    ap.add_argument("--breathe", type=float, default=0.015, help="swirl: size change, fraction")
    ap.add_argument("--flock-thr", type=float, default=150, help="swirl: pixels darker than this are flock")
    ap.add_argument("--flock-maxy", type=int, default=960, help="swirl: flock lies above this row ...")
    ap.add_argument("--flock-extra", help="swirl: ... plus inside this x0,y0,x1,y1 box")
    ap.add_argument("--kinds", help="insect mode: comma list per box, 'butterfly', 'bee' or 'bird' (default butterfly)")
    ap.add_argument("--base-frames", help="dir of f0000.png... (unframed art, already animated) used as each "
                                         "frame's background instead of the static art; holes filled the same way")
    ap.add_argument("--frames", type=int, default=96)
    ap.add_argument("--fps", type=float, default=24)
    ap.add_argument("--radius", type=float, default=24, help="mean horizontal radius in px of each loop")
    ap.add_argument("--drift", type=float, default=10, help="px the whole flock drifts together")
    ap.add_argument("--bank", type=float, default=7, help="max tilt in degrees")
    ap.add_argument("--flap", type=float, default=0.12, help="wing-beat squash (fraction of height)")
    ap.add_argument("--beats", type=int, default=4, help="wing beats per clip")
    ap.add_argument("--min-size", type=int, default=150)
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)
    T = a.frames
    if a.mode == "swirl":
        return swirl(a, rng, T)

    art = Image.open(a.art).convert("RGB")
    W, H = art.size
    px = np.array(art).astype(float)
    if a.boxes:
        bg, birds, P = find_insects(a, px, rng, T)
    else:
        x0, y0, x1, y1 = [int(v) for v in a.box.split(",")]
        fit, res = fit_sky(px[y0:y1, x0:x1], x0, y0)
        found = nd.binary_fill_holes(nd.binary_closing(res > 40, iterations=2))
        lab, n = nd.label(found)

        bg = px.copy()
        birds = []
        P = int(a.radius * 1.4 + a.drift + 30)                       # patch margin around each bird
        for i, sl in enumerate(nd.find_objects(lab)):
            m = lab[sl] == i + 1
            if m.sum() < a.min_size:
                continue
            m = np.pad(m, 4)
            bys, bxs = sl[0].start + y0 - 4, sl[1].start + x0 - 4
            m = nd.binary_dilation(m, iterations=2)
            hh, ww = m.shape
            rgb = px[bys:bys + hh, bxs:bxs + ww]
            alpha = nd.gaussian_filter(m.astype(float), 0.6)
            sprite = Image.fromarray(np.dstack([rgb, alpha * 255]).astype(np.uint8), "RGBA")
            # the sky behind: fitted surface plus grain like the original's
            hole = np.zeros((H, W), bool); hole[bys:bys + hh, bxs:bxs + ww] = m
            hole = nd.binary_dilation(hole, iterations=2)
            fy, fx = np.nonzero(hole)
            bg[fy, fx] = fit[fy - y0, fx - x0] + rng.normal(0, 1.0, (len(fy), 1))
            birds.append(dict(sprite=sprite, x=bxs, y=bys, cx=ww / 2, cy=hh / 2,
                              rx=a.radius * rng.uniform(0.85, 1.15), ry=a.radius * rng.uniform(0.35, 0.5),
                              # same direction for all, phase staggered by position: neighbours keep their spacing
                              ph=2 * np.pi * (bxs + ww / 2) / 1400 + rng.uniform(0, 0.6), dirn=1,
                              fph=rng.uniform(0, 2 * np.pi), beats=a.beats + int(rng.integers(0, 2))))
    print(len(birds), "birds found")
    def centre(b, t):
        if "kind" in b:
            dx, dy = insect_motion(b, t)[:2]
            return b["x"] + b["cx"] + dx, b["y"] + b["cy"] + dy
        ang = 2 * np.pi * t * b["dirn"] + b["ph"]
        return b["x"] + b["cx"] + b["rx"] * np.cos(ang), b["y"] + b["cy"] + b["ry"] * np.sin(ang)
    worst = 0                                        # most pixels where two birds' shapes overlap in a frame
    for f in range(T):
        occ = np.zeros((H, W), np.uint8)
        for b in birds:
            cx_, cy_ = centre(b, f / T)
            ox, oy = int(round(cx_ - b["cx"])), int(round(cy_ - b["cy"]))
            m = np.array(b["sprite"])[..., 3] > 80
            occ[oy:oy + m.shape[0], ox:ox + m.shape[1]] += m
        worst = max(worst, int((occ > 1).sum()))
    print("max overlapping bird pixels in any frame:", worst)
    base = Image.fromarray(np.clip(bg, 0, 255).astype(np.uint8))
    filled = np.abs(bg - px).sum(-1) > 0                              # pixels the hole fill changed
    hole_px = nd.binary_dilation(filled, iterations=3)

    def base_for(f):
        if not a.base_frames:
            return base
        raw = np.array(Image.open(os.path.join(a.base_frames, f"f{f:04d}.png")).convert("RGB")).astype(float)
        if np.abs(raw[hole_px] - px[hole_px]).max() > 0:                # the animation reaches under a creature
            lab_, n_ = nd.label(hole_px)
            for k in range(1, n_ + 1):
                raw = local_fill(raw, lab_ == k, np.random.default_rng(f), grain=True)
        else:
            raw[filled] = bg[filled]
        return Image.fromarray(np.clip(raw, 0, 255).astype(np.uint8))
    if a.base_frames:
        raw0 = np.array(Image.open(os.path.join(a.base_frames, "f0000.png")).convert("RGB")).astype(float)
        print("base frames: animation", "reaches" if np.abs(raw0[hole_px] - px[hole_px]).max() > 0 else
              "stays clear of", "the creatures' holes")

    work = tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(a.out)) or ".")
    static = os.path.join(work, "static.png")
    subprocess.run([sys.executable, f"{SKILL}/frame_card.py", "--art", a.art, "--title", a.title, "--out", static,
                    *FRAME_FLAGS], check=True)
    card = Image.open(static).convert("RGB")
    margin = round(W * 0.020); border = max(2, round(W * 0.008)); banner_h = round(H * 0.085)
    il, it, ir, ib = margin + border, margin + border, W - margin - border, H - margin - border
    banner_top = ib - banner_h

    for f in range(T):
        t = f / T
        fdx = a.drift * np.sin(2 * np.pi * t); fdy = 0.4 * a.drift * np.sin(4 * np.pi * t + 0.7)
        frame = base_for(f).copy()
        for b in birds:
            sx = 1.0
            if "kind" in b:
                dx, dy, th, sx, sy = insect_motion(b, t)
            else:
                ang = 2 * np.pi * t * b["dirn"] + b["ph"]
                dx = b["rx"] * np.cos(ang) + fdx
                dy = b["ry"] * np.sin(ang) + fdy
                vy = b["ry"] * np.cos(ang) * b["dirn"]                    # vertical speed -> banking
                th = np.radians(a.bank * vy / max(b["ry"], 1e-6))
                sy = 1 + a.flap * np.sin(2 * np.pi * b["beats"] * t + b["fph"])
            sp = b["sprite"]
            pw, ph = sp.width + 2 * P, sp.height + 2 * P
            cpx, cpy = b["cx"] + P + dx, b["cy"] + P + dy               # bird centre in the patch
            c, s = np.cos(th), np.sin(th)
            # inverse map patch -> sprite: undo translation, rotation, then the wing squash
            M = np.array([[c / sx, s / sx], [-s / sy, c / sy]]) if sx != 1.0 else np.array([[c, s], [-s / sy, c / sy]])
            off = np.array([b["cx"], b["cy"]]) - M @ np.array([cpx, cpy])
            patch = sp.transform((pw, ph), Image.AFFINE, (M[0, 0], M[0, 1], off[0], M[1, 0], M[1, 1], off[1]),
                                 resample=Image.BICUBIC)
            frame.paste(patch, (b["x"] - P, b["y"] - P), patch)
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
