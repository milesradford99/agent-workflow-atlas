# AGENTS.md

## Commands

```bash
pip install -r scripts/requirements.txt
python scripts/validate.py        # rule checks; prints the next free AWF id
python scripts/build_index.py     # regenerate INDEX.md after any change under workflows/
python scripts/build_diagrams.py  # redraw the Mermaid diagram under each `shape` line
python scripts/build_site.py      # build the browsable site into site/ (git-ignored)
python scripts/freshness.py --links   # entries due for re-checking + broken links (network)
python scripts/i18n.py status     # Chinese translations: missing, broken, behind the English
python scripts/i18n.py stamp AWF-0001   # after translating README.zh-CN.md
```

Re-checking an entry or running a collection sweep: follow MAINTAINING.md. Set `last_verified` to the current month only after actually re-opening the entry's sources.

CI runs `validate.py`, `build_index.py --check` and `build_diagrams.py --check`, so commit the regenerated INDEX.md and diagrams. Never edit a diagram by hand; change the `shape` line and rerun.

## Gotchas

- Never change or reuse an `AWF-####` id. Moving a workflow keeps its id; merging sets `status: merged` and `merged_into`, never deletes the folder.
- Folder path and the `kingdom`/`phylum`/`class` fields must agree; allowed codes are in `taxonomy.yaml`.
- `checkpoints` must equal the set of `🛑 <word>` entries in `shape`.
- `status: accepted` requires `reference_example` pointing at an `examples/YYYY-MM-name/` folder with a README.md.
- Don't invent example runs, numbers or sources. Example folders hold real runs from contributors only.
- Entries mix English and Chinese (短剧, 网文 terms); keep the Chinese terms as written.
- Every workflow needs a one-sentence `summary` (≤200 chars). Display names for taxonomy codes live in `i18n/labels.yaml` (both `en` and `zh-CN` required); every workflow also has a Chinese `README.zh-CN.md` beside its README (name, summary, deliverable, shape, intro, steps, public-run descriptions; sources stay in English). Follow `i18n/TRANSLATING.md`: keep the shape symbols and `🛑 <type>` words, step count, citations, links, numbers and public-run quotes identical to the English, then run `i18n.py stamp`. When you change an English README, update its `README.zh-CN.md` in the same change and re-stamp; if you can't, `validate.py` only warns.
- `research/` is a dated report, not live data. Don't edit it to match catalog changes.
