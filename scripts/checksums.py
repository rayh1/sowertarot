#!/usr/bin/env python3
"""The checksum list of the reference files (decision 8 of the site plan): <content>/checksums.txt, one
`<sha256>  <file name>` line per file in <content>/media/, sorted by name, the format `sha256sum` writes
and `sha256sum -c` reads. The site serves it at /checksums.txt; the build fails when it is out of date.

  python3 scripts/checksums.py write    rewrite the list from the media folder
  python3 scripts/checksums.py check    exit 1 if a file is missing, unlisted or changed

Write it only after scripts/label_media.sh: the label is part of each file. Standard library only.
Option: --content DIR (default: $SOWER_CONTENT or content).
"""
import argparse
import hashlib
import os
import sys
from pathlib import Path


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def current(media):
    return {p.name: sha256(p) for p in sorted(media.iterdir()) if p.is_file()}


def listed(path):
    out = {}
    for line in path.read_text().splitlines():
        digest, name = line.split("  ", 1)
        out[name] = digest
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("cmd", choices=["write", "check"])
    p.add_argument("--content", default=os.environ.get("SOWER_CONTENT", "content"))
    a = p.parse_args()
    content = Path(a.content)
    media, listfile = content / "media", content / "checksums.txt"
    have = current(media)
    if a.cmd == "write":
        listfile.write_text("".join(f"{d}  {n}\n" for n, d in have.items()))
        print(f"{listfile}: {len(have)} files")
        return
    want = listed(listfile) if listfile.exists() else {}
    problems = [f"not listed: {n}" for n in have if n not in want]
    problems += [f"listed but missing: {n}" for n in want if n not in have]
    problems += [f"changed: {n}" for n in have if n in want and want[n] != have[n]]
    for line in problems:
        print(line, file=sys.stderr)
    if problems:
        sys.exit(1)
    print(f"{listfile}: all {len(have)} files match")


if __name__ == "__main__":
    main()
