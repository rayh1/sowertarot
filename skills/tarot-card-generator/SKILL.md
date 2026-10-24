---
name: tarot-card-generator
description: "Generate completely original tarot cards in the Rider-Waite tradition. Creates one Joplin note per card under `Tarot/Cards/` (Visual Description + Archetypal Essence + render prompt), updates the `Tarot/Registry` deck index, renders the image locally through the bundled ComfyUI/FLUX pipeline (art -> upscale -> framed title card), and attaches it to the note. Use when the user asks to (1) create a new tarot card, (2) generate an original Rider-Waite style card, (3) expand a custom tarot deck, (4) design a card around an archetype or theme, (5) re-render an existing card's image in the deck style, or (6) animate a card as a short loop."
---

## Objective
Generate ONE completely original Rider-Waite-inspired tarot card per invocation: write it as a single Joplin note at `Tarot/Cards/<Card Name>`, append an entry to `Tarot/Registry` (the thin deck index) to enforce uniqueness, render the image locally with the bundled ComfyUI/FLUX pipeline, and attach it to the note. The note holds card-as-object content only — Visual Description, Archetypal Essence, render prompt. No Upright/Reversed interpretation: meaning is produced fresh at reading time by the reading skill.

**Style consistency is the point of a deck.** Every card must read as one deck. That is enforced by freezing everything except the scene and the seed — see § Deck style consistency and `assets/style.md`. Never re-style a single card by hand; if the look must change, change it for the whole deck in `assets/style.md`.

## Quick start
- Optional inputs — see § Inputs
- Output: one Joplin note at `Tarot/Cards/<Card Name>` + updated `Tarot/Registry` + attached image (or explicit deferral with `image_status: pending`) + the card PNG in the Dropbox card library (§ Dropbox card library)
- Prereq (Joplin): reachable via the `joplink` CLI (see `joplink-cli` skill); `Tarot/`, `Tarot/Cards/`, and `Tarot/Registry` exist (auto-created on first run with user approval). Step 6 attach invokes `scripts/attach_image.py`, whose deps (`requests`, `Pillow`) must be importable and which talks to Joplin's Web Clipper service directly (the `joplink` CLI does not expose resource upload).
- Prereq (local render, Step 5): ComfyUI running locally with the `comfy` CLI on PATH; a CUDA GPU (~16 GB VRAM); `Pillow` importable for `scripts/frame_card.py`. Three model files, all referenced by `assets/tarot-card-flux.json` by filename:
  - `flux1-dev-fp8.safetensors` in `models/checkpoints/` — base model (download: `https://huggingface.co/Comfy-Org/flux1-dev/resolve/main/flux1-dev-fp8.safetensors`, ~16 GB).
  - `sowtarot_woodcut-v1.safetensors` in `models/loras/` — the deck **style LoRA**; supplies the woodcut look and is invoked by the `wdctarot` trigger in `assets/style.md`. Trained via `lora-training/` in Dropbox `/Lora/` (see its `RUNPOD.md`); the trained file is the one irreplaceable asset — back it up (see § LoRA backup).
  - `4x-UltraSharp.pth` in `models/upscale_models/` — upscaler.

  If any of this is missing, use the § External-render fallback.

## Inputs
Required: none (generates autonomously).
Optional:
- `card_name` — user-suggested name (still passes uniqueness check)
- `theme` — concept/archetype/theme to explore
- `image_path` — absolute path to a pre-rendered image. If given at invocation, Step 5 local render is skipped and Step 6 attaches this path directly. If omitted, Step 5 renders four candidates and places the user's pick at `/workspace/tarot/card_<slug>.png`; on the External-render fallback that default path is where the user saves their render.

## Decision points (routing)
- User asks for a new or conforming image for a card that already exists in `Tarot/Registry` → § Re-render an existing card (skip Steps 1–4).
- `card_name` provided → use it (must still pass uniqueness). Else generate a name in Rider-Waite archetypal style.
- Target note `Tarot/Cards/<Card Name>` already exists → ask before overwriting (§ User approval).
- Registry missing / malformed JSON → § Fallback chain.
- Uniqueness fails AND user gave `card_name` → ask for an alternative OR propose 2–3 options; proceed only after the user selects.
- Uniqueness fails AND name was generated → propose a new name + key_terms and re-check (max 3 retries; still conflicting → escalate to user with the conflicting candidates).
- After escalation the user MAY explicitly accept a `near-match` candidate (acknowledging the overlap) → record acceptance; G2 then passes.
- Render (Step 5): local pipeline available → render four seeds with `render_card.py`, recommend one, the user picks (5c); the user may ask for another batch or a revised scene instead. Server down or model missing → § External-render fallback.
- Attach pause (Step 6, fallback path only): `image_path` input present → use it, skip the path question. `attach` → default `/workspace/tarot/card_<slug>.png`. `attach <path>` → that absolute path. `skip` → deferral (G6b). Resolved path missing on disk → ask for the correct path (max 3 retries, then default to skip-deferral). User wants to change the scene and re-render → revise the note's `## Render Prompt`, re-run Step 5 (a new batch of four), no registry change beyond `seed`, re-enter attach.

## Quality gates
G1 (start of Step 1): Joplin reachable; `Tarot/Registry` readable per § Fallback chain.
G2 (end of Step 1): uniqueness comparison table produced (see Step 1). Passes if no row has verdict `conflict` or `near-match`, OR the user explicitly accepted a near-match after escalation.
G3 (end of Step 3): note `Tarot/Cards/<Card Name>` exists with required sections — title, Rider-Waite tagline, `## Visual Description` (Composition, Symbolism, Atmosphere), `## Archetypal Essence` paragraph, `## Render Prompt` fenced block (scene only — no style/border/title).
G4 (end of Step 4): `Tarot/Registry` re-reads as valid JSON, contains the new entry matching the Step 4 schema (name, created, key_terms, concept, note_id, image_status, prompt_status, seed), and metadata reflects updates (`total_cards` incremented, `last_updated` set, `version` preserved).
G5 (end of Step 5): either — (a) **rendered**: the user picked one of a batch of four (5c), `card_<slug>.png` exists at 1024×1792 with the deck frame + correct title, and the registry entry's `seed` is the picked render's seed; OR (b) **fallback**: local render unavailable, § External-render fallback taken (registry `seed` stays `null`). The user declines every candidate and asks for no further batch → report the candidates and stop, do not attach.
G6 (end of Step 6): either — (a) **attached**: `dropbox:Tarot/cards/card_<slug>.png` matches the attached PNG (`rclone check`), AND note body contains `![<Name>](:/<resource-id>)` replacing the pending placeholder AND (for a `render_card.py` image) a `## Render Record` section whose seed and `comfy_file` match the attached render AND registry entry has `image_status: "present"` AND the source image still exists at its original path on disk (not deleted, not moved); OR (b) **deferred**: user declined (explicit `skip` or 3 failed path resolutions), placeholder remains, registry keeps `image_status: "pending"`, deferral recorded in the Step 7 summary.
If a gate fails: fix once → re-check; else stop and report which gate failed and why.

