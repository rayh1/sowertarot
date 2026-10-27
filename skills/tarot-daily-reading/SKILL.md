---
name: tarot-daily-reading
description: "Draw today's card from the user's own tarot deck (the card files in the sowertarot repository), write a fresh reading, commit it to the repository's content/readings/ and push it, so the website shows it. Runs by itself at 07:00 from cron; also use when the user asks for today's card, card of the day, a daily draw or daily reading."
---

# Daily tarot reading

One card a day from the user's deck, shown on the website with the card's looping clip. Everything lives in the repository this skill sits in (the sowertarot repository, two folders above this file): one card file per card in `content/cards/<slug>.md` (front matter `title`, `image`, `clip`; body the card note), its picture and clip in `content/media/`, one reading per day in `content/readings/<date>.md`. The deck of a draw is the card files on `main` at the last commit that changed `content/cards/` before 07:00 that day, so cards added later join from the next morning. This skill only draws; it never renders a card.

Everything mechanical is in `scripts/daily.py` (run it directly; it uses `/opt/venv/bin/python`). Your part is writing the reading.

- Readings: `content/readings/YYYY-MM-DD.md`, committed to `main` as "Sower Tarot" and pushed to GitHub; the push makes the website rebuild.
- Working folder (`draw.json` and the draft `reading.md`): `draw/` in the folder of the setting `SOWER_DAILY_DIR`.
- Backup: the scheduled run copies `content/` to the rclone destination in the setting `SOWER_BACKUP`, under `content/` (none when that is empty).
- Settings: the repository's `settings.env` (defaults, with an explanation per key) and `settings.local.env` (the user's own values, not in git); `scripts/daily.py settings` prints the values in force.

## Steps

1. **Check.** `scripts/daily.py pull` (brings `main` up to date; if it fails, stop and report it), then `scripts/daily.py status`. Exit 0 means today's reading exists: tell the user the card and the reading's page on the site (`/readings/<date>/`), and stop. One reading per day; do not draw again.
2. **Draw.** `scripts/daily.py draw`. It prints JSON with `card`, `orientation`, `lens` (the lens card), `drand` (round number), `deck` (number of cards), `deck_list`, `deck_source` (the commit the deck came from), `reading_file`, `card_note` and `lens_note` (each: Composition, Symbolism, Atmosphere, Archetypal Essence), `earlier_readings` of this card (with the `lead` each one led with) and `avoid_phrases` (stock phrases earlier readings keep repeating; `scripts/daily.py phrases` prints the same list). Card, lens card and orientation come from the drand round of 07:00 that day (see "Verifiable draw" below).
   If the draw fails because drand cannot be reached or 07:00 has not come yet, stop and report the error; do not draw another way.
3. **Write** the reading to the `reading_file` path from the draw, in exactly this form:

   ```
   lead: <the element of the card's scene this reading leads with, a few words>
   lede: <one sentence, the card's message for today>
   alt: <image description for screen readers, one or two sentences, from Composition>

   ## The card
   <what the card shows, 1–2 short paragraphs>

   ## Essence
   <what the card stands for, 1 paragraph>

   ## For today
   <2–3 short paragraphs: what this means for today>
   ```

   How to write it:
   - Build only on `card_note`. The card note has no upright/reversed meaning; you supply it here.
   - **Lens card**: a second card that is not read; it only sets the angle on the card. Read its `lens_note`, above all its Archetypal Essence, and let it decide (1) which one specific element of the card's scene (from `card_note`) leads "The card" and "For today", (2) the question "For today" asks, and (3) what "For today" asks the reader to do: carry over the stance its Archetypal Essence asks for (effort, waiting, release, sharing, whatever it is), applied to this card's element. Interpret it freely; there is no fixed list of angles. The lens card gets no section and is never named, quoted or hinted at by its title; the card leads everywhere. Treat it as upright.
   - **Lead**: the element you lead with goes on the `lead:` line. It must differ from the `lead` of every earlier reading of this card; if the lens points to an element already used, find another element of the scene it bears on.
   - **Reversed**: the same essence turned inward, blocked, delayed or overdone. Never a curse or a prediction of bad luck.
   - Read `earlier_readings`: do not reuse their phrasing or advice in "For today".
   - Use none of the `avoid_phrases`, in any form close to them ("let go of the need to" also rules out "release the need to"). They are what the readings drift into; say the thing in this card's own concrete terms instead.
   - Plain English, short sentences, second person. No predictions of events, no fortune-telling claims, no medical, legal or money advice.
