#!/usr/bin/env python3
"""Animate falling snow over a card in code: ink-outlined flakes drift down over the art.

  falling_particles.py --art ../batch/the-frost/art.png --title "The Frost" --out frost_snow_v1

Flakes are added on top of the art (no element mask). Each flake lives exactly one clip length:
it fades in, falls a short way with a gentle sideways sway, and fades out, on its own phase, so
the clip loops seamlessly. Depth: far flakes are small, slow and faint; near ones larger and faster.
--glitter N adds frost glints: four-pointed sparkles that flash once per clip on white frost rims beside ink.

Other kinds (opt-in, --kind; snow stays the default and is unchanged):
  leaf  lens-shaped leaves with an ink outline that tumble (spin and flip) and sway as they fall; same
        one-life-per-clip loop as snow.
  sand  a stream of fine grains along --path (x,y;x,y;...), entering at its first point and leaving at its
        last, accelerating (--ease > 1). Each grain runs the path --laps times per clip, so the loop is exact.
  seed  like sand but lens-shaped seeds that tumble and fade out over the last part of the path (--ease < 1
        slows them down as they scatter).
--still PNG: white pixels are restored from the art after drawing, so particles pass behind figures.
--bounce N (sand): N grains hop in small arcs where the stream lands, a whole number of hops per clip.
--erase PNG: white pixels are removed from the art and filled from their surroundings before animating.
--avoid x0,y0,x1,y1;...: falling particles (snow, leaf) whose path would cross a box are placed elsewhere.
"""
import argparse, os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage as nd

SKILL = os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../../skills/tarot-card-generator/scripts"))
sys.path.insert(0, SKILL)
from frame_card import cover_resize  # noqa: E402
from animate_compose import FRAME_FLAGS  # noqa: E402

