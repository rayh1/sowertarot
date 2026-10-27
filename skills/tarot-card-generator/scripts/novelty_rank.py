#!/usr/bin/env -S uv run --no-config --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["sentence-transformers==5.1.1", "torch"]
# [[tool.uv.index]]
# name = "pytorch-cpu"
# url = "https://download.pytorch.org/whl/cpu"
# explicit = true
# [tool.uv.sources]
# torch = { index = "pytorch-cpu" }
# ///
"""Rank candidate cards by how far their meaning lies from every existing card (§ Find something new).

  uv run --no-config --script novelty_rank.py CANDIDATES.json

CANDIDATES.json is a list of {"title", "seed", "seed_source", "essence"}: seed_source says where the seed came
from (e.g. "bibliomancy", "the day", "suggested by Claude"; "gap" for a Miner round, with the gap described in
seed). Each essence is embedded with MODEL, as is the ## Archetypal Essence section of every card file in
content/cards/; a candidate's distance is 1 minus its highest cosine similarity to any card (cosine similarity:
how closely two embedding vectors point the same way, 1 = the same direction). Prints a Markdown list, most
distant first, with each distance and nearest card. There is no cut-off: distance only orders the list, and far
is not the same as meaningful, so the user reads the list and keeps one candidate or none.

Runs with uv (it installs the dependencies, CPU-only torch; --no-config keeps uv from demanding the
devcontainer's exact Python in .python-version); the first run downloads MODEL from Hugging Face (about 420 MB,
cached in ~/.cache/huggingface), then a run takes about 10 s on CPU. Scores from different models do not compare:
keep MODEL pinned. Chosen 2026-10-27 over all-MiniLM-L6-v2, all-mpnet-base-v2 and bge-small-en-v1.5: given
plain-word paraphrases of four card essences and a loose description of The Anchor, it was the only one that
named the source card every time with a clear margin (similarity to the source 0.74-0.81, to the runner-up
0.07-0.10 lower).
"""
import json
import os
import re
import sys
from pathlib import Path

MODEL = "BAAI/bge-base-en-v1.5"
REPO = Path(os.environ.get("TAROT_REPO") or Path(__file__).resolve().parents[3])
WORDS = (75, 150)        # an existing card's essence length; a much shorter candidate would skew its score


def essences():
    """{title: Archetypal Essence text} of every card file."""
    out = {}
    for p in sorted((REPO / "content" / "cards").glob("*.md")):
        text = p.read_text(encoding="utf-8")
        title = re.search(r'^title: "(.*)"$', text, re.M).group(1)
        m = re.search(r"^## Archetypal Essence\n(.*?)(?=^## |\Z)", text, re.S | re.M)
        if not m:
            sys.exit(f"{p.name}: no ## Archetypal Essence section")
        out[title] = m.group(1).strip()
    return out


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    cands = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    bad = [c.get("title", "?") for c in cands if not all(c.get(k) for k in ("title", "seed", "seed_source", "essence"))]
    if bad:
        sys.exit(f"candidates lack title, seed, seed_source or essence: {', '.join(bad)}")
    cards = essences()
    os.environ.setdefault("TRANSFORMERS_VERBOSITY", "error")
    os.environ.setdefault("HF_HUB_DISABLE_PROGRESS_BARS", "1")
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(MODEL, device="cpu")
    card_vecs = model.encode(list(cards.values()), normalize_embeddings=True)
    cand_vecs = model.encode([c["essence"] for c in cands], normalize_embeddings=True)
    sims = cand_vecs @ card_vecs.T            # cosine similarity, since the vectors are normalised
    titles = list(cards)
    deck = card_vecs @ card_vecs.T
    deck[range(len(titles)), range(len(titles))] = -1
    spacing = sorted(1 - float(x) for x in deck.max(1))
    rows = []
    for c, row in zip(cands, sims):
        i = int(row.argmax())
        rows.append((1 - float(row[i]), c, titles[i]))
    rows.sort(key=lambda r: -r[0])
    print(f"Ranked by distance in meaning to the nearest of {len(cards)} cards ({MODEL}); most distant first.")
    print(f"For scale: each existing card's distance to its nearest other card runs from {spacing[0]:.2f} to "
          f"{spacing[-1]:.2f}, median {spacing[len(spacing) // 2]:.2f}.\n")
    for n, (dist, c, near) in enumerate(rows, 1):
        words = len(c["essence"].split())
        warn = f" (essence is {words} words; cards have {WORDS[0]}–{WORDS[1]})" if not WORDS[0] <= words <= WORDS[1] else ""
        print(f"{n}. **{c['title']}** — distance {dist:.3f}, nearest card: {near}{warn}")
        print(f"   - Seed: {c['seed']} ({c['seed_source']})")
        print(f"   - Essence: {c['essence']}\n")


if __name__ == "__main__":
    main()
