# animate

The code that makes the card clips, copied from the user's own working folder on 2026-10-18 (step 14 of
the site plan), so a fork can remake them.

- `procedural/`: the effect scripts, one `card_<slug>.code.txt` per code-made card (the command that
  made its clip) and the layer and mask PNGs those commands read. Run the scripts from inside
  `procedural/`: they open their masks by relative path. They import the card skill's scripts from
  `skills/tarot-card-generator/scripts/` in this repository.
- `check/check.py`: the motion check for AI-made clips.
- `batch/` (not in git): one folder per card, `batch/<slug>/art.png`, the card's unframed art that the
  commands read (`--art ../batch/<slug>/art.png`); the card skill makes it (§ Animate a card).

The one-off scripts that delivered the first clips to the old Dropbox archive are left out. The card skill's
§ Animate a card points here after its rewrite at step 26; until then it names the old folder.
