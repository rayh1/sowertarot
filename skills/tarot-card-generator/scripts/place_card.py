#!/usr/bin/env python3
"""Put a card into the repository and publish it. The repository is the deck's only source (no Joplin, no
registry note): one card file content/cards/<slug>.md, its picture and clip in content/media/, listed with
their checksums in content/checksums.txt.

  place_card.py terms                   every card's title, concept and key_terms (for the uniqueness check)
  place_card.py new --title T --concept C --key-terms "a, b, c" --body FILE [--sown-by DATE]
                                        write a new card file (image pending); FILE holds its sections
                                        (## Visual Description, ## Archetypal Essence, ## Render Prompt)
  place_card.py attach --card T --image PNG [--renders N] [--replace]
                                        copy the picked render into content/media/card_<slug>.png byte for
                                        byte, label it, write its Render Record into the card file, update
                                        the checksum list; --replace for a card that already has a picture
  place_card.py clip --card T --mp4 FILE
                                        make FILE the card's clip: copy, label, front matter `clip`, checksums;
                                        the old clip file is removed when no other card uses it
  place_card.py review --card T [--clips] FILE...
                                        copy candidates where the user looks at them: <SOWER_REVIEW>/seed-sheets/<slug>/
                                        (renders) or <SOWER_REVIEW>/animations/procedural/ (--clips); with
                                        SOWER_REVIEW empty, <SOWER_WORK>/review/ in the same layout
  place_card.py backup --card T         copy the card's files git does not hold (tools/animate/batch/<slug>/)
                                        to <SOWER_BACKUP>/animations/source/batch/<slug>/ (rclone, never deletes)
  place_card.py publish --card T [--also PATH ...] [--message M]
                                        check, commit the card's files to main as Sower Tarot and push

Run `daily.py pull` (skills/tarot-daily-reading/scripts/) before starting work in the production clone.
Environment overrides as in daily.py: TAROT_REPO (repository root), TAROT_NO_GIT=1 (publish checks but neither
commits nor pushes).
"""
import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from card_repo import (MEDIA, PLACEHOLDER, REPO, SETTINGS, TAGLINE, all_cards, review_root, card_path,  # noqa: E402
                       checksums, daily, fail, place_labelled, png_record, read_card, record_section, section,
                       slug, upsert_record, write_card)

REQUIRED = ["Visual Description", "Archetypal Essence", "Render Prompt"]


def stem(word):
    return re.sub(r"(ing|ers|er|es|s)$", "", word.lower())


def cmd_terms(_):
    for title, f in all_cards().items():
        print(f"{title} | {f.get('concept', '')} | {', '.join(f.get('key_terms', []))}")


def cmd_new(a):
    path = card_path(a.title)
    if path.exists():
        fail(f"{path.relative_to(REPO)} already exists")
    terms = [t.strip().lower() for t in a.key_terms.split(",") if t.strip()]
    if not 3 <= len(terms) <= 6:
        fail(f"give 3 to 6 key terms, not {len(terms)}")
    used = [(title, t) for title, f in all_cards().items() for t in f.get("key_terms", [])]
    clashes = [f"{title}: {t}" for title, t in used if t.lower() in terms]
    if clashes:
        fail("key terms already used: " + "; ".join(clashes))
    near = [f"{title}: {t}" for title, t in used if stem(t) in {stem(x) for x in terms}]
    if near:
        print("warning: key terms sharing a stem (check them in the comparison table): " + "; ".join(near),
              file=sys.stderr)
    sections = Path(a.body).read_text(encoding="utf-8").strip()
    missing = [h for h in REQUIRED if section(sections, h) is None]
    if missing:
        fail(f"{a.body} lacks ## {', ## '.join(missing)}")
    if re.search(r"^# ", sections, re.M) or TAGLINE in sections:
        fail(f"{a.body} must hold only the sections; the title, tagline and image line are added")
    fields = {"title": a.title, "concept": a.concept, "key_terms": terms, "created": dt.date.today().isoformat(),
              "image_status": "pending", "prompt_status": "original", "image": f"card_{slug(a.title)}.png",
              "sown_by": a.sown_by}
    write_card(a.title, fields, f"\n# {a.title}\n\n{TAGLINE}\n\n{PLACEHOLDER}\n\n{sections}\n")
    print(f"written: {path.relative_to(REPO)} (image pending)")