4. **Save.** `scripts/daily.py save`. It validates the form (and refuses a reading that names the lens card), adds the date, card, orientation, lens card, drand round and deck list from the draw, writes `content/readings/<date>.md`, commits it to `main` and pushes it. If it reports something missing, fix `reading.md` and run it again. If only the push fails, the reading is saved and committed: report the error in your final line (the scheduled run pushes again at its end; by hand, `scripts/daily.py push`).
5. **Report** in one line: date, card, orientation, and whether the push succeeded.

## Verifiable draw

The draw uses drand (the League of Entropy's public randomness beacon, `https://api.drand.sh`, mainnet chain): the round published at 07:00 Europe/Amsterdam on the draw date. Its randomness, read as one integer, picks the card, the lens card and the orientation from the deck sorted by name; the formula is in the docstring of `scripts/daily.py`. The reading file stores `drand` (the round) and `deck_list` (the sorted deck), so the draw can be recomputed after cards are added. `scripts/daily.py verify [YYYY-MM-DD]` does that and reports any mismatch; the repository's `scripts/draw_check.py verify DATE` also checks `deck_list` against the repository's deck. The website shows the round and names the lens card, so anyone can check a draw; the reading text itself never names the lens card.

The round and the deck are fixed by the date, so a run that fails (drand down) can be redone by hand later that day with the same result. Before 07:00 the draw refuses. `draw --card/--orientation/--lens` are for tests: they skip drand and the reading says `drand: "none (manual draw)"`.

## Scheduled run

Cron runs this skill every day at 07:00 in the dev container:

- `scripts/run-daily.sh`: first `daily.py pull` (on failure it logs the error and stops), then starts itself again from the updated copy (`TAROT_UPDATED=1` marks that second start), so the run uses the updated scripts and deck; unless today's reading exists, runs `claude -p "/tarot-daily-reading" --allowedTools=Bash,Read,Write` and waits for it (at most 30 minutes). It starts the session in the folder of the setting `SOWER_CLAUDE_DIR`, from which this skill must be visible. It logs `done: <the session's last line>` when the reading file exists afterwards; otherwise it saves the session output to `failed-<date>-<time>.log` in the folder of the setting `SOWER_DAILY_DIR` and logs `FAILED`. At the end it runs `daily.py push` once more, so a reading whose push failed in the session still reaches GitHub, and then `daily.py backup`, which copies `content/` (card files, readings, media, `checksums.txt`) with `rclone copy` to the `SOWER_BACKUP` destination: new and changed files only, nothing deleted there, so hand edits reach the backup within a day too. A failed push or backup is logged and never undoes the reading.
- `scripts/install-cron.sh`: makes the crontab's line (marker `# tarot-daily`) run `run-daily.sh` at 07:00 and log to `cron.log` in the folder of the setting `SOWER_DAILY_DIR`. The line names `run-daily.sh` by the path `install-cron.sh` was started by, so start it from the production clone or its skill link, never from a test clone. `~/.profile` runs it at every container start, so the job returns after a container rebuild. After changing `SOWER_DAILY_DIR`, run it once by hand.

If the container is down at 07:00, that day has no reading (cron does not catch up); the user accepted this.

`daily.py` only writes when the repository is on branch `main` (it refuses otherwise), and `pull` only fast-forwards. `push` replays the local reading commit on top of GitHub's `main` when that moved meanwhile; if that does not apply cleanly it stops and leaves the commit for a person.

Test overrides for `daily.py`: `TAROT_DATE=YYYY-MM-DD`, `TAROT_REPO=<repository root>`, `TAROT_NO_GIT=1` (no git at all: deck from the working tree, `save` neither commits nor pushes), `TAROT_DAILY_DIR=<folder>` (the working folder itself). Set `TAROT_REPO` (a scratch clone) or `TAROT_NO_GIT=1`, plus `TAROT_DAILY_DIR`, on every `daily.py` call of a test run, so it never touches the real repository or GitHub; `backup` takes its destination from the settings files only, so run it in a test only from a scratch clone whose `settings.local.env` points `SOWER_BACKUP` at a scratch folder.
