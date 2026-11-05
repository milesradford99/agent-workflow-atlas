# Phase 1 Report (v3): A Simple Classification of Agentic Work

**Version:** v3 · 2026-11-05
**What changed from v2:** the classification keeps the biology idea but drops most of the machinery.
- 4 levels instead of 7.
- 6 rules instead of a 12-article code.
- A plain-word "shape" line instead of a stage formula with 12 codes and 5 operators.
- 3 evidence grades and 4 statuses.

The detailed v2 is kept in [archive/phase1-report-v2.md](archive/phase1-report-v2.md). Workflows, sources and the verification log (§6) are unchanged; citations use [n] → §7.

---

## 0. What counts as a workflow

A workflow is listed only if it meets **all four** criteria:

| # | Criterion | Excludes |
|---|---|---|
| C1 | **Multi-step**: ≥3 model or tool steps with state carried between them | One-shot prompts |
| C2 | **Acts on real things** (files, repos, databases, documents, media, external systems) through tools, MCP, APIs, or a UI | Advice-only chat |
| C3 | **Named human checkpoints**: it says where people approve, edit, or sample | "Let the AI handle it" |
| C4 | **Reproducible**: at least one dated example run that someone else can rerun (rule 3) | "Use AI to brainstorm" |

---

## 1. The Classification System

### 1.1 The idea

Biology sorts animals by **ancestry**, not by what they happen to have in common. Bats and birds both fly, but a bat is a mammal. We sort workflows the same way:

- **Ancestry = the profession and the deliverable.** A contract-review agent descends from lawyers reviewing contracts. That decides where it lives in the tree.
- **Shared tricks are traits, not branches.** Generate-then-critique loops, parallel workers and autonomy levels appear in law, film and software alike, like wings. They are tags you can search by, never folders.
- **Tools are the bottom layer.** Claude Code vs. Codex, or Kling vs. Veo, are *variants* of the same workflow, so tool churn never moves anything.

Four more ideas come from biology, each turned into one simple rule (§1.3): permanent IDs, a reference example for every entry, one name per workflow with duplicates merged, and a key that places each workflow in exactly one spot.

### 1.2 Levels

| Level | Question it answers | Count | Example |
|---|---|---|---|
| **Kingdom** | What broad field is the deliverable in? | 5 | `CRE` Creative & Media |
| **Phylum** | Which profession? | 18 | `MED` Media Production |
| **Class** | Which discipline within it? | listed in §1.4 | `AIGCVIDEO` AI-generated video |
| **Species** | Which specific workflow? | open | *AI shot factory* · `AWF-0015` |
| *Variant* | Which toolchain? | open | `jimeng-kling-capcut` |
| *Example* | Which dated real run shows it working? | open | `2026-03-studio-x` |

Folders follow the first four levels. Variants and examples live inside a species folder.

### 1.3 Six rules

1. **Classify by what the work is.** Place a workflow by its profession and deliverable only. Tools are variants; agent patterns and autonomy are traits; industry, region and language are tags.
2. **One spot per workflow.** Use the keys in §1.4: at each level, the first matching row wins. If nothing fits, file it under `unplaced/` with a note. Once three unplaced workflows share a likely home, a maintainer can open a new class or phylum.
3. **Every species gets a permanent ID and a reference example.**
   - The ID (`AWF-####`) never changes, even if the workflow is renamed or moved. Links use the ID.
   - The first example run is the **reference example**: a dated folder with the context files (`CLAUDE.md`, playbook, story bible, prompt pack, n8n/Dify export), a short run log, and one input → output sample.
   - Without one, the species stays `draft`.
4. **Same species or not? Use the swap test.** Two submissions are the same species if a practitioner could swap one for the other without changing the deliverable, the human checkpoints or the autonomy level. If only the tools differ, add a variant. If only the prompt wording differs, add an example.
5. **First name wins.** If a new submission turns out to duplicate an existing species, it's merged in: its examples move over and its ID redirects to the older one.
6. **Status is one of four:** `draft` (no reference example yet) · `accepted` · `merged` (points to another ID) · `retired` (no new examples in 18 months and its tools are discontinued).

### 1.4 Placing a workflow (keys)

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

### 1.5 Traits and tags

These are searchable fields. They never decide placement.

