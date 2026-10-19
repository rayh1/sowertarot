#!/usr/bin/env python3
"""Repair one defect in a rendered card: Qwen Image 2.1 edit -> masked paste-back -> frame.

The card's render record (from its Joplin note `Tarot/Cards/<name>` § Render Record, or
from a card PNG's `tarot_render` chunk via --card) names the unframed ComfyUI output,
title and frame flags. The script edits that unframed art at full size with
assets/tarot-card-qwen-edit.json, keeps the edit only inside --box (soft edge
--feather), evens the box's tone to the original (repair_tools.tone_match; Qwen shifts
it 4-16 levels, which shows as a patch; --no-tone-match to skip), frames the result and writes a card PNG whose record gains a `repairs`
entry. Attach it with attach_image.py --replace.

    python3 edit_card.py --note "The Forge" --seed 1 --box 380,0,660,200 \
        --instruction "Remove the gold star at the top." --out <scratchpad>/forge_s1.png

Repairs stack: pass the output of a previous repair as --card (with --art pointing
at its unframed art, see --keep-art) to fix a second defect.
Emits {"ok":true,"out":...,"seed":...,"comfy_file":...}.
"""
import argparse, json, os, subprocess, sys, urllib.request
from datetime import datetime

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from render_card import (FRAME, RECORD_KEY, SKILL, comfy_version,  # noqa: E402
                         note_record, paste_back, post_graph, upload_image, write_record)
from repair_tools import tone_match  # noqa: E402

WORKFLOW = os.path.join(SKILL, "assets", "tarot-card-qwen-edit.json")
KEEP = (" Keep everything else, including the woodcut linework and hatching, exactly the same.")


def main():
    ap = argparse.ArgumentParser()
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--note", help="card name; the render record is read from its Joplin note")
    src.add_argument("--card", help="card PNG carrying a tarot_render record")
    ap.add_argument("--art", help="unframed art to edit (default: the record's comfy_file from ComfyUI)")
    ap.add_argument("--instruction", required=True, help="what to change, in plain words")
    ap.add_argument("--box", required=True, help="x0,y0,x1,y1 in unframed-art pixels; only this area is kept")
    ap.add_argument("--feather", type=int, default=24, help="soft-edge width of the box in pixels")
    ap.add_argument("--no-tone-match", action="store_true",
                    help="keep Qwen's tone inside the box (by default it is evened to the original, "
                         "since Qwen shifts it 4-16 levels and the box shows as a patch)")
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("--out", required=True, help="framed card PNG to write")
    ap.add_argument("--keep-art", help="also save the repaired unframed art here")
    ap.add_argument("--comfy-url", default=os.environ.get("COMFY_LOCAL_URL", "http://127.0.0.1:8188"))
    a = ap.parse_args()
    url = a.comfy_url

    if a.note:
        record = note_record(a.note)
    else:
        raw = Image.open(a.card).info.get(RECORD_KEY)
        if not raw:
            raise SystemExit(f"{a.card} has no {RECORD_KEY} record")
        record = json.loads(raw)
    if a.art:
        art = a.art
    else:
        art = os.path.join(os.path.dirname(os.path.abspath(a.out)), ".edit_src.png")
        try:
            urllib.request.urlretrieve(f"{url}/view?filename={record['comfy_file']}&type=output", art)
        except Exception as e:
            raise SystemExit(f"{record['comfy_file']} not in ComfyUI output ({e}); pass --art "
                             "(re-render it from the record's workflow)")
    orig = Image.open(art).convert("RGB")

    up = upload_image(url, art)

    graph = json.load(open(WORKFLOW))
    prompt = a.instruction.strip()
    if "exactly the same" not in prompt:
        prompt += KEEP
    for node in graph.values():
        cls, inp = node["class_type"], node["inputs"]
        if cls == "LoadImage":
            inp["image"] = up
        elif cls == "TextEncodeQwenImage21":
            inp["prompt"] = prompt
        elif cls == "KSampler":
            inp["seed"] = a.seed
    fn = post_graph(url, graph)[0]
    edit_path = os.path.join(os.path.dirname(os.path.abspath(a.out)), ".edit_out.png")
    urllib.request.urlretrieve(f"{url}/view?filename={fn}&type=output", edit_path)
    edit_img = Image.open(edit_path)
    edit_graph = json.loads(edit_img.info["prompt"])
    edit = edit_img.convert("RGB")
    x0, y0, x1, y1 = map(int, a.box.split(","))
    repaired = os.path.abspath(a.keep_art) if a.keep_art else os.path.join(
        os.path.dirname(os.path.abspath(a.out)), ".edit_repaired.png")
    pasted = paste_back(orig, edit, (x0, y0, x1, y1), a.feather)
    offset = None
    if not a.no_tone_match:
        pasted, offset = tone_match(orig, pasted, (x0, y0, x1, y1), a.feather)
    pasted.save(repaired)

    fr = subprocess.run([sys.executable, FRAME, "--art", repaired, "--title", record["title"],
                         "--out", a.out] + record["frame_flags"], capture_output=True, text=True)
    if fr.returncode:
        raise SystemExit(f"frame_card.py failed:\n{fr.stdout}\n{fr.stderr}")

    record.setdefault("repairs", []).append({
        "edited": datetime.now().astimezone().isoformat(timespec="seconds"),
        "comfyui_version": comfy_version(url), "comfy_file": fn, "seed": a.seed,
        "instruction": prompt, "box": [x0, y0, x1, y1], "feather": a.feather,
        "tone_match": not a.no_tone_match,
        "tone_offset": None if offset is None else [round(float(v), 1) for v in offset],
        "workflow": edit_graph,
    })
    write_record(a.out, record)
    for p in (edit_path,) + (() if a.keep_art else (repaired,)) + (() if a.art else (art,)):
        try:
            os.remove(p)
        except OSError:
            pass
    print(json.dumps({"ok": True, "out": a.out, "seed": a.seed, "comfy_file": fn,
                      "art": a.keep_art or None}))


if __name__ == "__main__":
    main()
