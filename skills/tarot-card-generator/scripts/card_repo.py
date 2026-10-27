"""Card files in the repository this skill lives in: content/cards/<slug>.md, content/media/, content/checksums.txt.

A card file is front matter of `key: <JSON value>` lines (CARD_KEYS order; the daily draw and
scripts/draw_check.py parse them) followed by the card's Markdown: title heading, tagline, image line,
## Visual Description, ## Archetypal Essence, ## Render Prompt, ## Render Record. The front matter is the deck
index: there is no separate registry.

Settings, git and push come from the daily skill's daily.py (same repository), so both skills share one
implementation: the repository root (TAROT_REPO overrides it), settings.env/settings.local.env, the Sower Tarot
committer, the gh-token credential helper, `pull --ff-only`, and push with rebase onto a moved main.
"""
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
SKILL = HERE.parent
REPO = Path(os.environ.get("TAROT_REPO") or SKILL.parent.parent)
sys.path.insert(0, str(REPO / "skills" / "tarot-daily-reading" / "scripts"))
import daily  # noqa: E402  (shares REPO: both follow TAROT_REPO or their own place in the repository)

CONTENT = REPO / "content"
CARDS = CONTENT / "cards"
MEDIA = CONTENT / "media"
SETTINGS = daily.SETTINGS
WORK = Path(SETTINGS["SOWER_WORK"])

# Front matter keys in file order; a key with no value is left out. The site needs title, concept, key_terms,
# created and image (src/content.config.ts); joplin_note exists only on the 37 cards migrated from Joplin.
CARD_KEYS = ["title", "concept", "key_terms", "created", "seed", "image_status", "prompt_status", "image", "clip",
             "joplin_note", "sown_by", "renders_tried"]
KEEP_NULL = {"seed"}                 # written as null when set to None (an external render has no seed)
TAGLINE = "*An original tarot card in the Rider-Waite tradition*"
PLACEHOLDER = "_(image pending)_"
RECORD_KEY = "tarot_render"          # PNG text chunk written by render_card.py
RECORD_HEADING = "## Render Record"

slug = daily.slug
fail = daily.fail


def card_path(name):
    """content/cards/<slug>.md for a card title or slug."""
    return CARDS / f"{slug(name)}.md"


def read_card(name):
    """(fields, body) of an existing card file."""
    path = card_path(name)
    if not path.exists():
        fail(f"no card file {path.relative_to(REPO)} (card names: {', '.join(all_cards())})")
    return daily.split_front_matter(path.read_text(encoding="utf-8"))


def write_card(name, fields, body):
    unknown = set(fields) - set(CARD_KEYS)
    if unknown:
        fail(f"unknown front matter keys: {', '.join(sorted(unknown))}")
    head = "".join(f"{k}: {json.dumps(fields[k], ensure_ascii=False)}\n" for k in CARD_KEYS
                   if fields.get(k) is not None or (k in KEEP_NULL and k in fields))
    CARDS.mkdir(parents=True, exist_ok=True)
    card_path(name).write_text(f"---\n{head}---\n{body}", encoding="utf-8")


def all_cards():
    """{title: fields} of every card file in the working tree, sorted by title."""
    return {t: c["fields"] for t, c in sorted(daily.tree_cards().items())}