| Field | Values |
|---|---|
| `autonomy` | `assist`: a person reviews each piece before the next step · `checkpointed`: the agent runs freely between fixed checkpoints · `sampled`: the agent runs end to end; people audit samples and exceptions |
| `checkpoints` | `plan` approve the brief or plan · `action` approve a side effect (send, push, pay) · `review` edit or approve a draft · `sample` spot-check a share of outputs · `sign-off` an accountable or licensed person signs · `handoff` the agent passes hard cases to a person |
| `patterns` | `chain` · `route` · `parallel` · `orch-workers` · `eval-opt` (from Anthropic's workflow patterns [1]) · `auto-loop` · `role-crew` · `computer-use` |
| `evidence` | `A` public, detailed write-up by a practitioner or named organization · `B` vendor documentation or vendor-reported numbers · `C` community reports or anecdotes |
| `tags` | `industry`, `region`, `lang`, `risk` (`low` · `medium` for customer-facing or money · `high` for regulated: legal, clinical, hiring, credit) |

### 1.6 The shape line

Each species gets one line summarizing its steps, for quick scanning and comparison. It uses plain words and five symbols:

| Symbol | Meaning |
|---|---|
| `→` | next step |
| `(a ⟲ b)` | repeat a and b until b passes |
| `each X:` | do this for every X, in parallel |
| `a \| b` | alternative paths after a routing step |
| `🛑 type` | work stops until a person does this checkpoint |

**Example:** `read issue + code → plan → 🛑 plan → failing tests → (code ⟲ tests) → fresh review → 🛑 action → open PR → 🛑 review`

### 1.7 Coverage check

To show nothing is silently missing, every major group of the US occupation classification (SOC 2018 [30]) maps to a phylum or is marked as having no agent workflows yet. The Anthropic Economic Index already maps AI use to O*NET tasks [31], so records can optionally carry SOC codes for joining with labor data.

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

### 1.8 Record template

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

### 1.9 What v3 dropped from v2, and why

| Dropped | Why it's not needed |
|---|---|
| Order, Family and Genus levels | Few classes will hold more than a handful of species. The deliverable is kept as a field, and the shape line shows structural similarity. |
| 12-code stage formula and grammar | Hard to write and review. The shape line is plain words with five symbols. |
| 7 gate codes (`G-spec`, `G-plan`…) | Merged into 6 plain checkpoint words. |
| L1–L5 autonomy | L1 and L5 had no entries. The three remaining levels are named. |
| 4 evidence grades and a separate adoption status | Three evidence grades are enough. Adoption is described in the landscape (§2), not tracked per entry. |
| Latin-style two-part names, type species, synonym ranks | A plain name plus a permanent ID does the same job. |

---

## 2. Cross-Industry Landscape (verified November 2026)

| Phylum | Maturity | Species in this report | Typical autonomy | Verified signals |
|---|---|---|---|---|
| SWE | Mainstream | Plan-gated build, Fan-out codemod, Delegated PR | checkpointed locally, sampled when async | The vendor-documented explore → plan → code → commit loop [2]. `@claude` GitHub Actions [3] and the Copilot coding agent, which works from issue → draft PR [4]. Airbnb migrated ~3.5k files in about 6 weeks [5]. AGENTS.md has been under the Linux Foundation's AAIF since December 2025 [6]. |
| ITS | Growing | Triage then remediate, Alert enrich and adjudicate | assist or checkpointed for writes | Vendor-documented (B); no independent benchmark found |
| DAT | Growing | Governed query | checkpointed | Vendor-documented (B) |
| PRD | Growing | Feedback to prototype, Design to code | checkpointed | Figma MCP server exposes design context, variables, and Code Connect mappings [7] |
| RES | Growing | Screening funnel, Reviewer-response revision | checkpointed + sign-off | ICMJE: disclose AI use; chatbots can't be authors [8]. LLM screening sensitivity varies widely (pooled 0.73 in one meta-analysis; ensembles report ~96% in preprints) [9] |
| WRI | Growing (high volume in CN) | Bible-driven novel, Daily web serial, Beat-to-scene screenplay, Hook-cadence drama script | assist or checkpointed | Story Bible and Codex tools [10]. KDP requires disclosure of AI-*generated* content, though not AI-*assisted* content [11]. 番茄 has disputed AI-training terms and cracked down on low-quality AI text [12]. WGA MBA AI terms [13]. |
| MED | Mainstream in CN micro-drama | AI shot factory, Live-action assist, Dubbing pipeline | checkpointed or sampled | AI labeling rules in force since September 1, 2025 [15]. NRTA tiered review of micro-dramas [14]. AI 漫剧 cost reportedly fell from ¥2–5k to ¥1–2.5k per minute [16]. Kling multi-image reference for consistency [17]. ReelShort and DramaBox each made ~$120–130M in IAP in Q1 2025 [18]. |
| MKT | Growing | Cluster-brief-draft content, Ad variant matrix | checkpointed | Google's "scaled content abuse" spam policy (March 2024) targets mass-generated pages with no added value [19] |
| SAL | Growing | Research-then-personalize outbound | checkpointed | Clay's Claygent research and waterfall enrichment feed sequencers [20] |
| CSX | Mainstream | Procedure agent | sampled + handoff | Decagon AOPs: natural language compiled into workflows, with sensitive steps run in code [21]. Fin claims a 76% average resolution rate, while independent observers report 38–53% [22]. |
| FIN | Growing | Invoice extract-match-route, Event-driven model update | checkpointed or sampled | Claude for Financial Services (July 2025) and the Claude for Excel beta (October 2025) [23] |
| LEG | Growing | Playbook contract review, Grounded legal memo | assist or checkpointed + sign-off | *Mata v. Avianca* sanctions, June 22, 2023 [24] |
| HLT | Mainstream (ambient documentation) | Ambient scribe | checkpointed + sign-off | Microsoft Dragon Copilot (March 2025) [25]. Abridge inside Epic with "Linked Evidence" [26]. |
| EDU | Growing | Backward-design course, Anchor-calibrated grader | assist or checkpointed | Not independently verified (B/C) |
| BIZ | Growing | Source-screen-schedule hiring, Issue-tree research | checkpointed | LinkedIn Hiring Assistant, global English release (2025) [29]. NYC LL144 [27]. EU AI Act employment obligations: dates are unsettled [28]. |
| ENG, GOV | Early | (none yet) | assist | Not enough real examples yet; left empty rather than invented |
| XFN | Growing | Daily inbox triage | assist | Not independently verified (A/C) |

**Five patterns that show up across professions:**
1. **A persistent context file carries the know-how.** `CLAUDE.md`/`AGENTS.md`, playbooks, story bibles, AOPs and procedures all play this role [2][6][10][21]. Decagon explicitly frames AOPs as SOPs written for agents [21]. That's why rule 3 makes them part of the reference example.
2. **Automated checks run before the human checkpoint.** Mature workflows put tests, citation checkers, 3-way matching or source links ahead of human review [5][26].
3. **Checkpoints sit where actions can't be undone:** send, merge, pay, file, publish, sign.
4. **Per-item fan-out is the productivity multiplier:** per file [5], per shot, per clause, per account.
5. **Regulated professions always end in a sign-off.** A licensed person stays the accountable author [8][13][24][25].

---

## 3. Workflow Descriptions (SOPs)

Each entry gives the name and ID, its **place** (Kingdom › Phylum › Class), autonomy, status and evidence, the **shape** line, then **Input → Roles/Tools → Steps → Checkpoints → Output**. 🛑 marks a human checkpoint.

### Kingdom TEC

#### Plan-gated build · AWF-0001
`TEC › SWE › FEAT` · checkpointed · accepted · evidence A/B [2]
**Shape:** `read issue + code → plan → 🛑 plan → failing tests → (code ⟲ tests) → fresh review → 🛑 action → open PR → 🛑 review → update context file`
**Traits:** `auto-loop, orch-workers` · **Variants:** `claude-code` · `codex-cli` · `cursor-agent`

- **Input:** an issue with acceptance criteria; a repo with `CLAUDE.md`/`AGENTS.md` (build, test, and lint commands, conventions, no-go areas); a working test suite.
- **Roles/Tools:** the lead agent (read, edit, allow-listed shell); read-only explorer sub-agents; a verifier (formatter and lint hooks, tests, typecheck, browser screenshots for UI); a fresh-context reviewer sub-agent.

**Steps**
1. The agent reads the context file, the issue (`gh issue view` or the tracker's MCP), and relevant code. Explorers fan out to map affected modules.
2. In plan mode (read-only), the agent writes a plan: files to touch, approach, test strategy, open questions [2]. 🛑 **Plan**: this is the highest-leverage correction point.
3. Write failing tests that encode the acceptance criteria and confirm they fail.
4. Implement in increments, with targeted tests and typecheck after each one. Loop on the failure output, and cap iterations before escalating.
5. A fresh-context reviewer checks the diff against the spec: edge cases, dead code, security.
6. For UI changes, run the dev server, take a screenshot, and compare with the design.
7. 🛑 **Action**: commit, push, and open the PR, unless these were pre-authorized.
8. 🛑 **Review**: a human reviews the PR and CI.
9. Write recurring corrections back into the context file.

**Output:** a reviewed PR with tests, and an updated context file.
**Failure modes → guards:** the agent edits tests to make them pass → forbid test edits after the tests are written. Scope creep → flag any file changed outside the plan's list. Context saturation → clear context between tasks and persist the plan to a file [2].
**Close relative:** a version that asks approval for every edit (`assist`) is a separate species by the swap test.

#### Fan-out codemod · AWF-0002
`TEC › SWE › MAINT` · sampled · accepted · evidence A [5]
**Shape:** `pilot on 10–20 files → 🛑 plan → each file: (refactor ⟲ lint → types → tests) → add context to failures → each failure: (retry ⟲ checks) → 🛑 sample → batch PRs → 🛑 review`
**Traits:** `parallel, eval-opt, chain` · **Variants:** `claude-code-headless` · `agent-sdk` · `codex-exec`
**Reference example:** Airbnb's Enzyme → React Testing Library migration [5]. About 3.5k test files were migrated in roughly 6 weeks, against an estimated 1.5 years by hand. A per-file step state machine retried with error feedback. About 75% of files passed within hours, and the remaining ~900 got richer context and more retries. Fewer than 100 were finished by hand.

**Steps**
1. Pilot on 10–20 representative files and tune the prompt and examples. 🛑 **Plan**: freeze the prompt, few-shot examples, and success definition.
2. Run a per-file state machine: refactor → fix lint → fix types → fix tests. Each step is an LLM call that receives its validator's output. Run N parallel headless workers (`claude -p`, Codex exec, Agent SDK), each with a retry budget.
3. Long tail: add context (sibling files, component source, more examples) and rerun. Cluster the failures and patch the prompt [5].
4. 🛑 **Sample**: check semantic fidelity on a random sample, beyond "tests pass."
5. Batch PRs by owner. 🛑 **Review**: code owners review. Hand-fix the residue.

**Output:** a migrated codebase, a failure log, and a reusable migration prompt pack.

#### Delegated PR · AWF-0003
`TEC › SWE › FEAT` · sampled · accepted · evidence B [3][4]
**Shape:** `🛑 plan (label suitable issues) → agent reads issue + repo → (code ⟲ tests) → draft PR → (bot review ⟲ fixes) → 🛑 action (run CI) → 🛑 review → merge`
**How it differs from Plan-gated build:** no planning checkpoint mid-run; the issue *is* the plan, and the agent runs in the cloud.
**Variants:** `copilot-coding-agent` · `claude-code-action` · `codex-cloud` · `devin` · `jules`

**Steps**
1. 🛑 **Plan**: only self-contained, testable issues are labeled for agents.
2. Dispatch by assigning the issue to Copilot, which opens a draft PR and runs in an Actions-based environment configured by `.github/workflows/copilot-setup-steps.yml` [4]. Alternatively, comment `@claude`, which triggers Claude Code GitHub Actions [3].
3. The agent implements, runs tests, and pushes. Later instructions go as PR comments, because Copilot doesn't see issue comments added after assignment [4].
4. A review bot comments, and the agent addresses the comments for 1–2 rounds.
5. 🛑 **Action**: a human clicks "Approve and run workflows" so CI runs on agent PRs [4].
6. 🛑 **Review**: human review and merge.

**Output:** merged PRs. Track the merge rate per issue label to tune what gets dispatched.

#### Triage then remediate · AWF-0004
`TEC › ITS › SRE` · checkpointed · accepted · evidence B
**Shape:** `alert → route to runbook → each signal: investigate (metrics, logs, traces, deploys) → ranked hypotheses → 🛑 action → runbook step → check SLO → draft postmortem → 🛑 review → update runbook`

**Steps**
1. An alert starts the agent, which routes by service tag to the matching runbook.
2. Read-only investigation runs in parallel: the error spike, deploys in the window, exemplar traces, and the suspect diff.
3. Post ranked hypotheses with evidence links to the incident channel.
4. 🛑 **Action**: the on-call engineer approves a specific runbook command (rollback, scale, restart).
5. Verify recovery against the SLO.
6. Draft the postmortem. 🛑 **Review**: the incident owner edits it, especially root cause and action items.
7. Update the runbook.

**Guard:** write tools are restricted to an allow-list of runbook commands, enforced in code.

#### Alert enrich and adjudicate · AWF-0005
`TEC › ITS › SECOPS` · sampled · accepted · evidence B
**Shape:** `alert → each source: enrich (threat intel, identity, EDR) → verdict + evidence → benign: auto-close | suspicious: 🛑 handoff · weekly 🛑 sample`

**Steps**
1. Normalize the alert.
2. Run enrichment lookups in parallel.
3. Investigate as an analyst would.
4. Return a verdict with confidence and evidence.
5. Auto-close benign alerts with the evidence attached.
6. 🛑 **Handoff**: send everything else to tier 2 as a prepared case.
7. 🛑 **Sample**: QA auto-closed alerts weekly.

**Metric:** analyst minutes per alert.

#### Governed query · AWF-0006
`TEC › DAT › ANALYTICS` · checkpointed · accepted · evidence B
**Shape:** `question → load metric definitions + schema → (SQL ⟲ sanity checks) → chart + summary → 🛑 review → 🛑 sign-off → publish → save to golden queries`

**Steps**
1. Map business terms to governed metric definitions. If a term is ambiguous, ask instead of guessing.
2. Inspect the schema and sample rows.
3. Draft SQL, preferring the semantic layer.
4. Validate: sanity bounds, join fan-out (did row counts explode?), and reconciliation with a canonical dashboard total.
5. Chart the result and attach the SQL.
6. 🛑 **Review**: an analyst reviews the logic.
7. 🛑 **Sign-off**: required before the result goes to execs.
8. Save the verified query to the golden set for reuse.

#### Feedback to prototype · AWF-0007
`TEC › PRD › PROTO` · checkpointed · accepted · evidence A
**Shape:** `feedback → theme clusters + quotes → 🛑 plan → PRD → red-team critique → each variant: prototype → iterate → 🛑 review → 5 user tests → back to feedback`

**Steps**
1. Cluster tickets, call transcripts, and NPS verbatims into themes, each with counts and source-linked quotes.
2. 🛑 **Plan**: the PM picks the problem to solve.
3. Draft the PRD: problem, users, non-goals, metrics, stories, edge cases. A critic red-teams it ("what would engineering push back on?").
4. Build 2–3 prototype variants (v0, Lovable, Bolt, Figma Make, Claude artifacts) from the PRD plus design tokens.
5. Iterate.
6. 🛑 **Review**: design review.
7. Run 5 user tests and feed the transcripts back to step 1.

**Output:** the PRD and prototype become the input to AWF-0001 or AWF-0008.

#### Design to code · AWF-0008
`TEC › PRD › DSYS` · checkpointed · accepted · evidence B [7]
**Shape:** `frame link → load design context, tokens, component map → (code ⟲ screenshot diff) → 🛑 review → PR`

**Steps**
1. Pull the frame's design context, variables (color, spacing, typography), and Code Connect mappings through the Figma MCP server [7].
2. Reuse mapped code components instead of re-creating them.
3. Use tokens only, with no hardcoded values.
4. Render, take a screenshot, compare with the Figma screenshot, and loop.
5. 🛑 **Review**: designer review in a preview build.

**Output:** a PR. Token gaps are reported back to the design-system team.

### Kingdom PRO

#### Screening funnel · AWF-0009
`PRO › RES › LITREV` · checkpointed · accepted · evidence A [8][9]
**Shape:** `PICO question → search strings → 🛑 plan → each database: search → dedupe → each record: two independent screeners → conflicts and includes → 🛑 sample → each paper: extract with quote + page → 🛑 review → synthesis → check citations → 🛑 sign-off`

| Role | Tools |
|---|---|
| Search strategist | LLM + PubMed, Scopus, OpenAlex, and Semantic Scholar APIs |
| Screeners ×2 (independent) | Elicit, ASReview, Rayyan AI, or a custom classifier |
| Extractor | PDF parser (e.g. GROBID) → LLM into a fixed schema, quoting the source span |
| Verifier | Crossref DOI resolution + Zotero |

**Steps**
1. Draft Boolean and MeSH search strings. 🛑 **Plan**: a librarian or PI approves, then the protocol is registered (PROSPERO, OSF).
2. Search, deduplicate, and log counts for the PRISMA flow diagram.
3. Two independent LLM screeners, each giving a reason per decision. **Tune for sensitivity, not accuracy.** A missed eligible study biases the result, and published sensitivity varies widely: a pooled 0.73 in one meta-analysis versus ~96% for dual-model ensembles in recent preprints [9]. 🛑 **Sample**: calibrate against a human-screened set (sensitivity, Cohen's κ) before trusting the screeners at scale. Humans resolve all conflicts.
4. Full-text screening follows the same pattern with closer human involvement.
5. Extraction: every field quotes its source span and page. 🛑 **Review**: humans verify 100% of the numbers that feed the meta-analysis.
6. Synthesis and draft: risk-of-bias table, meta-analysis script, narrative.
7. Resolve every reference and flag unsupported claims.
8. 🛑 **Sign-off**: authors take responsibility and disclose AI use. Under ICMJE, chatbots can't be authors and use must be disclosed [8].

**Output:** a PRISMA diagram, extraction dataset, draft manuscript, and an audit log of AI decisions.

#### Reviewer-response revision · AWF-0010
`PRO › RES › WRITE` · assist · accepted · evidence A
**Shape:** `reviews → response matrix → 🛑 plan → each comment: (edit or reanalysis ⟲ compile, rerun, cite check) → latexdiff + letter → 🛑 review → 🛑 sign-off`

**Steps**
1. Parse the reviewer comments into `response.md` (comment → planned change → location).
2. 🛑 **Plan**: the authors decide accept, rebut, or partial for each comment.
3. Run sub-agents per comment: text edits, re-run analyses and regenerate figures, add citations.
4. Compile and produce a `latexdiff` version.
5. Verify that every number matches the regenerated outputs and every citation key resolves.
6. Draft the response letter.
7. 🛑 **Review + sign-off**: the authors edit rebuttals for tone and substance.

#### Grounded legal memo · AWF-0025
`PRO › LEG › RESEARCH` · assist · accepted · evidence A [24]
**Shape:** `issue + jurisdiction → 🛑 plan → (search grounded database ⟲ draft IRAC memo) → each citation: verify exists, quote, holding, still good law → 🛑 sign-off`

**Steps**
1. Frame the issue and jurisdiction. 🛑 **Plan**.
2. Search primary law in a grounded database (Westlaw/CoCounsel, Lexis+ AI, Harvey), not the open web.
3. Draft an IRAC memo with pinpoint cites.
4. **Run a separate verification pass on every citation**, including a citator check.
5. 🛑 **Sign-off**: the attorney reads every authority cited.

**Why the citation check is mandatory:** in *Mata v. Avianca* (S.D.N.Y., sanctions June 22, 2023), counsel submitted ChatGPT-fabricated opinions with fake quotes and citations [24].

#### Playbook contract review · AWF-0024
`PRO › LEG › CONTRACT` · checkpointed · accepted · evidence A
**Shape:** `contract → classify type → load playbook → each clause: compare to position (green/yellow/red) → tracked changes + comments → consistency check → 🛑 review → 🛑 sign-off → send`
**Variants:** `harvey` · `spellbook` · `luminance` · `claude-playbook-skill`

**Steps**
1. Classify the agreement and load the matching playbook (standard positions, fallbacks, walk-away points per clause).
2. Segment the clauses, map each to a playbook entry, and flag missing clauses.
3. Analyze clauses in parallel for deviation.
4. Generate Word tracked changes with margin comments explaining each change.
5. Check internal consistency: defined terms, cross-references, liability caps vs. indemnities.
6. 🛑 **Review**: an attorney reviews yellow and red items.
7. 🛑 **Sign-off**: the attorney sends.

#### Invoice extract-match-route · AWF-0022
`PRO › FIN › AP` · sampled · accepted · evidence B
**Shape:** `invoice → extract fields with confidence → check vendor, duplicates, bank details → 3-way match → GL coding → matched: queue for payment | exception: 🛑 handoff → 🛑 sign-off on payment run`

**Rules:** a bank-detail change *always* goes to a person, because it's a fraud signal. Payment approval follows the delegation-of-authority matrix. The full audit trail is kept for SOX.

#### Event-driven model update · AWF-0023
`PRO › FIN › INVEST` · checkpointed · accepted · evidence A/B [23]
**Shape:** `load consensus + guidance → new release, filing or transcript → each KPI: extract with citation → compare to model → update Excel drivers with per-cell comments → transcript themes → note → 🛑 review → 🛑 sign-off (compliance) → publish`
**Variants:** `claude-excel` (Claude for Excel beta since October 2025 [23]) · `hebbia` · `alphasense` · `rogo`

#### Ambient scribe · AWF-0026
`PRO › HLT › CLINDOC` · checkpointed · accepted · evidence A [25][26]
**Shape:** `🛑 plan (patient consent) → record visit → diarized transcript → load EHR context → note + codes + patient summary → link each sentence to transcript → 🛑 review → 🛑 sign-off → file to EHR`

**Steps**
1. 🛑 **Plan**: patient consent to recording.
2. Ambient capture in the room or on a phone.
3. Diarized transcription, then a structured note in the specialty template.
4. Each note phrase links to its source audio or transcript. Abridge calls this "Linked Evidence," inside Epic Haiku → Hyperdrive [26].
5. 🛑 **Review**: the clinician edits.
6. 🛑 **Sign-off**: the clinician signs and is the legal author.

**Variants:** `abridge-epic` [26] · `dragon-copilot` (launched March 2025; combines Dragon Medical One dictation with DAX ambient [25]) · `nabla` · `ambience`
**Tags:** risk `high`, HIPAA, BAA required.

#### Backward-design course · AWF-0027
`PRO › EDU › COURSE` · assist · accepted · evidence A
**Shape:** `standards → objectives by Bloom's level → 🛑 plan → assessments + rubrics → module plan → 🛑 plan → each lesson: materials + differentiated versions → check every objective is assessed, accuracy, accessibility → 🛑 review → LMS import`

#### Anchor-calibrated grader · AWF-0028
`PRO › EDU › ASSESS` · checkpointed · accepted · evidence A
**Shape:** `🛑 plan (rubric + 5–10 human-graded anchors) → (calibration grades ⟲ agreement within 1 point) → each submission: score + evidence quote + feedback → low confidence: 🛑 sample → 🛑 sign-off → release`

Students can always request human review.

### Kingdom CRE

#### Bible-driven novel draft · AWF-0011
`CRE › WRI › FICTION` · assist · accepted · evidence A/B [10]
**Shape:** `premise + voice samples → story bible via interview → 🛑 plan → beats → chapters → scene cards → 🛑 plan → each scene in order: load card, bible, summary, last ~2k words → draft → continuity check → style check → 🛑 review → update bible and summary`

| Role | Responsibility | Variants |
|---|---|---|
| Bible keeper | Characters, places, timeline, rules | Sudowrite Story Bible, a guided pipeline from braindump → synopsis → outline → scenes [10]; NovelCrafter Codex, wiki entries linked into the manuscript with bring-your-own model [10]; Markdown vault + Claude Code |
| Outliner | Beats → scene cards (goal, conflict, outcome, POV, information revealed) | Same |
| Drafter | Scene prose | LLM with long context |
| Continuity checker | Fresh context; flags contradictions (eye color, travel time, premature knowledge) | Separate agent |
| Line editor | Style sheet: banned clichés, POV, tense | Critic agent |

**Checkpoints:** 🛑 the author owns the bible and the outline (both **Plan**), where most creative control is exercised. The author also rewrites every chapter (**Review**).
**Tag note:** Amazon KDP requires disclosure of AI-*generated* text, images, and translations, even when heavily edited afterward. Purely AI-*assisted* work doesn't need disclosure [11]. Record which applies in each example.

#### Daily web serial · AWF-0012
`CRE › WRI › SERIAL` · checkpointed · **draft** · evidence C [12]
**Shape:** `study top-ranked works (hooks, 爽点 cadence) → 大纲 → 卷纲 → 细纲 (payoff every 1–3 chapters) → 🛑 plan → each day: load 细纲, character sheet, previous summary → ~2,000-字 chapter → check names, power levels, timeline → 🛑 review → publish → read 段评 comments → adjust`
**How it differs from Bible-driven novel draft:** the deliverable is a daily chapter stream, not a manuscript, and reader comments feed back into every cycle.
**Tags:** `lang:zh`. Platform risk: 番茄小说 faced an author boycott in 2024 over an AI-training supplementary agreement and added a way to opt out. In February 2025 it banned accounts for low-quality "water" (水文) content [12]. No explicit 起点 AI-content rule was found (§6). Status stays `draft` until a reference example with evidence A or B is added.

#### Beat-to-scene screenplay · AWF-0013
`CRE › WRI › SCREEN` · assist · accepted · evidence A [13]
**Shape:** `logline → variants → critique → 🛑 plan → treatment → beat sheet → scene list → 🛑 plan → (draft ⟲ coverage notes + TTS table read + 🛑 review) → 🛑 sign-off → Final Draft or Highland`
**Compliance (WGA 2023 MBA, in effect through May 1, 2026; check successor terms):**
- AI-generated material is not "literary material" or "source material."
- Companies must disclose AI-generated material given to writers.
- Writers can't be required to use AI, but may choose to with company consent [13].

Log AI-assisted portions in each example.

#### Hook-cadence drama script · AWF-0014
`CRE › WRI › SCREEN` · checkpointed · accepted · evidence A/C
**Shape:** `study top dramas (hooks, 反转 density, 卡点 placement) → core setup → 🛑 plan → 60–100 one-line episodes, each ending on a cliffhanger → 🛑 plan → each batch of 10: draft episodes → each episode: check 3-second hook, end cliffhanger, line length, cast and location budget → 🛑 review (head writer rewrites eps 1–10 + paywall ep) → content-rule check → 场次表`
**How it differs from Beat-to-scene screenplay:** the deliverable is a 60–100-episode series with a paywall episode to pace toward, and episodes are drafted in parallel batches.
**Tags:** domestic releases go through the NRTA's tiered review, with three categories by budget and subject. Platforms may not carry micro-dramas without a license or filing number [14]. **Feeds into:** AWF-0015, AWF-0016.

#### AI shot factory · AWF-0015
`CRE › MED › AIGCVIDEO` · checkpointed · accepted · evidence A [15][16][17]
**Shape:** `script → shot list → 🛑 plan → character lock → each shot: (keyframes ⟲ critic) → (video ⟲ check) → voice + lip-sync → edit → 🛑 review → AI label → 🛑 sign-off → publish`

| Step | Tools (CN / global) |
|---|---|
| Shot list (分镜: number, framing, camera move, action, dialogue, duration) | Doubao, DeepSeek, Claude, GPT |
| Character lock | 即梦 / Midjourney references; ComfyUI + per-character LoRA; Kling multi-image reference, 1–4 references per generation [17] |
| Keyframes | 即梦/Seedream, Flux, Midjourney |
| Motion | 可灵 Kling, 海螺 Hailuo, Vidu, Seedance, Veo, Runway |
| Voice and lip-sync | MiniMax, 火山引擎 TTS, ElevenLabs; lip-sync tools or native audio-video models |
| Assembly | 剪映/CapCut, Premiere |

**Steps**
1. Script → 20–40-shot list. 🛑 **Plan**: the director approves the shot list and style frames.
2. Lock the characters. Practitioners generate front, side, and back views plus expression sheets, and use them as references in every later generation [16].
3. Generate 4 keyframe candidates per shot in parallel. A vision-model critic filters, then a human selects.
4. Image → video per shot. Re-roll on morphing or physics breaks.
5. Generate voice per line with emotion tags, then lip-sync.
6. Assemble and check the first-3-seconds hook.
7. 🛑 **Review**: the director lists re-rolls (loop back to step 3 or 4).
8. 🛑 **Sign-off**: compliance and labeling. CN rules require explicit and implicit labels on AI-generated content (in force since September 1, 2025 [15]). The draft 微短剧 regulation also requires a label in a visible position in every AI-generated episode [14].

**Reported economics (B):** a brokerage report citing Ocean Engine data puts traditional 漫剧 at ¥2–5k per minute and AI-assisted production at ¥1–2.5k. It also reports one company cutting 11 production stages to 5 [16].
**Metrics to record in examples:** usable-shot rate per generation, cost per finished minute, hours per episode.

#### Live-action assist · AWF-0016
`CRE › MED › SHORTDRAMA` · assist · accepted · evidence A/C
**Shape:** `script (from AWF-0014) → 场次表, cast, props, locations, 7–10-day schedule → 🛑 plan → previs keyframes → human shoot → captions, rough cut, color, VFX touch-ups → 🛑 review → each hook: ad cut (20–50) → 投流 test → keep best by ROI → 🛑 sign-off → publish`
**How it differs from AI shot factory:** people shoot the footage. AI covers pre- and post-production, plus a batch of ad cuts tested against real spend.

#### Dubbing pipeline · AWF-0017
`CRE › MED › DUB` · sampled · accepted · evidence A/B [18]
**Shape:** `episode + script → diarized ASR aligned to script → per-series glossary + cultural notes → 🛑 plan → each language: (translate ⟲ fits line duration) → voice-clone TTS → lip-sync → subtitles → 🛑 sample (native QA: eps 1–10 in full, then sampled) → 🛑 sign-off → publish`
**Tags:** overseas (出海) apps. ReelShort and DramaBox made roughly $130M and $120M in IAP in Q1 2025 [18]. Vendor claims for AI dubbing throughput (e.g. "120 minutes in 4–5 hours") are evidence B and unverified.

### Kingdom COM

#### Cluster-brief-draft content · AWF-0018
`COM › MKT › CONTENT` · checkpointed · accepted · evidence A [19]
**Shape:** `seed topics → SEO API → keyword clusters → 🛑 plan → each article: top-10 SERP → brief → product docs + SME input → draft → fact, voice, link check → 🛑 review → CMS → check rank at 30/90 days → refresh`
**Constraint:** Google's March 2024 "scaled content abuse" policy targets mass-generated pages made mainly to rank, without adding value, whether automated or not [19]. That's why the SME-input step and editor review are part of this species, not optional.

#### Ad variant matrix · AWF-0019
`COM › MKT › ADS` · checkpointed · accepted · evidence B
**Shape:** `ad libraries, reviews, tickets → angle × hook × format × persona matrix → 🛑 plan → each cell: copy, static, avatar UGC video → claims + brand-safety check → 🛑 review → bulk upload → weekly: read performance → cut losers → next matrix`

#### Research-then-personalize outbound · AWF-0020
`COM › SAL › PROSPECT` · checkpointed · accepted · evidence B [20]
**Shape:** `ICP → build list → each account: waterfall enrichment → research agent answers fixed questions with source URLs → score and tier → each contact: first line from research only → 🛑 plan (20-row sample) → 🛑 sample (5–10%) → 🛑 action → launch sequence → route replies`
**Practitioner pattern:** run cheap enrichment first, and spend agent-research credits (Claygent) only on accounts that fit the ICP [20].

#### Procedure agent · AWF-0021
`COM › CSX › RESOLVE` · sampled · accepted · evidence A/B [21][22]
**Shape:** `load KB + procedures → each message: route → info: answer | transaction: authenticate → 🛑 action (limits in code) → tool call | sensitive: 🛑 handoff → 🛑 sample (QA) → KB-gap clusters → new articles`

**Steps**
1. Rewrite tribal knowledge as natural-language procedures with explicit conditions and limits. Decagon AOPs compile these into workflows where refunds and identity checks run in code [21]. Intercom Fin Procedures and Sierra journeys are equivalent variants.
2. Route each message by intent.
3. Authenticate before any account action.
4. 🛑 **Action**: limits are enforced in code, not in the prompt.
5. 🛑 **Handoff**: hand off with a summary.
6. 🛑 **Sample**: QA scores every conversation; humans review flagged and random ones.
7. Turn weekly KB-gap clusters into new articles.

**Metric caution:** resolution rates aren't defined the same way across vendors. Fin's site reportedly claims a 76% average, while independent and small-business tests cluster at 38–53% [22]. Decagon customer figures above 70% come from an analyst write-up [21]. All are evidence B.

### Kingdom ORG

#### Source-screen-schedule hiring · AWF-0029
`ORG › BIZ › HR` · checkpointed · accepted · evidence B [27][28][29]
**Shape:** `job description → 🛑 plan → each channel: source → match rationale per criterion → 🛑 action → outreach → each candidate: evidence summary (no reject decision) → schedule → interview kits → 🛑 sign-off (a person decides)`
**Variants:** `linkedin-hiring-assistant` (global English release by end of September 2025; sources candidates, screens via InMail Q&A, schedules [29]) · `paradox` · `juicebox`
**Why "evidence, not verdict" matters (compliance):**
- **NYC LL144.** It requires an annual independent bias audit before an automated hiring tool is used, a public summary of the results, and candidate notice 10 business days in advance. The employer is responsible, not the vendor [27].
- **EU AI Act.** It classifies recruitment AI as high-risk. Its obligations were originally due August 2, 2026, and the Digital Omnibus provisionally moves them to December 2, 2027. Confirm which date is legally in force [28].

Keeping the agent at *evidence*, never *verdict*, reduces exposure to both.

#### Issue-tree research · AWF-0030
`ORG › BIZ › STRAT` · checkpointed · accepted · evidence A
**Shape:** `key question → MECE issue tree → 🛑 plan → each branch: deep research → claims table (claim, number, source, date, confidence) → each number: re-fetch source → so-what pages → 🛑 review → deck from firm template`

#### Daily inbox triage · AWF-0031
`ORG › XFN › INBOX` · assist · accepted · evidence A
**Shape:** `07:00 schedule: email, calendar, DMs → sort (action / FYI / delegate / archive) → each thread: reply saved as draft → meeting-slot proposals → top-5 brief → 🛑 action (a person sends every message and accepts every invite)`
**Guard:** inbound email is untrusted input (prompt-injection surface). The agent may never send on its own.

---

## 4. Catalog Status

| Kingdom | Phylum | Species (ID) | Empty classes (backlog) |
|---|---|---|---|
| TEC | SWE | Plan-gated build (0001), Fan-out codemod (0002), Delegated PR (0003) | TEST, REVIEW, DEBUG, ARCH |
| TEC | ITS | Triage then remediate (0004), Alert enrich and adjudicate (0005) | INFRA, APPSEC, HELPDESK |
| TEC | DAT | Governed query (0006) | DATAENG, DS, MLOPS |
| TEC | PRD | Feedback to prototype (0007), Design to code (0008) | PM, UXR, UI |
| TEC | ENG | none | all (early) |
| PRO | RES | Screening funnel (0009), Reviewer-response revision (0010) | ANALYSIS, GRANT, PEER |
| PRO | LEG | Playbook contract review (0024), Grounded legal memo (0025) | LITIG, REG, DD |
| PRO | FIN | Invoice extract-match-route (0022), Event-driven model update (0023) | CLOSE, FPA, AUDIT, TAX |
| PRO | HLT | Ambient scribe (0026) | RCM, CLINTRIAL, DRUGDISC |
| PRO | EDU | Backward-design course (0027), Anchor-calibrated grader (0028) | TUTOR, LND |
| CRE | WRI | Bible-driven novel draft (0011), Daily web serial (0012), Beat-to-scene screenplay (0013), Hook-cadence drama script (0014) | NONFIC, JOURN, TECHW, TRANS |
| CRE | MED | AI shot factory (0015), Live-action assist (0016), Dubbing pipeline (0017) | POST, AUDIO, GAMEART |
| COM | MKT | Cluster-brief-draft content (0018), Ad variant matrix (0019) | SOCIAL, LIFECYCLE, MKTRES |
| COM | SAL | Research-then-personalize outbound (0020) | DEAL, RFP, REVOPS |
| COM | CSX | Procedure agent (0021) | QA, KB, CS |
| ORG | BIZ | Source-screen-schedule hiring (0029), Issue-tree research (0030) | PROC, PMO, ADMIN |
| ORG | GOV | none | all (early) |
| ORG | XFN | Daily inbox triage (0031) | MEET, PKM |

**Totals:** 5 kingdoms · 18 phyla (16 with entries) · 31 species · 30 `accepted` + 1 `draft`.

**Why patterns are traits, shown with data:** `eval-opt` (generate, critique, retry) appears independently in SWE (0001, 0002), RES (0009), WRI (0011, 0013, 0014), MED (0015, 0017), MKT (0019) and EDU (0028), across four kingdoms. As a branch of the tree it would cut across everything; as a trait it's one search.

---

## 5. Implications for Phase 2

1. **Folders follow the tree:**
   `workflows/<KINGDOM>/<PHYLUM>/<CLASS>/<species-slug>/{README.md, variants/, examples/<date>-<slug>/}`
   plus `workflows/unplaced/` for rule 2.
2. **CI checks are simple:**
   - Required fields are present and use the allowed values (§1.5).
   - The class exists under the given phylum and kingdom (§1.4).
   - IDs are unique and never reused.
   - `accepted` requires a reference-example folder.
3. **Three contribution templates:** (a) a new example of an existing species (the most common case), (b) a new species, (c) a move or merge.
4. **Generated views** from the front matter: by profession (SOC), by industry tag, by trait (e.g. all `sampled` with `risk: high`), and by region (a CN 短剧/网文 guide).

---

## 6. Verification Log (November 3, 2026)

✓ = confirmed · ✎ = corrected from v1 · ⚠ = unresolved, so the claim is kept but flagged

| # | Claim | Result | Source |
|---|---|---|---|
| 1 | Airbnb migrated ~3.5k Enzyme → RTL files in about 6 weeks vs. an estimated 1.5 years | ✓ Added pipeline detail: ~75% within hours, ~900 retried, <100 by hand | [5] |
| 2 | Copilot coding agent works issue → draft PR; setup file; workflow approval | ✓ The path is `.github/workflows/copilot-setup-steps.yml`. Issue comments made after assignment aren't seen by the agent. | [4] |
| 3 | `@claude` triggers Claude Code GitHub Actions | ✓ | [3] |
| 4 | Explore → plan → code → commit; plan mode is read-only | ✓ | [2] |
| 5 | AGENTS.md is a cross-tool standard | ✎ Updated: it was donated to the Linux Foundation's Agentic AI Foundation (December 2025), alongside MCP | [6] |
| 6 | Anthropic workflow patterns (chain, route, parallel, orchestrator-workers, evaluator-optimizer) | ✓ | [1] |
| 7 | Figma MCP tools: design context, variables, Code Connect | ✓ Tool lists differ between the desktop and remote servers | [7] |
| 8 | ICMJE: AI can't be an author; disclosure required | ✓ | [8] |
| 9 | LLM screening is reliable enough as a screener | ✎ Revised: sensitivity varies widely (pooled 0.73 in one meta-analysis; ~96% for ensembles in preprints). The SOP now tunes for sensitivity and calibrates first. | [9] |
| 10 | Sudowrite Story Bible, NovelCrafter Codex | ✓ | [10] |
| 11 | KDP requires AI disclosure | ✎ Made precise: AI-*generated* content must be disclosed, AI-*assisted* doesn't need to be (policy since September 2023) | [11] |
| 12 | 番茄 and 起点 tightened AI policies | ✎ Partly: 番茄 AI-training terms dispute (2024) and crackdown on low-quality content (February 2025) are confirmed. **No explicit 起点 rule found.** | [12] |
| 13 | WGA 2023 MBA AI provisions | ✓ Added: the MBA term ran through May 1, 2026. ⚠ Successor terms not checked. | [13] |
| 14 | NRTA (广电) rules for 微短剧 | ✎ Updated: tiered three-category review; the 《微短剧发展管理办法》 draft (June 2026) requires an AI label per episode and was reportedly in force from September 1. ⚠ Full text not reviewed. | [14] |
| 15 | CN AI-content labeling in force since September 1, 2025 | ✓ Explicit and implicit labels plus a mandatory national standard | [15] |
| 16 | AI 漫剧 cost and market | ✓ (B) ¥2–5k → ¥1–2.5k per minute. ⚠ Market-size estimates conflict (¥18.9B vs. ¥24.3B), so none is stated. | [16] |
| 17 | Kling supports character consistency | ✓ Multi-image reference (January 2025). ⚠ Kling-specific lip-sync not confirmed, so the wording is generalized. | [17] |
| 18 | ReelShort and DramaBox scale | ✓ ~$130M and ~$120M IAP in Q1 2025 | [18] |
| 19 | Google penalizes scaled AI content | ✎ Made precise: the "scaled content abuse" policy (March 2024) applies whatever the production method | [19] |
| 20 | Clay Claygent and waterfall enrichment | ✓ (B) | [20] |
| 21 | Decagon AOPs | ✓ | [21] |
| 22 | Fin resolution "50–70%+" | ✎ Revised: vendor claim of 76% vs. 38–53% independent | [22] |
| 23 | Claude for Financial Services; Excel agent | ✎ Made precise: FS launched July 2025; the Claude for Excel beta came in October 2025 | [23] |
| 24 | *Mata v. Avianca* sanctions, 2023 | ✓ June 22, 2023 | [24] |
| 25 | Microsoft Dragon Copilot | ✓ Announced March 2025 | [25] |
| 26 | Abridge in Epic; note-to-transcript linking | ✓ "Linked Evidence" | [26] |
| 27 | NYC LL144 bias audits | ✓ Added: annual independent audit, public summary, 10-business-day notice | [27] |
| 28 | EU AI Act: employment is high-risk | ✓ ⚠ Application date unsettled: August 2, 2026 vs. December 2, 2027 (Digital Omnibus) | [28] |
| 29 | LinkedIn Hiring Assistant | ✓ Global English release (2025) | [29] |
| 30 | SOC 2018: 23/98/459/867 | ✓ | [30] |
| 31 | Mapping AI usage to O*NET has precedent | ✓ Anthropic Economic Index | [31] |
| — | Tools listed only as variants or in role tables (Datadog Bits AI, incident.io, Dropzone, Hebbia, Rogo, Harvey, Spellbook, Arcads, Creatify, MagicSchool, Paradox, Juicebox, Hailuo, Vidu, Seedance, etc.) | ⚠ Not individually re-verified. They're used as variant labels only, and none of the claims depend on them. | — |

---

## 7. References

1. Anthropic, *Building effective agents* (December 2024). https://www.anthropic.com/engineering/building-effective-agents (patterns corroborated via https://docs.spring.io/spring-ai/reference/api/effective-agents.html)
2. Claude Code docs, *Best practices*. https://code.claude.com/docs/en/best-practices
3. Claude Code docs, *GitHub Actions*. https://code.claude.com/docs/en/github-actions
4. GitHub Blog, *Onboarding your AI peer programmer: setting up GitHub Copilot coding agent* (July 2025). https://github.blog/ai-and-ml/github-copilot/onboarding-your-ai-peer-programmer-setting-up-github-copilot-coding-agent-for-success/ · Microsoft Learn, *Assigning, tracking, and troubleshooting Copilot coding agent tasks*. https://learn.microsoft.com/en-us/training/modules/github-copilot-code-agent/3-assign-track-troubleshoot-copilot-code-agent-tasks
5. Airbnb Tech, *Accelerating Large-Scale Test Migration with LLMs* (March 2025). https://airbnb.tech/?p=366 · InfoQ coverage: https://www.infoq.com/news/2025/03/airbnb-llm-test-migration/
6. OpenAI, *Agentic AI Foundation* (December 2025). https://openai.com/index/agentic-ai-foundation/
7. Figma, *MCP server guide*. https://github.com/figma/mcp-server-guide
8. ICMJE AI guidance (summary). https://utsouthwestern.libguides.com/artificial-intelligence/ai-publishing-icmje
9. LLM screening evidence: JMIR (2024) https://www.jmir.org/2024//e52758 · Dual-model ensemble preprint (medRxiv, November 2025) https://www.medrxiv.org/content/10.1101/2025.11.03.25339455.full.pdf · Cochrane-based benchmark preprint (2026) https://www.medrxiv.org/content/10.64898/2026.06.02.26354724v1.full.pdf
10. Sudowrite, *Story Bible template*. https://sudowrite.com/blog/story-bible-template/ · *Sudowrite vs NovelCrafter (2026)*. https://www.inkfluenceai.com/blog/sudowrite-vs-novelcrafter-2026
11. Authors Guild, *Amazon's new disclosure policy for AI-generated book content* (September 2023). https://authorsguild.org/news/amazons-new-disclosure-policy-for-ai-generated-book-content-is-a-welcome-first-step/
12. 人人都是产品经理, 番茄小说 AI 争议. https://www.woshipm.com/ai/5988474.html · 澎湃新闻. https://m.thepaper.cn/newsDetail_forward_28167849
13. WGA, *Know Your Rights: Artificial Intelligence*. https://www.wga.org/contracts/know-your-rights/artificial-intelligence
14. 新华网, 微短剧分类分层审核 (February 2025). https://www.news.cn/politics/20250205/3fbf8abbfa344641b01f799ae42a6318/c.html · 新华网, 《微短剧发展管理办法(征求意见稿)》 (June 2026). https://www.news.cn/politics/20260624/5794e5cd877e440cb678a7f27112ffc7/c.html · IT之家. https://www.ithome.com/0/984/306.htm
15. 国家网信办, 《人工智能生成合成内容标识办法》 (March 14, 2025; in force September 1, 2025). https://www.cac.gov.cn/2025-03/14/c_1743654685899683.htm
16. Brokerage report on AI 漫剧 (October 2025). https://pdf.dfcfw.com/pdf/H3_AP202510241768351710_1.pdf · Practitioner storyboard notes: https://www.woshipm.com/it/6295336.html
17. Kuaishou, *Kling AI Unveils Multi-Image Reference* (January 2025). https://seekingalpha.com/pr/19978699-kuaishou-kling-ai-unveils-multi-image-reference-feature-to-further-tackle-ai-video · 环球网 coverage of Kling 3.0: https://tech.huanqiu.com/article/4QFI3Up2VEA
18. Short-drama app revenue, Sensor Tower Q1 2025 data, via https://www.webull.com/news/12816921610159104 and https://gamebiz.jp/news/406943
19. Google Search Central, *March 2024 core update and new spam policies*. https://developers.google.com/search/blog/2024/03/core-update-spam-policies
20. Lindy, *Clay review*. https://wf.lindy.ai/blog/clay-review
21. Decagon, *AOP*. https://decagon.ai/product/aop · Futurum Group (August 2025). https://futurumgroup.com/press-release/decagon-aims-to-simplify-ai-agent-development-with-natural-language/
22. Fin resolution-rate discussion: https://community.intercom.com/questions/3622 · https://superframeworks.com/articles/best-ai-customer-support-tools
23. VentureBeat, Claude for Financial Services (July 2025). https://venturebeat.com/ai/anthropic-rolls-out-claude-ai-for-finance-integrates-with-excel-to-rival · Anthropic, *Advancing Claude for Financial Services*. https://anthropic.com/news/advancing-claude-for-financial-services
24. *Mata v. Avianca, Inc.*, 678 F. Supp. 3d 443 (S.D.N.Y. 2023). https://en.wikipedia.org/wiki/Mata_v._Avianca,_Inc.
25. Fierce Healthcare / Maginative on Dragon Copilot. https://www.maginative.com/article/microsoft-unveils-dragon-copilot-an-ai-assistant-for-clinicians/ · https://www.fiercehealthcare.com/ai-and-machine-learning/microsoft-debuts-dragon-copilot-ai-clinical-assistant-nurses-expands-access
26. Business Wire, *Abridge Inside with Epic Integration* (February 2024). https://www.businesswire.com/news/home/20240213503774/en
27. NYC DCWP, *AEDT FAQ*. https://www.nyc.gov/assets/dca/downloads/pdf/about/DCWP-AEDT-FAQ.pdf
28. Cuatrecasas, *The Digital Omnibus on AI: impact on employment relations*. https://www.cuatrecasas.com/en/global/labor-and-employment/art/digital-omnibus-on-ai-how-does-it-impact-employment-relations
29. LinkedIn, *Hiring Assistant to launch globally in English* (2025). https://news.linkedin.com/2025/hiring-assistant-globally-available
30. BLS, *SOC 2018 User Guide*. https://www.bls.gov/soc/2018/soc_2018_user_guide.pdf
31. Anthropic, *The Anthropic Economic Index*. https://www.anthropic.com/research/the-anthropic-economic-index · Paper: https://arxiv.org/html/2503.04761v1
32. Background on workflow-pattern taxonomies: *A Survey on Agent Workflow: Status and Future* (2025). https://arxiv.org/pdf/2508.01186