## Scope fence
In scope: generate ONE new original card; create its `Tarot/Cards/` note; append its `Tarot/Registry` entry; render the image locally via the bundled ComfyUI/FLUX pipeline (`scripts/render_card.py`); attach the rendered image (default `/workspace/tarot/card_<slug>.png`), including JPEG compression + Joplin resource upload.

Also in scope: re-rendering an existing card's image per § Re-render an existing card, including the note and registry edits that section names; and repairing one defect in a card's image per § Repair a defect in one card; and animating one card per § Animate a card.

Also in scope, on the user's request: a seed sheet for ONE existing card — render its `## Render Prompt` scene at many seeds with `render_card.py` (e.g. overnight), outside the batch-of-four limit, into a folder the user names, plus one contact sheet of thumbnails labelled with their seeds. A seed sheet only renders: no note, registry or attach change, and nothing is ranked. The user picks the seed; attaching that render then follows § Re-render an existing card.

Out of scope: Upright/Reversed interpretation (meaning is per-use, produced at reading time from Visual + Essence); writing local markdown files (Joplin is the sole backend); editing existing cards beyond § Re-render an existing card (name, key_terms and Archetypal Essence stay untouched); deleting cards; generating more than one new card per invocation; **deleting, moving, or renaming the source image file after upload — the source is always preserved at its original location**; modifying the schema of an existing valid registry (reinit of a missing/malformed one is allowed via § Fallback chain under user approval); installing ComfyUI or downloading model files (the user provides these — see Quick start prereqs); training a style LoRA (a later, separate task — see `assets/style.md`).

## Stop conditions
Done when G1–G6 pass (via Step 7). G6 passes on successful attach OR explicit user deferral. Do not loop indefinitely: renders come in batches of four, and a further batch goes ahead only on the user's request (5c) — never on your own initiative. Attach path resolution is capped at 3 failures → skip-with-deferral.

## User approval gate
Before any destructive or irreversible action — overwriting an existing `Tarot/Cards/<Card Name>` note, or reinitializing/repairing malformed `Tarot/Registry` JSON — proceed only after explicit user approval. Never self-approve: if no interactive user is present to answer, STOP and report what needs approval rather than performing the destructive action.

## Clarifying questions
Triggers: `card_name` conflicts or is too close to existing entries; `theme` too broad to produce a distinct concept; `card_name` and `theme` misaligned.
Constraints: max 3 per phase; batch related questions.
Fallback: no `card_name` given → use safe defaults (generate a new unique name/theme), document assumptions. `card_name` given → ask for an alternative or propose 2–3 options; never override user-provided input silently.

## Fallback chain
primary: read + parse `Tarot/Registry` via `joplink --json note get "Tarot/Registry" --fields body`. `--fields body` is required — without it `note get` returns only default metadata and the body is lost.
fallback_1: note not found OR JSON malformed → request approval to reinitialize using § Initial registry schema. Approved → reinit, continue. Refused → terminal (do not generate or write the note).
terminal: ERROR: REGISTRY_UNAVAILABLE — do not generate or write the card note.
trigger: any Joplin read/parse failure that persists after one retry.

**Joplin CLI troubleshooting** (distinguish failure modes before giving up):
- Connection refused / server not running → verify Joplin desktop's Web Clipper service in Settings > Extensions > Joplin.
- Auth / token expired → `joplink --json config show` and check `token_present: true`; if missing/stale, edit `~/.config/joplink/settings.json` directly (keys `joplin_base_url`, `joplin_token`) — `joplink config` only exposes the `show` subcommand.
- Isolation test → run `joplink --json config show` directly to confirm the failure is CLI/Joplin, not skill logic.

## Initial registry schema
When reinitializing (per § Fallback chain), write this canonical structure as the body of `Tarot/Registry`:

````markdown
# Tarot Card Registry

Source of truth for the deck. Each card is a note under `Tarot/Cards/`. This note is a thin index.

```json
{
  "metadata": {
    "version": "2.0",
    "total_cards": 0,
    "last_updated": "[today's date YYYY-MM-DD]",
    "backend": "joplin",
    "base_path": "Tarot"
  },
  "cards": []
}
```
````

After reinit, proceed with normal Step 4 — the new card increments `total_cards` to 1 and refreshes `last_updated`. G4's "version preserved" applies from here on (initial `2.0` is preserved across subsequent updates).

## Workflow

### Step 1 — Propose name/theme and validate uniqueness
**1a. Propose a name + theme.** Use the user's `card_name`/`theme` if given; else generate using an archetypal pattern:
- `"The [Noun]"` (The Wanderer, The Threshold)
- `"[Abstract Concept]"` (Resonance, Eclipse)
- `"The [Adjective] [Noun]"` (The Silent Observer, The Broken Mirror)

Also propose 3–6 `key_terms` for the registry: the main noun(s) from the name, core concept words, and similar/related terms to avoid (e.g. "Weaver" vs "Thread Weaver" — reuse of a term even in a slightly different form counts as a collision).

**1b. Validate uniqueness.** Read `Tarot/Registry` and verify the proposed name does NOT match any existing card name, does NOT reuse any existing key term, and explores a genuinely new archetype/object/metaphor (avoid close thematic near-duplicates).

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

Pre-filter for which cards get their own row: a card earns a row if (a) its name shares a stem with the proposed name, OR (b) any of its `key_terms` overlaps (exact or stem) with the proposed `key_terms`, OR (c) it occupies a closely related archetypal/symbolic neighborhood. All others collapse into the summary row. Any individual `conflict`/`near-match` row → revise name or key_terms and reproduce the table (max 3 retries before escalating per § Decision points).

### Step 2 — Generate card content
Using the validated name/theme, create three sections only — no Upright/Reversed bullets.

**Visual Description (Rider-Waite style):**
- **Composition:** central figure/focal point; foreground/middle/background elements; symmetry or asymmetry; positioning and posture of any figures.
- **Symbolism:** adapt traditional Rider-Waite symbolic vocabulary (color conventions, natural/animal/object symbols, sacred geometry, clothing cues) to the new concept — elements that reinforce the archetype, not decorate it.
- **Atmosphere:** time of day; weather/celestial conditions; emotional tone; lighting quality (harsh, soft, mystical).

**Archetypal Essence:** a 3–4 sentence paragraph capturing the deep archetypal significance — its place in human experience and the universal truth it represents. This is the canonical meaning layer; reading-time interpretation builds on it but is not stored here.

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
- Store it in the note under `## Render Prompt` (see Step 3). This is the canonical prompt.
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

### Step 3 — Create Joplin note
Create the note at `Tarot/Cards/<Card Name>` via `joplink --json --no-input note save "Tarot/Cards/<Card Name>" --stdin` (pipe the body via stdin to avoid quoting issues). Body template:

````markdown
# [Card Name]

*An original tarot card in the Rider-Waite tradition*

_(image pending — attach manually)_

## Visual Description

### Composition
[...]

### Symbolism
[...]

### Atmosphere
[...]

## Archetypal Essence

