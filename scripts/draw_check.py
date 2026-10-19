#!/usr/bin/env python3
"""Check a daily draw against the public record: the repository and drand. Python standard library only.

  draw_check.py deck DATE      the deck as it stood in the repository at DATE's draw time
  draw_check.py verify DATE    recompute DATE's draw and compare it with its reading

The deck on a day is the set of card files in content/cards/ on `main` in the last commit before the draw
(07:00 Europe/Amsterdam), found through GitHub's API by commit date; sorted by card title. A reading from
before the repository's history begins (2026-10-13 to 2026-10-19; the history starts with the site's
publication on 2026-10-19) has no such commit: its own recorded `deck_list` is used, and the output says so. `verify` also checks that the recorded `deck_list` equals the
deck found in the repository.

The draw: drand (League of Entropy) mainnet round published at the draw time; its randomness read as one
integer n; with N cards, card = deck[n % N], lens card = (deck without card)[(n // N) % (N - 1)],
orientation = ["upright", "reversed"][(n // (N * (N - 1))) % 2].

Options: --repo OWNER/NAME (default rayh1/sowertarot); --reading FILE reads the reading from a local file
instead of GitHub. Set GITHUB_TOKEN to read a private repository or to raise GitHub's rate limit.
Exit 0 when everything matches, 1 on a mismatch.
"""

import argparse
import datetime as dt
import hashlib
import json
import os
import sys
import urllib.parse
import urllib.request
import zoneinfo

DRAND = "https://api.drand.sh/8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce"
DRAND_GENESIS, DRAND_PERIOD = 1595431050, 30
DRAW_TIME, DRAW_TZ = dt.time(7, 0), zoneinfo.ZoneInfo("Europe/Amsterdam")


def get(url: str, github: bool = False) -> bytes:
    headers = {"User-Agent": "sower-draw-check"}
    if github and os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers)) as r:
        return r.read()


def front_matter(text: str) -> dict:
    """The `key: value` lines between the two --- lines; values are JSON where they parse, else plain text."""
    lines = text.split("\n")
    if lines[0] != "---":
        raise SystemExit("no front matter")
    out = {}
    for line in lines[1:lines.index("---", 1)]:
        key, _, value = line.partition(": ")
        try:
            out[key] = json.loads(value)
        except json.JSONDecodeError:
            out[key] = value
    return out


def draw_time(date: str) -> dt.datetime:
    return dt.datetime.combine(dt.date.fromisoformat(date), DRAW_TIME, DRAW_TZ)


def deck_at(repo: str, date: str) -> tuple[list[str] | None, str]:
    """The sorted card titles in content/cards/ at the last commit before DATE's draw, and that commit."""
    until = draw_time(date).astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    api = f"https://api.github.com/repos/{repo}"
    commits = json.loads(get(f"{api}/commits?sha=main&path=content/cards&per_page=1&until={until}", github=True))
    if not commits:
        return None, "no commit with content/cards before the draw"
    sha, when = commits[0]["sha"], commits[0]["commit"]["committer"]["date"]
    files = json.loads(get(f"{api}/contents/content/cards?ref={sha}", github=True))
    raw = f"https://raw.githubusercontent.com/{repo}/{sha}/content/cards/"
    titles = [front_matter(get(raw + urllib.parse.quote(f["name"]), github=True).decode())["title"]
              for f in files if f["name"].endswith(".md")]
    return sorted(titles), f"commit {sha[:7]} of {when}"


def drand_number(round_: int) -> int:
    beacon = json.loads(get(f"{DRAND}/public/{round_}"))
    if beacon["round"] != round_ or hashlib.sha256(bytes.fromhex(beacon["signature"])).hexdigest() != beacon["randomness"]:
        raise SystemExit(f"drand round {round_}: randomness does not match its signature")
    return int(beacon["randomness"], 16)


def derive(n: int, deck: list[str]) -> tuple[str, str, str]:
    size = len(deck)
    card = deck[n % size]
    lens = [c for c in deck if c != card][(n // size) % (size - 1)]
    return card, ["upright", "reversed"][(n // (size * (size - 1))) % 2], lens


def verify(repo: str, date: str, reading_file: str | None) -> bool:
    text = open(reading_file, encoding="utf-8").read() if reading_file else \
        get(f"https://raw.githubusercontent.com/{repo}/main/content/readings/{date}.md", github=True).decode()
    r = front_matter(text)
    recorded = r["deck_list"].split(" | ")
    ok = True
    deck, source = deck_at(repo, date)
    if deck is None:
        print(f"deck: recorded in the reading ({source}; the reading predates the repository's cards)")
        deck = recorded
    else:
        print(f"deck: {len(deck)} cards, from {source}")
        if deck != recorded:
            ok = False
            print(f"MISMATCH deck: only in the repository {sorted(set(deck) - set(recorded))}, "
                  f"only in the reading {sorted(set(recorded) - set(deck))}" if set(deck) != set(recorded)
                  else "MISMATCH deck: same cards, different order")
    expected_round = int(draw_time(date).timestamp() - DRAND_GENESIS) // DRAND_PERIOD + 1
    if int(r["drand"]) != expected_round:
        ok = False
        print(f"MISMATCH drand round: reading {r['drand']}, 07:00 on {date} is round {expected_round}")
    card, orientation, lens = derive(drand_number(int(r["drand"])), deck)
    print(f"draw: {card}, {orientation}, lens card {lens} (drand round {r['drand']})")
    for name, want, got in (("card", card, r["card"]), ("orientation", orientation, r["orientation"]), ("lens", lens, r["lens"])):
        if want != got:
            ok = False
            print(f"MISMATCH {name}: draw gives {want}, reading says {got}")
    print("OK: the reading matches its draw" if ok else "FAILED")
    return ok


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("command", choices=["deck", "verify"])
    p.add_argument("date", help="YYYY-MM-DD")
    p.add_argument("--repo", default="rayh1/sowertarot")
    p.add_argument("--reading", help="local reading file instead of the one on GitHub")
    a = p.parse_args()
    if a.command == "deck":
        deck, source = deck_at(a.repo, a.date)
        if deck is None:
            sys.exit(f"{source} on {a.date}: that day's deck is only in its reading's deck_list")
        print(f"{len(deck)} cards, from {source}:")
        print("\n".join(deck))
    else:
        sys.exit(0 if verify(a.repo, a.date, a.reading) else 1)
