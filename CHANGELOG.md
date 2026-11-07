# Changelog

Catalog-level changes: new workflows, taxonomy changes, and tooling. Changes to a single entry show up in its git history and its `last_verified` month.

## 2026-11

### Added
- Second collection pass, with workflows from new fields and second workflows in busy classes. See [research/2026-11-second-pass.md](research/2026-11-second-pass.md).
- New phyla `PRO/INS` (insurance, class `CLAIMS`) and `COM/RET` (retail and e-commerce operations, class `CATALOG`), each opened with at least three workflows.
- First unplaced workflows (logistics, real estate, construction submittals, safety audits, agriculture, insurance underwriting). Each waits for two more similar workflows before a class opens.
- A browsable site (`scripts/build_site.py`) with a map by field, search, filters, and a detail panel for every workflow.
- A Mermaid diagram of the shape line in every workflow README (`scripts/build_diagrams.py`).
- Freshness checks (`scripts/freshness.py`) and a monthly report issue; the upkeep process is in [MAINTAINING.md](MAINTAINING.md).
- A Public runs section in every workflow, with verified links and a coverage grade.
- Workflows for all 56 previously empty classes, AWF-0032 to AWF-0087 ([research note](research/2026-11-new-workflows.md)).
- The first accepted workflow, AWF-0030, with its reference example ([research](research/2026-11-real-runs.md)).

### Started
- 31 workflows seeded from [the Phase 1 research report](research/phase1-report.md), the taxonomy, validation and index scripts, and contribution templates.
