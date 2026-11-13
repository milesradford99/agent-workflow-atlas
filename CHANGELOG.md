# Changelog

Catalog-level changes: new workflows, taxonomy changes, and tooling. Changes to a single entry show up in its git history and its `last_verified` month.

## 2026-11

### Changed
- Catalog site redesigned for reading. Each workflow's route is written out in words (one chip per step, human checkpoints in red) in the detail sheet and on its page; the dot strip stays for scanning lists. Steps that hold a 🛑 are highlighted, tables in entries render as tables, and public runs read as separate cards.
- *Start here* now opens with every field as a tile (count and public-evidence mix) that jumps into the field map. The field map shows a one-line summary under each workflow name. Cards name the approvals a person gives (plan, review, sign-off) instead of counting them.
- New typeface (Geist), a light and dark switch that remembers the choice, and one Markdown renderer (`site_pages.markdown`) for both the app and the static pages.

### Added
- Third collection pass: 60 new workflows (AWF-0156 to AWF-0215) and newer runs, sources and practice notes for 20 existing ones, with every cited link re-checked. See [research/2026-11-third-pass.md](research/2026-11-third-pass.md).
- Redesigned catalog site: a route strip for every workflow (agent steps in teal, human checkpoints in red), a calmer field directory, a detail sheet with section navigation, and full English and Simplified Chinese support (UI, field, profession and category names, workflow names and summaries; steps and sources stay in English). Chinese static pages at `w/<ID>/zh/`.
- A one-sentence `summary` on every workflow, required by `validate.py`; display labels in `i18n/labels.yaml` and Chinese names and summaries in `i18n/workflows.zh-CN.yaml`.
- A shareable static page per workflow (`w/<ID>/`) with a preview image, a sitemap, and catalog exports (`catalog.json`, `catalog.csv`) built by `scripts/build_site.py`.
- A *Start here* view on the site with the workflows that have kits and the best-documented ones.
- 15 starter issues labelled `good first issue`: wanted sources, kit runs to add as examples, and weak entries to strengthen.
- Claude Code agent kits (`variants/claude-code.md`) for 10 workflows, linked from each entry and from both READMEs.
- Full steps, output and failure modes for the 16 seed workflows that had only a shape line. `validate.py` now requires a Steps section and a step for every 🛑 checkpoint.
- A Chinese README (`README.zh-CN.md`), a screenshot at the top of the README, and repository topics.
- Second collection pass, with workflows from new fields and second workflows in busy classes. See [research/2026-11-second-pass.md](research/2026-11-second-pass.md).
- New phyla `PRO/INS` (insurance, class `CLAIMS`) and `COM/RET` (retail and e-commerce operations, class `CATALOG`), each opened with at least three workflows.
- First unplaced workflows (logistics, real estate, construction submittals, safety audits, agriculture, insurance underwriting). Each waits for two more similar workflows before a class opens.
- A browsable site (`scripts/build_site.py`) with a map by field, search, filters, and a detail panel for every workflow.
- A Mermaid diagram of the shape line in every workflow README (`scripts/build_diagrams.py`).
- Freshness checks (`scripts/freshness.py`) and a monthly report issue; the upkeep process is in [MAINTAINING.md](MAINTAINING.md).
- A Public runs section in every workflow, with verified links and a coverage grade.
- Workflows for all 56 previously empty classes, AWF-0032 to AWF-0087 ([research note](research/2026-11-new-workflows.md)).
- The first accepted workflow, AWF-0030, with its reference example ([research](research/2026-11-real-runs.md)).

### Fixed
- Shape diagrams no longer pull the step before an `each X:` box inside the box, and checkpoint nodes are styled red wherever they appear.

### Started
- 31 workflows seeded from [the Phase 1 research report](research/phase1-report.md), the taxonomy, validation and index scripts, and contribution templates.
