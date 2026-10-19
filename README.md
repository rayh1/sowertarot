# sowertarot

The Sower tarot deck and its daily card: the site sowertarot.com, its content, and the skills that
make the cards and the daily reading.

## What is where

- `content/cards/<slug>.md`: one file per card (front matter with title, concept, key terms and the
  picture and clip; then the card's sections).
- `content/readings/<date>.md`: one file per daily reading.
- `content/media/`: the reference files, the original card PNGs and their MP4 clips;
  `content/checksums.txt` lists their SHA-256 checksums.
- `src/`: the Astro site. It reads `content/` (another folder through the environment variable
  `SOWER_CONTENT`).
- `skills/tarot-daily-reading/`: the daily draw and reading, run at 07:00 by cron
  (`scripts/install-cron.sh` writes the cron line).
- `skills/tarot-card-generator/`: how the cards are made.
- `tools/animate/`: the code that makes the clips (see its `README.md`).
- `scripts/`: `checksums.py` and `label_media.sh` for the reference files, `draw_check.py` to check a
  day's draw, and `migrate.py` and `check_migration.py`, which copied the deck from its old archive.
- `settings.env`: the settings of the skills and tools, each explained in the file. Put your own
  values in `settings.local.env` next to it (ignored by git).

## The site

```sh
npm ci
npm run dev     # dev server on port 3000
npm run build   # into dist/
npm test
```

The build fails when `content/checksums.txt` does not match `content/media/`. After adding or
changing a reference file, run `scripts/label_media.sh FILE...` on new files, then
`python3 scripts/checksums.py write`.

The dev container is described in `.devcontainer/README.md`.

## Licence

- Code (everything not listed below): MIT, see `LICENSE`.
- Cards, clips and texts (everything in `content/`, and the layer and mask images in
  `tools/animate/procedural/`): CC BY-NC-SA 4.0, credited to "Sower Tarot", see `LICENSE-content`.
