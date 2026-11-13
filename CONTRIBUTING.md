# Contributing

This catalog collects **real** agentic workflows: multi-step, acting on real files or systems, with named human checkpoints, and rerunnable by someone else (the four criteria in [TAXONOMY.md](TAXONOMY.md)). The most useful thing you can add is evidence that a workflow works: a dated example run with the context files you used.

There are three ways to contribute. Pick the first one that fits.

| You have… | Do this |
|---|---|
| A real run of a workflow that's already listed | [1. Add an example run](#1-add-an-example-run) |
| A workflow that isn't listed | [2. Add a new workflow](#2-add-a-new-workflow) |
| A workflow that's in the wrong place, or two that are really the same | [3. Move or merge](#3-move-or-merge) |

Don't use git? [Open a "Propose a workflow" issue](../../issues/new/choose) instead and a maintainer will turn it into a pull request.

## Before you share anything

Example runs include prompts, context files and outputs. Before committing, remove:
- secrets, API keys, tokens, internal URLs;
- personal data: names, emails, patient or student information, candidate details;
- client or employer material you don't have the right to share.

Replace them with realistic placeholders. If in doubt, leave it out and describe it in words.

## 1. Add an example run

1. Find the workflow in [INDEX.md](INDEX.md).
2. Copy [templates/example/](templates/example/) to `<workflow folder>/examples/YYYY-MM-short-name/`.
3. Fill in the README, put your context files in `context/` and a small input and output in `sample/`.
4. If you used a toolchain that isn't in the workflow's `variants` list, add its slug.
5. If the workflow is `draft` and this is its first example, set `reference_example: examples/YYYY-MM-short-name/` and `status: accepted`.
6. Run the checks (below) and open a pull request.

If your run differs from the listed steps, check the swap test first: a different checkpoint, autonomy level or deliverable makes it a new workflow (path 2), not an example.

## 2. Add a new workflow

1. **Is it new?** Search [INDEX.md](INDEX.md). Apply the swap test (TAXONOMY.md rule 4): if a practitioner could swap your workflow for a listed one without changing the deliverable, the human checkpoints or the autonomy level, it's the same workflow. Add an example instead.
2. **Place it.** Use the keys in TAXONOMY.md §4: the first matching kingdom row, then the first matching phylum, then the class. If nothing fits, use `workflows/unplaced/`.
3. **Create it.** Copy [templates/workflow/README.md](templates/workflow/README.md) to `workflows/<KINGDOM>/<PHYLUM>/<CLASS>/<short-name>/README.md`. Use the next free ID printed by `python scripts/validate.py`.
4. **Fill it in.** Write the shape line first; it forces you to name every step and checkpoint. Then a one-sentence `summary`, the steps (one for every 🛑 checkpoint in the shape), failure modes and sources.
   Then add the Simplified Chinese version: `python scripts/i18n.py scaffold AWF-xxxx` writes `README.zh-CN.md` next to it. Translate it following [i18n/TRANSLATING.md](i18n/TRANSLATING.md), then run `python scripts/i18n.py stamp AWF-xxxx`. If you can't write Chinese, ask a maintainer or a coding agent to do this step; `validate.py` fails until the file exists.
5. **Evidence.** Grade honestly: `A` for a public, detailed write-up, `B` for vendor material, `C` for community reports. Link every claim with a number in it to a source.
6. It stays `draft` until it has an example run. You can include one in the same pull request.

## 3. Move or merge

- **Move:** change `kingdom`/`phylum`/`class` and move the folder. Keep the ID. Explain in the pull request which key row it should have matched.
- **Merge:** when two entries are the same workflow, the one with the lower ID keeps its name (TAXONOMY.md rule 5). Move the other's examples and variants into it, then set the other to `status: merged` and `merged_into: AWF-xxxx`. Don't delete it; its ID must keep resolving.
- **New class or phylum:** edit [taxonomy.yaml](taxonomy.yaml) and TAXONOMY.md in a separate pull request. A new class needs three unplaced workflows that would go in it.

## Checks

```bash
pip install -r scripts/requirements.txt
python scripts/validate.py
python scripts/build_index.py
```

`validate.py` checks the rules and prints the next free ID. `build_index.py` regenerates [INDEX.md](INDEX.md); commit the result. CI runs both on every pull request.

## Review

A maintainer checks that:
- the placement follows the keys;
- the swap test was applied;
- claims are sourced and the evidence grade fits;
- example runs are anonymized and could actually be rerun.

Expect questions rather than a quick merge on new workflows; the classification only stays useful if entries are consistent.

## AI-assisted contributions

Welcome, with two conditions:
- **Disclose it.** Say in the pull request how AI helped (drafting, translation, research, formatting). The template has a field for this.
- **Vouch for it.** A person must have checked every claim, number and source in the contribution, and stands behind it.

Example runs must be **real runs** that you or your team did. Generated, reconstructed or "illustrative" runs aren't accepted, because the catalog's value is evidence that workflows work in practice.

## License

Workflows, examples and docs are shared under [CC BY 4.0](LICENSE-CONTENT); scripts under [MIT](LICENSE). By opening a pull request, you agree your contribution is shared under those terms.
