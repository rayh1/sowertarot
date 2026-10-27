#!/usr/bin/env python3
"""Seed sheet for ONE existing card: render its scene at many seeds, then build a
contact sheet of thumbnails labelled with seed and image number.

Resumable: renders already on disk are skipped, so a stalled run can be restarted.
Only renders — no card file, media or commit change (SKILL.md § Scope fence).

  python3 scripts/seed_sheet.py --card "The Well" --scene "<scene>" \
      --seeds 24 --out-dir work/cards/the-well/seed-sheet
"""
import argparse
import json
import math
import random
import subprocess
import sys
import time
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def pick_seeds(key, n):
    """Deterministic per output folder, so a restart renders the same seeds and a
    new round (new --out-dir) gets new ones."""
    rng = random.Random(key)
    return sorted({rng.randrange(1, 2**31) for _ in range(n * 2)})[:n] if n else []


def render(card, scene, seed, out, retries):
    for attempt in range(1, retries + 1):
        p = subprocess.run(
            [sys.executable, str(HERE / "render_card.py"), "--scene", scene,
             "--title", card, "--seed", str(seed), "--out", str(out),
             # keep the unframed art: repairs start from it, and the server may not keep its output
             "--keep-raw", str(out.with_name(out.stem + "_art.png"))],
            capture_output=True, text=True)
        last = (p.stdout.strip().splitlines() or [""])[-1]
        if p.returncode == 0 and out.exists():
            try:
                return json.loads(last)
            except json.JSONDecodeError:
                return {"ok": True, "seed": seed}
        log(f"  seed {seed} attempt {attempt} failed (rc {p.returncode}): "
            f"{(p.stderr or last).strip()[-400:]}")
        time.sleep(30)
    return None


def contact_sheet(items, dest, cols, thumb_w):
    tiles = []
    for it in items:
        im = Image.open(it["path"]).convert("RGB")
        h = round(im.height * thumb_w / im.width)
        tiles.append((it, im.resize((thumb_w, h), Image.LANCZOS)))
    th = max(t.height for _, t in tiles)
    label_h, pad = 34, 10
    rows = math.ceil(len(tiles) / cols)
    sheet = Image.new("RGB", (cols * (thumb_w + pad) + pad,
                              rows * (th + label_h + pad) + pad), "white")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.truetype(FONT, 20)
    for i, (it, t) in enumerate(tiles):
        x = pad + (i % cols) * (thumb_w + pad)
        y = pad + (i // cols) * (th + label_h + pad)
        sheet.paste(t, (x, y))
        num = it.get("num")
        label = f"seed {it['seed']}" + (f"  #{num}" if num else "")
        draw.text((x + 4, y + th + 6), label, fill="black", font=font)
    sheet.save(dest, quality=88)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--card", required=True)
    ap.add_argument("--scene", required=True)
    ap.add_argument("--seeds", type=int, default=24)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--cols", type=int, default=6)
    ap.add_argument("--thumb-w", type=int, default=300)
    ap.add_argument("--retries", type=int, default=3)
    a = ap.parse_args()

    slug = a.card.lower().replace(" ", "-")
    out_dir = Path(a.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "scene.txt").write_text(a.scene + "\n")
    index_path = out_dir / "index.json"
    index = json.loads(index_path.read_text()) if index_path.exists() else {}

    seeds = pick_seeds(out_dir.name, a.seeds)
    for i, seed in enumerate(seeds, 1):
        out = out_dir / f"{slug}_{seed}.png"
        if out.exists() and str(seed) in index:
            continue
        t0 = time.time()
        res = render(a.card, a.scene, seed, out, a.retries)
        if res is None:
            log(f"{a.card} {i}/{len(seeds)} seed {seed}: GAVE UP")
            continue
        cf = res.get("comfy_file", "")
        digits = "".join(c for c in cf if c.isdigit())
        index[str(seed)] = {"comfy_file": cf, "num": int(digits) if digits else None}
        index_path.write_text(json.dumps(index, indent=1))
        log(f"{a.card} {i}/{len(seeds)} seed {seed} {cf} ({time.time()-t0:.0f}s)")

    items = [{"seed": s, "path": out_dir / f"{slug}_{s}.png", **index[str(s)]}
             for s in seeds if str(s) in index and (out_dir / f"{slug}_{s}.png").exists()]
    if not items:
        log(f"{a.card}: no renders, no sheet")
        sys.exit(1)
    dest = out_dir.parent / f"{out_dir.name}.jpg"
    contact_sheet(items, dest, a.cols, a.thumb_w)
    log(f"{a.card}: sheet {dest} ({len(items)}/{len(seeds)} renders)")
    print(json.dumps({"ok": True, "card": a.card, "sheet": str(dest),
                      "rendered": len(items), "wanted": len(seeds)}))


if __name__ == "__main__":
    main()
