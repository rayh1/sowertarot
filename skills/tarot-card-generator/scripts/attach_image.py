#!/usr/bin/env python3
"""
Attach a rendered card image to its Joplin card note and flip the registry.

This is the bundled attach helper for the `tarot-card-generator` skill. It is
called from Step 5 of that skill's workflow (fresh card attach) and from
Step 5i option 2 (deferred-card follow-up). Both cases are the same operation:
transition a card from `image_status: pending` to `image_status: present`.

The skill's SKILL.md is the behavioral spec. This script is the implementation.

Pipeline per card:
  1. Resolve Joplin API URL + token (env or ~/.config/joplink/settings.json)
  2. Preflight the Joplin Web Clipper service
  3. Open the image (PNG/JPG/WEBP), compress to JPEG 1024x1536 Q85 in memory
  4. Upload as a Joplin resource (POST /resources, multipart form data)
  5. Find the card note at `Tarot/Cards/<Card Name>` by exact title
  6. Replace `_(image pending — attach manually)_` in its body with
     `![<Card Name>](:/<resource-id>)` and PUT the note back
  7. Find the card's entry in `Tarot/Registry` by name, flip `image_status`
     from `pending` to `present`, refresh `metadata.last_updated`, PUT back

Render record: a card PNG from render_card.py carries a `tarot_render` text
chunk (seed, title, scene, full prompt, frame flags, ComfyUI version, executed
ComfyUI graph). Step 6 also writes it into the note as `## Render Record`, so
the note alone is enough to re-render the image. An image without a record
(external render) attaches with a warning; on --replace any old record is
removed, because it would describe the previous image.

Idempotent: if the note body already has an image reference (not the
placeholder), or the registry entry is already `present`, the corresponding
step is skipped with a notice. The source image file is never deleted or moved.

Requirements:
  pip install requests Pillow

Usage:
  python3 attach_image.py --card "The Cairn" --image /workspace/tarot/card_the-cairn.png
  python3 attach_image.py --card "The Cairn" --image /path/to/any.png --dry-run
  python3 attach_image.py --card "The Cairn" --image /path/to/new.png --replace

Modes:
  Default (fresh attach): Attaches the image. If the note already has an image,
    skips upload (prevents orphan resource) and only reconciles the registry.
  --replace: Replaces an already-attached image with the new one. Uploads a
    fresh resource and swaps the note's image reference. The previously
    attached Joplin resource is left as an unreferenced orphan in the Joplin
    DB — remove it manually via the Joplin UI if storage matters. The source
    PNG is still never deleted.
"""
import argparse
import io
import json
import os
import re
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    sys.exit("Install requests: pip install requests")
try:
    from PIL import Image
except ImportError:
    sys.exit("Install Pillow: pip install Pillow")


# ---- Config resolution (env → joplink CLI settings file) ----

def _config_from_env():
    token = os.environ.get("JOPLIN_TOKEN") or os.environ.get("JOPLINK_JOPLIN_TOKEN")
    if not token:
        return None
    url = os.environ.get("JOPLIN_API_URL") or os.environ.get("JOPLINK_JOPLIN_BASE_URL")
    return (url or "http://host.docker.internal:41184"), token, "env"


def _config_from_joplink_cli():
    p = os.path.expanduser("~/.config/joplink/settings.json")
    if not os.path.exists(p):
        return None
    try:
        with open(p) as f:
            data = json.load(f)
        token = data.get("joplin_token")
        if not token:
            return None
        url = data.get("joplin_base_url") or "http://host.docker.internal:41184"
        return url, token, "~/.config/joplink/settings.json"
    except Exception:
        return None


def _resolve_config():
    for getter in (_config_from_env, _config_from_joplink_cli):
        r = getter()
        if r:
            return r
    sys.exit("No Joplin token found. Set JOPLIN_TOKEN or write ~/.config/joplink/settings.json with keys 'joplin_base_url' and 'joplin_token'.")


