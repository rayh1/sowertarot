#!/opt/venv/bin/python
"""Mechanical steps of the daily tarot reading. The model only writes the reading text.

  daily.py pull                        bring the repository's main up to date (fast-forward only)
  daily.py status                      exit 0 if today's reading file exists, else 1
  daily.py draw [--card NAME] [--orientation upright|reversed] [--lens NAME]
                                       draw a card and a lens card from drand -> draw.json
  daily.py verify [DATE]               recompute a saved draw from its drand round and deck list (default: today)
  daily.py save [--file reading.md]    write content/readings/<date>.md, commit it to main and push
  daily.py push                        push main if it has commits GitHub lacks (save does this itself)
  daily.py phrases                     list the stock phrases the next reading must avoid (also in draw.json)
  daily.py backup                      copy content/ to the backup location SOWER_BACKUP (rclone, never deletes)
  daily.py settings                    print the settings as shell assignments (run-daily.sh, install-cron.sh)

Everything comes from the repository this skill lives in (the folder two levels above this script, after
following links): card files in content/cards/, readings in content/readings/, pictures and clips in
content/media/. Personal values (GitHub account, backup, folders) come from the repository's settings.env and
settings.local.env (see settings.env). The deck of a draw is the card files on `main` at the last commit that changed content/cards/
before the draw time, so a later manual run that day draws from the same deck.

Environment overrides (for tests): TAROT_DATE (YYYY-MM-DD), TAROT_REPO (repository root), TAROT_NO_GIT=1
(no git at all: the deck is the working tree's content/cards/, save neither commits nor pushes, pull and push
do nothing), TAROT_DAILY_DIR (working folder for draw.json and reading.md, instead of <SOWER_DAILY_DIR>/draw).

Verifiable draw: drand (League of Entropy's public randomness beacon) publishes a signed random value every
30 seconds. The draw takes the round of 07:00 Europe/Amsterdam on the draw date, reads its randomness as one
integer n, and with the deck sorted by name (N cards):
  card        = deck[n % N]
  lens card   = (deck without card)[(n // N) % (N - 1)]
  orientation = ["upright", "reversed"][(n // (N * (N - 1))) % 2]
The reading file stores the round and the sorted deck list, so anyone can recompute the draw later.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import random
import re
import shlex
import subprocess
import sys
import time
import urllib.request
import zoneinfo
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
REPO = Path(os.environ.get("TAROT_REPO") or SKILL.parent.parent)
CARDS = REPO / "content" / "cards"
READINGS = REPO / "content" / "readings"
MEDIA = REPO / "content" / "media"
NO_GIT = os.environ.get("TAROT_NO_GIT") == "1"
BRANCH = "main"
COMMITTER = ("Sower Tarot", "daily@sowertarot.com")
# Defaults when settings.env lacks a key (settings.env explains each one).
SETTING_DEFAULTS = {"SOWER_WORK": "work", "SOWER_DAILY_DIR": "work/daily-card", "SOWER_GH_USER": "",
                    "SOWER_BACKUP": "", "SOWER_REVIEW": "", "SOWER_CLAUDE_DIR": "."}
SETTING_PATHS = {"SOWER_WORK", "SOWER_DAILY_DIR", "SOWER_CLAUDE_DIR"}


def load_settings():
    """settings.env, then settings.local.env, from the repository root: KEY=value lines, # comments, optional
    quotes. Relative paths become absolute, relative to the repository."""
    out = dict(SETTING_DEFAULTS)
    for name in ("settings.env", "settings.local.env"):
        f = REPO / name
        if not f.exists():
            continue
        for line in f.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, val = (x.strip() for x in line.split("=", 1))
            if len(val) >= 2 and val[0] == val[-1] and val[0] in "'\"":
                val = val[1:-1]
            out[key] = val
    for key in SETTING_PATHS & out.keys():
        out[key] = str((REPO / out[key]).resolve())
    return out


SETTINGS = load_settings()
GH_USER = SETTINGS["SOWER_GH_USER"]         # GitHub account whose gh token pulls and pushes; "" = gh's active one
DRAW_DIR = Path(os.environ.get("TAROT_DAILY_DIR") or Path(SETTINGS["SOWER_DAILY_DIR"]) / "draw")

# drand mainnet ("default" chain: 30-second rounds since genesis 2020-07-22); the chain hash pins it.
DRAND_API = "https://api.drand.sh"
DRAND_CHAIN = "8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce"
DRAND_GENESIS = 1595431050
DRAND_PERIOD = 30
DRAW_TIME = dt.time(7, 0)
DRAW_TZ = zoneinfo.ZoneInfo("Europe/Amsterdam")

SECTIONS = ["The card", "Essence", "For today"]
# Reading file front matter, in this order; every value is written as a JSON string.
READING_KEYS = ["date", "card", "orientation", "lens", "lead", "drand", "deck", "deck_list", "lede", "alt"]

# Cliche mirror: 3-5 word phrases used in PHRASE_MIN_READINGS or more readings are passed to the writer to avoid.
PHRASE_MIN_READINGS = 3
PHRASE_MAX = 15
PHRASE_MIN_CONTENT = 2     # a phrase needs this many words outside FILLER ("it is the" is not a cliche)
FILLER = set("""a an the and or but of to in on at by for with from into as than then so
i you he she it we they me him her us them my your his its our their this that these those
is are was were be been being am there here what which who where when how""".split())


def today():
    return os.environ.get("TAROT_DATE") or dt.date.today().isoformat()


def slug(title):
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def fail(msg, code=2):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)


# --- Git --------------------------------------------------------------------

def git(*args, auth=False, check=True):
    """Run git in the repository. With auth, the gh token of GH_USER answers GitHub's password prompt;
    it travels in the environment, never on the command line."""
    env, pre = os.environ.copy(), []
    if auth:
        cmd = ["gh", "auth", "token", *(["--user", GH_USER] if GH_USER else [])]
        tok = subprocess.run(cmd, capture_output=True, text=True)
        if tok.returncode != 0:
            fail(f"{' '.join(cmd)}: {tok.stderr.strip()}")
        env["SOWER_GIT_TOKEN"] = tok.stdout.strip()
        user = GH_USER or "x-access-token"    # GitHub ignores the user name when the password is a token
        pre = ["-c", "credential.helper=",
               "-c", f'credential.helper=!f() {{ echo username={user}; echo "password=$SOWER_GIT_TOKEN"; }}; f']
    r = subprocess.run(["git", "-C", str(REPO), *pre, *args], capture_output=True, text=True, env=env)
    if check and r.returncode != 0:
        fail(f"git {' '.join(args[:2])}: {(r.stderr or r.stdout).strip()}")
    return r


def on_branch():
    """Refuse to write when the clone is not on BRANCH: the reading must land on main."""
    head = git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    if head != BRANCH:
        fail(f"{REPO} is on branch {head!r}, not {BRANCH!r}")


# --- Repository files --------------------------------------------------------

def split_front_matter(text):
    """The `key: <JSON value>` lines between the --- lines (values that are not JSON stay text), and the body."""
    lines = text.split("\n")
    if lines[0] != "---" or "---" not in lines[1:]:
        return {}, text
    end = lines.index("---", 1)
    fields = {}
    for line in lines[1:end]:
        k, sep, v = line.partition(": ")
        if sep:
            try:
                fields[k] = json.loads(v)
            except json.JSONDecodeError:
                fields[k] = v
    return fields, "\n".join(lines[end + 1:])


def card_files(texts):
    """{title: {"fields": front matter, "body": text}} from an iterable of card file texts."""
    out = {}
    for text in texts:
        fields, body = split_front_matter(text)
        if fields.get("title"):
            out[fields["title"]] = {"fields": fields, "body": body}
    return out


def tree_cards():
    """The card files in the working tree."""
    return card_files(p.read_text(encoding="utf-8") for p in sorted(CARDS.glob("*.md")))


def deck_at(date):
    """The cards of DATE's draw and where they came from: the card files on main at the last commit that
    changed content/cards/ before the draw time (by commit date, as scripts/draw_check.py looks it up on
    GitHub). With TAROT_NO_GIT, the working tree."""
    if NO_GIT:
        return tree_cards(), "working tree (TAROT_NO_GIT)"
    until = dt.datetime.combine(dt.date.fromisoformat(date), DRAW_TIME, DRAW_TZ).isoformat()
    sha = git("log", "-1", "--format=%H", f"--until={until}", BRANCH, "--", "content/cards").stdout.strip()
    if not sha:
        fail(f"no commit on {BRANCH} changed content/cards/ before {until}")
    names = git("ls-tree", "--name-only", sha, "content/cards/").stdout.split()
    return card_files(git("show", f"{sha}:{n}").stdout for n in names if n.endswith(".md")), f"commit {sha[:7]}"


def parse_reading(text):
    """Front matter fields plus '## <section>' blocks of the body under "sections"."""
    fields, body = split_front_matter(text)
    sections, current = {}, None
    for line in body.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            current = m.group(1)
            sections[current] = []
        elif current:
            sections[current].append(line)
    fields["sections"] = {k: "\n".join(v).strip() for k, v in sections.items()}
    return fields


def parse_draft(text):
    """The model's draft: 'key: value' lines up to the first blank line, then '## <section>' blocks."""
    head, _, rest = text.partition("\n\n")
    fields = {k.strip(): v.strip() for k, sep, v in (line.partition(":") for line in head.splitlines()) if sep}
    fields["sections"] = parse_reading(rest)["sections"]
    return fields