INK = (26, 22, 18)
SNOW = (252, 252, 248)
GLINT = (236, 248, 255)   # ice-white with a hint of blue
GLINT_INK = (38, 62, 92)  # dark blue outline so the glint shows on white frost


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--art", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--frames", type=int, default=96)
    ap.add_argument("--fps", type=float, default=24)
    ap.add_argument("--count", type=int, default=70, help="flakes on screen at any time")
    ap.add_argument("--speed", type=float, default=1.6, help="px per frame for the nearest flakes")
    ap.add_argument("--size", type=float, default=5.0, help="radius in px of the nearest flakes")
    ap.add_argument("--sway", type=float, default=6.0, help="sideways sway amplitude in px")
    ap.add_argument("--outline", type=float, default=1.3, help="ink outline width in px (0 = none)")
    ap.add_argument("--region", help="x0,y0,x1,y1 where flakes may appear (default: whole art)")
    ap.add_argument("--glitter", type=int, default=0, help="frost glints per clip (each flashes once)")
    ap.add_argument("--glitter-size", type=float, default=30, help="ray length in px of the largest glints")
    ap.add_argument("--glitter-box", help="x0,y0,x1,y1 to look for frost (white next to ink); default: whole art")
    ap.add_argument("--kind", choices=("snow", "leaf", "sand", "seed"), default="snow")
    ap.add_argument("--path", help="sand/seed: x,y;x,y;... centre line of the stream, from emitter to end")
    ap.add_argument("--laps", type=int, default=1, help="sand/seed: times each particle runs the path per clip")
    ap.add_argument("--spread", default="2,10", help="sand/seed: stream half-width in px at start,end")
    ap.add_argument("--ease", type=float, default=1.0, help="sand/seed: >1 speeds up along the path, <1 slows down")
    ap.add_argument("--fade-end", type=float, default=0.05, help="sand/seed: share of the path over which it fades out")
    ap.add_argument("--fill", help="r,g,b[;r,g,b...] particle colours (leaf/sand/seed); one is picked per particle")
    ap.add_argument("--spin", type=float, default=1.0, help="leaf/seed: tumbling speed, turns per clip")
    ap.add_argument("--still", help="PNG: white = restore the art there after drawing (particles pass behind)")
    ap.add_argument("--bounce", type=int, default=0, help="sand: grains hopping where the stream lands")
    ap.add_argument("--bounce-at", help="sand: x,y where the stream lands (default: the path's last point)")
    ap.add_argument("--bounce-height", type=float, default=8, help="sand: highest hop in px")
    ap.add_argument("--bounce-width", type=float, default=14, help="sand: how far sideways hops reach, px")
    ap.add_argument("--erase", help="PNG (leaf/sand/seed): white = remove from the art first (drawn particles that"
                                    " would stay still), filled from the surrounding background")
    ap.add_argument("--avoid", help="x0,y0,x1,y1[;...] boxes falling snow/leaves must not cross")
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)

    art = Image.open(a.art).convert("RGB")
    W, H = art.size
    x0, y0, x1, y1 = [int(v) for v in a.region.split(",")] if a.region else (0, 0, W, H)
    T = a.frames

    glints = []
    if a.glitter:
        px = np.array(art).astype(int)
        mx, mn = px.max(-1), px.min(-1)
        frost = (mn > 238) & (mx - mn < 14) & nd.binary_dilation(mx < 90, iterations=4)  # white rim beside an ink line
        if a.glitter_box:
            gx0, gy0, gx1, gy1 = [int(v) for v in a.glitter_box.split(",")]
            box = np.zeros_like(frost); box[gy0:gy1, gx0:gx1] = True; frost &= box
        ys, xs = np.nonzero(frost)
        dur = max(6, T // 7)                               # one flash lasts ~0.6 s
        for k in rng.choice(len(ys), a.glitter, replace=False):
            glints.append(dict(x=xs[k], y=ys[k], start=int(rng.integers(T)), dur=dur,
                               L=a.glitter_size * rng.uniform(0.6, 1.0), rot=rng.uniform(-0.3, 0.3)))

    if a.kind != "snow":
        return other_kinds(a, rng, art, glints)

    flakes = []
    for _ in range(a.count):
        depth = rng.uniform(0.35, 1.0) ** 0.8          # 1 = nearest
        v = a.speed * depth * rng.uniform(0.85, 1.15)
        fall = v * T
        flakes.append(dict(
            x=rng.uniform(x0, x1), y=rng.uniform(y0 - fall * 0.3, y1 - fall * 0.7), v=v,
            r=a.size * depth * rng.uniform(0.8, 1.2), op=0.55 + 0.45 * depth,
            sway=a.sway * depth * rng.uniform(0.5, 1.2), cyc=int(rng.integers(1, 3)),
            sph=rng.uniform(0, 2 * np.pi), phase=int(rng.integers(T))))
    flakes.sort(key=lambda fl: fl["r"])                  # far flakes drawn first

    work = tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(a.out)) or ".")
    static = os.path.join(work, "static.png")
    subprocess.run([sys.executable, f"{SKILL}/frame_card.py", "--art", a.art, "--title", a.title, "--out", static,
                    *FRAME_FLAGS], check=True)
    card = Image.open(static).convert("RGB")
    margin = round(W * 0.020); border = max(2, round(W * 0.008)); banner_h = round(H * 0.085)
    il, it, ir, ib = margin + border, margin + border, W - margin - border, H - margin - border
    banner_top = ib - banner_h

    SS = 3  # draw at 3x and downsample for round anti-aliased flakes
    for f in range(T):
        layer = Image.new("RGBA", (W * SS, H * SS), (0, 0, 0, 0))
        dl = ImageDraw.Draw(layer)
        for g in glints:                                   # behind the snow: four-pointed sparkle, flashes once
            age = (f - g["start"]) % T
            if age >= g["dur"]:
                continue
            k = min(1.0, 1.6 * np.sin(np.pi * (age + 0.5) / g["dur"]))   # quick rise, short full-bright hold
            L, al, cx, cy = g["L"] * (0.4 + 0.6 * k) * SS, int(255 * k), g["x"] * SS, g["y"] * SS
            rays = ((g["rot"], L), (g["rot"] + np.pi / 2, L), (g["rot"] + np.pi / 4, L * 0.45),
                    (g["rot"] - np.pi / 4, L * 0.45))
            for col, grow, wid in ((GLINT_INK, 2.2 * SS, 0.20), (GLINT, 0, 0.09)):   # outline first, then the light
                for ang, ln in rays:
                    ux, uy = np.cos(ang) * (ln + grow), np.sin(ang) * (ln + grow)
                    vx, vy = np.cos(ang) * ln, np.sin(ang) * ln
                    dl.polygon([(cx - ux, cy - uy), (cx - vy * wid, cy + vx * wid), (cx + ux, cy + uy),
                                (cx + vy * wid, cy - vx * wid)], fill=col + (al,))
            rc = 2.2 * k * SS
            dl.ellipse([cx - rc, cy - rc, cx + rc, cy + rc], fill=(255, 255, 255, al))
        for fl in flakes:
            age = (f + fl["phase"]) % T
            env = min(1.0, age / (0.2 * T), (T - age) / (0.2 * T))      # fade in/out over 20 % of life
            if env <= 0:
                continue
            x = fl["x"] + fl["sway"] * np.sin(2 * np.pi * fl["cyc"] * age / T + fl["sph"])
            y = fl["y"] + fl["v"] * age
            r = fl["r"]
            al = int(255 * fl["op"] * env)
            ro = (r + a.outline) * SS
            dl = ImageDraw.Draw(layer)   # flakes rarely overlap, so drawing straight onto the layer is enough
            if a.outline > 0:
                dl.ellipse([x * SS - ro, y * SS - ro, x * SS + ro, y * SS + ro], fill=INK + (al,))
            dl.ellipse([x * SS - r * SS, y * SS - r * SS, x * SS + r * SS, y * SS + r * SS], fill=SNOW + (al,))
        layer = layer.resize((W, H), Image.LANCZOS)
        frame = art.copy(); frame.paste(layer, (0, 0), layer)
        interior = cover_resize(frame, ir - il, ib - it).crop((0, 0, ir - il, banner_top - it))
        out = card.copy(); out.paste(interior, (il, it))
        out.save(os.path.join(work, f"f{f:04d}.png"))
    pat = os.path.join(work, "f%04d.png")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", pat, "-c:v", "libx264",
                    "-pix_fmt", "yuv420p", "-crf", "16", "-movflags", "+faststart", a.out + ".mp4"], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(a.fps), "-i", pat, "-vf", "scale=512:-1",
                    "-c:v", "libwebp", "-loop", "0", "-quality", "85", a.out + ".webp"], check=True)
    print(a.out + ".mp4", T, "frames; work dir", work)


