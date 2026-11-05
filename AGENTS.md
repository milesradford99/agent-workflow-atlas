# AGENTS.md

## Commands

```bash
pip install -r scripts/requirements.txt
python scripts/validate.py        # rule checks; prints the next free AWF id
python scripts/build_index.py     # regenerate INDEX.md after any change under workflows/
```

CI runs `validate.py` and `build_index.py --check`, so commit the regenerated INDEX.md.

## Gotchas

- Never change or reuse an `AWF-####` id. Moving a workflow keeps its id; merging sets `status: merged` and `merged_into`, never deletes the folder.
- Folder path and the `kingdom`/`phylum`/`class` fields must agree; allowed codes are in `taxonomy.yaml`.
- `checkpoints` must equal the set of `🛑 <word>` entries in `shape`.
- `status: accepted` requires `reference_example` pointing at an `examples/YYYY-MM-name/` folder with a README.md.
- Don't invent example runs, numbers or sources. Example folders hold real runs from contributors only.
- Entries mix English and Chinese (短剧, 网文 terms); keep the Chinese terms as written.
- `research/` is a dated report, not live data. Don't edit it to match catalog changes.
