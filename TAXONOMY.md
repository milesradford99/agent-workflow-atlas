# Taxonomy

How workflows are classified in this catalog. The machine-readable lists live in [taxonomy.yaml](taxonomy.yaml); `scripts/validate.py` enforces them. The research behind these choices is in [research/phase1-report.md](research/phase1-report.md).

## 1. The idea

Biology sorts animals by **ancestry**, not by what they happen to have in common. Bats and birds both fly, but a bat is a mammal. We sort workflows the same way:

- **Ancestry = the profession and the deliverable.** A contract-review agent descends from lawyers reviewing contracts. That decides where it lives in the tree.
- **Shared tricks are traits, not branches.** Generate-then-critique loops, parallel workers and autonomy levels appear in law, film and software alike, like wings. They are tags you can search by, never folders.
- **Tools are the bottom layer.** Claude Code vs. Codex, or Kling vs. Veo, are *variants* of the same workflow, so tool churn never moves anything.

Four more ideas come from biology, each turned into one simple rule (§3): permanent IDs, a reference example for every entry, one name per workflow with duplicates merged, and a key that places each workflow in exactly one spot.

## 2. Levels

| Level | Question it answers | Count | Example |
|---|---|---|---|
| **Kingdom** | What broad field is the deliverable in? | 5 | `CRE` Creative & Media |
| **Phylum** | Which profession? | 18 | `MED` Media Production |
| **Class** | Which discipline within it? | listed in §4 | `AIGCVIDEO` AI-generated video |
| **Species** | Which specific workflow? | open | *AI shot factory* · `AWF-0015` |
| *Variant* | Which toolchain? | open | `jimeng-kling-capcut` |
| *Example* | Which dated real run shows it working? | open | `2026-03-studio-x` |

Folders follow the first four levels. Variants and examples live inside a species folder.

## 3. Six rules

1. **Classify by what the work is.** Place a workflow by its profession and deliverable only. Tools are variants; agent patterns and autonomy are traits; industry, region and language are tags.
2. **One spot per workflow.** Use the keys in §4: at each level, the first matching row wins. If nothing fits, file it under `unplaced/` with a note. Once three unplaced workflows share a likely home, a maintainer can open a new class or phylum.
3. **Every species gets a permanent ID and a reference example.**
   - The ID (`AWF-####`) never changes, even if the workflow is renamed or moved. Links use the ID.
   - The first example run is the **reference example**: a dated folder with the context files (`CLAUDE.md`, playbook, story bible, prompt pack, n8n/Dify export), a short run log, and one input → output sample.
   - Without one, the species stays `draft`.
4. **Same species or not? Use the swap test.** Two submissions are the same species if a practitioner could swap one for the other without changing the deliverable, the human checkpoints or the autonomy level. If only the tools differ, add a variant. If only the prompt wording differs, add an example.
5. **First name wins.** If a new submission turns out to duplicate an existing species, it's merged in: its examples move over and its ID redirects to the older one.
6. **Status is one of four:** `draft` (no reference example yet) · `accepted` · `merged` (points to another ID) · `retired` (no new examples in 18 months and its tools are discontinued).

## 4. Placing a workflow (keys)

**Kingdom.** Look at the final deliverable and take the first row that matches.

| # | If the deliverable is… | Kingdom |
|---|---|---|
| 1 | Professional work in **research, law, finance, healthcare or education** (paper, legal memo, financial record, clinical note, lesson, grade) | **PRO** Professional services |
| 2 | **Customer-facing** marketing, sales outreach or support | **COM** Commerce & customers |
| 3 | A **technical system or its definition**: code, infrastructure, data, a product spec, design or prototype, an engineering design | **TEC** Technology & product |
| 4 | An **authored work** for an audience to read, watch or hear | **CRE** Creative & media |
| 5 | Anything else (internal operations, public sector, personal work) | **ORG** Organization & public |

**Phylum and class.** Within the kingdom, take the first phylum that matches, then pick the class.

| Kingdom | Phylum (first match wins) | Classes |
|---|---|---|
| **PRO** | 1. `HLT` Patient care or life-science R&D | `CLINDOC` · `RCM` · `CLINTRIAL` · `DRUGDISC` |
| | 2. `LEG` Legal advice, documents, filings, compliance | `CONTRACT` · `RESEARCH` · `LITIG` · `REG` · `DD` |
| | 3. `FIN` Transactions, books, financial models, investment views | `AP` · `CLOSE` · `FPA` · `INVEST` · `AUDIT` · `TAX` |
| | 4. `EDU` Teaching and assessing learners | `COURSE` · `ASSESS` · `TUTOR` · `LND` |
| | 5. `RES` Scholarly papers, reviews, grants | `LITREV` · `WRITE` · `ANALYSIS` · `GRANT` · `PEER` |
| **COM** | 1. `CSX` Helping an existing customer | `RESOLVE` · `QA` · `KB` · `CS` |
| | 2. `SAL` Pursuing specific accounts or deals | `PROSPECT` · `DEAL` · `RFP` · `REVOPS` |
| | 3. `MKT` One-to-many demand generation | `CONTENT` · `ADS` · `SOCIAL` · `LIFECYCLE` · `MKTRES` |
| **TEC** | 1. `ENG` Physical engineering, construction, manufacturing | `CAD` · `SIM` · `CODECOMP` · `MFG` |
| | 2. `PRD` Deciding *what* to build: specs, research, design, prototypes | `PM` · `UXR` · `UI` · `PROTO` · `DSYS` |
| | 3. `DAT` Queries, analyses, pipelines, models, evals | `ANALYTICS` · `DATAENG` · `DS` · `MLOPS` |
| | 4. `ITS` Running systems: incidents, infrastructure, security, IT help | `SRE` · `INFRA` · `SECOPS` · `APPSEC` · `HELPDESK` |
| | 5. `SWE` Application code or code review | `FEAT` · `MAINT` · `TEST` · `REVIEW` · `DEBUG` · `ARCH` |
| **CRE** | 1. `WRI` Final deliverable is text, including scripts and translations | `FICTION` · `SERIAL` (网文) · `SCREEN` · `NONFIC` · `JOURN` · `TECHW` · `TRANS` |
| | 2. `MED` Video, images or audio | `SHORTDRAMA` (live-action) · `AIGCVIDEO` (AI video, 漫剧) · `POST` · `DUB` · `AUDIO` · `GAMEART` |
| **ORG** | 1. `GOV` Public administration | `POLICY` · `CASEWORK` · `CIVIC` |
| | 2. `BIZ` Company functions: people, procurement, projects, strategy | `HR` · `PROC` · `PMO` · `STRAT` · `ADMIN` |
| | 3. `XFN` One person's own email, meetings, notes | `INBOX` · `MEET` · `PKM` |