def section(body, heading):
    """Text under `## heading` up to the next `## ` heading, or None."""
    m = re.search(rf"^## {re.escape(heading)}\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    return m.group(1).strip() if m else None


def card_record(name):
    """The render record JSON from the card file's ## Render Record section."""
    _, body = read_card(name)
    if RECORD_HEADING not in body:
        fail(f"{card_path(name).relative_to(REPO)} has no {RECORD_HEADING}: render the card with --scene instead")
    m = re.search(r"```json\n(.*?)\n```", body[body.index(RECORD_HEADING):], re.S)
    return json.loads(m.group(1))


def png_record(path):
    """The render record embedded in a card PNG by render_card.py, or None."""
    raw = Image.open(path).info.get(RECORD_KEY)
    return json.loads(raw) if raw else None


def record_section(record):
    """Markdown for the card file's ## Render Record section."""
    graphs = [record.get("workflow", {})] + [r.get("workflow", {}) for r in record.get("repairs", [])]
    models = []
    for node in (n for g in graphs for n in g.values()):
        inp = node.get("inputs", {})
        for key in ("ckpt_name", "unet_name", "clip_name", "clip_name1", "clip_name2", "vae_name", "model_name"):
            if isinstance(inp.get(key), str):
                models.append(f"`{inp[key]}`")
        if isinstance(inp.get("lora_name"), str):
            models.append(f"`{inp['lora_name']}` (LoRA, strength {inp.get('strength_model')})")
    lines = [
        RECORD_HEADING, "",
        "<details>",
        f"<summary>Seed {record.get('seed')} · {record.get('comfy_file')} — full render recipe</summary>",
        "",
        "Written by `place_card.py` with the image above. It holds everything needed to "
        "re-render that image without the ComfyUI output file — `render_card.py --from-card \"<title>\"` does all "
        "of it: post `workflow` to ComfyUI's `/prompt` endpoint, then run `frame_card.py --art <output> --title "
        "<title> <frame_flags>`; for each entry in `repairs`, first apply it to the unframed art: a Qwen "
        "edit runs its `workflow` and keeps the result only inside `box` (soft edge `feather`), then, "
        "if `tone_match` is true, evens the box's tone (`repair_tools.tone_match`), as `edit_card.py` "
        "does; a `method: fill_disc` entry fills the disc in `box` from the sky around it with its "
        "`grow`/`thresh` (`repair_tools.fill_disc`, no AI model); a `method: fill_halo` entry fills "
        "the light rim round the linework in `box` from the sky with its `grow` (`repair_tools.fill_halo`, "
        "no AI model). The model files named below must exist in ComfyUI.", "",
        f"- Rendered: {record.get('rendered')} · ComfyUI {record.get('comfyui_version')} "
        f"· output `{record.get('comfy_file')}`",
        f"- Seed: {record.get('seed')}",
        f"- Models: {', '.join(dict.fromkeys(models)) or 'unknown'}",
        f"- Frame flags: `{' '.join(record.get('frame_flags', []))}`",
    ]
    for r in record.get("repairs", []):
        if r.get("method") == "fill_disc":
            lines.append(f"- Repair: sun/moon filled from the sky, no AI edit (box {r.get('box')}, "
                         f"grow {r.get('grow')}, thresh {r.get('thresh')}, {r.get('edited')})")
        elif r.get("method") == "fill_halo":
            lines.append(f"- Repair: light rim round the linework filled from the sky, no AI edit "
                         f"(box {r.get('box')}, grow {r.get('grow')}, {r.get('edited')})")
        else:
            lines.append(f"- Repair: {r.get('instruction')} (box {r.get('box')}, seed {r.get('seed')}, "
                         f"output `{r.get('comfy_file')}`{', tone-matched' if r.get('tone_match') else ''}, "
                         f"{r.get('edited')})")
    if record.get("note"):
        lines.append(f"- Note: {record['note']}")
    lines += ["", "```json", json.dumps(record, indent=2, ensure_ascii=False), "```", "", "</details>"]
    return "\n".join(lines) + "\n"


def upsert_record(body, section_md):
    """Replace the ## Render Record section, append it, or (None) remove it."""
    pat = re.compile(r"\n*^" + re.escape(RECORD_HEADING) + r"\n.*?(?=^## |\Z)", re.S | re.M)
    body = pat.sub("\n", body).rstrip() + "\n"
    return body if section_md is None else f"{body}\n{section_md}"


def review_root():
    """Where candidates go for the user to look at: SOWER_REVIEW (an rclone remote such as dropbox:Tarot, or a
    folder, relative to the repository), or <SOWER_WORK>/review when it is empty."""
    root = SETTINGS.get("SOWER_REVIEW", "").rstrip("/")
    if not root:
        return str(WORK / "review")
    return root if ":" in root.split("/")[0] else str((REPO / root).resolve())


def label(*files):
    """Write the AI-generated label into reference files (scripts/label_media.sh, exiftool, in place)."""
    r = subprocess.run(["sh", str(REPO / "scripts" / "label_media.sh"), *map(str, files)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        fail(f"label_media.sh: {(r.stderr or r.stdout).strip()}")


def checksums(cmd):
    """scripts/checksums.py write|check on this repository's content/."""
    r = subprocess.run([sys.executable, str(REPO / "scripts" / "checksums.py"), cmd, "--content", str(CONTENT)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        fail(f"checksums.py {cmd}: {(r.stdout + r.stderr).strip()}", 1)
    return r.stdout.strip()


def copy_bytes(src, dest):
    """Copy a file byte for byte (never through an image library: the PNG's tarot_render record must survive)."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dest)


def place_labelled(src, dest):
    """Copy src to the reference file dest with the AI-generated label: label a copy in <SOWER_WORK>/tmp first,
    so a failed label leaves content/media/ untouched."""
    tmp = WORK / "tmp" / dest.name
    copy_bytes(src, tmp)
    try:
        label(tmp)
    except SystemExit:
        tmp.unlink(missing_ok=True)
        raise
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(tmp, dest)          # not os.replace: SOWER_WORK may be on another filesystem
