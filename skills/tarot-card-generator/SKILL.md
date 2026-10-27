---
name: tarot-card-generator
description: "Make, re-render, repair or animate a card of the Sower tarot deck in the repository this skill lives in: one card file `content/cards/<slug>.md` per card (Visual Description, Archetypal Essence, render prompt, render record), its picture and clip in `content/media/`, rendered locally through the bundled ComfyUI/FLUX pipeline (art -> upscale -> framed title card), labelled, listed in `content/checksums.txt`, committed to main and pushed. Use when the user asks to (1) make the new card a Sower or Miner trigger draw calls for, or find something new for the deck, (2) re-render an existing card's image in the deck style, (3) repair a defect in a card's picture, or (4) animate a card as a short loop."
---

## Objective
Make ONE original card per invocation in the Rider-Waite look, write it as one card file `content/cards/<slug>.md` in this repository, put its picture in `content/media/`, and commit and push it to `main` once the user approves it (website decision 77). The card file holds card-as-object content only: Visual Description, Archetypal Essence, render prompt and render record. No Upright/Reversed interpretation: meaning is produced fresh at reading time by the `tarot-daily-reading` skill.

**The repository is the deck.** The card files on `main` are the deck the 07:00 draw uses (a card committed before 07:00 joins that day's draw), the website shows them, and their front matter is the deck index: there is no registry note. Joplin `Tarot/Cards`, `Tarot/Registry` and the old Dropbox folders are a read-only archive; never write to them.

**New cards come only through a trigger.** When The Sower or The Miner is the day's card of a reading (upright or reversed, never as the lens card), exactly one new card is due, and no card enters the deck any other way: The Sower's card grows from a seed from outside the deck, The Miner's from a gap inside it (§ Find something new). The user never makes a card by hand. Re-rendering, repairing and animating existing cards are not new cards.

**Style consistency is the point of a deck.** Every card must read as one deck. That is enforced by freezing everything except the scene and the seed — see § Deck style consistency and `assets/style.md`. Never re-style a single card by hand; if the look must change, change it for the whole deck in `assets/style.md`.

Paths in this file are relative to the repository root (the folder two levels above this skill after following links: `/workspace/sowertarot`, the production clone, when run through `/workspace/.claude/skills/tarot-card-generator`). Run everything from the repository root. `scripts/label_media.sh`, `scripts/checksums.py` and `scripts/draw_check.py` are the repository's own `scripts/` folder; every other `scripts/…` named here (`render_card.py`, `place_card.py` and the rest) is this skill's, `skills/tarot-card-generator/scripts/`.

## Quick start
- Output: one card file `content/cards/<slug>.md`, its picture `content/media/card_<slug>.png` (and later its clip), an updated `content/checksums.txt`, one commit on `main` by Sower Tarot, pushed to GitHub (the site rebuilds on the push).
- Prereq (repository): the clone is on `main` and up to date — run `python3 skills/tarot-daily-reading/scripts/daily.py pull` first (it refuses a clone on another branch or one that cannot fast-forward). `place_card.py` shares that script's settings, git and push code. `exiftool` (the label, `scripts/label_media.sh`) and `rclone` (review copies and backups, also to a local folder) on PATH. Settings in `settings.env`, own values in `settings.local.env` (`SOWER_WORK`, `SOWER_REVIEW`, `SOWER_BACKUP`, `SOWER_GH_USER`).
- Prereq (local render, Step 4): ComfyUI running locally with the `comfy` CLI on PATH; a CUDA GPU (~16 GB VRAM); `Pillow` importable for `scripts/frame_card.py`. Three model files, all referenced by `assets/tarot-card-flux.json` by filename:
  - `flux1-dev-fp8.safetensors` in `models/checkpoints/` — base model (download: `https://huggingface.co/Comfy-Org/flux1-dev/resolve/main/flux1-dev-fp8.safetensors`, ~16 GB).
  - `sowtarot_woodcut-v1.safetensors` in `models/loras/` — the deck **style LoRA**; supplies the woodcut look and is invoked by the `wdctarot` trigger in `assets/style.md`. Not published (it derives from FLUX.1-dev, whose licence is non-commercial); a fork trains its own (see § LoRA backup).
  - `4x-UltraSharp.pth` in `models/upscale_models/` — upscaler.

  If any of this is missing, use the § External-render fallback.
- Prereq (§ Find something new): `uv` on PATH; `scripts/novelty_rank.py` installs its own dependencies and downloads its embedding model once (~420 MB).

## Inputs
Required: none.
Optional:
- `trigger` — the date of the trigger reading the new card is for (its day's card is The Sower or The Miner); becomes the card's `sown_by` field. Without it, `python3 skills/tarot-daily-reading/scripts/daily.py triggers` lists the trigger draws still waiting for a card, oldest first; take the oldest, or ask the user when several wait. None waiting → no new card (§ Scope fence).
- `card_name` — the user's name for the card (still passes uniqueness).
- `image_path` — absolute path to a pre-rendered image. If given, Step 4 is skipped and Step 5 places this file.

## Decision points (routing)
- A new card → § Find something new first: it produces the title and Archetypal Essence that Step 1 checks; Step 1a's own name proposal is skipped.
- The user asks for a new or conforming image for a card that already has a card file → § Re-render an existing card (skip Steps 1–4).
- One small defect in a card's picture → § Repair a defect in one card.
- A moving loop for a card → § Animate a card.
- `content/cards/<slug>.md` already exists for a new card's title → it is not new: pick another title (Step 1).
- Uniqueness fails → revise the key terms and reproduce the table (max 3 retries, then escalate to the user with the conflicting candidates). The title and essence of a kept candidate are never revised: if the title itself clashes, or no clash-free key terms fit its meaning, the candidate drops, which counts as "none" in § Find something new. The user MAY explicitly accept a `near-match` after escalation → record acceptance; G2 then passes. A shared key term (`conflict`) is never accepted: `place_card.py new` refuses it.
- Render (Step 4): local pipeline available → render four seeds with `render_card.py`, recommend one, the user picks (4c); the user may ask for another batch or a revised scene instead. Server down or model missing → § External-render fallback.

## Quality gates
G1 (before Step 1): the clone is on `main` and `daily.py pull` succeeded.
G2 (end of Step 1): uniqueness comparison table produced (see Step 1). Passes if no row has verdict `conflict` or `near-match`, OR the user explicitly accepted a near-match after escalation.
G3 (end of Step 3): `content/cards/<slug>.md` exists, written by `place_card.py new`, with front matter `title`, `concept`, `key_terms`, `created`, `image_status: "pending"`, `image`, `sown_by`, and the sections `## Visual Description` (Composition, Symbolism, Atmosphere), `## Archetypal Essence`, `## Render Prompt` (fenced block, scene only — no style/border/title).
G4 (end of Step 4): either — (a) **rendered**: the user picked one of a batch of four (4c), the picked PNG is 1024×1792 with the deck frame + correct title; OR (b) **fallback**: § External-render fallback taken; OR (c) **given**: `image_path` was supplied at invocation and the user confirmed it as the card's picture. The user declines every candidate and asks for no further batch → report the candidates and stop; the card file stays uncommitted with `image_status: "pending"`.
G5 (end of Step 5): `place_card.py attach` succeeded: `content/media/card_<slug>.png` is a byte copy of the pick plus the label, the card file shows `![<Name>](/media/card_<slug>.png)` and (for a `render_card.py` image) a `## Render Record` whose seed and `comfy_file` match the pick, front matter `image_status: "present"`, `seed` and `renders_tried`, and `scripts/checksums.py check` passes.
G6 (end of Step 6): the user approved the card, and `place_card.py publish` committed it ("New card: <Name>") and pushed: `git log origin/main -1` shows that commit.
If a gate fails: fix once → re-check; else stop and report which gate failed and why.

## Scope fence
In scope: make ONE new card per invocation through § Find something new; write its card file; render its image locally (`scripts/render_card.py`); place, label and checksum it (`scripts/place_card.py`); commit and push it. Also in scope: re-rendering an existing card's image (§ Re-render an existing card), repairing one defect in a card's image (§ Repair a defect in one card), animating one card (§ Animate a card), each with the card file, media and checksum changes those sections name and their own commit.

Also in scope, on the user's request: a seed sheet for ONE existing card — render its `## Render Prompt` scene at many seeds with `scripts/seed_sheet.py` (e.g. overnight), outside the batch-of-four limit, into a folder under `<SOWER_WORK>/cards/<slug>/`, plus one contact sheet of thumbnails labelled with their seeds, shown with `place_card.py review`. A seed sheet only renders: no card file, media or commit change, and nothing is ranked. The user picks the seed; placing that render then follows § Re-render an existing card.

Out of scope: Upright/Reversed interpretation (meaning is per-use, produced at reading time from Visual + Essence); a new card without a trigger draw; more than one new card per invocation; editing existing cards beyond the re-render, repair and animate sections (title, key_terms and Archetypal Essence stay untouched); deleting cards; writing to Joplin or changing the old Dropbox archive (`dropbox:Tarot/cards/`, `legacy/`, and the deck clips and `deck.json` in `animations/`; only new files go to `seed-sheets/`, `animations/procedural/`, `animations/batch/` and `animations/source/`, through `SOWER_REVIEW` and `SOWER_BACKUP`); changing a reference file in `content/media/` other than through `place_card.py` (the label and the checksum list must follow every change, or the site build fails); installing ComfyUI or downloading model files (the user provides these); training a style LoRA (see `assets/style.md`).

## Stop conditions
Done when G1–G6 pass (via Step 6). Do not loop indefinitely: renders come in batches of four, and a further batch goes ahead only on the user's request (4c) — never on your own initiative.

## User approval gate
Nothing is committed or pushed before the user has approved it: the picked render for a new card or a re-render, the picked repair, the picked clip. Rewriting an existing card's `## Visual Description` needs the user's approval too. Never self-approve: if no interactive user is present to answer, STOP and report what needs approval, leaving the work uncommitted.

## Clarifying questions
Triggers: no trigger date given for a new card; a `card_name` that conflicts or is too close to existing cards.
Constraints: max 3 per phase; batch related questions.

## Find something new
How a trigger's new card is found: **reality exploring**. There is no reference list (traditional tarot, the I Ching or any other) to cover; the new card must be far in meaning from every existing card. One round:

1. **Seed.** The user always provides the seed; nothing draws seeds automatically. Ask for one and offer these sources:
   - bibliomancy: open any book at a random page and take the first noun or sentence the eye lands on;
   - something from the day: an event, an idea, a thought, an emotion;
   - someone else: a sentence about another person's day;
   - what is in front of you: the nearest object, a sound, a headline;
   - a calendar event, if the user allows reading the calendar with `khal` (read-only);
   - asking Claude for a seed. Only then improvise one, e.g. a random Wikipedia article (`https://en.wikipedia.org/api/rest_v1/page/random/summary`), a tarot card, an I Ching hexagram or an Elder Futhark rune, and mark it `suggested by Claude` as its source, because it carries Claude's own reference.

   **A Miner trigger starts from a gap** inside the deck instead of an outside seed: a meaning no card holds yet, found between two cards. `uv run --no-config --script skills/tarot-card-generator/scripts/novelty_rank.py gaps` lists the five widest gaps: pairs of cards whose shared meaning lies farthest from every other card, each card in one pair at most. Show the list as printed; the user picks one gap (nothing picks it for them). The seed is `between <card> and <card>` with source `gap`. Read both cards' files before writing candidates: a candidate holds what the two share that neither holds alone, as its own place, object, process or figure, not a blend of the two. When a gap's round ends with none kept, offer the list again.
2. **Candidates.** For the seed write 3 candidate cards: a title and a full Archetypal Essence of 75 to 150 words (the length of the cards' own; a one-line essence against full ones skews the scores), in the deck's own idiom (most cards are places, objects or processes; few are figures). Each candidate stays with its seed: do not vary the seed into opposites or other viewpoints. Write them to `<SOWER_WORK>/cards/candidates-<date>.json` as a list of `{"title", "seed", "seed_source", "essence"}`.
3. **Ranking.** `uv run --no-config --script skills/tarot-card-generator/scripts/novelty_rank.py <that file>` scores each candidate by its distance in meaning to its nearest existing card and prints the list, most distant first, with the deck's own spacing for scale. Show the list as printed. There is no cut-off: distance only orders the list, and far is not the same as meaningful.
4. **Choice.** The user keeps one candidate, or none. Under a trigger, "none" means another seed (or gap) and a new round, until one card is kept. A kept candidate goes on to Step 1 with its title and essence as given; Step 1 may change only its key terms, and a candidate that cannot pass drops, which counts as "none". Record the round (seed, source, candidates, distances, the pick) in the Step 6 report.
5. **Image variety** (Step 2's composition brief and Step 4's review): the new card's image must differ from the existing cards within the deck style. Steer at the brief, warn on the renders; never maximise image distance, because in a one-style deck the renders farthest from the other cards are often the ones that break the style.
   a. **Brief from the composition map, before rendering.** Tag every existing card by figure count, interior or landscape, sun/moon disc or not, and action or stillness, from each card file's `### Composition` text (`the-ember.md` and `the-forge.md` have one "Visual Description" text instead) or the PNGs in `content/media/`; list the tag combinations in use; propose 2–3 unused combinations that fit the candidate's meaning; the user picks one for the composition brief.
   b. **Duplicate guard on the seed sheet.** When renders are shown (4c), flag any render that looks like an existing card, naming it. A warning only; the user still picks. Compare by eye against the existing cards that share the most tags with the new card.

## Workflow

### Step 1 — Validate uniqueness
**1a. Name and key terms.** Take the title from § Find something new (or the user's `card_name`). Propose 3–6 `key_terms`: the main noun(s) from the name, core concept words, and similar/related terms to avoid (e.g. "Weaver" vs "Thread Weaver" — reuse of a term even in a slightly different form counts as a collision). Also a `concept` of 3–6 words.

**1b. Validate uniqueness.** `python3 skills/tarot-card-generator/scripts/place_card.py terms` lists every card's title, concept and key terms. Verify the proposed name does NOT match any existing card name, does NOT reuse any existing key term, and explores a genuinely new archetype/object/metaphor.

**Proof-of-work: uniqueness comparison table.** Before Step 2, output this and keep it in the conversation:
1. **Proposed name:** `"..."`
2. **Proposed key_terms:** `[...]`
3. **Comparison table** — one row per existing card with name-stem or key-term overlap, plus a single summary row for the rest:

| Existing card | Existing key_terms | Verdict | Rationale |
|---|---|---|---|
| The Lighthouse Keeper | lighthouse, keeper, light | no-conflict | No shared nouns or concepts |
| The Mirror Lake | mirror, lake, reflection | near-match ⚠ | "reflection" thematic overlap — revise the proposed name |
| {N} other cards | — | no-conflict | No name-stem or key-term overlap with proposal (verified by scan) |

Verdicts: `no-conflict` | `near-match` (thematic overlap) | `conflict` (shared key_term or name).

Pre-filter for which cards get their own row: a card earns a row if (a) its name shares a stem with the proposed name, OR (b) any of its `key_terms` overlaps (exact or stem) with the proposed `key_terms`, OR (c) it occupies a closely related archetypal/symbolic neighborhood. All others collapse into the summary row. Any individual `conflict`/`near-match` row → revise the key_terms and reproduce the table (max 3 retries before escalating per § Decision points).

### Step 2 — Generate card content
Using the validated name, write three sections only — no Upright/Reversed bullets.

**Visual Description (Rider-Waite style)**, from the composition brief (§ Find something new, 5a):
- **Composition:** central figure/focal point; foreground/middle/background elements; symmetry or asymmetry; positioning and posture of any figures.
- **Symbolism:** adapt traditional Rider-Waite symbolic vocabulary (color conventions, natural/animal/object symbols, sacred geometry, clothing cues) to the new concept — elements that reinforce the archetype, not decorate it.
- **Atmosphere:** time of day; weather/celestial conditions; emotional tone; lighting quality (harsh, soft, mystical).

**Archetypal Essence:** the kept candidate's essence from § Find something new, as given. This is the canonical meaning layer; reading-time interpretation builds on it but is not stored here.

**Render prompt (the scene — this is what gets rendered).** Write ONLY the
card-specific scene: the figure, symbols, setting, light and mood from the Visual
Description above, as one flowing paragraph. Do NOT write the style, palette,
border, banner, or title into it — `render_card.py` prepends the frozen style
block and appends the frame-agnostic tail from `assets/style.md`, and
`frame_card.py` draws the border + title. Writing a border or title text into the
scene causes a double border and garbled lettering (the model cannot spell).

Rules for the scene text:
- Describe the scene edge-to-edge; leave the bottom ~12% free of critical detail (the title banner sits there).
- No words for style/medium/palette (the style block owns those), no "tarot card", no "border/banner/title/frame", no lettering.
- Store it in the card file under `## Render Prompt` (see Step 3). This is the canonical prompt.
- **One figure, one focal object, one gesture.** Lead with the action in the first sentence; add at most two or three supporting symbols. About 120 words. A long scene with a dozen props makes FLUX drop the core action (The Forge: 21 renders at ~190 words).
- **Name the figure's clothing concretely and vary it across the deck** — "leather apron", "linen tunic", "woollen habit", "ochre travelling coat". Left generic, the style LoRA falls back on a hooded robe (its training default) and the deck turns monotonous; "hooded figure" alone renders as a modern hoodie with drawstrings.
- **Say what the model should draw, not what it should leave out.** Negations ("no flame", "no stars") tend to backfire; describe the wanted thing instead ("flameless", "plain dark stone wall").
- **Known word traps:**
  | Wording | Renders as | Use instead |
  |---|---|---|
  | "ember", "glowing coal" | a flame | "a walnut-sized lump of black charcoal cracked with glowing red veins" |
  | "a thin thread of smoke rises straight up" | an orange line topped by a cross | "a faint grey wisp of smoke curls upward" |
  | "window shows pre-dawn light" (no view named) | a blank cream panel, or a gold sun | name the view: "a pale grey pre-dawn sky over distant hills" |
  | symbols, patterns or writing drawn in ash, sand or on walls | stray glyphs | leave them out |
  | matches, clocks, modern tools | breaks the style block's "no modern objects" | a period equivalent, or leave out |
  | "both hands cupped around her mouth" | she holds a cup or bowl | "hands raised to her mouth, calling" |
  | "sound rings spreading from her" (with a sun or moon in the scene) | the rings drawn around the sun | leave the rings out, or the sun/moon out |
  | "the right half of the valley hidden in mist" | no mist; FLUX ignores half-frame layout instructions (0 of 50 renders, 2026-10-01) | accept without, or add the mist with § Repair |
  | an old man, no eyewear named | sometimes modern-looking glasses | check the face; remove with § Repair |
- **Expect more renders for content the style LoRA has not seen.** Its training images are mostly one figure outdoors with one object and a sun or moon above; such scenes land in 1–4 renders. Indoor close-ups lit by a tiny source, transparency or refraction, and precise two-handed actions took 12–21 renders. Tell the user up front when a scene is in that class.

**DALL-E 3 prompt (fallback only).** Generate this ONLY when the local pipeline
is unavailable and you are taking the § External-render fallback. It is the
self-contained variant that bakes in style + border + title for an external
renderer. Template:
```
Create a tarot card in the traditional Rider-Waite style with the title "[CARD NAME]" at the bottom.

[Detailed visual description with all symbolic elements...]

Style specifications:
- Traditional Rider-Waite tarot aesthetic
- The card must fill the entire image canvas edge-to-edge — NO white, cream, or empty margin outside the card's border; the border runs along the actual edges of the image
- ONLY ONE single, simple thin rectangular border in beige/tan/cream color - no inner decorative borders, no ornate frames, no flourishes or decorative elements on the border
- Clean rectangular name tag at the bottom with "[CARD NAME]" in uppercase serif font on a solid tan/beige background
- The border should be plain and minimal - just a simple frame along the image edges
- Rich, symbolic imagery with mystical atmosphere
- Classic tarot card proportions and layout
```

### Step 3 — Write the card file
Write the three sections to `<SOWER_WORK>/cards/<slug>/sections.md` in this form (headings exactly so):

````markdown
## Visual Description

### Composition
[...]

### Symbolism
[...]

### Atmosphere
[...]

## Archetypal Essence

[the essence]

## Render Prompt

```
[scene-only render prompt from Step 2 — no style/border/title]
```
````

Then create the card file:
```bash
python3 skills/tarot-card-generator/scripts/place_card.py new --title "<Card Name>" --concept "<concept>" \
  --key-terms "<term1>, <term2>, <term3>" --body <SOWER_WORK>/cards/<slug>/sections.md --sown-by <trigger date>
```
It writes `content/cards/<slug>.md` (`<slug>` = the title lowercased, every run of other characters a hyphen: "The Compass Rose" → `the-compass-rose`) with the front matter (`created` today, `image_status: "pending"`, `prompt_status: "original"`, `image: "card_<slug>.png"`, `sown_by`), the title heading, the tagline, the placeholder `_(image pending)_` and the sections. It refuses a `--sown-by` date that is no trigger draw waiting for a card (`daily.py triggers`), an existing card file, a key term another card already has, fewer than 3 or more than 6 key terms, and a missing section; it warns about key terms sharing a word stem with another card's. A DALL-E fallback adds a `## DALL-E Prompt` section to the card file by hand after this step.

### Step 4 — Render the image locally
Render the card with the bundled pipeline: FLUX art → ESRGAN upscale → framed title card. One call does everything.

**4-pre. Skip if pre-rendered.** If `image_path` was given at invocation, skip Step 4 and go to Step 5 with that path.

**Instance.** Run every render or edit script, and every `comfy` command below, through `with-comfy`:
`/workspace/.claude/tools/with-comfy/with-comfy local|remote <command>` (`$W` below). It forwards a loopback
port to the instance (`local` = the host GPU; `remote` = a second machine on the local network, up 19:00–07:00), checks it
answers (exit 69 = not answering: tell the user) and sets `COMFY_LOCAL_URL`, which the scripts and the
`comfy` CLI read. Batch each model's jobs together on `remote`: a FLUX↔Qwen switch costs ~4 min there. (A fork without `with-comfy` sets `COMFY_LOCAL_URL` itself or uses the default `http://127.0.0.1:8188`.)

**4a. Preflight.** Confirm the local server answers and the models are present:
`comfy --json model list-folder checkpoints --where local` lists `flux1-dev-fp8.safetensors`, and `comfy --json model list-folder upscale_models --where local` lists `4x-UltraSharp.pth`. If the server is down (`server_not_running`) or either model is missing, take the § External-render fallback instead of failing.

**4b. Render a batch of four seeds.** Render four different seeds into the card's work folder — never straight into `content/`:
```bash
$W local python3 skills/tarot-card-generator/scripts/render_card.py \
  --scene "<the ## Render Prompt scene text from the card file>" \
  --title "<Card Name>" \
  --seed <integer> \
  --out <SOWER_WORK>/cards/<slug>/<slug>_<seed>.png
```
- Any four distinct integer seeds. Each run prints a JSON result line with the `seed` and `comfy_file` (e.g. `tarot_flux_final_00090_.png` — its number, 90, is the image number used to talk about the render).
- The script prepends the frozen style block and appends the frame-agnostic tail from `assets/style.md`, runs `assets/tarot-card-flux.json`, then frames via `scripts/frame_card.py` with the frozen frame flags. Do NOT pass style, palette, border, or title into `--scene` — that causes a double border and garbled text.
- Count every render the user is shown for this card; the total goes into Step 5's `--renders`.
- On any render failure, invoke the `comfy-debug` skill before retrying.

**4c. Review, recommend, let the user pick.** Build a side-by-side contact sheet of the four renders with Pillow and look at it; open the strongest candidate at full size. Copy the renders and the sheet where the user looks at them: `python3 skills/tarot-card-generator/scripts/place_card.py review --card "<Card Name>" <files>` (into `<SOWER_REVIEW>/seed-sheets/<slug>/`, Dropbox for this user; the rejected renders stay there as the card's tailings). Every render must show the scene in the frozen style, a single clean border and the correct title. Defects that rule a render out: stray glyphs, numbers or ornaments (especially at the top edge), duplicated objects, extra limbs, modern objects. A candidate that is right except for one small, local defect can be picked and then fixed per § Repair a defect in one card, instead of re-rolling seeds. Run the duplicate guard (§ Find something new, 5b). Report each candidate by image number and seed with its strengths and defects, recommend one, and ask the user to choose (AskUserQuestion). The user may instead ask for four more seeds or a revised scene; do what they choose, then review again. Never pick on the user's behalf: with no interactive user, stop with the four candidates reported and the card file left uncommitted.

Batch-level fixes: a double border in every render → the scene text wrongly included a border/frame; remove it from `## Render Prompt` and re-render. The same content defect across seeds → revise the scene per the Step 2 rules, not the seed. Palette drift beyond the earthy range that persists across seeds → tighten the palette words in `assets/style.md` (this re-styles the WHOLE deck — a deliberate deck-level change, not a per-card fix).

**4d. Scene used.** If the scene was revised during 4c, update the card file's `## Render Prompt` to the scene actually used (`place_card.py attach` warns when they differ).

### Step 5 — Place the picture
```bash
python3 skills/tarot-card-generator/scripts/place_card.py attach --card "<Card Name>" \
  --image <SOWER_WORK>/cards/<slug>/<slug>_<seed>.png --renders <renders shown for this card>
```
It refuses a render made with another title, then: labels a byte copy of the PNG (`scripts/label_media.sh`: IPTC "trainedAlgorithmicMedia", creator "Sower Tarot", CC BY-NC-SA 4.0, as XMP; the PNG's `tarot_render` record is kept) and moves it to `content/media/card_<slug>.png`; replaces `_(image pending)_` with `![<Card Name>](/media/card_<slug>.png)`; writes the PNG's render record into the card file as a collapsed `## Render Record` section (seed, title, scene, full prompt, frame flags, ComfyUI version and the executed ComfyUI graph — enough to re-render the image with `render_card.py --from-card`); sets `image_status: "present"`, `seed` and `renders_tried`; and rewrites `content/checksums.txt` (`scripts/checksums.py write`). A PNG without a record (external render) is placed with a warning and gets no Render Record. Never copy a card PNG through an image library: the record lives in its PNG text chunk.

### Step 6 — Approve, publish, report
1. Show the user the placed card (the PNG and the card file's text) and ask for approval to publish (§ User approval gate).
2. `python3 skills/tarot-card-generator/scripts/place_card.py publish --card "<Card Name>"`: checks the front matter, the attached picture and `checksums.py check`, refuses while `content/media/` holds files git does not track that belong to no card being published (the published checksum list would name them and the site build would fail), commits the card file, its media and `content/checksums.txt` as Sower Tarot ("New card: <Name>") and pushes (rebasing onto a moved `main` when needed). The card joins the first 07:00 draw after the commit. Then it closes the trigger draw's Parked note (when `SOWER_PARKED` is set; the 07:00 job opened it, titled "Make the new card from the <Sower|Miner> draw of <date>"): found by its exact path, then by id it prepends `Status: closed <date> — <Name> committed (<commit>)`, removes the tags `parked` and `handoff` and moves the note to `<SOWER_PARKED>/Done`. If it warns that the note was not closed, do the same by hand: `joplink --json note get "Parked/<note title>" --fields id`, then `joplink note prepend <id> --text "Status: closed <date> — <Name> committed (<commit>)" --separator $'\n\n---\n\n'`, `joplink tag untag-note <id> parked`, the same for `handoff`, and `joplink note move <id> Parked/Done` (always by id: a write by path to a moved note creates a duplicate).
3. Run G1–G6.
4. Report: card name, card file, the § Find something new round (seed, source, candidates with distances, pick), render seed and image number, `renders_tried`, the commit, and that the site rebuilds on the push.
5. Offer to animate the new card (§ Animate a card, New card). Until it has a clip, the site shows it as a still.

## Card file fields
Front matter, one `key: <JSON value>` line each, in this order (`place_card.py` writes them; the daily draw and `scripts/draw_check.py` parse this form, so never hand-write another):
- `title`, `concept` (3–6 words), `key_terms` (3–6), `created` (YYYY-MM-DD) — required by the site (`src/content.config.ts`).
- `seed` — the seed of the base render, or `null` for an external render. The full recipe is the `## Render Record`; the `## Render Prompt` can later be edited, so it alone does not guarantee the image.
- `image_status` — `pending` (no picture placed yet; never published) | `present`.
- `prompt_status` — `original` (prompt written at creation) | `legacy_no_prompt` (imported legacy card).
- `image` — `card_<slug>.png` in `content/media/`, required by the site. `clip` — the card's MP4 in `content/media/`, if it has one.
- `joplin_note` — only on the 37 cards migrated from Joplin (their old note id).
- `sown_by` — the date of the trigger reading the card grew from; the public record of which trigger made which card.
- `renders_tried` — every render the user was shown for the card (website decision 80; The Miner took 124); cards made before 2026-10-27 have none.

## Deck style consistency
Every card must read as one deck. Consistency comes from freezing everything
except the scene and the seed. Four layers, three frozen:

| Layer | Role | Where |
|---|---|---|
| Style block (prompt preamble) | fixed woodcut Rider-Waite descriptors + explicit palette | `assets/style.md` § Style block — prepended by `render_card.py` |
| Render params | fixed checkpoint, sampler, guidance, steps, size, upscale | `assets/tarot-card-flux.json` (contract listed in `assets/style.md`) |
| Frame | fixed margin/border/banner/font/colors → identical layout + typography | `scripts/frame_card.py` + frozen flags in `render_card.py` |
| Scene + seed | the ONLY per-card variables | card file `## Render Prompt` + Step 4 `--seed` |

Rules:
- Never re-style a single card by editing the scene toward a style. A per-card look drift is fixed by reseeding, not by prompt-styling.
- A genuine style change is a **deck-level** edit to `assets/style.md` (palette words, medium, frame colors). It changes all future cards by design; it does not retro-fit existing ones.
- Prompt-only style is *recognizably* one deck; per-card wobble in linework/palette is expected. For published-deck tightness, train a style LoRA (see `assets/style.md` § Maximum-fidelity option) — a separate, later task, out of this skill's scope.

## External-render fallback
Use ONLY when the local render pipeline is unavailable (no ComfyUI/`comfy` on
PATH, `flux1-dev-fp8.safetensors` or `4x-UltraSharp.pth` missing, or no GPU).
In place of Step 4:
1. In Step 2 also produce the **DALL-E 3 prompt** (self-contained: style + border + title baked in) and add it to the card file under a `## DALL-E Prompt` fenced block after Step 3.
2. Give the user the prompt in a copy-friendly code block; the user renders in ChatGPT/DALL-E and saves the result as a PNG, then names its path.
3. Step 5 places that file (`place_card.py attach` warns that it has no render record; `seed` stays `null`, no `## Render Record`). G4 passes via its `fallback` branch.

This path forgoes the deck-style guarantees — an external renderer will not match the frozen style block, so mixing fallback cards into a locally-rendered deck will show a visible style seam. Prefer the local pipeline whenever it is available.

## Re-render an existing card
Use when a card that already has a card file needs a new image in the deck style. Steps 1–3 are skipped: the name, key_terms and Archetypal Essence already exist and stay untouched. The old picture is not copied anywhere: git history keeps it (website decision 78).

**R1. Read the card.** `content/cards/<slug>.md`: its sections and front matter.

**R2. Write the scene fresh.** Do not trim the card's old DALL-E text into a scene; its prop lists and ritual details carry the word traps from Step 2. Write a new scene per the Step 2 render-prompt rules, keeping the card's meaning. If the card has no figure (a still life, hands only), consider adding one — scenes without a figure render worst. A changed composition means R5 must rewrite the Visual Description, so tell the user before rendering.

**R3. Render four seeds and let the user pick.** Run Step 4a–4c exactly as for a new card: preflight, a batch of four seeds into `<SOWER_WORK>/cards/<slug>/`, then review, recommend and let the user choose. Never place a render without the user's pick. Before recommending a render (here or from a seed sheet), open it at full size and check the sky and the top edge: a seed-sheet thumbnail is too small to show a sun, moon or glyph reliably (on 2026-10-03 a recommended render turned out to have a moon).

**R4. Place the pick.** `place_card.py attach --card "<Card Name>" --image <pick> --replace` (add `--renders <n>` only for a card that has `renders_tried`). It replaces `content/media/card_<slug>.png`, the card file's `## Render Record` and `seed`, and the checksum list.

**R5. Update the card file.** Put the scene used into the `## Render Prompt` fenced block (replace the old scene; add the section before `## DALL-E Prompt` only if the card has none). If the composition changed, rewrite `## Visual Description` (Composition, Symbolism, Atmosphere) to match the new image — only with the user's approval. Edit the file directly; keep the front matter as `place_card.py` wrote it.

**R6. Publish.** `place_card.py publish --card "<Card Name>" --message "Re-render card: <Card Name>"`. The card's clip, if any, still shows the old picture: tell the user, and offer § Animate a card.

**Done when:** the commit is on GitHub, the card file has `## Render Prompt`, the new `seed` and a Render Record matching the pick. Report the image number, seed and commit.

## Repair a defect in one card
Use when one rendered card is right except for a small, local defect — a stray ornament at the top edge, a hanging line, an extra object — and the user wants that fixed, not a new render. The image-edit model is Qwen Image 2.1 (`assets/tarot-card-qwen-edit.json`; chosen over FLUX Kontext on 2026-09-24 because it edits at full 1024 × 1792 and its edits line up pixel for pixel with the original). Prereq: ComfyUI 0.37.0 or later with `qwen_image_2.1_int8_convrot.safetensors` (`diffusion_models`), `qwen3vl_8b_int8_convrot.safetensors` (`text_encoders`) and `qwen_image_2.1_vae_bf16.safetensors` (`vae`). The card file must have a `## Render Record` (Step 5); a card without one is re-rendered instead.

**Sun or moon on a flat sky: fill it, don't edit it.** A disc on a plain or gently graded sky (no clouds, linework or texture crossing it) is removed with `scripts/fill_disc.py`, not Qwen: it fills the disc from the sky around it, so no box-shaped patch can appear, and needs no ComfyUI. Choose the box as in E2 but with plain sky on every side of the disc and its glow, then:
```bash
python3 skills/tarot-card-generator/scripts/fill_disc.py --name "<Card Name>" --art <unframed art> --box <x0,y0,x1,y1> \
  --out <SOWER_WORK>/cards/<slug>/<slug>_fill.png --keep-art <SOWER_WORK>/cards/<slug>/<slug>_fill_art.png
```
`--art` is the card's current unframed art (regenerate it as in E3 if needed). Add `--grow 24` when a faint rim or glow remains, `--thresh 40` on a graded sky where the mask runs to the box edge. Review as in E4 and attach as in E5. A disc with clouds or drawing across it goes through E1–E5 with Qwen. So does a disc on a dark night sky: `fill_disc.py` treats every pixel darker than 90 (of 255) as ink linework (`repair_tools.py`), so on a black sky it stops with "no disc found in the box" (The Veil, 2026-10-04). There, say "Fill its place with the same black night sky scattered with small white stars"; the edit adds stars spaced like the rest of the sky.

**A light halo round linework on a flat sky: fill it, don't edit it.** For a pale rim round a drawn bird or figure, run `fill_disc.py` with `--halo --grow 2` and a box round the figure with plain sky on every side: it repaints only the rim from the sky and keeps the drawing (`repair_tools.fill_halo`, recorded as `method: fill_halo`). Qwen cannot do this: asked to remove the halo it deleted the whole gull, asked to recolour it it widened the rim (The Anchor, 2026-10-24).

**Before editing, check the art is the card's current art.** `render_card.py --from-card` may no longer reproduce the picture (The Anchor's base render drifted to a different anchor by 2026-10-24). Frame the art you will edit (`frame_card.py` with the record's frame flags) and compare it with the card PNG; if they differ, look for the saved art in the old Dropbox archive (`dropbox:Tarot/seed-sheets/discs/`, `seed-sheets/repairs/`, the Render Record's `note`; read only) or `tools/animate/batch/<slug>/art.png` instead.

**Adding an object across the picture, or combining several repairs.** To add something large (The Miner's timber props, 2026-10-25), run Qwen with one box over the whole area. It redraws everything in that box: the figure and the lamp moved by 20–40 levels. So keep only the new object. Tone-match the raw output once over the box it was run with, then paste it through one mask, the union of rectangles round the object, with a single soft edge. Two boxes pasted one after the other, edge to edge, each reach only half strength at their joint and leave a faint line of the original. Separate per-box tone matching leaves a tone step where boxes meet. Step the boxes around anything in front of the object (the lamp) so it stays original. Apply the separate repairs in an order that keeps earlier fixes: a later paste from a whole-box output brings back defects that an earlier repair removed (the smudge's flecks came back beside the post). Qwen also redraws a whole object when asked to fix part of it (the pick's handle moved), so the paste box must cover the whole object and stay off its neighbours (the lamp foot). Name the new object's place and what must stay visible: "posts against the outer walls; the rock heap stays in front of the left post's foot". Without that it covered the heap.

**E1. Check the defect survives framing.** The frame crops 3.5% from every side and covers the bottom ~8.5% with the title banner. A defect only in those areas needs no repair — say so and stop.

**E2. Choose the repair box.** Open the unframed art (the record's `comfy_file`, `<instance URL>/view?filename=<comfy_file>&type=output`, e.g. `http://127.0.0.1:8188` for `local`) at full size with a pixel grid and pick a box `x0,y0,x1,y1` around the defect. The box must span the whole structure the defect belongs to — for example the full width for a border or banner element — or its edges cut through that structure and leave stubs or seams. Only the box is kept; everything outside it stays exactly as rendered.

**E3. Edit three seeds.** Write the instruction in plain words: what to remove and what to fill its place with, for example "Remove the thin hanging line at the top center of <image1>. Fill its place with the same dark night sky." (`edit_card.py` appends "Keep everything else, including the woodcut linework and hatching, exactly the same."). Run seeds 1–3 into the card's work folder:
```bash
python3 skills/tarot-card-generator/scripts/edit_card.py --name "<Card Name>" --seed <n> --box <x0,y0,x1,y1> \
  --instruction "<instruction>" --out <SOWER_WORK>/cards/<slug>/<slug>_repair_<n>.png --keep-art <SOWER_WORK>/cards/<slug>/<slug>_repair_<n>_art.png
```
`edit_card.py` evens the box's tone to the original by default (`repair_tools.tone_match`): Qwen returns the whole edit 4–16 colour levels lighter or darker, which on a flat area shows as a rectangle even when the defect is gone (2026-10-03 sun removals). Pass `--no-tone-match` only for an edit meant to change the colour inside the box. If `comfy_file` is no longer in ComfyUI's output, regenerate the unframed art with `render_card.py --from-card "<Card Name>" --out <SOWER_WORK>/cards/<slug>/x.png --keep-raw <SOWER_WORK>/cards/<slug>/<slug>_art.png` and pass that as `--art`.

**E4. Review and let the user pick.** Compare each repair with the original inside the box only, at full size: the defect gone, the fill continuous with its surroundings, no seam at the box edge, the woodcut hatching intact. Then view the same crop at contrast ×5 (subtract the crop's median colour, multiply by 5, add 128): a box or round patch that shows there may be visible to the user at normal contrast on a good screen; say what remains in your recommendation rather than calling it clean. Recommend one and let the user choose (AskUserQuestion). If every seed fails, adjust the box (E2) or the instruction, not the seed count.

**E5. Place and publish.** `place_card.py attach --card "<Card Name>" --image <pick> --replace`, then, after the user's approval, `place_card.py publish --card "<Card Name>" --message "Repair card: <Card Name>"`. The card's record gains a `repairs` entry (instruction, box, seed, edit workflow and `tone_match`; or for a sky fill `method: fill_disc` with box, grow and thresh), so the card file still reproduces its image: `render_card.py --from-card` replays both kinds. Not exactly replayed: a combined repair (one Qwen output pasted through a union mask with one `tone_box`, as The Miner's timber on 2026-10-25), which `--from-card` re-runs box by box; for such a card start from its saved art (`tools/animate/batch/<slug>/art.png`, or the old archive). The old picture stays in git history. If the `## Visual Description` mentions the removed element, update it with the user's approval (before publishing). If the card has a clip, its frames still show the defect: tell the user, and offer to re-render the clip on the repaired art (§ Animate a card).

**Done when:** the commit is on GitHub and the card file's `## Render Record` lists the repair.

## Animate a card
Use when the user wants a card as a short looping animation (moving flames, water, stars). Only the part that should move is animated; everything else stays the card's original pixels, because an image-to-video model run over the whole card softens the ink outlines and hatching and drifts figures. Every card has one clip, named in its card file's `clip` field and stored in `content/media/` (`<slug>_code_v<N>.mp4` on the code route, e.g. `the-miner_code_v2.mp4`; AI-route clips keep their render names, e.g. `the-forge_s2_v2.mp4`). A code-made clip's exact command is `tools/animate/procedural/card_<slug>.code.txt`.

**Pick the route per card.** The **code route** (§ Code route below) draws the motion with a script: no AI model, exact style, exact loops. It is the default: 27 of the 36 picks use it. The **AI route** (A1–A5, Wan 2.2 5B image-to-video) only for an element that moves strongly by nature and is hard to draw: fire in a hearth, a pouring stream, a running hourglass, smoke curling, sea waves breaking. On the AI route, subtle elements failed (2026-10-07/08): calm prompts gave motion the user could not see, stronger ones random movement; light effects (stars, glows, beams) moved strangely; small birds and bees duplicated or vanished.

Prereq: ComfyUI 0.37.0 or later with Wan 2.2 5B — `wan2.2_ti2v_5B_fp16.safetensors` (`diffusion_models`), `umt5_xxl_fp8_e4m3fn_scaled.safetensors` (`text_encoders`), `wan2.2_vae.safetensors` (`vae`); files and settings from ComfyUI's template `video_wan2_2_5B_ti2v`. Also installed: Wan 2.2 14B first-and-last-frame (`--model 14b`, template `video_wan2_2_14B_flf2v`), which loops without a crossfade. Tested on The Forge 2026-10-06 and not used: with its 4-step speed-up LoRAs the fire moved half as much as the 5B (12 vs 26.5); with `--full` (20 steps, ~19 min a clip) still 15–16 and blown out to white mid-clip. Use 5B.

**A1. Prepare the art.** Take the card's current unframed art (the `## Render Record`'s `comfy_file`, or its last repair's output). Trim 3.5 % off each side and resize back to 1024 × 1792 — the same as `frame_card.py --art-crop 0.035` — and save it as the card's art. Save a 576 × 1024 copy anywhere local; `animate_wan.py` uploads a local file to ComfyUI's `input` folder itself (the remote PC's `input` is not mounted, and is emptied at 07:00).

**A2. Draw the mask.** A greyscale PNG at 1024 × 1792 over the trimmed art: white where the motion goes, black elsewhere, blurred ~10 px for a soft edge. Cut figures, faces and hands out of it, even where they overlap the moving area. Leave a margin of 10–40 px around them, widest at loose hair and clothing: the model shifts a figure by a few pixels, and without a margin that shifted copy shows as a ghost next to the real one (The Tide seed 3, 2026-10-06). A small drawn element inside the moving area that should stay put (water poured from a bowl) may drift in the model's output: track its position across the raw frames and freeze a strip covering the whole drift, taken from the original card (The Tide: a 135 px strip). Do not paint the element out of the model's input instead: with nothing there to animate, the model moved the figure's bowl and hands into the sea and made the waves jerk (2026-10-07). Check it as a pink overlay on the art before rendering. Keep the mask small: over a large or empty area (a whole sky, a whole field) the model invents objects (a duck's head, a beetle, a motorboat) or redraws the scene (batch of 2026-10-07). An element that is small on the card (an hourglass, a torch flame, a thin wisp of smoke, a small tree) renders as a blob at 576 × 1024; give the model a 9:16 box around it instead with `scripts/animate_mask.py crop <card dir> x0,y0,x1` (writes `crop.txt` and the model input; `animate_compose.py --crop` and the batch worker paste the frames back into that box). Prompts for small elements describe calm motion; "thousands of leaves churning" turned a tree crown into a blob.

**A3. Render.** `scripts/animate_wan.py --model 5b --image <576×1024 PNG> --seed <n> --prefix <slug>_5b_s<n> --prompt "<motion>"` (121 frames at 24 fps, ~3 min on the RTX 4080 once loaded, ~5 min cold). Run both scripts through `with-comfy local` or `with-comfy remote` (a second ComfyUI machine on the local network, available evenings only; has the same Wan files since 2026-10-06); they read the `COMFY_LOCAL_URL` it sets. The prompt describes the motion strongly and ends with "Camera static, no zoom, no pan." Do not ask for stillness or for the style to "stay unchanged": that damps the motion, and the mask already keeps the rest still. Style words ("ink outlines, no glare") also damp it — on The Forge, motion inside the mask (mean pixel change per 4 frames) was 8.9 with a gentle prompt, 10.7 with a style-heavy one, and 24–27 with a strong one. Render two or three seeds; strong prompts vary a lot between seeds (one may blow out to a white blaze, another add smear streaks).

**A4. Compose.** `scripts/animate_compose.py --frames-prefix <prefix> --count 121 --fps 24 --art <trimmed art> --mask <mask> --title "<Card Name>" --out <slug>_5b_s<n> --crossfade 0.5` pastes each frame into the art inside the mask, frames the card once with the deck frame flags (so the paper texture doesn't flicker), blends the last half second into the first to close the loop (5B cannot end on its start image), and writes `<out>.mp4` and `<out>.webp`. For `--model 14b` output use `--fps 16 --count 81` and no `--crossfade`.

Speed and loop are chosen per card: `--slow N` slows the clip by motion interpolation (water read best at 3×; a bird was right at 1×), and `--pingpong` plays it forward then backward, which the user preferred over a crossfade (a crossfade of 0.5 or 1.5 s shows). Do not slow past 2× for anything with edges that travel: 3× interpolation showed as jumping frames (lighthouse beams, lake ripples). Prompts must not ask for speed ("fast", "racing", "rapidly"): the user found such clips much too fast.

**A5. Review and let the user pick.** Pre-filter on motion first: `tools/animate/check/check.py` (it reads `tools/animate/batch/<slug>/<slug>_s<seed>.mp4` with that card's `mask.png` and `art.png`; set its card and seed loop) measures the mean pixel change inside the mask; every clip the user kept scored 9.4 or more, and below about 9 the user saw no movement, so don't show those. Still frames show ghosts, smears and edges, not whether motion looks natural — waves that jerk back and forth look fine as stills — so only the user's viewing judges the motion. Look at close-ups of the masked area across the clip (start, middle, end) for blown-out areas, smears and a visible mask edge, and compare the jump from the last frame to the first with the change between neighbouring frames. Show every candidate's MP4 with `place_card.py review --card "<Card Name>" --clips <files>` (into `<SOWER_REVIEW>/animations/procedural/`); the user judges them by watching. After the pick, deliver it (§ Code route, Deliver); keep the mask and prompt as `tools/animate/procedural/card_<slug>_mask.png` and `card_<slug>.prompt.txt`.

**Done when:** the user picked a clip and it is delivered and published (§ Code route, Deliver).

**Batch (many cards, unattended).** For a run over many cards, use a batch folder with one subfolder per card slug holding `art.png` (A1), `input_576x1024.png`, `mask.png` and `prompt.txt`, plus `jobs.json` (`[{"slug","name","seed"}]`, all cards' seed 2 first, then seed 3, ...). `scripts/animate_mask.py grid|make|zoom <card dir>` draws and checks a mask from polygons in art pixels. Mark a card `READY` (empty file in its folder) only after checking its pink preview. Start one detached worker per ComfyUI instance: `setsid nohup python3 scripts/animate_batch.py --dir <batch> --worker local|remote > worker_<name>.out 2>&1 < /dev/null &` — never stop them with `pkill -f animate_batch.py` from a shell whose own command line contains that name (it kills the shell); kill by PID. Workers share the queue (`state.json`, `run.log`), skip cards without `READY` until they appear, retry a failed job once, release the job and exit when their instance is down (the remote after 07:00), and copy each MP4 to `<SOWER_REVIEW>/animations/batch/` (`--copy-to` overrides; with `SOWER_REVIEW` empty the MP4 stays in the batch folder). A worker restarted later resumes where the queue stands. First batch: 34 cards × seeds 2–4, 2026-10-07. Use `tools/animate/batch/` as the batch folder (ignored by git): `tools/animate/check/check.py` reads the clips from there.

### New card
A new card has no clip. To give it one:
1. Prepare its art as in A1 into `tools/animate/batch/<slug>/art.png` (ignored by git; the recorded commands read it).
2. Propose one moving element with the user.
3. Make it on the code route if a script fits the element (§ Code route); use the AI route only for strong natural motion (fire, pouring water, breaking waves). Show the pilot with `place_card.py review --clips` and let the user judge.
4. After approval: deliver as in § Code route, Deliver.

### Code route
The motion is drawn by a script over the card's unframed art. Scripts are in `tools/animate/procedural/` (run them from inside that folder: they open masks by relative path; masks are kept there too). Each takes `--art ../batch/<slug>/art.png` (the A1-trimmed 1024 × 1792 art in `tools/animate/batch/<slug>/`), `--title "<Card Name>"` and `--out <name>`. Each draws the frame and banner itself (`frame_card.py` with the deck frame flags), renders 96 frames at 24 fps and writes `<name>.mp4` and `.webp`. Every moving part runs whole cycles per clip, so the loop is seamless without a crossfade. Read a script's `--help`; all options are opt-in, and the defaults reproduce the approved clips.

| Effect | Script | Example card (its command: `tools/animate/procedural/card_<slug>.code.txt`) |
|---|---|---|
| Water strokes drifting down a water mask; `--warp` moves the drawn water itself; `--glints`, `--star` | `flow_strokes.py` | compass-rose, breath, anchor (`--warp`) |
| Falling particles: snow (+ `--glitter` on frost), `--kind sand\|seed\|leaf` along a `--path` or falling; `--erase` removes drawn copies | `falling_particles.py` | frost, keystone, sower, witness |
| Candle flames: stretch, tip sway, breathing glow | `flicker.py` | candelabra |
| Star twinkle, pulsing or travelling glow along a light mask | `glow.py` | oracle, root, lighthouse-keeper |
| Fog ribbons in a box, or a chimney `--plume` | `drifting_fog.py` | threshold, weaver |
| Sway of plants, rooted at the bottom; `--parts` bends each blade from its own base | `sway.py` | bramble, convergence |
| Glide: birds or insects cut out and flown on closed loops; `--mode swirl` twists a flock | `glide.py` | pilgrim, garden-gate, murmuration |
| Hanging ribbons bend from their fixed top (one polygon per ribbon); `--cloth` ripples a hanging cloth's folds in place, outline kept still | `ribbon.py` | mask |

Two effects on one card: render the first with `--save-raw <dir>` (unframed frames; `flow_strokes.py`, `flicker.py`), then the second with `--base-frames <dir>` (`glide.py`, `glow.py`) — cartographer: river plus bird; miner: flame plus gold glints. `glow.py --star-mask` takes the glinting spots from a colour-picked mask when the brightness test misses them (gold on pale ore); `flicker.py --glow-soft` reads `--glow-mask` as a grey falloff, so lamplight flickers on the rock and fades with distance (miner: walls and ceiling only, figure and floor cut out — the user asked for that).

**Masks.** For an element that is in the art (water, flames, plants, creatures), make a precise mask by colour threshold plus the connected component of the element, and check it as an overlay at full size; the AI-route masks are far too rough. Add a still mask for figures next to a moving element (`--still`), so the motion fades out before them. An effect that adds something new (snow, fog, dust) needs no element mask, only a region or avoid boxes.

**What the user rejected, and the fix** (2026-10-08):
- Motion too subtle to see ("I do not see the fog moving at all"): long ribbons drifting along their own length show no change. Moving shapes need ends or texture the eye can track. Make the motion plainly visible first; calm it on request.
- White on white is invisible: snow and frost glints got a thin ink (or dark blue) outline, which also suits the woodcut style.
- Strokes sliding over drawn waves that stay put look unnatural (anchor): warp the drawn water itself (`--warp`).
- Drawn copies left under moving ones look wrong (sower's seeds): erase the drawn copies first (`--erase`).
- A cutout carried a patch of its old background with it (garden-gate butterfly): cut creatures out by their own colours, with halo-free edges.
- A mask cut off at a fixed row froze the stem tips above it, leaving a seam (bramble): follow the element to its real top.
- Fill behind a moving edge: row-wise for horizontal textures (`sway.py --fill rows`, field furrows); a fitted surface for smooth sky (glide); diffusion otherwise.
- Too much at once (veil, 122 twinkling stars; keystone sand): fewer, spaced-out events.
- Random loop directions made birds collide (pilgrim): fly a flock the same way round with phases staggered by position.

**Check before showing.** Compare the jump from the last frame to the first with a typical frame step (`procedural/wcheck.py <work dir> <mask.png> x0,y0,x1,y1 <strip.png>` does this on a render's work-dir frames, measures change outside the mask, and makes a frame strip of the box). Look at 2–3 frames at full size around the element and around nearby figures. Show pilots with `place_card.py review --card "<Card Name>" --clips <files>`.

**Deliver** an approved clip (either route), after the user's approval:
1. Name a code-route clip `<slug>_code_v<N>.mp4` (next free `N`); an AI-route clip keeps its render name.
2. `place_card.py clip --card "<Card Name>" --mp4 <clip>`: labels a copy into `content/media/`, sets the card file's `clip`, removes the old clip file if no other card uses it (git history keeps it), rewrites the checksum list.
3. Code route: put its masks in `tools/animate/procedural/` as `card_<slug>_<element>.png` (or the names its command reads) and the exact commands, run from `tools/animate/procedural/` with `--art ../batch/<slug>/art.png`, as `tools/animate/procedural/card_<slug>.code.txt` (first line: what moves and how it was made; the existing files show the pattern).
4. `place_card.py publish --card "<Card Name>" --also <the new or changed files under tools/animate/procedural/> --message "Clip for <Card Name>"`.
5. `place_card.py backup --card "<Card Name>"` copies `tools/animate/batch/<slug>/` (the art git does not hold) to `<SOWER_BACKUP>/animations/source/batch/<slug>/`. Delete the pilots from the review folder.

No WebP: the site plays the MP4. `frame_card.py` adds unseeded paper grain, so a re-render differs in the frame border only; the animated picture is identical.

### Story loop
A figure acts out a short scene in a seamless loop (first and only one: The Sower, `dropbox:Tarot/animations/the-sower_story_v1.{mp4,webp}`, 2026-10-10, in the old archive). It is an extra clip, not on the site: the user kept the subtle clip as The Sower's `clip`, so do not repoint it unless asked. Its scripts are not in this repository: they are in the user's own folder `/workspace/tarot/animate/story/` (inputs per card in a subfolder, e.g. `sower/`; backup `dropbox:Tarot/animations/source/story/`); run the ComfyUI ones through `with-comfy local` (needs Qwen Image 2.1 edit and Wan 2.2 14B i2v high/low fp8; the remote PC has them too).
1. **Beats.** Agree 2–3 story moments with the user, the card pose as K0 (Sower: K0 throw → K1 hand in bag → K2 arm held out → K0).
2. **Keyframes.** `keyframe.py --art <png> --box 0,0,1024,1110 --instruction "..." --seed N --out K<n>.png` (Qwen edit; keeps only the box, tone-matched). Edit each keyframe from the previous keyframe, never from the card, so every persisting object (bag, strap) stays in the same place; otherwise Wan invents moves to carry it. Say what stays put in the instruction ("the birds stay exactly where they are").
3. **Transitions.** `segment.py --full --first A.png --last B.png --length 81|41 --seed N --prefix <dir> --prompt "..."` (Wan 14B first-and-last-frame; always `--full`, the 4-step LoRA halves the motion; ~20 min per 81 frames on the RTX 4080). Size the length to the move: a transition longer than its move makes Wan idle and then invent motion or objects (81 frames from bag to throw added a second bag). Render 2 seeds per transition; a failed job usually works on a plain retry. A finished render whose download failed can be fetched from ComfyUI `/history` by its prefix.
4. **Compose.** `story_compose.py --art art.png --mask mask.png --title "<Card Name>" --out <name> <seg1> <seg2> ...` joins the transition folders (it drops each folder's last frame) at 16 fps; only the mask (figure box plus every moving element) takes the video, the rest stays the card's pixels.
5. **Fix by editing frames, not re-rendering**, where possible:
   - Wan slows into and out of every keyframe, so a keyframe in the middle of a movement shows as a pause. Cut the near-still frames on both sides of the joint (copy the kept frames into new folders) — the Sower's arm became one fluent movement this way. Better still, put keyframes only where the figure really pauses.
   - A dip or extra move before a keyframe: end the transition on an earlier frame that is already right and use that frame as the next transition's first keyframe.
   - Stray drawn elements (seeds thrown too early) can be painted out of the frames by filling thin dark shapes from nearby sky.
6. **Check** arm paths and invented objects on a crop sheet of every 4th frame (start, joint, end), then let the user watch the pilots (`place_card.py review --clips`). After approval ask the user where the story clip goes; it is not a card's `clip` unless the user says so.

## Where things are
- `content/cards/<slug>.md` — the card files (the deck); `content/media/` — the reference files: each card's `card_<slug>.png` and its clip, all labelled; `content/checksums.txt` — their SHA-256 list, which the site serves and the build checks (a stale list fails the build).
- `tools/animate/procedural/` — the code-route effect scripts, masks and per-card commands; `tools/animate/check/check.py` — the AI-route motion check; `tools/animate/batch/<slug>/art.png` — each animated card's unframed art (not in git).
- `<SOWER_WORK>/cards/<slug>/` — renders, repairs and sections in progress (not in git, no backup).
- `<SOWER_REVIEW>/seed-sheets/<slug>/` and `<SOWER_REVIEW>/animations/procedural/` — candidates for the user to look at (`dropbox:Tarot` for this user; with `SOWER_REVIEW` empty, `<SOWER_WORK>/review/`). Rejected renders stay as the card's tailings; clip pilots are deleted after the pick.
- `<SOWER_BACKUP>` — backups: the 07:00 daily job copies all of `content/` to `<SOWER_BACKUP>/content/` every morning, so new card files and media need no copy here; `place_card.py backup` copies the art git does not hold.
- The old archive, read only: Joplin `Tarot/Cards` and `Tarot/Registry`; in `dropbox:Tarot/`, `cards/`, `legacy/`, and the deck clips and `deck.json` in `animations/` (new review and backup files do go into `seed-sheets/`, `animations/procedural/`, `animations/batch/` and `animations/source/`); and `/workspace/tarot/`, except `animate/story/` (still the story loop's working folder) and `daily-card/` (the daily job's log folder).

## LoRA backup
The trained style LoRA (`sowtarot_woodcut-v1.safetensors`) is the one asset that
can't be regenerated without another cloud training run, so keep a backup — but:
- **Don't zip it.** `.safetensors` are already-compressed weights; zip saves ~0%. Store as-is.
- **Don't put it inside this skill folder if the skill is version-controlled** — a ~100–300 MB binary bloats the repo. Keep the skill to code/config and reference the file by path.
- **Backup location:** off-site in **Dropbox `/Lora/`** (durable, survives a machine wipe) — holds both the trained `.safetensors` and the full `lora-training/` source dir (dataset + captions + `train_sowtarot_lora.yaml` + `prep_anchors.py` + `GUIDE.md`/`RUNPOD.md` + `painterly-source/`), so the LoRA can be retrained from scratch if needed. There is no local working copy; restore one with `rclone copy dropbox:Lora/lora-training /workspace/lora-training`. The runtime LoRA lives in ComfyUI `models/loras/`.
- If you *do* want it inside a git repo, use git-lfs rather than committing the binary directly.

## Bundled assets
- `assets/style.md` — frozen deck style (style block, render params, frame flags). The single source of truth for the look.
- `assets/tarot-card-flux.json` — the ComfyUI workflow (FLUX.1-dev fp8 → 4x-UltraSharp → ImageScale 1024×1792).
- `scripts/render_card.py` — one-call render: assembles the prompt from `style.md`, runs the workflow, frames the result, and embeds the render record in the card PNG. `--from-card "<Card Name>"` regenerates a card from its card file's `## Render Record` alone (base render, recorded repairs, frame) — use it when the local card PNG or the ComfyUI outputs are gone. Emits a JSON result line with the seed used and `comfy_file`, the unframed ComfyUI output filename.
- `scripts/frame_card.py` — deterministic frame + serif title banner (the border/title the model must not draw).
- `assets/tarot-card-qwen-edit.json` — the ComfyUI image-edit graph (API format) for § Repair a defect in one card: Qwen Image 2.1 at full size, 40 steps.
- `scripts/edit_card.py` — one-call repair: Qwen edit of the card's unframed art, masked paste-back inside `--box`, tone-matched to the original, frame, render record with a `repairs` entry.
- `scripts/fill_disc.py` — sun/moon removal on a flat sky without an AI edit (§ Repair a defect); deterministic, replayed by `--from-card`.
- `scripts/repair_tools.py` — `tone_match` and `fill_disc`, shared by the two repair scripts and `render_card.py --from-card`.
- `scripts/animate_wan.py` — runs Wan 2.2 image-to-video (5B, or 14B first-and-last-frame) on one image and saves the frames in ComfyUI's output (§ Animate a card).
- `scripts/animate_batch.py` — unattended queue of animate jobs over one or more ComfyUI instances (§ Animate a card, Batch).
- `scripts/animate_mask.py` — draw a mask from polygons and check it as a pink preview.
- `scripts/animate_compose.py` — pastes those frames into the card art inside a mask, frames once, closes the loop (`--crossfade`, or `--pingpong`), slows it (`--slow N`), writes MP4 + WebP.
- Code-route scripts live outside the skill, in `tools/animate/procedural/` (§ Animate a card, Code route), because the delivered per-card commands run there with relative mask paths.
- `scripts/card_repo.py` — card files, Render Record section, label and checksum helpers; takes settings, git and push from `skills/tarot-daily-reading/scripts/daily.py`.
- `scripts/place_card.py` — `terms`, `new`, `attach`, `clip`, `review`, `backup`, `publish` (see its `--help`).
- `scripts/novelty_rank.py` — ranks candidate cards by distance in meaning to the deck, and (`gaps`) lists the widest gaps between two cards for a Miner round (§ Find something new); a `uv` script with its own dependencies.
- `scripts/seed_sheet.py` — many seeds of one card's scene plus a contact sheet.