[3-4 sentence paragraph]

## Render Prompt

```
[scene-only render prompt from Step 2 — no style/border/title]
```

<!-- DALL-E fallback: add a "## DALL-E Prompt" fenced block here ONLY when taking the External-render fallback -->
````

The `_(image pending — attach manually)_` line is the placeholder the attach step (Step 6) swaps for `![<Card Name>](:/<resource-id>)`. Capture the returned note `id` from the `note save` JSON — it goes into the Step 4 registry entry. Step 6 appends a `## Render Record` section after attach. The `## Render Prompt` block holds the scene only; Step 5 assembles the full prompt (style block + scene + tail) at render time from `assets/style.md`.

### Step 4 — Update Tarot/Registry
1. Read current registry via `joplink --json note get "Tarot/Registry" --fields body`.
2. Extract JSON from the first ` ```json ` fence in the body. Tolerate variations: optional `json` hint, leading/trailing whitespace in the fence, `\r\n` vs `\n`.
3. Parse the JSON.
4. Append the new card entry to the `cards` array:
   ```json
   {
     "name": "The [Card Name]",
     "created": "YYYY-MM-DD",
     "key_terms": ["term1", "term2", "term3"],
     "concept": "Brief core concept (3-6 words)",
     "note_id": "<joplin-note-id-from-Step-3>",
     "image_status": "pending",
     "prompt_status": "original",
     "seed": null
   }
   ```
   `seed` stays `null` until Step 5 renders the card, then it is set to the seed used — so any card is reproducible. On the External-render fallback it stays `null`.
   Example key_terms: "The Hollow Crown" → `["crown", "hollow", "authority", "power", "sovereignty", "relinquishment"]`; "The Compass Rose" → `["compass", "rose", "direction", "navigation", "cardinal", "orientation"]`.
5. Update metadata (preserve existing fields; do not overwrite with literals):
   ```json
   "metadata": {
     "version": "[preserved from parsed registry; do not overwrite]",
     "total_cards": [previous_count + 1],
     "last_updated": "[today's date YYYY-MM-DD]",
     "backend": "joplin",
     "base_path": "Tarot"
   }
   ```
6. Serialize with 2-space indentation.
7. Persist back via `joplink --json --no-input note save "Tarot/Registry" --stdin`, preserving any non-JSON prose outside the fenced block (e.g. the "Source of truth…" preamble).

### Step 5 — Render the image locally
Render the card with the bundled pipeline: FLUX art → ESRGAN upscale → framed title card. One call does everything.

**5-pre. Skip if pre-rendered.** If `image_path` was given at invocation, skip Step 5 entirely and go to Step 6 with that path (attach it directly) — the image already exists, no render needed. Otherwise render as below.

**Instance.** Run every render or edit script, and every `comfy` command below, through `with-comfy`:
`/workspace/.claude/tools/with-comfy/with-comfy local|remote <command>` (`$W` below). It forwards a loopback
port to the instance (`local` = the host GPU; `remote` = a second machine on the local network, up 19:00–07:00), checks it
answers (exit 69 = not answering: tell the user) and sets `COMFY_LOCAL_URL`, which the scripts and the
`comfy` CLI read. Batch each model's jobs together on `remote`: a FLUX↔Qwen switch costs ~4 min there.

**5a. Preflight.** Confirm the local server answers and the models are present:
`comfy --json model list-folder checkpoints --where local` lists `flux1-dev-fp8.safetensors`, and `comfy --json model list-folder upscale_models --where local` lists `4x-UltraSharp.pth`. If the server is down (`server_not_running`) or either model is missing, take the § External-render fallback instead of failing.

**5b. Render a batch of four seeds.** Render four different seeds into the session scratchpad — never straight to the default path:
```bash
$W local python3 scripts/render_card.py \
  --scene "<the ## Render Prompt scene text from the note>" \
  --title "<Card Name>" \
  --seed <integer> \
  --out <scratchpad>/<slug>_<seed>.png
```
- `<slug>` = card name lowercased, spaces→hyphens (`name.lower().replace(" ","-")`).
- Any four distinct integer seeds. Each run prints a JSON result line with the `seed` and `comfy_file` (e.g. `tarot_flux_final_00090_.png` — its number, 90, is the image number used to talk about the render).
- The script prepends the frozen style block and appends the frame-agnostic tail from `assets/style.md`, runs `assets/tarot-card-flux.json`, then frames via `scripts/frame_card.py` with the frozen frame flags. Do NOT pass style, palette, border, or title into `--scene` — that causes a double border and garbled text.
- On any render failure, invoke the `comfy-debug` skill before retrying.

**5c. Review, recommend, let the user pick.** Build a side-by-side contact sheet of the four renders with Pillow and look at it; open the strongest candidate at full size. Every render must show the scene in the frozen style, a single clean border and the correct title. Defects that rule a render out: stray glyphs, numbers or ornaments (especially at the top edge), duplicated objects, extra limbs, modern objects. A candidate that is right except for one small, local defect can be picked and then fixed per § Repair a defect in one card, instead of re-rolling seeds. Report each candidate by image number and seed with its strengths and defects, recommend one, and ask the user to choose (AskUserQuestion). The user may instead ask for four more seeds or a revised scene; do what they choose, then review again. Never pick on the user's behalf: with no interactive user, stop with the four candidates reported and `image_status` left `pending`.

Batch-level fixes: a double border in every render → the scene text wrongly included a border/frame; remove it from `## Render Prompt` and re-render. The same content defect across seeds → revise the scene per the Step 2 rules, not the seed. Palette drift beyond the earthy range that persists across seeds → tighten the palette words in `assets/style.md` (this re-styles the WHOLE deck — a deliberate deck-level change, not a per-card fix).

**5d. Place the pick and record the seed.** Copy the chosen PNG to `/workspace/tarot/card_<slug>.png`. Re-read `Tarot/Registry`, set this card's `seed` (matched by `note_id`) to the chosen render's seed, and save back — so the card is reproducible. If the scene was revised during 5c, update the note's `## Render Prompt` to the scene actually used.

Copy the PNG as a file (`cp`), never re-save it through an image library — the render record lives in its PNG text chunk. The PNG at the default path is the input to Step 6 attach; `image_status` stays `pending` until attached.

### Step 6 — Attach generated image
The note and registry entry already exist with `image_status: "pending"`. This step closes the loop in-invocation so the status doesn't drift.

**6a. Announce and pause (fallback only).** If Step 5 produced the image at the default path, skip to 6c. Otherwise (§ External-render fallback), output the DALL-E prompt in a copy-friendly code block, then tell the user:
> Generate the image in ChatGPT/DALL-E using the prompt above, then save the result to `/workspace/tarot/card_<slug>.png` (default) or any path you prefer. When ready, reply:
> - `attach` — attach from the default path
> - `attach <absolute-path>` — attach from a path you specify
> - `skip` — defer; card stays `image_status: pending`. Finalize later via 6f (`scripts/attach_image.py` or manual Joplin edit).

If `image_path` was given at invocation, skip the path question and go straight to 6c with that path.