def cmd_attach(a):
    fields, body = read_card(a.card)
    if fields.get("image_status") == "present" and not a.replace:
        fail(f"{a.card} already has a picture; pass --replace to swap it (git history keeps the old one)")
    record = png_record(a.image)
    if record is None:
        print(f"warning: {a.image} has no render record (external render); the card file gets none", file=sys.stderr)
    elif record.get("title") != fields["title"]:
        fail(f"{a.image} was rendered with the title {record.get('title')!r}, not {fields['title']!r}")
    dest = MEDIA / fields["image"]
    place_labelled(a.image, dest)
    link = f"![{fields['title']}](/media/{fields['image']})"
    if PLACEHOLDER in body:
        body = body.replace(PLACEHOLDER, link)
    elif link not in body:
        fail(f"{card_path(a.card).relative_to(REPO)} has neither the image line {link} nor {PLACEHOLDER}")
    body = upsert_record(body, record_section(record) if record else None)
    if record:
        rs = section(body, "Render Prompt")
        if rs is not None and record.get("scene") and record["scene"] not in rs:
            print("warning: ## Render Prompt differs from the rendered scene; update it to the scene used",
                  file=sys.stderr)
    new_card = fields.get("image_status") == "pending"
    fields.update(image_status="present", seed=record.get("seed") if record else None)
    if a.renders:
        if new_card or "renders_tried" in fields:
            fields["renders_tried"] = fields.get("renders_tried", 0) + a.renders
        else:
            print("note: renders_tried not started for a card made before decision 80", file=sys.stderr)
    write_card(a.card, fields, body)
    print(checksums("write"))
    print(f"attached: {dest.relative_to(REPO)} (seed {fields.get('seed')}, renders_tried "
          f"{fields.get('renders_tried', '-')})")


def cmd_clip(a):
    fields, body = read_card(a.card)
    src = Path(a.mp4)
    if src.suffix != ".mp4":
        fail("the clip must be an MP4")
    old = fields.get("clip")
    dest = MEDIA / src.name
    if dest.exists() and src.name != old:
        fail(f"{dest.relative_to(REPO)} already exists; give the new clip its own name (…_v<N>.mp4)")
    place_labelled(src, dest)
    fields["clip"] = src.name
    write_card(a.card, fields, body)
    if old and old != src.name and not any(f.get("clip") == old for f in all_cards().values()):
        (MEDIA / old).unlink(missing_ok=True)
        print(f"removed the old clip {old} (git history keeps it)")
    print(checksums("write"))
    print(f"clip: {dest.relative_to(REPO)}")


def rclone_copy(files, dest):
    for f in files:
        r = subprocess.run(["rclone", "copyto", str(f), f"{dest}/{Path(f).name}"], capture_output=True, text=True)
        if r.returncode != 0:
            fail(f"rclone copyto {f} {dest}: {r.stderr.strip()}", 1)


def cmd_review(a):
    root = review_root()
    if not a.clips and not a.card:
        fail("renders need --card (they go into seed-sheets/<slug>/)")
    dest = f"{root}/animations/procedural" if a.clips else f"{root}/seed-sheets/{slug(a.card)}"
    rclone_copy(a.files, dest)
    print(f"copied {len(a.files)} file(s) to {dest}")


def cmd_backup(a):
    dest = SETTINGS["SOWER_BACKUP"].rstrip("/")
    if not dest:
        print("backup skipped (SOWER_BACKUP is empty)")
        return
    src = REPO / "tools" / "animate" / "batch" / slug(a.card)
    if not src.is_dir():
        fail(f"nothing to back up: {src.relative_to(REPO)} does not exist")
    target = f"{dest}/animations/source/batch/{slug(a.card)}"
    r = subprocess.run(["rclone", "copy", str(src), target], capture_output=True, text=True)
    if r.returncode != 0:
        fail(f"rclone copy to {target}: {r.stderr.strip()}", 1)
    print(f"backed up {src.relative_to(REPO)} to {target}")


