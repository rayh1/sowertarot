#!/usr/bin/env python3
"""Remove a sun or moon disc from a FLAT sky without an AI edit (repair_tools.fill_disc).

Use this instead of edit_card.py for a disc on a plain or gently graded sky: the disc is
filled from the sky around it, so there is no box-shaped patch. Clouds, linework or texture
crossing the disc need edit_card.py (Qwen, tone-matched) instead. The card's render record
gains a `repairs` entry {"method": "fill_disc", box, grow, thresh}, which
render_card.py --from-note replays exactly. Attach the result with attach_image.py --replace.

    python3 fill_disc.py --note "The Weaver" --art <unframed art> --box 570,90,800,320 \\
        --out <scratchpad>/weaver_fill.png --keep-art <scratchpad>/weaver_fill_art.png

--box must enclose the whole disc and its glow with plain sky on every side (the disc is
found as what differs from the sky at the box edge). --grow 24 when a faint rim remains;
--thresh 40 on a graded sky, where the default 18 also catches the gradient.
--halo removes a light rim round dark linework instead (repair_tools.fill_halo, recorded as
{"method": "fill_halo", box, grow}); use --grow 2.
Emits {"ok":true,"out":...,"disc_pixels":...}.
"""
import argparse, json, os, subprocess, sys
from datetime import datetime

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from render_card import FRAME, RECORD_KEY, note_record, write_record  # noqa: E402
from repair_tools import fill_disc, fill_halo  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--note", help="card name; the render record is read from its Joplin note")
    src.add_argument("--card", help="card PNG carrying a tarot_render record")
    ap.add_argument("--art", required=True, help="the card's current unframed art (with earlier repairs applied)")
    ap.add_argument("--box", required=True, help="x0,y0,x1,y1 in unframed-art pixels around the disc and its glow")
    ap.add_argument("--grow", type=int, default=14)
    ap.add_argument("--thresh", type=int, default=18)
    ap.add_argument("--halo", action="store_true", help="fill the light rim round dark linework, not a disc")
    ap.add_argument("--out", required=True, help="framed card PNG to write")
    ap.add_argument("--keep-art", help="also save the filled unframed art here")
    a = ap.parse_args()

    if a.note:
        record = note_record(a.note)
    else:
        raw = Image.open(a.card).info.get(RECORD_KEY)
        if not raw:
            raise SystemExit(f"{a.card} has no {RECORD_KEY} record")
        record = json.loads(raw)
    box = [int(v) for v in a.box.split(",")]
    if a.halo:
        filled, n = fill_halo(Image.open(a.art), box, a.grow)
        entry = {"method": "fill_halo", "box": box, "grow": a.grow, "rim_pixels": n}
    else:
        filled, n = fill_disc(Image.open(a.art), box, a.grow, a.thresh)
        entry = {"method": "fill_disc", "box": box, "grow": a.grow, "thresh": a.thresh, "disc_pixels": n}
    art = os.path.abspath(a.keep_art) if a.keep_art else os.path.join(
        os.path.dirname(os.path.abspath(a.out)), ".fill_art.png")
    filled.save(art)
    fr = subprocess.run([sys.executable, FRAME, "--art", art, "--title", record["title"],
                         "--out", a.out] + record["frame_flags"], capture_output=True, text=True)
    if fr.returncode:
        raise SystemExit(f"frame_card.py failed:\n{fr.stdout}\n{fr.stderr}")
    record.setdefault("repairs", []).append({
        "edited": datetime.now().astimezone().isoformat(timespec="seconds"), **entry})
    write_record(a.out, record)
    if not a.keep_art:
        os.remove(art)
    key = "rim_pixels" if a.halo else "disc_pixels"
    print(json.dumps({"ok": True, "out": a.out, key: n, "art": a.keep_art or None}))


if __name__ == "__main__":
    main()