**6b. Wait for the user signal.** A conversational turn, not a technical wait — stay idle until the user responds.

**6c. Resolve and verify the path.** From the reply (or `image_path`):
- `attach` (bare) → `/workspace/tarot/card_<slug>.png`, where `<slug>` = card name lowercased, spaces→hyphens (`name.lower().replace(" ","-")`, other punctuation preserved).
- `attach <path>` → the user-supplied absolute path.
- `skip` → deferral.

Verify the file exists. If not: ask for the correct path (max 3 retries per § Decision points); after 3 failures, default to deferral.

**6d. Attach via the bundled helper (preferred).** Steps 6d's compress → upload → note-update → registry-update are all implemented by `scripts/attach_image.py`. Invoke:
```bash
python3 .claude/skills/tarot-card-generator/scripts/attach_image.py \
  --card "<Card Name>" --image "<resolved path>"
```
Required args: `--card` (matches the Joplin note title under `Tarot/Cards/` exactly), `--image` (absolute path, PNG/JPG/WEBP). Flags: `--dry-run` (preflight + in-memory compress, no uploads/writes); `--replace` (swap an already-attached image — uploads a fresh resource, swaps the note reference; the old resource becomes an unreferenced orphan in the Joplin DB). Idempotent by default (safe to re-run; skips upload if an image is already attached). **The script never deletes or moves the source image — it is preserved at its original path on disk** (per § Scope fence). What the helper does, as the authoritative behavior spec:
- **Compress:** PNG/JPG/WEBP → JPEG at 1024×1536, quality 85, via Pillow (`Image.open(path).convert("RGB").thumbnail((1024,1536), Image.LANCZOS)` → `.save(buf,"JPEG",quality=85,optimize=True)`), target ~150–250 KB, in memory (no JPEG written to disk).
- **Upload:** POST the JPEG bytes to Joplin's Web Clipper API `POST {JOPLIN_API}/resources` as multipart form data with `data` (the JPEG), `props` (JSON `title: "card-<slug>.jpg"`), and `token` query param. The API URL and token resolve from the joplink settings file (`~/.config/joplink/settings.json`, keys `joplin_base_url`/`joplin_token`; inspectable via `joplink --json config show`), with env overrides `JOPLIN_TOKEN`/`JOPLIN_API_URL` (legacy aliases `JOPLINK_JOPLIN_TOKEN`/`JOPLINK_JOPLIN_BASE_URL`). Capture the returned `id` as `<resource-id>`.
- **Render record:** a card PNG from `render_card.py` carries a render record in its `tarot_render` PNG text chunk: seed, title, scene, full prompt, frame flags, ComfyUI version and the executed ComfyUI graph (models, LoRA, sampler, size, upscaler). The helper writes it into the note as a `## Render Record` section, collapsed in a `<details>` block (replacing any old one), so the note alone can re-render the image — the ComfyUI output PNGs and the local card PNG are not durable. The JPEG in Joplin carries no metadata. An image without a record (external render) attaches with a warning; on `--replace` the old record is removed, since it describes the previous image.
- **Update the note:** read via `joplink --json note get "<note_id>" --fields body`, replace `_(image pending — attach manually)_` with `![<Card Name>](:/<resource-id>)`, save via `joplink --json --no-input note save "<note_id>" --stdin`.
- **Update the registry:** read `Tarot/Registry`, find this card's entry by `note_id`, flip `image_status` `"pending"` → `"present"`, refresh `last_updated`, save back.

**6d2. Copy to the Dropbox card library.** After a successful attach, copy the attached PNG to `dropbox:Tarot/cards/card_<slug>.png` per § Dropbox card library.

**6e. Confirm.** Report: image path used, Dropbox library path, compressed size, resource ID, whether a render record was written, updated registry status. For the deferral path (`skip` or retries exhausted): leave `image_status: "pending"` untouched and record the deferral in the Step 7 summary.

**6f. Follow-up attach (deferred cards only).** If deferred, `image_status` stays `pending` until the user finalizes. Two paths:
1. **Bundled helper (default).** Run `scripts/attach_image.py --card "<Card Name>" --image "<absolute path>"` — same compress/upload/update pipeline, idempotent. Pass `--replace` to swap an already-attached image (old resource becomes an orphan; source PNG still never deleted).
2. **Manual Joplin path.** Drag-drop the image onto the card's note in the Joplin UI, then manually edit `Tarot/Registry` to flip that card's `image_status` to `present`. No tooling, but error-prone for the registry edit. Use when Web Clipper isn't reachable or the user prefers the GUI.

### Step 7 — Verify & report
1. Run gates G1–G6.
2. Re-fetch `Tarot/Cards/<Card Name>` via `joplink --json note get` and confirm required sections.
3. Confirm `Tarot/Registry` re-parses and contains the new entry with a `note_id` matching Step 3, incremented `total_cards`, and (local render) a non-null `seed`.
4. Report the attach outcome: (a) **attached** — resource ID, `image_status: "present"`, note shows the image reference; or (b) **deferred** — note the user skipped; point them to `scripts/attach_image.py` (6f).
5. Summarize: card name, note path + ID, registry `total_cards` after update, image status (attached with resource-id, or deferred with reason), render seed used, and — if generated autonomously — the § Assumption registry so the user can audit the creative choices.
6. Offer to animate the new card (§ Animate a card, New card). Until it has a clip, the daily card page shows it as a still.

## Assumption registry
When generating autonomously (inputs omitted), log assumptions made while choosing name/theme/visuals, and include them in the Step 7 summary:
- [theme] assumed: "{chosen theme/archetype}" | source: {registry-coverage gap / user hint / random-creative} | confidence: {high|medium|low}
- [visual palette] assumed: "{dominant colors + atmosphere}" | source: {theme-driven / archetypal default} | confidence: {level}
- [name style] assumed: "{The Noun | Abstract Concept | The Adjective Noun}" | source: {reason} | confidence: {level}

## Registry field semantics
- `note_id` — Joplin ID of the `Tarot/Cards/<Card Name>` note; primary pointer for downstream skills.
- `image_status` — `pending` (no image attached yet) | `present` (image resource attached). This field is the source of truth for attach state.
- `prompt_status` — `original` (prompt generated at creation) | `legacy_no_prompt` (imported legacy card, no prompt preserved).
- `seed` — integer seed used by the local render (Step 5), or `null` for legacy/fallback cards. The full recipe for the attached image is the note's `## Render Record` (Step 6d); the note's `## Render Prompt` can later be edited, so it alone does not guarantee the image.

## Deck style consistency
Every card must read as one deck. Consistency comes from freezing everything
except the scene and the seed. Four layers, three frozen:

| Layer | Role | Where |
|---|---|---|
| Style block (prompt preamble) | fixed woodcut Rider-Waite descriptors + explicit palette | `assets/style.md` § Style block — prepended by `render_card.py` |
| Render params | fixed checkpoint, sampler, guidance, steps, size, upscale | `assets/tarot-card-flux.json` (contract listed in `assets/style.md`) |
| Frame | fixed margin/border/banner/font/colors → identical layout + typography | `scripts/frame_card.py` + frozen flags in `render_card.py` |
| Scene + seed | the ONLY per-card variables | note `## Render Prompt` + Step 5 `--seed` |