API, TOKEN, TOKEN_SOURCE = _resolve_config()
TIMEOUT = (5, 30)
TARGET_SIZE = (1024, 1536)
JPEG_QUALITY = 85
PLACEHOLDER = "_(image pending — attach manually)_"
RECORD_KEY = "tarot_render"  # PNG text chunk written by render_card.py
RECORD_HEADING = "## Render Record"


# ---- HTTP helpers ----

def api_get(path, **params):
    params["token"] = TOKEN
    r = requests.get(f"{API}{path}", params=params, timeout=TIMEOUT)
    r.raise_for_status()
    return r.json()


def api_post(path, json_body=None, files=None, data=None):
    params = {"token": TOKEN}
    r = requests.post(f"{API}{path}", params=params, json=json_body, files=files, data=data, timeout=TIMEOUT)
    r.raise_for_status()
    return r.json()


def api_put(path, json_body):
    params = {"token": TOKEN}
    r = requests.put(f"{API}{path}", params=params, json=json_body, timeout=TIMEOUT)
    r.raise_for_status()
    return r.json()


def preflight():
    try:
        r = requests.get(f"{API}/ping", timeout=(3, 5))
        if "JoplinClipperServer" not in r.text:
            sys.exit(f"Reached {API}/ping but response doesn't look like Joplin: {r.text!r}")
    except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout):
        sys.exit(
            f"Timeout talking to {API}. Is Joplin running with Web Clipper enabled?"
        )
    except requests.exceptions.ConnectionError as e:
        sys.exit(f"Cannot connect to {API}: {e}")
    try:
        api_get("/folders", limit=1)
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            sys.exit("401 Unauthorized — token is wrong or missing.")
        raise


# ---- Joplin lookups ----

def find_folder_by_title(title, parent_id=""):
    page = 1
    while True:
        res = api_get("/folders", page=page, fields="id,title,parent_id")
        for f in res.get("items", []):
            if f["title"] == title and (f.get("parent_id") or "") == parent_id:
                return f["id"]
        if not res.get("has_more"):
            return None
        page += 1


def find_note_in_folder(title, folder_id):
    page = 1
    while True:
        res = api_get(f"/folders/{folder_id}/notes", page=page, fields="id,title,body")
        for n in res.get("items", []):
            if n["title"] == title:
                return n
        if not res.get("has_more"):
            return None
        page += 1


# ---- Image + note + registry updates ----

def compress_image(image_path):
    img = Image.open(image_path).convert("RGB")
    img.thumbnail(TARGET_SIZE, Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=JPEG_QUALITY, optimize=True)
    return buf.getvalue()


def upload_resource(jpeg_bytes, title):
    files = {"data": ("card.jpg", jpeg_bytes, "image/jpeg")}
    props = json.dumps({"title": title})
    return api_post("/resources", files=files, data={"props": props})["id"]


def update_note_body(note, resource_id, card_name, replace_existing=False):
    body = note["body"]
    image_md = f"![{card_name}](:/{resource_id})"
    if PLACEHOLDER in body:
        return body.replace(PLACEHOLDER, image_md), "placeholder_replaced"
    if re.search(r"!\[[^\]]*\]\(:/[a-f0-9]+\)", body):
        if replace_existing:
            new_body = re.sub(r"!\[[^\]]*\]\(:/[a-f0-9]+\)", image_md, body, count=1)
            return new_body, "replaced_existing_image"
        return None, "already_has_image"
    new_body, count = re.subn(
        r"(\*An original tarot card in the Rider-Waite tradition\*\s*\n)",
        rf"\1\n{image_md}\n",
        body,
        count=1,
    )
    if count > 0:
        return new_body, "inserted_after_tagline"
    return None, "pattern_not_found"


def read_record(image_path):
    """Return the render record embedded by render_card.py, or None."""
    raw = Image.open(image_path).info.get(RECORD_KEY)
    return json.loads(raw) if raw else None