def reading_path(date):
    return READINGS / f"{date}.md"


def readings():
    """All readings in the repository, newest first."""
    out = [parse_reading(p.read_text(encoding="utf-8")) for p in READINGS.glob("????-??-??.md")]
    return sorted(out, key=lambda r: r["date"], reverse=True)


def phrases(text):
    """The distinct 3-5 word phrases of a text; phrases never cross a sentence or line break."""
    out = set()
    for sentence in re.split(r"[.!?;:\n]+", text.lower()):
        w = re.findall(r"[a-z']+", sentence)
        for n in (3, 4, 5):
            for i in range(len(w) - n + 1):
                gram = w[i:i + n]
                if sum(x not in FILLER for x in gram) >= PHRASE_MIN_CONTENT:
                    out.add(" ".join(gram))
    return out


def stock_phrases(rs):
    """Phrases the readings keep repeating, most used first; phrases taken from card notes are allowed."""
    counts = {}
    for r in rs:
        for ph in phrases("\n".join([r.get("lede", "")] + list(r["sections"].values()))):
            counts[ph] = counts.get(ph, 0) + 1
    common = {ph: c for ph, c in counts.items() if c >= PHRASE_MIN_READINGS}
    if not common:
        return []
    from_cards = phrases("\n".join(c["body"] for c in tree_cards().values()))
    kept = []
    for ph in sorted(common, key=lambda ph: (-common[ph], -len(ph.split()), ph)):
        if ph in from_cards or any(f" {ph} " in f" {k} " for k in kept):
            continue    # card wording, or part of a longer phrase already listed
        kept.append(ph)
    return merge_overlaps(kept)[:PHRASE_MAX]