def lens(cx, cy, length, width, ang, n=10):
    """Points of a pointed leaf/seed outline centred on (cx, cy), long axis at angle ang."""
    t = np.linspace(0, np.pi, n)
    pts = [(length / 2 * np.cos(v), width / 2 * np.sin(v)) for v in t] + \
          [(length / 2 * np.cos(v), -width / 2 * np.sin(v)) for v in t[::-1]]
    c, s_ = np.cos(ang), np.sin(ang)
    return [(cx + x * c - y * s_, cy + x * s_ + y * c) for x, y in pts]


def colours(a, default):
    if not a.fill:
        return [default]
    return [tuple(int(v) for v in c.split(",")) for c in a.fill.split(";")]


def path_points(spec, n=600):
    """Resample a polyline 'x,y;x,y;...' (smoothed) to n points evenly spaced along its length."""
    p = np.array([[float(v) for v in q.split(",")] for q in spec.split(";")])
    t = np.linspace(0, 1, len(p)); tt = np.linspace(0, 1, 50 * len(p))
    if len(p) >= 3:                       # smooth with a Catmull-Rom-like quadratic interpolation
        from scipy.interpolate import make_interp_spline
        k = min(3, len(p) - 1)
        q = make_interp_spline(t, p, k=k)(tt)
    else:
        q = np.c_[np.interp(tt, t, p[:, 0]), np.interp(tt, t, p[:, 1])]
    d = np.r_[0, np.cumsum(np.hypot(*np.diff(q, axis=0).T))]
    u = np.linspace(0, d[-1], n)
    pts = np.c_[np.interp(u, d, q[:, 0]), np.interp(u, d, q[:, 1])]
    tang = np.gradient(pts, axis=0); tang /= np.hypot(*tang.T)[:, None] + 1e-9
    return pts, tang