def cmd_publish(a):
    fields, body = read_card(a.card)
    path = card_path(a.card)
    problems = [f"front matter lacks {k}" for k in ("title", "concept", "key_terms", "created", "image")
                if not fields.get(k)]
    if fields.get("image_status") != "present" or PLACEHOLDER in body:
        problems.append("the picture is not attached (place_card.py attach)")
    files = [path, MEDIA / fields.get("image", "")] + ([MEDIA / fields["clip"]] if fields.get("clip") else [])
    problems += [f"missing: {f.relative_to(REPO)}" for f in files[1:] if not f.is_file()]
    if problems:
        fail("; ".join(problems))
    checksums("check")
    if daily.NO_GIT:
        print("checked; commit and push skipped (TAROT_NO_GIT)")
        return
    daily.on_branch()
    rels = [str(f.relative_to(REPO)) for f in files] + ["content/checksums.txt"] + a.also
    changed = (daily.git("ls-files", "--others", "--exclude-standard", "--", "content/media").stdout.split()
               + daily.git("diff", "--name-only", "HEAD", "--", "content/media").stdout.split())
    stray = set(changed) - set(rels) - set(daily.git("ls-files", "--deleted", "--", "content/media").stdout.split())
    if stray:   # checksums.txt lists their new state, so committing it without them would fail the site build
        fail(f"content/media/ holds changes that are not this card's: {', '.join(sorted(stray))}; publish the card "
             "they belong to first, or undo them (git checkout / rm) and run scripts/checksums.py write")
    removed = daily.git("ls-files", "--deleted", "--", "content/media").stdout.split()
    daily.git("add", "--", *rels)
    if removed:
        daily.git("rm", "--quiet", "--cached", "--", *removed)
    pathspec = rels + removed
    if daily.git("diff", "--cached", "--quiet", "--", *pathspec, check=False).returncode == 0:
        print("nothing to commit")
    else:
        is_new = daily.git("ls-tree", "--name-only", "HEAD", "--", str(path.relative_to(REPO))).stdout.strip() == ""
        msg = a.message or f"{'New card' if is_new else 'Update card'}: {fields['title']}"
        daily.git("-c", f"user.name={daily.COMMITTER[0]}", "-c", f"user.email={daily.COMMITTER[1]}", "commit",
                  "--quiet", "-m", msg, "--", *pathspec)
        print(f"committed: {daily.git('log', '-1', '--format=%h %s').stdout.strip()}")
    daily.cmd_push(a)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("terms")
    s = sub.add_parser("new")
    s.add_argument("--title", required=True)
    s.add_argument("--concept", required=True, help="3-6 words")
    s.add_argument("--key-terms", required=True, help="comma-separated, 3-6")
    s.add_argument("--body", required=True, help="file with the card's ## sections")
    s.add_argument("--sown-by", help="date of the trigger reading this card grew from (YYYY-MM-DD)")
    s = sub.add_parser("attach")
    s.add_argument("--card", required=True)
    s.add_argument("--image", required=True)
    s.add_argument("--renders", type=int, default=0, help="renders the user was shown for this card in this round")
    s.add_argument("--replace", action="store_true")
    s = sub.add_parser("clip")
    s.add_argument("--card", required=True)
    s.add_argument("--mp4", required=True)
    s = sub.add_parser("review")
    s.add_argument("--card", help="required for renders")
    s.add_argument("--clips", action="store_true")
    s.add_argument("files", nargs="+")
    s = sub.add_parser("backup")
    s.add_argument("--card", required=True)
    s = sub.add_parser("publish")
    s.add_argument("--card", required=True)
    s.add_argument("--also", nargs="*", default=[], help="more repository paths to commit (masks, code records)")
    s.add_argument("--message")
    a = p.parse_args()
    {"terms": cmd_terms, "new": cmd_new, "attach": cmd_attach, "clip": cmd_clip, "review": cmd_review,
     "backup": cmd_backup, "publish": cmd_publish}[a.cmd](a)


if __name__ == "__main__":
    main()
