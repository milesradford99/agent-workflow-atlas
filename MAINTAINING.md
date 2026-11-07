# Maintaining the catalog

AI tools and practices change every few months, so an entry that was accurate when it was written goes stale. Three loops keep the catalog current:

| Loop | How often | What it catches | Who runs it |
|---|---|---|---|
| [Freshness report](#freshness-report) | Monthly, automatic | Entries not re-checked in 6 months; source links that stopped working | GitHub Actions opens the issue; a maintainer works through it |
| [Re-checking an entry](#re-checking-an-entry) | When an entry is due or reported | Changed numbers, renamed or discontinued tools, a practice that moved on | Anyone, through a pull request |
| [Collection sweep](#collection-sweep) | Quarterly | New workflows and new fields that the catalog doesn't have yet | A maintainer, with research agents |

Readers can also report a problem at any time with the [correction issue form](.github/ISSUE_TEMPLATE/correction.yml).

## Freshness report

On the 1st of each month, [`.github/workflows/freshness.yml`](.github/workflows/freshness.yml) runs `scripts/freshness.py --links` and keeps one open issue labelled `freshness` up to date. The report has two parts:

- **Due for re-checking:** every entry whose `last_verified` month is 6 or more months old.
- **Dead links:** sources and public runs that return 404 or 410, or whose domain no longer exists. Fix these.
- **Couldn't reach:** timeouts, dropped connections and server errors, listed in a collapsed section. These are usually slow sites or sites that block automated traffic; look only at ones that stay there several months running. Sites that refuse automated checks outright (403, 429) are just counted.

To run it locally:

```bash
python scripts/freshness.py --links
python scripts/freshness.py --as-of 2027-06    # see what will be due by June 2027
```

## Re-checking an entry

One pull request per entry, or one per class if several are due together.

1. **Public runs.** Re-open each link in the entry's Public runs section. Check that the number is still on the page in the same words. Fix the wording, mark the run as gone, or remove it. Update the coverage grade (Strong, Partial, Weak, None found) if it changed.
2. **Sources.** Replace dead links with an archived copy (web.archive.org) or a newer source that supports the same step. If nothing supports a step any more, rewrite or remove the step.
3. **Tools.** Check each `variants` slug still names a tool that exists. Rename or remove the ones that don't. A tool switch alone never changes the workflow (TAXONOMY.md rule 4).
4. **Practice.** If the way people run it has changed (new checkpoints, different autonomy, different deliverable), apply the swap test:
   - *Small change:* update the steps.
   - *Different checkpoints, autonomy or deliverable:* add a new workflow with a new ID, and leave this one as it is.
5. **Date.** Set `last_verified` to the current month. Run `python scripts/validate.py` and `python scripts/build_index.py`.

**Retiring.** An entry with no new example runs in 18 months whose tools have all been discontinued becomes `status: retired` (TAXONOMY.md rule 6). Keep the folder and the ID.

## Collection sweep

Once a quarter, look for workflows the catalog doesn't have. The sweep follows the catalog's own [Issue-tree research](workflows/ORG/BIZ/STRAT/issue-tree-research/) shape:

1. **Plan.** Export the existing workflows with their shape lines (one line each: class, ID and name, autonomy, shape). Split the classes into 6–8 groups, plus one group for fields outside the taxonomy. A maintainer approves the split.
2. **Research.** Give each group's agent [research/prompts/collect.md](research/prompts/collect.md), filled in with its classes. Run them in parallel. Each one returns YAML blocks in the catalog's record format, or "none found".
3. **Re-check.** Collect every public run into a table and give it to separate agents with [research/prompts/check.md](research/prompts/check.md). Drop runs whose page won't open or whose number isn't there. Correct the first-hand labels.
4. **File.** Turn each surviving block into `workflows/<K>/<P>/<C>/<name>/README.md` with the next free IDs, and put fields that don't fit in `workflows/unplaced/`. When three similar unplaced workflows exist, propose a new class (CONTRIBUTING.md, "New class or phylum").
5. **Record.** Write a dated note in `research/` with the counts, what was dropped and the caveats, as [research/2026-11-new-workflows.md](research/2026-11-new-workflows.md) does. Then run the checks and open the pull request.

## Merging pull requests

- `python scripts/validate.py` and `python scripts/build_index.py --check` must pass. CI runs both.
- Placement follows the keys, and the swap test was applied (CONTRIBUTING.md, "Review").
- A pull request that touches `.github/workflows/`, `scripts/` or `AGENTS.md` gets a second look. These run with repository permissions or steer agents that edit the catalog.
