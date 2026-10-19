#!/usr/bin/env python3
"""Copy the deck from Joplin and Dropbox into content/ (step 15 of the site plan).

Reads only: Joplin through `joplink` (card notes in Tarot/Cards, the registry note) and Dropbox through `rclone` (dropbox:Tarot/cards/, dropbox:Tarot/animations/).
Writes:
- content/cards/<slug>.md: the registry entry as front matter, the whole card note as body, its one
  embedded Joplin image link pointed at the PNG's site path /media/card_<slug>.png (an absolute
  path, so Astro does not copy the image into its own asset folder);
- content/media/: the 37 card PNGs and the 37 clips named in deck.json, copied only when absent,
  so a re-run never overwrites a file that step 21 has given metadata.

Re-runnable: card files are rewritten on every run. Readings are no longer copied: since the daily job
writes them into content/readings/ itself, the repository is their only source (Joplin Tarot/Daily keeps
the ones written before the switch as a read-only archive).

Usage: python3 scripts/migrate.py [--out DIR]   (default DIR: content/ in the repo)
"""

import argparse
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY_NOTE = "8d9777cf4892443cae439fca35ee760a"
# Registry fields copied into each card's front matter; `name` becomes `title`, `note_id` becomes
# `joplin_note` (the archived Joplin note it came from).
REGISTRY_FIELDS = ["concept", "key_terms", "created", "seed", "image_status", "prompt_status"]
IMAGE_LINK = re.compile(r"!\[([^\]]*)\]\(:/[0-9a-f]{32}\)")


def run(*args: str) -> str:
    return subprocess.run(args, check=True, capture_output=True, text=True).stdout


def note_body(note_id: str) -> str:
    return json.loads(run("joplink", "--json", "note", "get", note_id, "--fields", "body"))["body"]


def slugify(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def yaml_value(value) -> str:
    return json.dumps(value, ensure_ascii=False)  # JSON is valid YAML for strings, numbers and lists


def front_matter(fields: dict) -> str:
    return "---\n" + "".join(f"{k}: {yaml_value(v)}\n" for k, v in fields.items()) + "---\n"


def migrate_cards(out: Path) -> list[str]:
    registry = json.loads(re.search(r"```json\n(.*?)\n```", note_body(REGISTRY_NOTE), re.S).group(1))
    clips = json.loads(run("rclone", "cat", "dropbox:Tarot/animations/deck.json"))["clips"]
    (out / "cards").mkdir(parents=True, exist_ok=True)
    media = []
    for card in registry["cards"]:
        slug = slugify(card["name"])
        image = f"card_{slug}.png"
        body, links = IMAGE_LINK.subn(lambda m: f"![{m.group(1)}](/media/{image})", note_body(card["note_id"]))
        if links != 1:
            raise SystemExit(f"{card['name']}: expected one embedded Joplin image, found {links}")
        fields = {"title": card["name"], **{k: card[k] for k in REGISTRY_FIELDS if k in card},
                  "image": image, "clip": clips[slug], "joplin_note": card["note_id"]}
        (out / "cards" / f"{slug}.md").write_text(front_matter(fields) + "\n" + body.strip() + "\n", encoding="utf-8")
        media += [f"dropbox:Tarot/cards/{image}", f"dropbox:Tarot/animations/{clips[slug]}"]
    print(f"cards: {len(registry['cards'])}")
    return media


def copy_media(out: Path, remotes: list[str]) -> None:
    (out / "media").mkdir(parents=True, exist_ok=True)
    copied = 0
    for remote in remotes:
        target = out / "media" / remote.rsplit("/", 1)[1]
        if not target.exists():
            run("rclone", "copyto", remote, str(target))
            copied += 1
    print(f"media: {len(remotes)} ({copied} copied, {len(remotes) - copied} already present)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--out", type=Path, default=ROOT / "content")
    out = parser.parse_args().out
    copy_media(out, migrate_cards(out))