def merge_overlaps(kept):
    """Join phrases that overlap by 3+ words ("let go of the need" + "go of the need to") into one."""
    words = [k.split() for k in kept]
    merged = True
    while merged:
        merged = False
        for a in words:
            for b in words:
                if a is b:
                    continue
                n = next((n for n in range(min(len(a), len(b)) - 1, 2, -1) if a[-n:] == b[:n]), 0)
                if n:
                    a[len(a):] = b[n:]
                    words.remove(b)
                    merged = True
                    break
            if merged:
                break
    return [" ".join(w) for w in words]


# --- Card data --------------------------------------------------------------

def card_sections(body):
    """Keep the parts a reading draws on: Composition, Symbolism, Atmosphere, Archetypal Essence."""
    keep, out, current = {"Composition", "Symbolism", "Atmosphere", "Archetypal Essence"}, {}, None
    for line in body.splitlines():
        m = re.match(r"^#{2,3}\s+(.+?)\s*$", line)
        if m:
            current = m.group(1) if m.group(1) in keep else None
            if current:
                out[current] = []
        elif current:
            out[current].append(line)
    return {k: "\n".join(v).strip() for k, v in out.items()}


# --- Verifiable draw (drand) -------------------------------------------------

def drand_round(date):
    """The drand round published at DRAW_TIME (Europe/Amsterdam) on date, and its start as a Unix time."""
    at = dt.datetime.combine(dt.date.fromisoformat(date), DRAW_TIME, DRAW_TZ).timestamp()
    rnd = int(at - DRAND_GENESIS) // DRAND_PERIOD + 1
    return rnd, DRAND_GENESIS + (rnd - 1) * DRAND_PERIOD


