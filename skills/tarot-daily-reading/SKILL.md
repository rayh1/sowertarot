---
name: tarot-daily-reading
description: "Draw today's card from the user's own tarot deck (the card files in the sowertarot repository), write a fresh reading, commit it to the repository's content/readings/ and push it, and republish the fixed Card of the Day page. Runs by itself at 07:00 from cron; also use when the user asks for today's card, card of the day, a daily draw or daily reading, or to rebuild the daily page."
---

# Daily tarot reading

One card a day from the user's deck, shown as its looping animation when it has one. Everything lives in the repository this skill sits in (the sowertarot repository, two folders above this file): one card file per card in `content/cards/<slug>.md` (front matter `title`, `image`, `clip`; body the card note), its picture and clip in `content/media/`, one reading per day in `content/readings/<date>.md`. The deck of a draw is the card files on `main` at the last commit that changed `content/cards/` before 07:00 that day, so cards added later join from the next morning. This skill only draws; it never renders a card.

Everything mechanical is in `scripts/daily.py` (run it directly; it uses `/opt/venv/bin/python`). Your part is writing the reading and publishing the page.

- Readings: `content/readings/YYYY-MM-DD.md`, committed to `main` as "Sower Tarot" and pushed to GitHub; the push makes the website rebuild.
- Fixed page ("Card of the Day"): today's reading in full plus a list of earlier draws, at the claude.ai Artifact URL in the setting `SOWER_PAGE_URL`; none when that is empty.
- Working folder (output only): `page/` in the folder of the setting `SOWER_DAILY_DIR`.
- Settings: the repository's `settings.env` (defaults, with an explanation per key) and `settings.local.env` (the user's own values, not in git); `scripts/daily.py settings` prints the values in force.

## Steps

1. **Check.** `scripts/daily.py pull` (brings `main` up to date; if it fails, stop and report it), then `scripts/daily.py status`. Exit 0 means today's reading exists: tell the user the card and the page link, and stop. One reading per day; do not draw again.
2. **Draw.** `scripts/daily.py draw`. It prints JSON with `card`, `orientation`, `lens` (the lens card), `drand` (round number), `deck` (number of cards), `deck_list`, `image`, `animation` (the card's looping clip as an animated WebP, or null when it has none), `deck_source` (the commit the deck came from), `reading_file`, `card_note` and `lens_note` (each: Composition, Symbolism, Atmosphere, Archetypal Essence), `earlier_readings` of this card (with the `lead` each one led with) and `avoid_phrases` (stock phrases earlier readings keep repeating; `scripts/daily.py phrases` prints the same list). Card, lens card and orientation come from the drand round of 07:00 that day (see "Verifiable draw" below).
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
5. **Build.** `scripts/daily.py build-page`. It prints JSON with `url`, `page` (index.html), `image` (published name), `image_path`, and `animation` / `animation_path` (null when the card has no clip; the page then shows the still). The page shows the animated WebP as an ordinary image; viewers who ask for reduced motion see the still. (A `<video>` did not play on the published page.)
6. **Publish** to the page at the `url` that `build-page` printed (the fixed page unless a test override is set), with the Artifact tool. When `url` is null (no page configured), skip 6.1–6.3 and only run 6.4:
   1. `action: "read"` with `url` (required before republishing from a new conversation).
   2. `action: "list"`, `scope: "files"`, `url`: note the published `.jpg`, `.webp` and `.mp4` files.
   3. `action: "publish"` with `url`, `file_path` = `page`, `files` = `{ "<image>": "<image_path>", "<animation>": "<animation_path>" }` (leave out the animation entry when it is null) plus `null` for every other published `.jpg`, `.webp` and `.mp4` (so old files do not pile up). No `icon`.
   4. After a successful publish: `scripts/daily.py mark-published`. The scheduled run waits for this marker before it stops the session.
7. **Report** in one line: date, card, orientation, page link.

## Verifiable draw

The draw uses drand (the League of Entropy's public randomness beacon, `https://api.drand.sh`, mainnet chain): the round published at 07:00 Europe/Amsterdam on the draw date. Its randomness, read as one integer, picks the card, the lens card and the orientation from the deck sorted by name; the formula is in the docstring of `scripts/daily.py`. The reading file stores `drand` (the round) and `deck_list` (the sorted deck), so the draw can be recomputed after cards are added. `scripts/daily.py verify [YYYY-MM-DD]` does that and reports any mismatch; the repository's `scripts/draw_check.py verify DATE` also checks `deck_list` against the repository's deck. The website shows the round and names the lens card, so anyone can check a draw; the reading text itself never names the lens card. The Card of the Day page shows neither.

The round and the deck are fixed by the date, so a run that fails (drand down) can be redone by hand later that day with the same result. Before 07:00 the draw refuses. `draw --card/--orientation/--lens` are for tests: they skip drand and the reading says `drand: "none (manual draw)"`.

When the user asks only to rebuild the page (e.g. after editing a reading file), run steps 5–6.

## Scheduled run

Cron runs this skill every day at 07:00 in the dev container:

- `scripts/run-daily.sh`: first `daily.py pull` (on failure it logs the error and stops), then starts itself again from the updated copy (`TAROT_UPDATED=1` marks that second start), so the run uses the updated scripts and deck; exits at once if today's reading exists; otherwise starts `claude --bg "/tarot-daily-reading" --allowedTools=Artifact,Bash,Read,Write`, waits up to 30 minutes for `daily.py status --published`, and stops the session. (A session that has published a page keeps watching it for comments and never reports itself done, so the marker is the finish signal.) It starts the session in the folder of the setting `SOWER_CLAUDE_DIR`, from which this skill must be visible. On failure it saves the session output to `failed-<date>-<id>.log` in the folder of the setting `SOWER_DAILY_DIR`. At the end it runs `daily.py push` once more, so a reading whose push failed in the session still reaches GitHub.
- `scripts/install-cron.sh`: makes the crontab's line (marker `# tarot-daily`) run `run-daily.sh` at 07:00 and log to `cron.log` in the folder of the setting `SOWER_DAILY_DIR`. The line names `run-daily.sh` by the path `install-cron.sh` was started by, so start it from the production clone or its skill link, never from a test clone. `~/.profile` runs it at every container start, so the job returns after a container rebuild. After changing `SOWER_DAILY_DIR`, run it once by hand.

`claude -p` cannot be used: print mode has no Artifact tool. If the container is down at 07:00, that day has no reading (cron does not catch up); the user accepted this.

`daily.py` only writes when the repository is on branch `main` (it refuses otherwise), and `pull` only fast-forwards. `push` replays the local reading commit on top of GitHub's `main` when that moved meanwhile; if that does not apply cleanly it stops and leaves the commit for a person.

Test overrides for `daily.py`: `TAROT_DATE=YYYY-MM-DD`, `TAROT_REPO=<repository root>`, `TAROT_NO_GIT=1` (no git at all: deck from the working tree, `save` neither commits nor pushes), `TAROT_DAILY_DIR=<folder>` (the page build folder itself), `TAROT_PAGE_URL=<artifact url>`. Set `TAROT_REPO` (a scratch clone) or `TAROT_NO_GIT=1`, plus `TAROT_DAILY_DIR` and `TAROT_PAGE_URL`, on every `daily.py` call of a test run, so it never touches the real repository, GitHub or page.