Rules:
- Never re-style a single card by editing the scene toward a style. A per-card look drift is fixed by reseeding, not by prompt-styling.
- A genuine style change is a **deck-level** edit to `assets/style.md` (palette words, medium, frame colors). It changes all future cards by design; it does not retro-fit existing ones.
- Prompt-only style is *recognizably* one deck; per-card wobble in linework/palette is expected. For published-deck tightness, train a style LoRA (see `assets/style.md` § Maximum-fidelity option) — a separate, later task, out of this skill's scope.

## External-render fallback
Use ONLY when the local render pipeline is unavailable (no ComfyUI/`comfy` on
PATH, `flux1-dev-fp8.safetensors` or `4x-UltraSharp.pth` missing, or no GPU).
In place of Step 5:
1. In Step 2 also produce the **DALL-E 3 prompt** (self-contained: style + border + title baked in) and add it to the note under a `## DALL-E Prompt` fenced block.
2. Step 6 runs its announce-and-pause path (6a–6b): the user renders in ChatGPT/DALL-E and saves to `/workspace/tarot/card_<slug>.png` (default) or a path they give, then signals `attach`/`skip`.
3. Attach from that path (6c–6e). Registry `seed` stays `null`; G5 passes via its `fallback` branch.

This path forgoes the deck-style guarantees — an external renderer will not match the frozen style block, so mixing fallback cards into a locally-rendered deck will show a visible style seam. Prefer the local pipeline whenever it is available.

## Re-render an existing card
Use when a card already in `Tarot/Registry` needs a new image in the deck style — typically a legacy card whose registry `seed` is `null` (its image came from DALL-E or another renderer). Steps 1–4 are skipped: the name, key_terms and Archetypal Essence already exist and stay untouched.

**R1. Read the card.** Get the note (`joplink --json note get "Tarot/Cards/<Card Name>" --fields id,body`) and its registry entry. Note the `note_id`.

**R2. Preserve the old image.** `cp -n /workspace/tarot/card_<slug>.png /workspace/tarot/card_<slug>_legacy.png` before any render — R5 copies the pick over the default path. Never overwrite a `_legacy` file.

**R3. Write the scene fresh.** Do not trim the note's old DALL-E text into a scene; its prop lists and ritual details carry the word traps from Step 2. Write a new scene per the Step 2 render-prompt rules, keeping the card's meaning. If the note has no figure (a still life, hands only), consider adding one — scenes without a figure render worst. A changed composition means R6 must rewrite the Visual Description, so tell the user before rendering.

**R4. Render four seeds and let the user pick.** Run Step 5a–5c exactly as for a new card: preflight, a batch of four seeds into the scratchpad, then review, recommend and let the user choose. Never attach without the user's pick. Before recommending a render (here or from a seed sheet), open it at full size and check the sky and the top edge: a seed-sheet thumbnail is too small to show a sun, moon or glyph reliably (on 2026-10-03 a recommended render turned out to have a moon).

**R5. Attach the pick.** Copy the chosen PNG to `/workspace/tarot/card_<slug>.png`, then run `scripts/attach_image.py --card "<Card Name>" --image /workspace/tarot/card_<slug>.png --replace`. `--replace` leaves the old Joplin resource unreferenced; report its id so the user can delete it in Joplin. It also replaces the note's `## Render Record` with the new render's. Then update the Dropbox card library: the legacy file to `legacy/`, the pick to `cards/` (§ Dropbox card library).

**R6. Update the note.** Insert a `## Render Prompt` fenced block with the scene used, before `## DALL-E Prompt` if that section exists (leave the DALL-E section in place). If the composition changed, rewrite `## Visual Description` (Composition, Symbolism, Atmosphere) to match the attached image — only with the user's approval. Save via `joplink --json --no-input note save <note_id> --stdin`.

**R7. Record the seed.** Re-read `Tarot/Registry`, set this card's `seed` (matched by `note_id`), refresh `last_updated`, save. `image_status` stays `present`.

**Done when:** a re-read confirms the note shows the new resource and has `## Render Prompt`, the registry entry has the new `seed`, and `card_<slug>_legacy.png` exists. Report the image number, seed, new resource id, orphaned resource id and legacy path.

## Repair a defect in one card
Use when one rendered card is right except for a small, local defect — a stray ornament at the top edge, a hanging line, an extra object — and the user wants that fixed, not a new render. The image-edit model is Qwen Image 2.1 (`assets/tarot-card-qwen-edit.json`; chosen over FLUX Kontext on 2026-09-24 because it edits at full 1024 × 1792 and its edits line up pixel for pixel with the original). Prereq: ComfyUI 0.37.0 or later with `qwen_image_2.1_int8_convrot.safetensors` (`diffusion_models`), `qwen3vl_8b_int8_convrot.safetensors` (`text_encoders`) and `qwen_image_2.1_vae_bf16.safetensors` (`vae`). The card's note must have a `## Render Record` (Step 6d); a card without one is re-rendered instead.

**Sun or moon on a flat sky: fill it, don't edit it.** A disc on a plain or gently graded sky (no clouds, linework or texture crossing it) is removed with `scripts/fill_disc.py`, not Qwen: it fills the disc from the sky around it, so no box-shaped patch can appear, and needs no ComfyUI. Choose the box as in E2 but with plain sky on every side of the disc and its glow, then:
```bash
python3 scripts/fill_disc.py --note "<Card Name>" --art <unframed art> --box <x0,y0,x1,y1> \
  --out <scratchpad>/<slug>_fill.png --keep-art <scratchpad>/<slug>_fill_art.png
```
`--art` is the card's current unframed art (regenerate it as in E3 if needed). Add `--grow 24` when a faint rim or glow remains, `--thresh 40` on a graded sky where the mask runs to the box edge. Review as in E4 and attach as in E5. A disc with clouds or drawing across it goes through E1–E5 with Qwen. So does a disc on a dark night sky: `fill_disc.py` treats every pixel darker than 90 (of 255) as ink linework (`repair_tools.py`), so on a black sky it stops with "no disc found in the box" (The Veil, 2026-10-04). There, say "Fill its place with the same black night sky scattered with small white stars"; the edit adds stars spaced like the rest of the sky.

**A light halo round linework on a flat sky: fill it, don't edit it.** For a pale rim round a drawn bird or figure, run `fill_disc.py` with `--halo --grow 2` and a box round the figure with plain sky on every side: it repaints only the rim from the sky and keeps the drawing (`repair_tools.fill_halo`, recorded as `method: fill_halo`). Qwen cannot do this: asked to remove the halo it deleted the whole gull, asked to recolour it it widened the rim (The Anchor, 2026-10-24).

