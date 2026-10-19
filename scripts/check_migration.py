#!/usr/bin/env python3
"""Check content/ against Joplin and Dropbox (step 16 of the site plan). Reads only.

- Cards: one file per registry card and no others; front matter equal to the registry entry (plus
  `image` and `clip` from deck.json); body equal to the Joplin note with its one image link pointed
  at /media/card_<slug>.png.
- Media: `rclone check` of the 37 PNGs and the 37 deck.json clips (Dropbox's content hash).

Readings are not checked: the daily job writes them into content/readings/ itself, so the repository
is their only source. Surrounding whitespace of a note body is not compared (migrate.py strips it). Exit 1 on any mismatch.

Usage: python3 scripts/check_migration.py [--content DIR] [--skip-media]
"""

import argparse
import difflib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REGISTRY_NOTE = "8d9777cf4892443cae439fca35ee760a"
problems: list[str] = []


def run(*args: str) -> str:
    return subprocess.run(args, check=True, capture_output=True, text=True).stdout


def note_body(note_id: str) -> str:
    return json.loads(run("joplink", "--json", "note", "get", note_id, "--fields", "body"))["body"]


def read_md(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    if not m:
        raise SystemExit(f"{path}: no front matter")
    return yaml.safe_load(m.group(1)), m.group(2)


def compare(label: str, want: str, got: str) -> None:
    if want.strip() != got.strip():
        diff = difflib.unified_diff(want.strip().splitlines(), got.strip().splitlines(), "joplin", "content", lineterm="", n=1)
        problems.append(f"{label}: text differs\n  " + "\n  ".join(list(diff)[:20]))


def same_set(label: str, want: set[str], got: set[str]) -> None:
    if want != got:
        problems.append(f"{label}: missing {sorted(want - got)}, extra {sorted(got - want)}")


def check_cards(content: Path) -> int:
    registry = json.loads(re.search(r"```json\n(.*?)\n```", note_body(REGISTRY_NOTE), re.S).group(1))["cards"]
    clips = json.loads(run("rclone", "cat", "dropbox:Tarot/animations/deck.json"))["clips"]
    by_slug = {re.sub(r"[^a-z0-9]+", "-", c["name"].lower()).strip("-"): c for c in registry}
    files = {p.stem: p for p in (content / "cards").glob("*.md")}
    same_set("cards", set(by_slug), set(files))
    for slug in sorted(set(by_slug) & set(files)):
        card, (fm, body) = by_slug[slug], read_md(files[slug])
        want = {"title": card["name"], **{k: v for k, v in card.items() if k not in ("name", "note_id")},
                "image": f"card_{slug}.png", "clip": clips[slug], "joplin_note": card["note_id"]}
        if fm != want:
            keys = sorted(k for k in set(fm) | set(want) if fm.get(k) != want.get(k))
            problems.append(f"card {slug}: front matter differs in {keys}")
        joplin = note_body(card["note_id"])
        links = re.findall(r"\]\(:/[0-9a-f]{32}\)", joplin)
        if len(links) != 1:
            problems.append(f"card {slug}: Joplin note has {len(links)} image links, expected 1")
        compare(f"card {slug}", joplin.replace(links[0], f"](/media/card_{slug}.png)") if links else joplin, body)
    return len(files)


def check_media(content: Path) -> None:
    clips = json.loads(run("rclone", "cat", "dropbox:Tarot/animations/deck.json"))["clips"].values()
    with tempfile.NamedTemporaryFile("w", suffix=".txt") as lst:
        lst.write("\n".join(clips) + "\n")
        lst.flush()
        for remote, extra in (("dropbox:Tarot/cards/", ["--include", "card_*.png"]),
                              ("dropbox:Tarot/animations/", ["--files-from", lst.name])):
            res = subprocess.run(["rclone", "check", remote, str(content / "media"), "--one-way", *extra],
                                 capture_output=True, text=True)
            summary = [l for l in res.stderr.splitlines() if "matching files" in l or "differences" in l or "ERROR" in l]
            print(f"media {remote}: " + "; ".join(s.rsplit(": ", 1)[-1] for s in summary))
            if res.returncode:
                problems.append(f"media {remote}: rclone check failed\n  " + "\n  ".join(summary))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--content", type=Path, default=ROOT / "content")
    parser.add_argument("--skip-media", action="store_true")
    args = parser.parse_args()
    print(f"cards: {check_cards(args.content)} files checked")
    if not args.skip_media:
        check_media(args.content)
    print("\n".join(problems) if problems else "OK: content/ matches Joplin and Dropbox")
    sys.exit(1 if problems else 0)