def erase(art, hole, rng, iters=300):
    """Fill hole pixels by repeated local averaging from their surroundings, plus grain like the art's."""
    px = np.array(art).astype(float)
    ys, xs = np.nonzero(nd.binary_dilation(hole, iterations=12))
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    sub, h = px[y0:y1, x0:x1].copy(), hole[y0:y1, x0:x1]
    # grain: the high-frequency part of the surrounding background
    ring = nd.binary_dilation(h, iterations=14) & ~nd.binary_dilation(h, iterations=8)
    grain = np.std(sub[ring] - np.stack([nd.uniform_filter(sub[..., c], 5) for c in range(3)], -1)[ring])
    sub[h] = 0
    for _ in range(iters):
        blur = np.stack([nd.uniform_filter(sub[..., c], 5) for c in range(3)], -1)
        sub[h] = blur[h]
    sub[h] += rng.normal(0, min(grain, 1.5), (int(h.sum()), 1))   # capped: near dense particles the ring overstates it
    px[y0:y1, x0:x1] = sub
    return Image.fromarray(np.clip(px, 0, 255).astype(np.uint8))


def other_kinds(a, rng, art, glints):
    W, H = art.size
    T = a.frames
    x0, y0, x1, y1 = [int(v) for v in a.region.split(",")] if a.region else (0, 0, W, H)
    avoid = [[float(v) for v in b.split(",")] for b in a.avoid.split(";")] if a.avoid else []
    still = np.array(Image.open(a.still).convert("L")) > 128 if a.still else None
    if a.erase:
        art = erase(art, np.array(Image.open(a.erase).convert("L")) > 128, rng)
    parts = []
    if a.kind == "leaf":
        pal = colours(a, (226, 132, 38))
        for _ in range(a.count):
            for _try in range(200):
                depth = rng.uniform(0.45, 1.0) ** 0.8
                v = a.speed * depth * rng.uniform(0.8, 1.2)
                fall = v * T
                p = dict(x=rng.uniform(x0, x1), y=rng.uniform(y0 - fall * 0.3, y1 - fall * 0.7), v=v,
                         r=a.size * depth * rng.uniform(0.8, 1.2), op=0.7 + 0.3 * depth,
                         sway=a.sway * depth * rng.uniform(0.6, 1.2), cyc=int(rng.integers(1, 3)),
                         sph=rng.uniform(0, 2 * np.pi), phase=int(rng.integers(T)),
                         rot=rng.uniform(0, 2 * np.pi), spin=a.spin * rng.uniform(0.6, 1.4) * rng.choice((-1, 1)),
                         flip=a.spin * rng.uniform(0.8, 2.0), col=pal[int(rng.integers(len(pal)))])
                pad = p["sway"] + p["r"] * 1.6
                if not any(p["x"] + pad > bx0 and p["x"] - pad < bx1 and p["y"] + fall + pad > by0 and p["y"] - pad < by1
                           for bx0, by0, bx1, by1 in avoid):
                    break
            parts.append(p)
        parts.sort(key=lambda q: q["r"])
    else:
        pts, tang = path_points(a.path)
        w0, w1 = [float(v) for v in a.spread.split(",")]
        pal = colours(a, (228, 162, 40) if a.kind == "sand" else (214, 140, 40))
        hops = []
        if a.kind == "sand" and a.bounce:
            bx, by = [float(v) for v in a.bounce_at.split(",")] if a.bounce_at else pts[-1]
            for _ in range(a.bounce):
                hops.append(dict(x=bx, y=by, side=rng.uniform(-1, 1) * a.bounce_width,
                                 h=a.bounce_height * rng.uniform(0.35, 1.0), k=int(rng.integers(4, 9)),
                                 ph=rng.uniform(0, 1), r=a.size * rng.uniform(0.7, 1.1),
                                 col=pal[int(rng.integers(len(pal)))]))
        for _ in range(a.count):
            parts.append(dict(u0=rng.uniform(0, 1), off=rng.uniform(-1, 1), wob=rng.uniform(0, 2 * np.pi),
                              r=a.size * rng.uniform(0.75, 1.25), rot=rng.uniform(0, 2 * np.pi),
                              spin=a.spin * rng.uniform(0.6, 1.4) * rng.choice((-1, 1)),
                              flip=a.spin * rng.uniform(0.8, 2.0), col=pal[int(rng.integers(len(pal)))]))

    work = tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(a.out)) or ".")
    static = os.path.join(work, "static.png")
    subprocess.run([sys.executable, f"{SKILL}/frame_card.py", "--art", a.art, "--title", a.title, "--out", static,
                    *FRAME_FLAGS], check=True)
    card = Image.open(static).convert("RGB")
    margin = round(W * 0.020); border = max(2, round(W * 0.008)); banner_h = round(H * 0.085)
    il, it, ir, ib = margin + border, margin + border, W - margin - border, H - margin - border
    banner_top = ib - banner_h
    art_px = np.array(art)

    SS = 3
    for f in range(T):
        layer = Image.new("RGBA", (W * SS, H * SS), (0, 0, 0, 0))
        dl = ImageDraw.Draw(layer)
        for p in parts:
            if a.kind == "leaf":
                age = (f + p["phase"]) % T
                env = min(1.0, age / (0.15 * T), (T - age) / (0.15 * T))
                x = p["x"] + p["sway"] * np.sin(2 * np.pi * p["cyc"] * age / T + p["sph"])
                y = p["y"] + p["v"] * age
                ang = p["rot"] + 2 * np.pi * p["spin"] * age / T + 0.5 * np.sin(2 * np.pi * p["cyc"] * age / T + p["sph"])
                squash = 0.25 + 0.75 * abs(np.cos(2 * np.pi * p["flip"] * age / T))
                op = p["op"]
            else:
                u = (p["u0"] + a.laps * f / T) % 1.0
                s_ = u ** a.ease
                i = min(len(pts) - 1, int(s_ * (len(pts) - 1)))
                half = w0 + (w1 - w0) * s_
                wob = 0.25 * np.sin(2 * np.pi * (a.laps * f / T) * 2 + p["wob"])
                nx, ny = -tang[i, 1], tang[i, 0]
                x = pts[i, 0] + nx * half * (p["off"] + wob)
                y = pts[i, 1] + ny * half * (p["off"] + wob)
                env = min(1.0, u / 0.02, (1 - u) / max(a.fade_end, 1e-3))
                ang = p["rot"] + 2 * np.pi * p["spin"] * a.laps * f / T
                squash = 0.35 + 0.65 * abs(np.cos(2 * np.pi * p["flip"] * a.laps * f / T + p["wob"]))
                op = 1.0
            if env <= 0:
                continue
            al = int(255 * op * env)
            r = p["r"]
            if a.kind == "sand":
                ro = (r + a.outline) * SS
                if a.outline > 0:
                    dl.ellipse([x * SS - ro, y * SS - ro, x * SS + ro, y * SS + ro], fill=INK + (al,))
                dl.ellipse([x * SS - r * SS, y * SS - r * SS, x * SS + r * SS, y * SS + r * SS], fill=p["col"] + (al,))
            else:
                L, Wd = 2.6 * r, max(0.6, 1.1 * r * squash)
                if a.outline > 0:
                    dl.polygon(lens(x * SS, y * SS, (L + 2 * a.outline) * SS, (Wd + 2 * a.outline) * SS, ang),
                               fill=INK + (al,))
                dl.polygon(lens(x * SS, y * SS, L * SS, Wd * SS, ang), fill=p["col"] + (al,))
        for hp in (hops if a.kind == "sand" else []):
            u = (hp["k"] * f / T + hp["ph"]) % 1.0          # one hop: kicked up and sideways, falls back
            x = hp["x"] + hp["side"] * u
            y = hp["y"] - hp["h"] * 4 * u * (1 - u)
            al = int(255 * min(1.0, (1 - u) / 0.15))
            r = hp["r"]; ro = (r + a.outline) * SS
            if a.outline > 0:
                dl.ellipse([x * SS - ro, y * SS - ro, x * SS + ro, y * SS + ro], fill=INK + (al,))
            dl.ellipse([x * SS - r * SS, y * SS - r * SS, x * SS + r * SS, y * SS + r * SS], fill=hp["col"] + (al,))
        layer = layer.resize((W, H), Image.LANCZOS)
        frame = art.copy(); frame.paste(layer, (0, 0), layer)
        if still is not None:
            fr = np.array(frame); fr[still] = art_px[still]; frame = Image.fromarray(fr)
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