**Before editing, check the art is the card's current art.** `render_card.py --from-note` may no longer reproduce the picture (The Anchor's base render drifted to a different anchor by 2026-10-24). Frame the art you will edit (`frame_card.py` with the record's frame flags) and compare it with the card PNG; if they differ, look for the saved art in Dropbox (`seed-sheets/discs/`, `seed-sheets/repairs/`, the Render Record's `note`) instead.

**E1. Check the defect survives framing.** The frame crops 3.5% from every side and covers the bottom ~8.5% with the title banner. A defect only in those areas needs no repair — say so and stop.

**E2. Choose the repair box.** Open the unframed art (the record's `comfy_file`, `<instance URL>/view?filename=<comfy_file>&type=output`, e.g. `http://127.0.0.1:8188` for `local`) at full size with a pixel grid and pick a box `x0,y0,x1,y1` around the defect. The box must span the whole structure the defect belongs to — for example the full width for a border or banner element — or its edges cut through that structure and leave stubs or seams. Only the box is kept; everything outside it stays exactly as rendered.

**E3. Edit three seeds.** Write the instruction in plain words: what to remove and what to fill its place with, for example "Remove the thin hanging line at the top center of <image1>. Fill its place with the same dark night sky." (`edit_card.py` appends "Keep everything else, including the woodcut linework and hatching, exactly the same."). Run seeds 1–3 into the scratchpad:
```bash
python3 scripts/edit_card.py --note "<Card Name>" --seed <n> --box <x0,y0,x1,y1> \
  --instruction "<instruction>" --out <scratchpad>/<slug>_repair_<n>.png --keep-art <scratchpad>/<slug>_repair_<n>_art.png
```
`edit_card.py` evens the box's tone to the original by default (`repair_tools.tone_match`): Qwen returns the whole edit 4–16 colour levels lighter or darker, which on a flat area shows as a rectangle even when the defect is gone (2026-10-03 sun removals). Pass `--no-tone-match` only for an edit meant to change the colour inside the box. If `comfy_file` is no longer in ComfyUI's output, regenerate the unframed art with `render_card.py --from-note "<Card Name>" --out <scratchpad>/x.png --keep-raw <scratchpad>/<slug>_art.png` and pass that as `--art`.

**E4. Review and let the user pick.** Compare each repair with the original inside the box only, at full size: the defect gone, the fill continuous with its surroundings, no seam at the box edge, the woodcut hatching intact. Then view the same crop at contrast ×5 (subtract the crop's median colour, multiply by 5, add 128): a box or round patch that shows there may be visible to the user at normal contrast on a good screen; say what remains in your recommendation rather than calling it clean. Recommend one and let the user choose (AskUserQuestion). If every seed fails, adjust the box (E2) or the instruction, not the seed count.

**E5. Attach.** Keep the current card: `cp -n /workspace/tarot/card_<slug>.png /workspace/tarot/card_<slug>_prerepair.png`. Copy the pick to `/workspace/tarot/card_<slug>.png` and run `scripts/attach_image.py --card "<Card Name>" --image /workspace/tarot/card_<slug>.png --replace`. The card's record gains a `repairs` entry (instruction, box, seed, edit workflow and `tone_match`; or for a sky fill `method: fill_disc` with box, grow and thresh), so the note still reproduces its image: `render_card.py --from-note` replays both kinds. Update the Dropbox card library: the prerepair file to `legacy/`, the pick to `cards/` (§ Dropbox card library). Report the old resource id as an orphan. The registry does not change. If the `## Visual Description` mentions the removed element, update it with the user's approval.

**Done when:** a re-read of the note shows the new resource and a `## Render Record` with the repair, and `card_<slug>_prerepair.png` exists.

## Animate a card
Use when the user wants a card as a short looping animation (moving flames, water, stars). Only the part that should move is animated; everything else stays the card's original pixels, because an image-to-video model run over the whole card softens the ink outlines and hatching and drifts figures. All 36 cards were animated by 2026-10-08; each picked clip is `dropbox:Tarot/animations/the-<slug>_code_v<N>` or `the-<slug>_s<seed>_v2` (The Forge: `forge_5b_strong_s2`, The Tide: `tide_5b_strong_s3_strip`), with its command or prompt in `masks/`.

**Pick the route per card.** The **code route** (§ Code route below) draws the motion with a script: no AI model, exact style, exact loops. It is the default: 27 of the 36 picks use it. The **AI route** (A1–A5, Wan 2.2 5B image-to-video) only for an element that moves strongly by nature and is hard to draw: fire in a hearth, a pouring stream, a running hourglass, smoke curling, sea waves breaking. On the AI route, subtle elements failed (2026-10-07/08): calm prompts gave motion the user could not see, stronger ones random movement; light effects (stars, glows, beams) moved strangely; small birds and bees duplicated or vanished.

Prereq: ComfyUI 0.37.0 or later with Wan 2.2 5B — `wan2.2_ti2v_5B_fp16.safetensors` (`diffusion_models`), `umt5_xxl_fp8_e4m3fn_scaled.safetensors` (`text_encoders`), `wan2.2_vae.safetensors` (`vae`); files and settings from ComfyUI's template `video_wan2_2_5B_ti2v`. Also installed: Wan 2.2 14B first-and-last-frame (`--model 14b`, template `video_wan2_2_14B_flf2v`), which loops without a crossfade. Tested on The Forge 2026-10-06 and not used: with its 4-step speed-up LoRAs the fire moved half as much as the 5B (12 vs 26.5); with `--full` (20 steps, ~19 min a clip) still 15–16 and blown out to white mid-clip. Use 5B.

**A1. Prepare the art.** Take the card's current unframed art (the `## Render Record`'s `comfy_file`, or its last repair's output). Trim 3.5 % off each side and resize back to 1024 × 1792 — the same as `frame_card.py --art-crop 0.035` — and save it as the card's art. Save a 576 × 1024 copy anywhere local; `animate_wan.py` uploads a local file to ComfyUI's `input` folder itself (the remote PC's `input` is not mounted, and is emptied at 07:00).

**A2. Draw the mask.** A greyscale PNG at 1024 × 1792 over the trimmed art: white where the motion goes, black elsewhere, blurred ~10 px for a soft edge. Cut figures, faces and hands out of it, even where they overlap the moving area. Leave a margin of 10–40 px around them, widest at loose hair and clothing: the model shifts a figure by a few pixels, and without a margin that shifted copy shows as a ghost next to the real one (The Tide seed 3, 2026-10-06). A small drawn element inside the moving area that should stay put (water poured from a bowl) may drift in the model's output: track its position across the raw frames and freeze a strip covering the whole drift, taken from the original card (The Tide: a 135 px strip). Do not paint the element out of the model's input instead: with nothing there to animate, the model moved the figure's bowl and hands into the sea and made the waves jerk (2026-10-07). Check it as a pink overlay on the art before rendering. Keep the mask small: over a large or empty area (a whole sky, a whole field) the model invents objects (a duck's head, a beetle, a motorboat) or redraws the scene (batch of 2026-10-07). An element that is small on the card (an hourglass, a torch flame, a thin wisp of smoke, a small tree) renders as a blob at 576 × 1024; give the model a 9:16 box around it instead with `scripts/animate_mask.py crop <card dir> x0,y0,x1` (writes `crop.txt` and the model input; `animate_compose.py --crop` and the batch worker paste the frames back into that box). Prompts for small elements describe calm motion; "thousands of leaves churning" turned a tree crown into a blob.