def drand_randomness(rnd, start):
    """Fetch a round's randomness (hex). Fails when drand cannot be reached; a manual run later that day
    uses the same round and so gives the same draw."""
    if time.time() < start:
        fail(f"drand round {rnd} is published at {dt.datetime.fromtimestamp(start, DRAW_TZ):%H:%M} "
             f"Europe/Amsterdam; draw after that")
    url = f"{DRAND_API}/{DRAND_CHAIN}/public/{rnd}"
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=15) as resp:
                beacon = json.load(resp)
            break
        except OSError as e:
            if attempt == 3:
                fail(f"drand unreachable ({url}): {e}")
            time.sleep(10)
    # drand defines a round's randomness as the SHA-256 of its signature; check the two agree.
    if beacon.get("round") != rnd or hashlib.sha256(bytes.fromhex(beacon["signature"])).hexdigest() != beacon["randomness"]:
        fail(f"drand round {rnd}: response does not match its round or signature")
    return beacon["randomness"]


def derive(randomness, deck_list):
    """Card, lens card and orientation from one drand value over the sorted deck list (see the docstring)."""
    n, size = int(randomness, 16), len(deck_list)
    card = deck_list[n % size]
    rest = [c for c in deck_list if c != card]
    lens = rest[(n // size) % (size - 1)]
    orientation = ["upright", "reversed"][(n // (size * (size - 1))) % 2]
    return card, lens, orientation


# --- Commands ---------------------------------------------------------------

def cmd_pull(_):
    if NO_GIT:
        print("pull skipped (TAROT_NO_GIT)")
        return
    on_branch()
    r = git("pull", "--ff-only", "--quiet", auth=True, check=False)
    if r.returncode != 0:
        fail(f"git pull --ff-only in {REPO}: {(r.stderr or r.stdout).strip()}")
    print(f"up to date: {git('log', '-1', '--format=%h %s').stdout.strip()}")


def cmd_push(_):
    if NO_GIT:
        print("push skipped (TAROT_NO_GIT)")
        return
    on_branch()
    git("fetch", "--quiet", "origin", BRANCH, auth=True)
    ahead = int(git("rev-list", "--count", f"origin/{BRANCH}..{BRANCH}").stdout)
    if not ahead:
        print(f"nothing to push: {BRANCH} equals origin/{BRANCH}")
        return
    if int(git("rev-list", "--count", f"{BRANCH}..origin/{BRANCH}").stdout):
        # main moved on GitHub since the pull: replay the local commits (the reading) on top of it
        # --autostash: uncommitted work in the clone (a card in progress) must not block the push
        if git("rebase", "--quiet", "--autostash", f"origin/{BRANCH}", check=False).returncode != 0:
            git("rebase", "--abort", check=False)
            fail(f"{BRANCH} and origin/{BRANCH} have diverged and the local commits do not rebase cleanly", 1)
        clash = git("diff", "--name-only", "--diff-filter=U").stdout.split()
        if clash:   # the autostash did not reapply over the new commits: keep the committed files, the edits stay stashed
            git("checkout", "HEAD", "--", *clash)
            print(f"warning: uncommitted changes to {', '.join(clash)} clashed with origin/{BRANCH}; those files are "
                  "back at the committed version and the changes are kept in `git stash list`", file=sys.stderr)
        print(f"rebased {ahead} local commit(s) onto origin/{BRANCH}")
    r = git("push", "--quiet", "origin", BRANCH, auth=True, check=False)
    if r.returncode != 0:
        fail(f"git push: {(r.stderr or r.stdout).strip()}", 1)
    print(f"pushed {ahead} commit(s) to origin/{BRANCH}")


def cmd_status(_):
    path = reading_path(today())
    print(f"done: {path}" if path.exists() else f"missing: no reading for {today()} in {READINGS}")
    sys.exit(0 if path.exists() else 1)


def cmd_draw(a):
    if reading_path(today()).exists():
        fail(f"a reading for {today()} already exists: {reading_path(today())}")
    deck, deck_source = deck_at(today())
    if len(deck) < 2:
        fail(f"the deck needs at least 2 cards (card + lens card); {deck_source} has {len(deck)}")
    deck_list = sorted(deck)
    if a.card or a.orientation or a.lens:    # test run: no drand, so the reading marks it unverifiable
        rnd = None
        card = a.card or random.choice(deck_list)
        lens = a.lens or random.choice([c for c in deck_list if c != card])
        orientation = a.orientation or random.choice(["upright", "reversed"])
    else:
        rnd, start = drand_round(today())
        card, lens, orientation = derive(drand_randomness(rnd, start), deck_list)
    for c in (card, lens):
        if c not in deck:
            fail(f"{c!r} is not in the deck")
    if card == lens:
        fail("the lens card must differ from the card")
    all_readings = readings()
    earlier = [r for r in all_readings if r.get("card") == card]
    draw = {
        "date": today(),
        "card": card,
        "orientation": orientation,
        "lens": lens,
        "drand": rnd,
        "deck": len(deck),
        "deck_list": deck_list,
        "deck_source": deck_source,
        "reading_file": str(DRAW_DIR / "reading.md"),
        "card_note": card_sections(deck[card]["body"]),
        "lens_note": card_sections(deck[lens]["body"]),
        "earlier_readings": [
            {"date": r["date"], "orientation": r.get("orientation"), "lead": r.get("lead"),
             "for_today": r["sections"].get("For today", "")}
            for r in earlier
        ],
        "avoid_phrases": stock_phrases(all_readings),
    }
    DRAW_DIR.mkdir(parents=True, exist_ok=True)
    (DRAW_DIR / "draw.json").write_text(json.dumps(draw, indent=2, ensure_ascii=False))
    print(json.dumps(draw, indent=2, ensure_ascii=False))


def cmd_save(a):
    draw = json.loads((DRAW_DIR / "draw.json").read_text())
    if draw["date"] != today():
        fail(f"draw.json is for {draw['date']}, not {today()}; run draw first")
    text = Path(a.file or DRAW_DIR / "reading.md").read_text()
    r = parse_draft(text)
    missing = [k for k in ("lead", "lede", "alt") if not r.get(k)] + [s for s in SECTIONS if not r["sections"].get(s)]
    if missing:
        fail(f"reading is missing: {', '.join(missing)}")
    if draw["lens"] in text:    # case-sensitive: "the horizon" in a scene is fine, "The Horizon" names the card
        fail(f"the reading names the lens card ({draw['lens']}); it must never be named")
    if not NO_GIT:
        on_branch()
    fields = {"date": draw["date"], "card": draw["card"], "orientation": draw["orientation"], "lens": draw["lens"],
              "lead": r["lead"], "drand": str(draw["drand"] or "none (manual draw)"), "deck": str(draw["deck"]),
              "deck_list": " | ".join(draw["deck_list"]), "lede": r["lede"], "alt": r["alt"]}
    head = "".join(f"{k}: {json.dumps(fields[k], ensure_ascii=False)}\n" for k in READING_KEYS)
    body = "\n\n".join(f"## {s}\n\n{r['sections'][s]}" for s in SECTIONS)
    path = reading_path(draw["date"])
    READINGS.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\n{head}---\n\n{body}\n", encoding="utf-8")
    print(f"saved: {path}")
    if NO_GIT:
        return
    rel = str(path.relative_to(REPO))
    git("add", "--", rel)
    if git("diff", "--cached", "--quiet", "--", rel, check=False).returncode != 0:
        git("-c", f"user.name={COMMITTER[0]}", "-c", f"user.email={COMMITTER[1]}", "commit", "--quiet",
            "-m", f"Daily reading {draw['date']}: {draw['card']}, {draw['orientation']}", "--", rel)
        print(f"committed: {git('log', '-1', '--format=%h %s').stdout.strip()}")
    cmd_push(a)


def cmd_verify(a):
    date = a.date or today()
    path = reading_path(date)
    if not path.exists():
        fail(f"no reading for {date}: {path}")
    r = parse_reading(path.read_text(encoding="utf-8"))
    if not str(r.get("drand", "")).isdigit() or not r.get("deck_list"):
        fail(f"the {date} reading has no drand round and deck list (drand: {r.get('drand', 'missing')})")
    rnd = int(r["drand"])
    card, lens, orientation = derive(drand_randomness(rnd, 0), r["deck_list"].split(" | "))
    got = {"card": card, "lens": lens, "orientation": orientation}
    bad = [f"{k}: reading says {r.get(k)!r}, drand gives {v!r}" for k, v in got.items() if r.get(k) != v]
    if drand_round(date)[0] != rnd:
        bad.append(f"drand: reading says round {rnd}, the 07:00 round of {date} is {drand_round(date)[0]}")
    print("\n".join(bad) if bad else f"verified: {date} {card}, {orientation}, lens {lens} (drand round {rnd})")
    sys.exit(1 if bad else 0)


def cmd_phrases(_):
    print("\n".join(stock_phrases(readings())) or "(none yet)")


def cmd_backup(_):
    """Copy content/ (card files, readings, media, checksums.txt) to <SOWER_BACKUP>/content with rclone copy:
    new and changed files only, nothing deleted there. Skipped when SOWER_BACKUP is empty."""
    dest = SETTINGS["SOWER_BACKUP"].rstrip("/")
    if not dest:
        print("backup skipped (SOWER_BACKUP is empty)")
        return
    r = subprocess.run(["rclone", "copy", str(REPO / "content"), f"{dest}/content", "--stats-one-line", "-v"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        fail(f"rclone copy to {dest}/content: {r.stderr.strip()}", 1)
    copied = re.findall(r"INFO\s*: (.+?): Copied", r.stderr)
    print(f"backed up to {dest}/content: " + (", ".join(copied) if copied else "nothing new"))


def cmd_settings(a):
    """Shell assignments for run-daily.sh and install-cron.sh: eval "$(daily.py settings)"."""
    for key, val in SETTINGS.items():
        print(f"{key}={shlex.quote(val)}")
    print(f"SOWER_REPO={shlex.quote(str(REPO))}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("pull").set_defaults(fn=cmd_pull)
    sub.add_parser("status").set_defaults(fn=cmd_status)
    d = sub.add_parser("draw")
    d.add_argument("--card")
    d.add_argument("--orientation", choices=["upright", "reversed"])
    d.add_argument("--lens")
    d.set_defaults(fn=cmd_draw)
    v = sub.add_parser("verify")
    v.add_argument("date", nargs="?")
    v.set_defaults(fn=cmd_verify)
    s = sub.add_parser("save")
    s.add_argument("--file")
    s.set_defaults(fn=cmd_save)
    sub.add_parser("push").set_defaults(fn=cmd_push)
    sub.add_parser("phrases").set_defaults(fn=cmd_phrases)
    sub.add_parser("backup").set_defaults(fn=cmd_backup)
    sub.add_parser("settings").set_defaults(fn=cmd_settings)
    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
