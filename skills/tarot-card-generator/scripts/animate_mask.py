#!/usr/bin/env python3
"""Draw and check an animation mask for one card (§ Animate a card, A2). Coordinates are pixels of the
trimmed 1024 x 1792 art (art.png in the card's folder).

  animate_mask.py grid  <card dir>                       -> grid.png: art with a labelled 100 px grid (half size)
  animate_mask.py make  <card dir> --include "x,y x,y ..." [--include ...] [--exclude "x,y ..."] [--blur 10]
                                                         -> mask.png (white = moves) + preview.png (pink = moves)
  animate_mask.py zoom  <card dir> x0,y0,x1,y1           -> zoom.png: full-size crop of preview.png, to check edges
  animate_mask.py crop  <card dir> x0,y0,x1             -> crop.txt + input_576x1024.png from a 9:16 box of the art
                                                         (y1 follows from the width), for elements too small to animate
                                                         at full-card size; the box is drawn green on preview.png
--include polygons are filled white, then --exclude polygons black (figures, faces, hands, with a margin).
"""
import argparse, os
from PIL import Image, ImageDraw, ImageFilter


def pts(s):
    return [tuple(int(float(v)) for v in p.split(",")) for p in s.split()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["grid", "make", "zoom", "crop"])
    ap.add_argument("dir")
    ap.add_argument("box", nargs="?")
    ap.add_argument("--include", action="append", default=[])
    ap.add_argument("--exclude", action="append", default=[])
    ap.add_argument("--blur", type=float, default=10)
    a = ap.parse_args()
    art = Image.open(os.path.join(a.dir, "art.png")).convert("RGB")
    W, H = art.size
    if a.cmd == "grid":
        g = art.copy(); d = ImageDraw.Draw(g)
        for x in range(0, W, 100):
            d.line([(x, 0), (x, H)], fill=(255, 0, 0), width=2)
            for y in range(50, H, 300): d.text((x + 4, y), str(x), fill=(255, 0, 0))
        for y in range(0, H, 100):
            d.line([(0, y), (W, y)], fill=(255, 0, 0), width=2)
            for x in range(50, W, 300): d.text((x, y + 4), str(y), fill=(255, 0, 0))
        g.resize((W // 2, H // 2)).save(os.path.join(a.dir, "grid.png"))
    elif a.cmd == "make":
        m = Image.new("L", (W, H), 0); d = ImageDraw.Draw(m)
        for p in a.include: d.polygon(pts(p), fill=255)
        for p in a.exclude: d.polygon(pts(p), fill=0)
        if a.blur: m = m.filter(ImageFilter.GaussianBlur(a.blur))
        m.save(os.path.join(a.dir, "mask.png"))
        prev = Image.composite(Image.new("RGB", (W, H), (255, 0, 255)), art, m.point(lambda v: v // 2))
        cp = os.path.join(a.dir, "crop.txt")
        if os.path.exists(cp):
            ImageDraw.Draw(prev).rectangle([int(v) for v in open(cp).read().split(",")], outline=(0, 200, 0), width=6)
        prev.resize((W // 2, H // 2)).save(os.path.join(a.dir, "preview.png"))
    elif a.cmd == "crop":
        x0, y0, x1 = (int(v) for v in a.box.split(",")[:3])
        y1 = y0 + round((x1 - x0) * 16 / 9)
        if x0 < 0 or x1 > W or y0 < 0 or y1 > H:
            raise SystemExit(f"box {x0},{y0},{x1},{y1} leaves the {W}x{H} art")
        open(os.path.join(a.dir, "crop.txt"), "w").write(f"{x0},{y0},{x1},{y1}\n")
        art.crop((x0, y0, x1, y1)).resize((576, 1024), Image.LANCZOS).save(os.path.join(a.dir, "input_576x1024.png"))
        print(f"crop.txt = {x0},{y0},{x1},{y1}")
    else:
        x0, y0, x1, y1 = (int(v) for v in a.box.split(","))
        m = Image.open(os.path.join(a.dir, "mask.png"))
        Image.composite(Image.new("RGB", (W, H), (255, 0, 255)), art, m.point(lambda v: v // 2)).crop((x0, y0, x1, y1)).save(os.path.join(a.dir, "zoom.png"))


if __name__ == "__main__":
    main()