**A3. Render.** `scripts/animate_wan.py --model 5b --image <576×1024 PNG> --seed <n> --prefix <slug>_5b_s<n> --prompt "<motion>"` (121 frames at 24 fps, ~3 min on the RTX 4080 once loaded, ~5 min cold). Run both scripts through `with-comfy local` or `with-comfy remote` (a second ComfyUI machine on the local network, available evenings only; has the same Wan files since 2026-10-06); they read the `COMFY_LOCAL_URL` it sets. The prompt describes the motion strongly and ends with "Camera static, no zoom, no pan." Do not ask for stillness or for the style to "stay unchanged": that damps the motion, and the mask already keeps the rest still. Style words ("ink outlines, no glare") also damp it — on The Forge, motion inside the mask (mean pixel change per 4 frames) was 8.9 with a gentle prompt, 10.7 with a style-heavy one, and 24–27 with a strong one. Render two or three seeds; strong prompts vary a lot between seeds (one may blow out to a white blaze, another add smear streaks).

**A4. Compose.** `scripts/animate_compose.py --frames-prefix <prefix> --count 121 --fps 24 --art <trimmed art> --mask <mask> --title "<Card Name>" --out <slug>_5b_s<n> --crossfade 0.5` pastes each frame into the art inside the mask, frames the card once with the deck frame flags (so the paper texture doesn't flicker), blends the last half second into the first to close the loop (5B cannot end on its start image), and writes `<out>.mp4` and `<out>.webp`. For `--model 14b` output use `--fps 16 --count 81` and no `--crossfade`.

Speed and loop are chosen per card: `--slow N` slows the clip by motion interpolation (water read best at 3×; a bird was right at 1×), and `--pingpong` plays it forward then backward, which the user preferred over a crossfade (a crossfade of 0.5 or 1.5 s shows). Do not slow past 2× for anything with edges that travel: 3× interpolation showed as jumping frames (lighthouse beams, lake ripples). Prompts must not ask for speed ("fast", "racing", "rapidly"): the user found such clips much too fast.

**A5. Review and let the user pick.** Pre-filter on motion first: `/workspace/tarot/animate/batch/check/check.py` (set its `B` folder and seed loop) measures the mean pixel change inside the mask; every clip the user kept scored 9.4 or more, and below about 9 the user saw no movement, so don't show those. Still frames show ghosts, smears and edges, not whether motion looks natural — waves that jerk back and forth look fine as stills — so only the user's viewing judges the motion. Look at close-ups of the masked area across the clip (start, middle, end) for blown-out areas, smears and a visible mask edge, and compare the jump from the last frame to the first with the change between neighbouring frames. Copy every candidate's MP4 to `dropbox:Tarot/animations/`; the user judges them by watching. After the pick, copy its WebP too, and the mask and prompt to `dropbox:Tarot/animations/masks/card_<slug>_mask.png` and `card_<slug>.prompt.txt`.

**Done when:** the user picked a clip, its MP4, WebP, mask and prompt are in `dropbox:Tarot/animations/`, and the card's entry in `deck.json` names the MP4. Notes and registry do not change.

**Batch (many cards, unattended).** For a run over many cards, use a batch folder with one subfolder per card slug holding `art.png` (A1), `input_576x1024.png`, `mask.png` and `prompt.txt`, plus `jobs.json` (`[{"slug","name","seed"}]`, all cards' seed 2 first, then seed 3, ...). `scripts/animate_mask.py grid|make|zoom <card dir>` draws and checks a mask from polygons in art pixels. Mark a card `READY` (empty file in its folder) only after checking its pink preview. Start one detached worker per ComfyUI instance: `setsid nohup python3 scripts/animate_batch.py --dir <batch> --worker local|remote > worker_<name>.out 2>&1 < /dev/null &` — never stop them with `pkill -f animate_batch.py` from a shell whose own command line contains that name (it kills the shell); kill by PID. Workers share the queue (`state.json`, `run.log`), skip cards without `READY` until they appear, retry a failed job once, release the job and exit when their instance is down (the remote after 07:00), and copy each MP4 to `dropbox:Tarot/animations/batch/`. A worker restarted later resumes where the queue stands. First batch: 34 cards × seeds 2–4, `/workspace/tarot/animate/batch/`, 2026-10-07.

### New card
A card added after 2026-10-08 has no clip. To give it one:
1. Prepare its art as in A1 into `/workspace/tarot/animate/batch/the-<slug>/art.png`.
2. Propose one moving element with the user and add it to `/workspace/tarot/animate/batch/cards_elements.json` (`slug`, `name`, `element`).
3. Make it on the code route if a script fits the element (§ Code route); use the AI route only for strong natural motion (fire, pouring water, breaking waves). Show the pilot in `dropbox:Tarot/animations/procedural/` and let the user judge.
4. After approval: deliver as in § Code route (or A5 for the AI route), add `"the-<slug>": "<mp4 name>"` under `clips` in `dropbox:Tarot/animations/deck.json`, delete the pilots, and refresh the backup with `rclone copy /workspace/tarot/animate dropbox:Tarot/animations/source/`.

### Code route
The motion is drawn by a script over the card's unframed art. Scripts are in `/workspace/tarot/animate/procedural/` (run them there; masks are kept there too). Each takes `--art /workspace/tarot/animate/batch/the-<slug>/art.png` (the A1-trimmed 1024 × 1792 art), `--title "<Card Name>"` and `--out <name>`. Each draws the frame and banner itself (`frame_card.py` with the deck frame flags), renders 96 frames at 24 fps and writes `<name>.mp4` and `.webp`. Every moving part runs whole cycles per clip, so the loop is seamless without a crossfade. Read a script's `--help`; all options are opt-in, and the defaults reproduce the approved clips.

| Effect | Script | Example card (its command: `dropbox:Tarot/animations/masks/card_the-<slug>.code.txt`) |
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

**Check before showing.** Compare the jump from the last frame to the first with a typical frame step (`procedural/wcheck.py <work dir> <mask.png> x0,y0,x1,y1 <strip.png>` does this on a render's work-dir frames, measures change outside the mask, and makes a frame strip of the box). Look at 2–3 frames at full size around the element and around nearby figures. Show pilots in `dropbox:Tarot/animations/procedural/`.

**Deliver** an approved clip (either route) by pointing the card's entry in `dropbox:Tarot/animations/deck.json` (card slug → MP4 file name; the daily card page plays that clip) at it, and for the code route store it as `dropbox:Tarot/animations/the-<slug>_code_v<N>.{mp4,webp}`, its masks as `masks/card_the-<slug>_<element>.png`, and the exact command as `masks/card_the-<slug>.code.txt` (`procedural/deliver_batch.py` shows the pattern). `frame_card.py` adds unseeded paper grain, so a re-render differs in the frame border only; the animated picture is identical.

### Story loop
A figure acts out a short scene in a seamless loop (first and only one: The Sower, `dropbox:Tarot/animations/the-sower_story_v1.{mp4,webp}`, 2026-10-10). It is an extra clip next to the card's deck clip: the user kept the subtle clip in `deck.json`, so do not repoint it unless asked. Scripts are in `/workspace/tarot/animate/story/` (inputs per card in a subfolder, e.g. `sower/`; backup `dropbox:Tarot/animations/source/story/`); run the ComfyUI ones through `with-comfy local` (needs Qwen Image 2.1 edit and Wan 2.2 14B i2v high/low fp8; the remote PC has them too).
1. **Beats.** Agree 2–3 story moments with the user, the card pose as K0 (Sower: K0 throw → K1 hand in bag → K2 arm held out → K0).
2. **Keyframes.** `keyframe.py --art <png> --box 0,0,1024,1110 --instruction "..." --seed N --out K<n>.png` (Qwen edit; keeps only the box, tone-matched). Edit each keyframe from the previous keyframe, never from the card, so every persisting object (bag, strap) stays in the same place; otherwise Wan invents moves to carry it. Say what stays put in the instruction ("the birds stay exactly where they are").
3. **Transitions.** `segment.py --full --first A.png --last B.png --length 81|41 --seed N --prefix <dir> --prompt "..."` (Wan 14B first-and-last-frame; always `--full`, the 4-step LoRA halves the motion; ~20 min per 81 frames on the RTX 4080). Size the length to the move: a transition longer than its move makes Wan idle and then invent motion or objects (81 frames from bag to throw added a second bag). Render 2 seeds per transition; a failed job usually works on a plain retry. A finished render whose download failed can be fetched from ComfyUI `/history` by its prefix.
4. **Compose.** `story_compose.py --art art.png --mask mask.png --title "<Card Name>" --out <name> <seg1> <seg2> ...` joins the transition folders (it drops each folder's last frame) at 16 fps; only the mask (figure box plus every moving element) takes the video, the rest stays the card's pixels.
5. **Fix by editing frames, not re-rendering**, where possible:
   - Wan slows into and out of every keyframe, so a keyframe in the middle of a movement shows as a pause. Cut the near-still frames on both sides of the joint (copy the kept frames into new folders) — the Sower's arm became one fluent movement this way. Better still, put keyframes only where the figure really pauses.
   - A dip or extra move before a keyframe: end the transition on an earlier frame that is already right and use that frame as the next transition's first keyframe.
   - Stray drawn elements (seeds thrown too early) can be painted out of the frames by filling thin dark shapes from nearby sky.
6. **Check** arm paths and invented objects on a crop sheet of every 4th frame (start, joint, end), then let the user watch the pilots in `dropbox:Tarot/animations/procedural/`. After approval store the clip as `the-<slug>_story_v<N>.{mp4,webp}` in `dropbox:Tarot/animations/`, delete the pilots, and back up the inputs and scripts.

## Dropbox card library
`dropbox:Tarot` (rclone remote `dropbox:`; `E:\Dropbox\Tarot` on the user's Windows PC) is where the user finds the card PNGs, like `dropbox:music-library` for music and `dropbox:audiobooks` for audiobooks. Layout:
- `cards/card_<slug>.png` — the current card, one per registry entry, the same file that is attached in Joplin.
- `legacy/` — replaced cards: `card_<slug>_legacy.png` (before a re-render), `card_<slug>_prerepair.png` (before a repair), and the pre-sowerstyle files; `legacy/notes/` holds old local markdown drafts.
- `seed-sheets/<slug>/` — seed sheets, with `deck-overview.jpg` at the top.
- `animations/` — card animations (§ Animate a card): exactly one deck clip per card (MP4 + WebP, 36 cards), plus extra story loops `the-<slug>_story_v<N>` (§ Story loop; not in `deck.json`), `masks/` with each card's masks and its prompt or code command, `source/` with a backup of `/workspace/tarot/animate/` (every card's unframed art, the code-route scripts and masks in `source/procedural/`, the AI-route inputs and the element list), `deck.json` (card slug → deck clip, read by the daily card page), and `review/` with the whole-deck overview videos. Drafts were deleted on 2026-10-08; new candidates go to `procedural/` or `batch*/` and are deleted once the user has picked.

Copy with rclone, which copies bytes and keeps the PNG's `tarot_render` record: `rclone copyto /workspace/tarot/card_<slug>.png dropbox:Tarot/cards/card_<slug>.png` (overwrites the old current card), and for a replaced card first `rclone copyto /workspace/tarot/card_<slug>_legacy.png dropbox:Tarot/legacy/card_<slug>_legacy.png --ignore-existing` (likewise `_prerepair`). Never delete from the library. Dropbox unreachable → attach anyway, report the copy as pending, and give the user the `rclone copyto` command.

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
- `scripts/render_card.py` — one-call render: assembles the prompt from `style.md`, runs the workflow, frames the result, and embeds the render record in the card PNG. `--from-note "<Card Name>"` regenerates a card from its note's `## Render Record` alone (base render, recorded repairs, frame) — use it when the local card PNG or the ComfyUI outputs are gone. Emits a JSON result line with the seed used and `comfy_file`, the unframed ComfyUI output filename.
- `scripts/frame_card.py` — deterministic frame + serif title banner (the border/title the model must not draw).
- `assets/tarot-card-qwen-edit.json` — the ComfyUI image-edit graph (API format) for § Repair a defect in one card: Qwen Image 2.1 at full size, 40 steps.
- `scripts/edit_card.py` — one-call repair: Qwen edit of the card's unframed art, masked paste-back inside `--box`, tone-matched to the original, frame, render record with a `repairs` entry.
- `scripts/fill_disc.py` — sun/moon removal on a flat sky without an AI edit (§ Repair a defect); deterministic, replayed by `--from-note`.
- `scripts/repair_tools.py` — `tone_match` and `fill_disc`, shared by the two repair scripts and `render_card.py --from-note`.
- `scripts/animate_wan.py` — runs Wan 2.2 image-to-video (5B, or 14B first-and-last-frame) on one image and saves the frames in ComfyUI's output (§ Animate a card).
- `scripts/animate_batch.py` — unattended queue of animate jobs over one or more ComfyUI instances (§ Animate a card, Batch).
- `scripts/animate_mask.py` — draw a mask from polygons and check it as a pink preview.
- `scripts/animate_compose.py` — pastes those frames into the card art inside a mask, frames once, closes the loop (`--crossfade`, or `--pingpong`), slows it (`--slow N`), writes MP4 + WebP.
- Code-route scripts live outside the skill, in `/workspace/tarot/animate/procedural/` (§ Animate a card, Code route), because the delivered per-card commands run there with relative mask paths.
- `scripts/attach_image.py` — compress + upload to Joplin + swap note placeholder + write `## Render Record` + flip registry `image_status`.

New cards from this skill are always `image_status: "pending"` and `prompt_status: "original"`; the other values are for imported/migrated cards.
