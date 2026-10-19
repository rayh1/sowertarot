#!/usr/bin/env python3
"""Composite a Rider-Waite-style tarot frame + title banner over a raw art image.

Draws a deterministic layout so every card matches: a beige paper margin, a thin
black border, the art filling the interior, and a bottom banner carrying the
title in a real serif font (pixel-perfect text the diffusion model can't render).

Usage:
    python3 frame_card.py --art in.png --title "THE KEYSTONE" --out out.png

The art is center-cropped to fill the interior, so any input aspect works; pass
art already close to the card aspect (~1:1.75) to avoid heavy cropping.
"""
import argparse, random
from PIL import Image, ImageDraw, ImageFont

FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSerifBold.ttf",
]


def load_font(path, size):
    return ImageFont.truetype(path or next(f for f in FONT_CANDIDATES), size)


def cover_resize(img, box_w, box_h):
    """Scale to cover (box_w, box_h), then center-crop to exactly that size."""
    src_w, src_h = img.size
    scale = max(box_w / src_w, box_h / src_h)
    new = img.resize((max(1, round(src_w * scale)), max(1, round(src_h * scale))), Image.LANCZOS)
    left = (new.width - box_w) // 2
    top = (new.height - box_h) // 2
    return new.crop((left, top, left + box_w, top + box_h))


def paper_fill(size, base, noise=6):
    """Flat beige with subtle per-pixel noise so the frame reads as aged paper."""
    w, h = size
    img = Image.new("RGB", size, base)
    if noise > 0:
        px = img.load()
        for y in range(h):
            for x in range(w):
                d = random.randint(-noise, noise)
                px[x, y] = tuple(max(0, min(255, c + d)) for c in base)
    return img


def fit_title(draw, text, font_path, max_w, max_h):
    """Largest serif size whose rendered text fits max_w x max_h."""
    lo, hi, best = 8, max_h, None
    while lo <= hi:
        mid = (lo + hi) // 2
        font = load_font(font_path, mid)
        l, t, r, b = draw.textbbox((0, 0), text, font=font)
        if (r - l) <= max_w and (b - t) <= max_h:
            best = font; lo = mid + 1
        else:
            hi = mid - 1
    return best or load_font(font_path, 8)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--art", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--font", default=None, help="path to a .ttf; default serif auto-picked")
    ap.add_argument("--paper", default="216,199,158", help="beige RGB")
    ap.add_argument("--ink", default="26,22,18", help="border/text RGB")
    ap.add_argument("--margin-frac", type=float, default=0.020)
    ap.add_argument("--border-frac", type=float, default=0.008)
    ap.add_argument("--banner-frac", type=float, default=0.085)
    ap.add_argument("--noise", type=int, default=6)
    ap.add_argument("--art-crop", type=float, default=0.0,
                    help="trim this fraction off each edge of the input art before framing "
                         "(removes a border the model drew, e.g. 0.03 for FLUX)")
    args = ap.parse_args()

    paper = tuple(int(x) for x in args.paper.split(","))
    ink = tuple(int(x) for x in args.ink.split(","))
    art = Image.open(args.art).convert("RGB")
    if args.art_crop > 0:
        aw, ah = art.size
        dx, dy = round(aw * args.art_crop), round(ah * args.art_crop)
        art = art.crop((dx, dy, aw - dx, ah - dy)).resize((aw, ah), Image.LANCZOS)
    W, H = art.size

    margin = round(W * args.margin_frac)
    border = max(2, round(W * args.border_frac))
    banner_h = round(H * args.banner_frac)

    inner_l, inner_t = margin + border, margin + border
    inner_r, inner_b = W - margin - border, H - margin - border
    banner_top = inner_b - banner_h

    canvas = paper_fill((W, H), paper, args.noise)
    # art fills the whole interior (banner is drawn over its bottom strip)
    interior = cover_resize(art, inner_r - inner_l, inner_b - inner_t)
    canvas.paste(interior, (inner_l, inner_t))

    draw = ImageDraw.Draw(canvas)
    # bottom banner (aged paper) over the art
    banner = paper_fill((inner_r - inner_l, inner_b - banner_top), paper, args.noise)
    canvas.paste(banner, (inner_l, banner_top))

    # black frame + banner separator
    for i in range(border):
        draw.rectangle([margin + i, margin + i, W - margin - 1 - i, H - margin - 1 - i], outline=ink)
    sep = max(2, border // 2)
    draw.rectangle([inner_l, banner_top, inner_r - 1, banner_top + sep], fill=ink)

    # title
    title = args.title.upper()
    pad_x = round((inner_r - inner_l) * 0.06)
    font = fit_title(draw, title, args.font, (inner_r - inner_l) - 2 * pad_x, round(banner_h * 0.55))
    l, t, r, b = draw.textbbox((0, 0), title, font=font)
    tx = inner_l + ((inner_r - inner_l) - (r - l)) / 2 - l
    ty = banner_top + sep + ((inner_b - (banner_top + sep)) - (b - t)) / 2 - t
    draw.text((tx, ty), title, font=font, fill=ink)

    canvas.save(args.out)
    print(f"wrote {args.out} ({W}x{H}) title='{title}' font_size={font.size}")


if __name__ == "__main__":
    main()