def record_section(record):
    """Markdown for the note's `## Render Record` section."""
    graphs = [record.get("workflow", {})] + [r.get("workflow", {}) for r in record.get("repairs", [])]
    models = []
    for node in (n for g in graphs for n in g.values()):
        inp = node.get("inputs", {})
        for key in ("ckpt_name", "unet_name", "clip_name", "clip_name1", "clip_name2",
                    "vae_name", "model_name"):
            if isinstance(inp.get(key), str):
                models.append(f"`{inp[key]}`")
        if isinstance(inp.get("lora_name"), str):
            models.append(f"`{inp['lora_name']}` (LoRA, strength {inp.get('strength_model')})")
    lines = [
        RECORD_HEADING, "",
        "<details>",
        f"<summary>Seed {record.get('seed')} · {record.get('comfy_file')} — full render recipe</summary>",
        "",
        "Written by `attach_image.py` with the image above. It holds everything needed to "
        "re-render that image without the ComfyUI output file — `render_card.py --from-note \"<title>\"` does all of it: post `workflow` to ComfyUI's "
        "`/prompt` endpoint, then run `frame_card.py --art <output> --title <title> "
        "<frame_flags>`; for each entry in `repairs`, first apply it to the unframed art: a Qwen "
        "edit runs its `workflow` and keeps the result only inside `box` (soft edge `feather`), then, "
        "if `tone_match` is true, evens the box's tone (`repair_tools.tone_match`), as `edit_card.py` "
        "does; a `method: fill_disc` entry fills the disc in `box` from the sky around it with its "
        "`grow`/`thresh` (`repair_tools.fill_disc`, no AI model); a `method: fill_halo` entry fills "
        "the light rim round the linework in `box` from the sky with its `grow` (`repair_tools.fill_halo`, "
        "no AI model). The model files named below must "
        "exist in ComfyUI.", "",
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
    lines += ["", "```json", json.dumps(record, indent=2, ensure_ascii=False), "```", "",
              "</details>"]
    return "\n".join(lines) + "\n"


def upsert_record(body, section):
    """Replace the note's `## Render Record` section, append it, or (None) remove it."""
    pat = re.compile(r"\n*^" + re.escape(RECORD_HEADING) + r"\n.*?(?=^## |\Z)", re.S | re.M)
    body = pat.sub("\n", body).rstrip() + "\n"
    return body if section is None else f"{body}\n{section}"


def update_registry_status(reg_body, card_name, new_status):
    m = re.search(r"```json\n(.*?)\n```", reg_body, re.DOTALL)
    if not m:
        raise RuntimeError("No JSON fence in Tarot/Registry")
    data = json.loads(m.group(1))
    for entry in data["cards"]:
        if entry["name"] == card_name:
            if entry.get("image_status") == new_status:
                return None, "already_set"
            entry["image_status"] = new_status
            break
    else:
        raise RuntimeError(f"Card '{card_name}' not in Tarot/Registry")
    from datetime import date
    data["metadata"]["last_updated"] = date.today().isoformat()
    new_json = json.dumps(data, indent=2, ensure_ascii=False)
    new_body = re.sub(r"```json\n.*?\n```", f"```json\n{new_json}\n```", reg_body, count=1, flags=re.DOTALL)
    return new_body, "updated"


def slugify(name):
    return name.lower().replace(" ", "-")


# ---- Main ----

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--card", required=True, help="Card name, matching the Joplin note title under Tarot/Cards/ exactly")
    ap.add_argument("--image", required=True, help="Absolute path to the image file (PNG/JPG/WEBP)")
    ap.add_argument("--dry-run", action="store_true", help="Preflight + compress in memory, skip uploads/writes")
    ap.add_argument("--replace", action="store_true", help="Replace an already-attached image with the new one. Uploads a fresh resource and swaps the note's image reference. The previously attached Joplin resource is left in the Joplin DB as an unreferenced orphan (delete it manually via the Joplin UI if you care about storage). Source PNG is still preserved.")
    args = ap.parse_args()

    card_name = args.card
    image_path = Path(args.image)
    if not image_path.is_absolute():
        sys.exit(f"--image must be an absolute path (got {image_path})")
    if not image_path.exists():
        sys.exit(f"Image not found: {image_path}")
    if not image_path.is_file():
        sys.exit(f"Not a file: {image_path}")

    print(f"Target: {API} (token from {TOKEN_SOURCE})")
    print(f"Card: {card_name!r}")
    print(f"Image: {image_path} ({image_path.stat().st_size // 1024} KB)")
    if args.dry_run:
        print("** DRY RUN **")

    print("Preflight…", flush=True)
    preflight()
    print("  OK")

    tarot_id = find_folder_by_title("Tarot")
    if not tarot_id:
        sys.exit("Folder 'Tarot' not found at Joplin root")
    cards_id = find_folder_by_title("Cards", parent_id=tarot_id)
    if not cards_id:
        sys.exit("Folder 'Tarot/Cards' not found")

    note = find_note_in_folder(card_name, cards_id)
    if not note:
        sys.exit(f"Note 'Tarot/Cards/{card_name}' not found — check spelling (must match registry/title exactly)")
    print(f"Note found: id={note['id'][:8]}")

    reg_note = find_note_in_folder("Registry", tarot_id)
    if not reg_note:
        sys.exit("Tarot/Registry not found")

    # Idempotency check: if the note already has an image reference and no placeholder,
    # skip the expensive compress + upload unless --replace was passed.
    # Without --replace: skip upload (would create an orphan resource), reconcile registry.
    # With --replace: log the existing resource ID (it becomes orphan), fall through to re-attach.
    note_has_image = (
        PLACEHOLDER not in note["body"]
        and bool(re.search(r"!\[[^\]]*\]\(:/[a-f0-9]+\)", note["body"]))
    )
    if note_has_image and not args.replace:
        print("Note already has an image reference — skipping compress/upload (would create orphan resource).")
        print("  (Use --replace if you want to swap it for a new image.)")
        if args.dry_run:
            print("Would reconcile Registry image_status if needed. (dry-run — nothing written.)")
            return
        new_reg_body, reg_action = update_registry_status(reg_note["body"], card_name, "present")
        if new_reg_body:
            print(f"Registry image_status → 'present' ({reg_action})…", end=" ", flush=True)
            api_put(f"/notes/{reg_note['id']}", {"body": new_reg_body})
            print("ok")
        else:
            print(f"Registry image_status: {reg_action} — already in sync")
        print(f"\nDone (already attached). Source preserved at: {image_path}")
        return

    if note_has_image and args.replace:
        m = re.search(r"!\[[^\]]*\]\(:/([a-f0-9]+)\)", note["body"])
        old_resource_id = m.group(1) if m else None
        print(f"--replace: existing image resource {old_resource_id[:8] if old_resource_id else '?'} will be replaced (becomes an orphan in Joplin; delete manually if desired).")

    record = read_record(image_path)
    if record:
        print(f"Render record found: seed {record.get('seed')}, {record.get('comfy_file')}")
    else:
        print("WARNING: image has no render record (not from render_card.py); "
              "the note will not be able to reproduce it.")

    print(f"Compressing {image_path.name}…", end=" ", flush=True)
    jpeg_bytes = compress_image(image_path)
    print(f"{len(jpeg_bytes) // 1024} KB")

    if args.dry_run:
        print("Would upload resource, update note body, flip Registry image_status. (dry-run — nothing written.)")
        return

    slug = slugify(card_name)
    print(f"Uploading resource…", end=" ", flush=True)
    resource_id = upload_resource(jpeg_bytes, f"card-{slug}.jpg")
    print(f"id={resource_id[:8]}")

    new_body, body_action = update_note_body(note, resource_id, card_name, replace_existing=args.replace)
    if new_body:
        new_body = upsert_record(new_body, record_section(record) if record else None)
        print(f"Updating note body ({body_action})…", end=" ", flush=True)
        api_put(f"/notes/{note['id']}", {"body": new_body})
        print("ok")
    else:
        print(f"Note body: {body_action} — left as-is")

    new_reg_body, reg_action = update_registry_status(reg_note["body"], card_name, "present")
    if new_reg_body:
        print(f"Registry image_status → 'present' ({reg_action})…", end=" ", flush=True)
        api_put(f"/notes/{reg_note['id']}", {"body": new_reg_body})
        print("ok")
    else:
        print(f"Registry image_status: {reg_action} — no change needed")

    print(f"\nDone. Source preserved at: {image_path}")


if __name__ == "__main__":
    main()