**Edge cases the keys settle:**
- *Issue → agent-opened PR* is `SWE.FEAT`, not `SWE.REVIEW`, because the deliverable is a PR.
- *Technical writing* is `WRI.TECHW`. A README edited inside a PR is part of the PR and stays `SWE`.
- *Short-drama scripts* are `WRI.SCREEN` (the deliverable is text); the filmed or generated episodes are `MED`.

## 5. Traits and tags

These are searchable fields. They never decide placement.

| Field | Values |
|---|---|
| `autonomy` | `assist`: a person reviews each piece before the next step · `checkpointed`: the agent runs freely between fixed checkpoints · `sampled`: the agent runs end to end; people audit samples and exceptions |
| `checkpoints` | `plan` approve the brief or plan · `action` approve a side effect (send, push, pay) · `review` edit or approve a draft · `sample` spot-check a share of outputs · `sign-off` an accountable or licensed person signs · `handoff` the agent passes hard cases to a person |
| `patterns` | `chain` · `route` · `parallel` · `orch-workers` · `eval-opt` (from Anthropic's workflow patterns) · `auto-loop` · `role-crew` · `computer-use` |
| `evidence` | `A` public, detailed write-up by a practitioner or named organization · `B` vendor documentation or vendor-reported numbers · `C` community reports or anecdotes |
| `tags` | `industry`, `region`, `lang`, `risk` (`low` · `medium` for customer-facing or money · `high` for regulated: legal, clinical, hiring, credit) |

## 6. The shape line

Each species gets one line summarizing its steps, for quick scanning and comparison. It uses plain words and five symbols:

| Symbol | Meaning |
|---|---|
| `→` | next step |
| `(a ⟲ b)` | repeat a and b until b passes |
| `each X:` | do this for every X, in parallel |
| `a \| b` | alternative paths after a routing step |
| `🛑 type` | work stops until a person does this checkpoint |

**Example:** `read issue + code → plan → 🛑 plan → failing tests → (code ⟲ tests) → fresh review → 🛑 action → open PR → 🛑 review`

## 7. Coverage check

To show nothing is silently missing, every major group of the US occupation classification (SOC 2018) maps to a phylum or is marked as having no agent workflows yet. The Anthropic Economic Index already maps AI use to O*NET tasks, so records can optionally carry SOC codes for joining with labor data.

| SOC major group | Phyla | SOC major group | Phyla |
|---|---|---|---|
| 11 Management | BIZ, MKT, SAL, FIN | 33 Protective Service | GOV (sparse) |
| 13 Business & Financial Ops | FIN, BIZ, MKT | 35 Food Prep & Serving | *none yet* |
| 15 Computer & Mathematical | SWE, ITS, DAT | 37 Building & Grounds | *none yet* |
| 17 Architecture & Engineering | ENG | 39 Personal Care & Service | *none yet* |
| 19 Life, Physical & Social Science | RES, HLT | 41 Sales & Related | SAL |
| 21 Community & Social Service | GOV, HLT | 43 Office & Admin Support | CSX, FIN, BIZ, XFN |
| 23 Legal | LEG | 45 Farming, Fishing & Forestry | *none yet* |
| 25 Educational Instruction & Library | EDU, RES | 47 Construction & Extraction | ENG (sparse) |
| 27 Arts, Design, Entertainment, Media | WRI, MED, PRD | 49 Installation, Maintenance & Repair | ENG (sparse) |
| 29 Healthcare Practitioners | HLT | 51 Production | ENG.MFG |
| 31 Healthcare Support | HLT | 53 Transportation & Material Moving | *none yet* |
| | | 55 Military Specific | out of scope |

## 8. Record template

```yaml
id: AWF-0015                 # permanent (rule 3)
name: AI shot factory
kingdom: CRE
phylum: MED
class: AIGCVIDEO
deliverable: episode
shape: "script → shot list → 🛑 plan → character lock → each shot: (keyframes ⟲ critic) → (video ⟲ check) → voice + lip-sync → edit → 🛑 review → AI label → 🛑 sign-off → publish"
autonomy: checkpointed
checkpoints: [plan, review, sign-off]
patterns: [chain, parallel, eval-opt]
variants: [jimeng-kling-capcut, comfyui-flux-veo]
tags: {industry: [media], region: [CN], lang: [zh], risk: medium}
evidence: A
status: accepted              # draft | accepted | merged | retired
reference_example: examples/2026-03-reference/
inputs_from: [AWF-0014]       # optional: upstream workflow
merged_into: null
last_verified: 2026-11
```

Required: everything except `inputs_from`, `merged_into` and `tags`.

Sources for the claims above (Anthropic's workflow patterns, SOC 2018, the Anthropic Economic Index) are listed in the research report, §7.
