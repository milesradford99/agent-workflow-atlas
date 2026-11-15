# The move: status and remaining work

A handover note for whoever (person or agent) finishes giving every entry its **move** ([STANDARD.md §8](STANDARD.md#8-the-move)). Delete this file in the pull request that completes step 5.

## Why

Read one after another, entries look alike: gather context, let the model work, a person decides, plus some industry background. The catalog's taxonomy fields barely separate them (190 of 238 entries have a `review` checkpoint, 174 are `chain`). What does separate them is the one thing each does beyond "AI drafts, a person reviews", which until now sat inside **Failure modes → guards**. §8 names it, classifies it with six codes drawn from context engineering (`prepare`, `restrict`, `verify`, `feedback`, `triage`, `standard`) and puts it in the front matter so the site and index can lead with it.

Readers this is for: someone browsing across fields for ideas, and someone in one field looking for a way in. Both should be able to read the move alone and decide whether to open the entry.

## State on 2026-11-15

- **Done:** §8 in STANDARD.md; `moves` in `taxonomy.yaml`; `validate.py` checks the pair wherever present; `i18n.py` requires a Chinese `move` when the English has one; the template and `i18n/TRANSLATING.md` mention the fields; `scripts/apply_moves.py` writes them.
- **Done:** 22 entries carry `moves` and `move` in both languages: AWF-0011, 0029, 0035, 0044, 0063, 0066, 0071, 0080, 0096, 0107, 0124, 0132, 0142, 0156, 0167, 0172, 0174, 0182, 0191, 0196, 0225, 0229.
- **Drafted, not applied:** a Chinese move and a category for 191 entries, in [research/2026-11-context-moves.md](research/2026-11-context-moves.md) and [its trial](research/2026-11-context-moves-trial.md). They were written from four lines of each entry (summary, shape, guards, how it differs), not from a full read. Category names there are Chinese: 放入 `prepare`, 挡住 `restrict`, 外验 `verify`, 回灌 `feedback`, 分流 `triage`, 标准 `standard`.
- **Not started:** the 47 entries whose newest source predates 2025-11 (listed at the end of the research note), the site, the index.

All four checks pass: `validate.py`, `build_index.py --check`, `build_diagrams.py --check`, `i18n.py status`.

## How to work

One batch = about 25 entries, one agent at a time. Per batch:

1. Take the next rows from the research note. For each entry, open its `README.md` and read **Failure modes → guards**, the shape and **How it differs**; read further only if the drafted move is not supported by those lines.
2. Write the English `move` (one or two sentences, 300 characters or fewer) following §8, and correct the Chinese draft to match it. Every number in the move must be in the entry, in the same words. Do not add a fact the entry does not carry. If the drafted category is wrong, change it.
3. Put the batch in a data file and apply it:

   ```python
   M = {
     '0063': (['verify'], "English sentence.", "中文句子。"),
   }
   ```

   ```bash
   python scripts/apply_moves.py batch.py
   ```

   The script adds the fields to both files and re-stamps the translation. It refuses an entry that already has a move.
4. Run the four checks:

   ```bash
   python scripts/validate.py
   ```

   ```bash
   python scripts/build_index.py --check
   ```

   ```bash
   python scripts/build_diagrams.py --check
   ```

   ```bash
   python scripts/i18n.py status
   ```

5. Read three entries of the batch against their moves. Reject a move that states a result the entry does not report, uses a number that is not in the entry, or would read the same for a different entry.
6. Commit and push. Commit message: `Moves: <field>, <n> entries`.

## Steps

- [x] **1. Framework** (this pull request).
- [ ] **2. Apply the drafted moves to the remaining 169 entries**, in the order of the research note: TEC (46 left), PRO (36), COM (22), ORG (20), CRE (13), unplaced (9), then the rest of the trial's 20. Nine early entries have no guards line (AWF-0002, 0003, 0005, 0006, 0007, 0008, 0009, 0015, 0021) and were drafted as `standard` for that reason alone; read each in full and give it its real move.
- [ ] **3. Decide the 47 older entries.** The owner's instruction is that entries with no source from the last year may go. Do not delete folders (AGENTS.md: ids are never reused; MAINTAINING.md: retiring sets `status: retired`). Before retiring any, check the date by reading the entry, because the list came from a script. Keep these whatever their dates: the model entries named in STANDARD.md (AWF-0001, 0024, 0164, 0137), the examples named in `i18n/TRANSLATING.md` (AWF-0069, 0164), and any entry with a `variants/` kit. For each kept entry, write its move. For each retired one, set `status: retired` in the README and re-stamp. Bring the proposed list to the owner before changing any status.
- [ ] **4. Show it.** Site (`scripts/build_site.py`, `scripts/site_pages.py`): put the move at the top of each entry page and on its card; add a filter by `moves` beside autonomy and checkpoints; make "browse by move" the first view and field the second. Index (`scripts/build_index.py`): add a section grouping entries by move. Labels for the six codes go in `i18n/labels.yaml` in both languages, and `validate.py` should check them as it does the other codes. README.md: say in the opening what the entries have in common and that the move is what differs.
- [ ] **5. Make the fields required.** Add `moves` and `move` to `REQUIRED` in `validate.py` once every non-retired entry has them, add a line to AGENTS.md under Gotchas, and delete this file.
- [ ] **6. Look again at entries that are `standard`.** After step 2, list them. For each: is there a number or a first-hand account that makes it worth keeping as it is (say so in the move), or is it a candidate to merge with a neighbour (AWF-0222 and AWF-0110 already look like one workflow)? This is a judgement for the owner.

## Open questions for the owner

- Whether the move should also appear in the body of each README (a line under the title) or only in the front matter and on the site. It is front matter only for now, so the body and its translation checks are untouched.
- Whether `standard` entries stay in the default view of the site or sit behind a filter.
