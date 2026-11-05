# Phase 1 Report (v2): A Systematic Classification of Agentic Work

**Version:** v2 · 2026-11-03
**What changed from v1:**
1. The flat tag taxonomy is replaced by a **Linnaean-style classification system**. It has ranks, a nomenclature code, type specimens, dichotomous identification keys, and a species criterion.
2. Key claims were **checked against live sources** in November 2026. Corrections are listed in §6 (Verification Log), and citations use [n] → §7.

---

## 0. Inclusion Criteria

A workflow can be described as a taxon only if it meets **all four** criteria:

| # | Criterion | Excludes |
|---|---|---|
| C1 | **Multi-step**: ≥3 model or tool steps with state carried between them | One-shot prompts |
| C2 | **Acts on real artifacts** (files, repos, databases, documents, media, external systems) through tools, MCP, APIs, or a UI | Advice-only chat |
| C3 | **Explicit human gates**: where people approve, edit, or sample is defined | "Let the AI handle it" |
| C4 | **Reproducible**: at least one dated specimen (§1.5 Art. 4) that a peer can rerun | "Use AI to brainstorm" |

---

## 1. The Classification System

### 1.1 Why borrow from biology

A flat tag list can't answer the questions that will dominate a growing catalog. Biological nomenclature has solved each of them for about 250 years:

| Catalog problem | Biological solution | Adopted here as |
|---|---|---|
| "Is this new submission a duplicate of an existing entry?" | **Species concept** plus synonymy | The interchangeability test (Art. 7); junior synonyms (Art. 5) |
| "Where does this go?" with two contributors disagreeing | **Dichotomous identification key** | Ordered couplet keys (§1.8): every workflow exits at exactly one leaf |
| Tools churn every quarter | Ranks rest on **stable, heritable characters**, not on environment | Tools sit *below* species, as strains (Art. 1) |
| Same agent pattern shows up in law and in film | **Homology vs. analogy**: bat and bird wings don't make bats birds | Agent patterns are *traits*, never ranks (§1.2) |
| Names change on reclassification, which breaks links | **Stable identifiers** separate from names (e.g. NCBI taxid) | Permanent `AWF-####` serial IDs (Art. 3) |
| Claims with no proof | **Type specimens** deposited in a collection | Holotype = a dated, rerunnable artifact bundle (Art. 4) |
| Dead workflows clutter the index | **Extinction and conservation status** | Status + adoption status (Art. 10, §1.7) |

### 1.2 Core principle: lineage defines ranks, convergence defines traits

Every agentic workflow **descends from a human professional practice**. Contract review agents descend from attorney contract review, and ambient scribes descend from medical transcription. That lineage, plus the deliverable it produces, is the **homologous character set**: it's stable, inherited, and shared because of common origin. Ranks are built only from it.

Everything that evolves independently across lineages is **analogous** and recorded as a trait:

| Character type | Biological analog | Members | How it's recorded |
|---|---|---|---|
| **Homologous** (lineage) | Skeleton, genome | Professional field, domain, discipline, task verb, deliverable, stage skeleton | **Ranks** (Kingdom → Species) |
| **Analogous** (convergent) | Wings, eyes, streamlining | Agent pattern (eval-opt, orchestrator-workers...), runtime, autonomy level, gate types, modality | **Character matrix** (§1.6) |
| **Ecological** | Habitat, range | Industry (NAICS), region, language, organization scale, regulatory regime | **Habitat** metadata (§1.6) |
| **Phenotypic, environmental** | Cultivar, strain | The concrete toolchain (Claude Code, Kling, n8n...) | **Strain** rank below species |

> Consequence: "all evaluator-optimizer workflows" is a *trait query*, like "all flying animals." It isn't a taxon, and there will never be an `eval-opt/` folder.

### 1.3 Ranks

Seven principal ranks plus two below species. Each rank is defined by **one diagnostic question**, so siblings at any rank differ on exactly one character.

| Rank | Diagnostic question | Value set | Example A | Example B |
|---|---|---|---|---|
| **Kingdom** | Which field of practice does the deliverable belong to? | 5, enumerated (§1.8 Key I) | `CRE` Creative & Media | `TEC` Technology & Product |
| **Phylum** | Which professional domain? | 18, enumerated (§1.8 Key II) | `MED` Media Production | `SWE` Software Engineering |
| **Class** | Which discipline within the domain? | Enumerated per phylum (§1.8) | `AIGCVIDEO` | `FEAT` |
| **Order** | What is the primary task verb? | 7 (§1.8 Key III) | `create` | `create` |
| **Family** | What deliverable type (work object) leaves the workflow? | Open list per class | `episode` | `pull-request` |
| **Genus** | What is the **stage skeleton**, i.e. the stage formula with gates removed? | Named archetype | *ShotFactory* | *PlanGatedBuild* |
| **Species** | Where are the human gates, and what is the autonomy level? | Full stage formula + autonomy | *ShotFactory character-locked* | *PlanGatedBuild test-first* |
| *Strain* | Which concrete toolchain? | `@toolchain` slug | `@jimeng-kling-capcut` | `@claude-code` |
| *Specimen* | Which dated real-world run proves it? | Case record | `2026-03 studio X run` | `2025-09 repo Y` |

**Why Genus and Species split on gates.** The stage skeleton defines *how the deliverable gets made*, which is the workflow's anatomy. Gate placement and autonomy define *how the work is governed*. Two teams with the same anatomy but different governance (L3 plan-gated vs. L4 sample-audited) run different SOPs and get different risk profiles, so they're different species. Two teams with identical anatomy and governance but different tools are the same species in different strains.

### 1.4 The stage formula (the workflow's "floral formula")

Botanists describe flowers with compact formulas. We describe workflow anatomy the same way, using a controlled stage vocabulary. The formula is machine-checkable, which lets Phase 2 CI validate it.

**Stage vocabulary (12):**

| Code | Stage | Code | Stage |
|---|---|---|---|
| `IN` | Intake and normalize the input | `CRIT` | Model critique against a rubric |
| `CTX` | Load or build context (retrieve, read bible, schema, codebase) | `SEL` | Select among candidates |
| `PLAN` | Decompose or plan | `RTE` | Classify and route |
| `GEN` | Generate the artifact or a portion of it | `ACT` | Side effect in an external system |
| `VAL` | Deterministic validation (tests, schema, citation resolver, 3-way match) | `ASM` | Assemble or merge parts |
| `PUB` | Deliver or publish | `LRN` | Write learnings back to persistent context |

**Operators:** `→` sequence · `[ … ]*` loop until pass or budget · `FAN{ … }` parallel per unit (file, clause, shot, account) · `a | b` branches after `RTE` · `‖G-x‖` human gate (types in §1.6).

**Example:** `IN → CTX → PLAN ‖G-plan‖ → [GEN → VAL]* → CRIT → ‖G-artifact‖ PUB → LRN`
**Genus signature** = the same formula with every `‖…‖` deleted: `IN → CTX → PLAN → [GEN → VAL]* → CRIT → PUB → LRN`

### 1.5 Nomenclature Code (Code of Agentic Workflow Nomenclature, "CAWN")

These articles are modeled on the zoological code (ICZN): priority, types, and synonymy.

- **Art. 1 · Ranks.** All seven principal ranks are mandatory in each record. Strain and specimen are mandatory for `valid` status. Intermediate ranks may be *monotypic*, meaning they hold one child, which is common for Order.
- **Art. 2 · Names.**
  - Kingdom, phylum, and class use uppercase codes.
  - Order uses a verb from the controlled vocabulary.
  - Family uses a kebab-case noun naming the deliverable.
  - **Genus** uses an UpperCamelCase name of at most 3 words describing the skeleton. It's unique across the whole catalog.
  - **Species epithet** uses a lowercase kebab-case word or phrase naming its governance trait.
  - The **binomial** is written *Genus epithet*, e.g. *PlanGatedBuild test-first*. The strain is appended: *PlanGatedBuild test-first* `@codex-cli`.
- **Art. 3 · Identifiers.** Every taxon at genus rank or below gets a permanent serial `AWF-####`, which is never reused and never changes on reclassification. The taxonomic path (`TEC.SWE.FEAT.create.pull-request`) *may* change through revision. Links must use the serial.
- **Art. 4 · Types.**
  - Every genus designates a **type species**.
  - Every species designates a **holotype specimen**: a dated bundle with the context files (`CLAUDE.md`, playbook, bible template, prompt pack, n8n/Dify export), a run log or transcript excerpt, and an input → output sample.
  - Additional specimens are **paratypes** and raise the evidence grade.
  - When a taxon is split, the name stays with the part containing the type.
- **Art. 5 · Priority and synonymy.** The first validly published name (the merged PR) has priority. A later submission found to be the same species becomes a **junior synonym**: its specimens move under the senior name and its ID redirects.
- **Art. 6 · Valid publication** requires all of the following:
  1. A diagnosis: how it differs from sibling taxa.
  2. Placement through the keys in §1.8.
  3. A complete stage formula.
  4. A completed character matrix.
  5. ≥1 specimen.

  Without a specimen, the status is `provisional`.
- **Art. 7 · Species criterion (interchangeability test).** Two SOPs are the **same species** if and only if a practitioner could swap one for the other without changing (a) the stage skeleton, (b) the gate types and positions, (c) the autonomy level, or (d) the *types* of required context artifacts. If they differ only in toolchain, they're different **strains**. If they differ only in prompt wording, they're the same strain and that's specimen variation.
- **Art. 8 · Genus criterion.** Same family **and** identical genus signature, except for optional `LRN` stages.
- **Art. 9 · Incertae sedis.** A workflow that can't be keyed below rank R is filed as `R.incertae-sedis` (e.g. `ORG.incertae-sedis`). There's no generic "Other" bucket.
- **Art. 10 · Status.** `provisional` (no specimen) · `valid` · `synonym` (→ senior ID) · `dubium` (claims can't be verified; specimens rejected) · `extinct` (no new specimen in 18 months **and** all strains depend on discontinued tools).
- **Art. 11 · Revision.** Lumping or splitting happens through a *Taxonomic Revision* PR with a rationale and the affected IDs. Paths redirect and IDs persist.
- **Art. 12 · High ranks are conservative.** A new phylum or kingdom requires an RFC plus ≥3 valid species that can't be placed under existing phyla. That's the "unoccupied niche" rule in §1.9.

### 1.6 Character matrix and habitat (non-rank metadata)

| Character | Card. | Vocabulary |
|---|---|---|
| `pattern` | 1..n | `chain` · `route` · `parallel` · `orch-workers` · `eval-opt` · `auto-loop` · `role-crew` · `computer-use`. The first five follow Anthropic's workflow patterns [1]. |
| `runtime` | 1..n | `ide-cli` · `chat-workspace` · `background-cloud` · `workflow-automation` (n8n, Zapier, Make, Dify, Coze) · `embedded-saas` · `custom-sdk` |
| `autonomy` | 1 | `L1` suggest · `L2` approve every action · `L3` runs between defined gates · `L4` completes, humans sample and audit · `L5` unattended |
| `hitl` (gate types) | 1..n | `G-spec` approve input or brief · `G-plan` approve plan · `G-action` permission for a side effect · `G-artifact` review a draft or diff · `G-sample` statistical QA · `G-signoff` accountable or licensed sign-off · `G-escalate` agent hands off on uncertainty |
| `modality` | in/out | `text` `code` `table` `doc` `image` `video` `audio` `ui` `structured` |
| **Habitat** `industry` | 0..n | NAICS 2-digit sector names |
| **Habitat** `region` / `lang` | 0..n | ISO codes. These matter for the CN 网文 and 短剧 ecosystems. |
| **Habitat** `scale` | 1 | `solo` · `team` · `org` |
| **Habitat** `risk` | 1 | `low` · `med` (customer-facing or financial) · `high` (regulated: legal, clinical, employment, credit) |

### 1.7 Evidence grade and adoption status

| Evidence (best specimen) | Meaning | Adoption status (IUCN-style) | Meaning |
|---|---|---|---|
| `E1` | Practitioner-documented with artifacts | `EM` Emerging | Pilots only |
| `E2` | Named organization's public case study | `ES` Established | Production use at multiple organizations |
| `E3` | Vendor-documented capability or vendor-reported metric | `DO` Dominant | Default practice in its class |
| `E4` | Anecdotal or community report | `DE` Declining · `EX` Extinct | Being replaced · no longer practiced |

### 1.8 Identification keys

Keys use **ordered couplets**: take the first branch that matches. Because exactly one leaf is always reached, the scheme is mutually exclusive and collectively exhaustive by construction.

#### Key I: Kingdom (judged on the **final deliverable** that leaves the workflow)

| Couplet | If | Then |
|---|---|---|
| 1a | Deliverable is a professional work product of **research, law, finance/accounting, healthcare, or education** (paper, legal instrument or memo, financial record, model or view, clinical record, instruction or assessment) | **PRO** Professional & Knowledge Services → Key II-PRO |
| 1b | Otherwise | → 2 |
| 2a | Deliverable is **customer-facing commercial communication or interaction** (marketing asset, outbound sale, support resolution) | **COM** Commerce & Customer → Key II-COM |
| 2b | Otherwise | → 3 |
| 3a | Deliverable is a **technical system or a definition of one**: code, configuration, infrastructure state, data, queries or models, a product spec, design or prototype, or a physical engineering design | **TEC** Technology & Product → Key II-TEC |
| 3b | Otherwise | → 4 |
| 4a | Deliverable is an **authored work for an audience** to read, watch, or hear | **CRE** Creative & Media → Key II-CRE |
| 4b | Otherwise | **ORG** Organization & Public → Key II-ORG |

#### Key II: Phylum

| Kingdom | Couplets (first match wins) |
|---|---|
| **PRO** | 1. Patient care or life-science R&D → **HLT** · 2. Legal advice, instrument, filing, or compliance determination → **LEG** · 3. Money: transactions, books, financial models, investment views → **FIN** · 4. Serves learners (instruction, assessment) → **EDU** · 5. Scholarly knowledge (papers, reviews, grants) → **RES** |
| **COM** | 1. Interaction with an *existing* customer to resolve or retain → **CSX** · 2. One-to-one pursuit of specific accounts or deals → **SAL** · 3. One-to-many demand generation → **MKT** |
| **TEC** | 1. Physical-world engineering artifact → **ENG** · 2. Defines *what* to build (PRD, research synthesis, design, non-production prototype) → **PRD** · 3. Data-centric (queries, analyses, pipelines, models, evals) → **DAT** · 4. Running-system operations (incidents, infra changes, security verdicts, internal IT) → **ITS** · 5. Application source code or a review of it → **SWE** |
| **CRE** | 1. Final deliverable is text, including scripts and translations → **WRI** · 2. Audiovisual, visual, or audio media → **MED** |
| **ORG** | 1. Public-administration function (policy, casework, civic process) → **GOV** · 2. Organizational function (people, procurement, projects, strategy, executive support) → **BIZ** · 3. An individual's own communication or knowledge → **XFN** · 4. Can't be keyed → `ORG.incertae-sedis` |

#### Key III: Order (task verb)

| Couplet | If the primary deliverable is… | Order |
|---|---|---|
| 1 | A **side effect** in an external system (sent, paid, resolved, deployed, mitigated) | `operate` |
| 2 | Coordination of other workflows as the product itself | `orchestrate` |
| 3 | A **judgment about an existing artifact** (verdict, issues, redlines, grade) | `verify` |
| 4 | An existing artifact **converted** with its meaning preserved (translate, migrate, transcribe, restructure, revise) | `transform` |
| 5 | **Found and assembled existing information** (search, screening, research brief) | `retrieve` |
| 6 | **New conclusions derived from data** | `analyze` |
| 7 | A **new artifact** | `create` |

#### Classes per phylum (enumerated)

| Kingdom | Phylum | Classes |
|---|---|---|
| TEC | `SWE` Software Engineering | `FEAT` · `MAINT` · `TEST` · `REVIEW` · `DEBUG` · `ARCH` |
| TEC | `ITS` IT, Infrastructure & Security | `SRE` · `INFRA` · `SECOPS` · `APPSEC` · `HELPDESK` |
| TEC | `DAT` Data & ML | `ANALYTICS` · `DATAENG` · `DS` · `MLOPS` |
| TEC | `PRD` Product & Design | `PM` · `UXR` · `UI` · `PROTO` · `DSYS` |
| TEC | `ENG` Physical Engineering & AEC | `CAD` · `SIM` · `CODECOMP` · `MFG` |
| CRE | `WRI` Writing & Publishing | `FICTION` · `SERIAL` (网文) · `SCREEN` · `NONFIC` · `JOURN` · `TECHW` · `TRANS` |
| CRE | `MED` Media Production | `SHORTDRAMA` (live-action) · `AIGCVIDEO` (AI-generated video, 漫剧) · `POST` · `DUB` · `AUDIO` · `GAMEART` |
| PRO | `RES` Research & Academia | `LITREV` · `WRITE` · `ANALYSIS` · `GRANT` · `PEER` |
| PRO | `LEG` Legal & Compliance | `CONTRACT` · `RESEARCH` · `LITIG` · `REG` · `DD` |
| PRO | `FIN` Finance & Accounting | `AP` · `CLOSE` · `FPA` · `INVEST` · `AUDIT` · `TAX` |
| PRO | `HLT` Healthcare & Life Sciences | `CLINDOC` · `RCM` · `CLINTRIAL` · `DRUGDISC` |
| PRO | `EDU` Education & Training | `COURSE` · `ASSESS` · `TUTOR` · `LND` |
| COM | `MKT` Marketing & Growth | `CONTENT` · `ADS` · `SOCIAL` · `LIFECYCLE` · `MKTRES` |
| COM | `SAL` Sales & Revenue | `PROSPECT` · `DEAL` · `RFP` · `REVOPS` |
| COM | `CSX` Customer Support & Success | `RESOLVE` · `QA` · `KB` · `CS` |
| ORG | `BIZ` Business Operations & People | `HR` · `PROC` · `PMO` · `STRAT` · `ADMIN` |
| ORG | `GOV` Public Sector | `POLICY` · `CASEWORK` · `CIVIC` |
| ORG | `XFN` Personal Knowledge Work | `INBOX` · `MEET` · `PKM` |

**Key placements that changed from v1** because the keys forced a decision:
- *Issue → async PR* moved from `SWE.REVIEW` to `SWE.FEAT`, because its deliverable is a PR, not a review.
- *Outbound prospecting* changed Order from `retrieve` to `operate`, because the deliverable is a sent campaign.
- *Technical writing* is always `WRI.TECHW`. A README edited inside a PR is part of a `pull-request` deliverable and stays `SWE`.

### 1.9 Exhaustiveness proof: crosswalk to SOC 2018

The US Standard Occupational Classification has 23 major groups, 98 minor groups, 459 broad occupations, and 867 detailed occupations [30]. Every major group maps to ≥1 phylum, or is explicitly recorded as an **unoccupied niche**: no agentic species has been observed, so no phylum exists yet (Art. 12). The Anthropic Economic Index already maps AI usage to O*NET tasks [31], so species records can also carry O*NET task IDs. That lets the catalog be joined with labor-market data.

| SOC major group | Phyla | SOC major group | Phyla |
|---|---|---|---|
| 11 Management | BIZ, MKT, SAL, FIN | 33 Protective Service | GOV (sparse) |
| 13 Business & Financial Ops | FIN, BIZ, MKT | 35 Food Prep & Serving | *unoccupied* |
| 15 Computer & Mathematical | SWE, ITS, DAT | 37 Building & Grounds | *unoccupied* |
| 17 Architecture & Engineering | ENG | 39 Personal Care & Service | *unoccupied* |
| 19 Life, Physical & Social Science | RES, HLT | 41 Sales & Related | SAL |
| 21 Community & Social Service | GOV, HLT | 43 Office & Admin Support | CSX, FIN, BIZ, XFN |
| 23 Legal | LEG | 45 Farming, Fishing & Forestry | *unoccupied* |
| 25 Educational Instruction & Library | EDU, RES | 47 Construction & Extraction | ENG (sparse) |
| 27 Arts, Design, Entertainment, Media | WRI, MED, PRD | 49 Installation, Maintenance & Repair | ENG (sparse) |
| 29 Healthcare Practitioners | HLT | 51 Production | ENG.MFG |
| 31 Healthcare Support | HLT | 53 Transportation & Material Moving | *unoccupied* |
| | | 55 Military Specific | out of scope |

### 1.10 Index record (front matter schema)

```yaml
id: AWF-0015                    # permanent serial (Art. 3)
name: ShotFactory character-locked
rank: species
classification:
  kingdom: CRE
  phylum: MED
  class: AIGCVIDEO
  order: create
  family: episode
  genus: ShotFactory            # type species of genus: AWF-0015
formula: "IN → PLAN ‖G-spec‖ → CTX → FAN{[GEN → CRIT → SEL]*} → FAN{[GEN → VAL]*} → GEN → ASM ‖G-artifact‖ → ‖G-signoff‖ PUB"
autonomy: L3
characters:
  pattern: [chain, parallel, eval-opt]
  runtime: [embedded-saas, workflow-automation]
  hitl: [G-spec, G-artifact, G-signoff]
  modality: {in: [text], out: [video]}
habitat: {industry: [information], region: [CN], lang: [zh], scale: org, risk: med}
status: valid                   # provisional | valid | synonym | dubium | extinct
adoption: ES                    # EM | ES | DO | DE | EX
evidence: E2
holotype: specimens/2026-03-holotype/
strains: ["@jimeng-kling-capcut", "@comfyui-flux-veo"]
synonyms: []
uses: [AWF-0014]                # upstream species in a pipeline
crosswalk: {soc: ["27-2012"], onet_tasks: []}
last_verified: 2026-11
```

---

## 2. Cross-Industry Landscape (verified November 2026)

| Phylum | Adoption | Dominant genera (this report) | Typical autonomy | Verified signals |
|---|---|---|---|---|
| SWE | DO | *PlanGatedBuild*, *FanOutCodemod*, *DelegatedPR* | L3 local / L4 async | The vendor-documented explore → plan → code → commit loop [2]. `@claude` GitHub Actions [3] and the Copilot coding agent, which works from issue → draft PR [4]. Airbnb migrated ~3.5k files in about 6 weeks [5]. AGENTS.md has been under the Linux Foundation's AAIF since December 2025 [6]. |
| ITS | ES | *TriageThenRemediate*, *EnrichAndAdjudicate* | L2–L3 for writes | Vendor-documented (E3); no independent benchmark found |
| DAT | ES | *GovernedQuery* | L3 | Vendor-documented (E3) |
| PRD | ES | *FeedbackToPrototype*, *DesignToCode* | L3 | Figma MCP server exposes design context, variables, and Code Connect mappings [7] |
| RES | ES | *ScreenFunnel*, *ResponseMatrix* | L3 + `G-signoff` | ICMJE: disclose AI use; chatbots can't be authors [8]. LLM screening sensitivity varies widely (pooled 0.73 in one meta-analysis; ensembles report ~96% in preprints) [9] |
| WRI | ES (high volume in CN) | *BibleDrivenDraft*, *DailySerial*, *BeatToScene*, *HookCadenceScript* | L2–L3 | Story Bible and Codex tools [10]. KDP requires disclosure of AI-*generated* content, though not AI-*assisted* content [11]. 番茄 has disputed AI-training terms and cracked down on low-quality AI text [12]. WGA MBA AI terms [13]. |
| MED | DO in CN micro-drama | *ShotFactory*, *LiveActionAssist*, *DubPipeline* | L3 / L4 | AI labeling rules in force since September 1, 2025 [15]. NRTA tiered review of micro-dramas [14]. AI 漫剧 cost reportedly fell from ¥2–5k to ¥1–2.5k per minute [16]. Kling multi-image reference for consistency [17]. ReelShort and DramaBox each made ~$120–130M in IAP in Q1 2025 [18]. |
| MKT | ES | *ClusterBriefDraft*, *VariantMatrix* | L3 | Google's "scaled content abuse" spam policy (March 2024) targets mass-generated pages with no added value [19] |
| SAL | ES | *ResearchThenPersonalize* | L3–L4 | Clay's Claygent research and waterfall enrichment feed sequencers [20] |
| CSX | DO | *ProcedureAgent* | L4 + `G-escalate` | Decagon AOPs: natural language compiled into workflows, with sensitive steps run in code [21]. Fin claims a 76% average resolution rate, while independent observers report 38–53% [22]. |
| FIN | ES | *ExtractMatchRoute*, *EventDrivenUpdate* | L3–L4 | Claude for Financial Services (July 2025) and the Claude for Excel beta (October 2025) [23] |
| LEG | ES | *PlaybookReview*, *GroundedMemo* | L2–L3 + `G-signoff` | *Mata v. Avianca* sanctions, June 22, 2023 [24] |
| HLT | DO (ambient documentation) | *AmbientScribe* | L3 + `G-signoff` | Microsoft Dragon Copilot (March 2025) [25]. Abridge inside Epic with "Linked Evidence" [26]. |
| EDU | ES | *BackwardDesign*, *RubricGrader* | L2–L3 | Not independently verified (E3/E4) |
| BIZ | ES | *SourceScreenSchedule*, *IssueTreeResearch* | L3 | LinkedIn Hiring Assistant, global English release (2025) [29]. NYC LL144 [27]. EU AI Act employment obligations: dates are unsettled [28]. |
| ENG, GOV | EM | (none yet) | L1–L2 | Not enough specimens yet; held as niches, not invented |
| XFN | ES | *DailyTriage* | L2 | Not independently verified (E1/E4) |

**Five cross-phylum regularities.** These are convergent traits, the biological equivalent of "streamlining in aquatic animals":
1. **Persistent context files carry the heredity.** `CLAUDE.md`/`AGENTS.md`, playbooks, story bibles, AOPs, and procedures all play this role [2][6][10][21]. Decagon explicitly frames AOPs as SOPs written for agents [21]. This is why Art. 4 makes them part of the holotype.
2. **`VAL` before the human gate.** Mature species put deterministic validators (tests, citation resolvers, 3-way match, Linked Evidence) ahead of human review [5][26].
3. **Gates sit at irreversibility boundaries:** send, merge, pay, file, publish, sign.
4. **`FAN{}` is the productivity multiplier:** per file [5], per shot, per clause, per account.
5. **Regulated phyla always end in `G-signoff`.** Licensed humans remain the accountable author [8][13][24][25].

---

## 3. Species Descriptions (SOP Breakdowns)

Each description gives the binomial, a **classification line** (Kingdom › Phylum › Class › Order › Family), the **stage formula**, characters, the loop **Input → Roles/Tools → Execution → Gates → Output**, and failure modes. 🛑 marks a gate.

### Kingdom TEC

#### *PlanGatedBuild test-first* · AWF-0001 · type species of *PlanGatedBuild*
`TEC › SWE › FEAT › create › pull-request` · autonomy **L3** · status valid · adoption DO · evidence E1/E3 [2]
**Formula:** `IN → CTX → FAN{CTX} → PLAN ‖G-plan‖ → GEN(tests) → [GEN → VAL]* → CRIT → ‖G-action‖ ACT → ‖G-artifact‖ PUB → LRN`
**Characters:** pattern `auto-loop, orch-workers` · runtime `ide-cli` · gates `G-plan, G-action, G-artifact`
**Strains:** `@claude-code` · `@codex-cli` · `@cursor-agent`

- **Input:** an issue with acceptance criteria; a repo with `CLAUDE.md`/`AGENTS.md` (build, test, and lint commands, conventions, no-go areas); a working test suite.
- **Roles/Tools:** the lead agent (read, edit, allow-listed shell); read-only explorer sub-agents; a verifier (formatter and lint hooks, tests, typecheck, browser screenshots for UI); a fresh-context reviewer sub-agent.

**Execution**
1. The agent reads the context file, the issue (`gh issue view` or the tracker's MCP), and relevant code. Explorers fan out to map affected modules.
2. In plan mode (read-only), the agent writes a plan: files to touch, approach, test strategy, open questions [2]. 🛑 **G-plan**: this is the highest-leverage correction point.
3. Write failing tests that encode the acceptance criteria and confirm they fail.
4. Implement in increments, with targeted tests and typecheck after each one. Loop on the failure output, and cap iterations before escalating.
5. A fresh-context reviewer checks the diff against the spec: edge cases, dead code, security.
6. For UI changes, run the dev server, take a screenshot, and compare with the design.
7. 🛑 **G-action**: commit, push, and open the PR, unless these were pre-authorized.
8. 🛑 **G-artifact**: a human reviews the PR and CI.
9. `LRN`: write recurring corrections back into the context file.

**Output:** a reviewed PR with tests, and an updated context file.
**Failure modes → guards:** the agent edits tests to make them pass → forbid test edits in the green phase. Scope creep → flag any file changed outside the plan's list. Context saturation → clear context between tasks and persist the plan to a file [2].
**Sibling species (diagnosis):** *PlanGatedBuild step-approved* (L2: `G-action` on every edit) differs only in gating.

#### *FanOutCodemod validator-ladder* · AWF-0002 · type of *FanOutCodemod*
`TEC › SWE › MAINT › transform › migration-changeset` · **L4** · valid · ES · E2 [5]
**Formula:** `IN → CTX ‖G-spec‖ → FAN{[GEN → VAL(lint) → VAL(types) → VAL(tests)]*} → CTX+ → FAN{[GEN → VAL]*} ‖G-sample‖ → ASM → ‖G-artifact‖ PUB`
**Characters:** `parallel, eval-opt, chain` · `custom-sdk, background-cloud` · gates `G-spec, G-sample, G-artifact`
**Holotype:** Airbnb's Enzyme → React Testing Library migration [5]. About 3.5k test files were migrated in roughly 6 weeks, against an estimated 1.5 years by hand. A per-file step state machine retried with error feedback. About 75% of files passed within hours, and the remaining ~900 got richer context and more retries. Fewer than 100 were finished by hand.

**Execution**
1. Pilot on 10–20 representative files and tune the prompt and examples. 🛑 **G-spec**: freeze the prompt, few-shot examples, and success definition.
2. Run a per-file state machine: refactor → fix lint → fix types → fix tests. Each step is an LLM call that receives its validator's output. Run N parallel headless workers (`claude -p`, Codex exec, Agent SDK), each with a retry budget.
3. Long tail: add context (sibling files, component source, more examples) and rerun. Cluster the failures and patch the prompt [5].
4. 🛑 **G-sample**: check semantic fidelity on a random sample, beyond "tests pass."
5. Batch PRs by owner. 🛑 **G-artifact**: code owners review. Hand-fix the residue.

**Output:** a migrated codebase, a failure log, and a reusable migration prompt pack.

#### *DelegatedPR bot-reviewed* · AWF-0003 · type of *DelegatedPR*
`TEC › SWE › FEAT › create › pull-request` · **L4** · valid · DO · E3 [3][4]
**Formula:** `‖G-spec‖ IN → CTX → [GEN → VAL]* → PUB(draft) → [CRIT(bot) → GEN]* → ‖G-action‖ VAL(CI) → ‖G-artifact‖ ACT(merge)`
**Diagnosis vs. *PlanGatedBuild*:** there's no `PLAN` stage and no human mid-run gate. The issue *is* the plan, so a different genus.
**Strains:** `@copilot-coding-agent` · `@claude-code-action` · `@codex-cloud` · `@devin` · `@jules`

**Execution**
1. 🛑 **G-spec**: only self-contained, testable issues are labeled for agents.
2. Dispatch by assigning the issue to Copilot, which opens a draft PR and runs in an Actions-based environment configured by `.github/workflows/copilot-setup-steps.yml` [4]. Alternatively, comment `@claude`, which triggers Claude Code GitHub Actions [3].
3. The agent implements, runs tests, and pushes. Later instructions go as PR comments, because Copilot doesn't see issue comments added after assignment [4].
4. A review bot comments, and the agent addresses the comments for 1–2 rounds.
5. 🛑 **G-action**: a human clicks "Approve and run workflows" so CI runs on agent PRs [4].
6. 🛑 **G-artifact**: human review and merge.

**Output:** merged PRs. Track the merge rate per issue label to tune what gets dispatched.

#### *TriageThenRemediate runbook-gated* · AWF-0004
`TEC › ITS › SRE › operate › incident` · **L3** · valid · ES · E3
**Formula:** `IN → RTE → FAN{CTX(metrics, logs, traces, deploys)} → PLAN(ranked hypotheses) → PUB(findings) → ‖G-action‖ ACT(runbook step) → VAL(SLO) → GEN(postmortem) ‖G-artifact‖ → LRN`

**Execution**
1. An alert starts the agent, which routes by service tag to the matching runbook.
2. Read-only investigation runs in parallel: the error spike, deploys in the window, exemplar traces, and the suspect diff.
3. Post ranked hypotheses with evidence links to the incident channel.
4. 🛑 **G-action**: the on-call engineer approves a specific runbook command (rollback, scale, restart).
5. Verify recovery against the SLO.
6. Draft the postmortem. 🛑 **G-artifact**: the incident owner edits it, especially root cause and action items.
7. Update the runbook.

**Guard:** write tools are restricted to an allow-list of runbook commands, enforced in code.

#### *EnrichAndAdjudicate auto-close-benign* · AWF-0005
`TEC › ITS › SECOPS › verify › alert-verdict` · **L4** · valid · ES · E3
**Formula:** `IN → FAN{CTX(threat intel, identity, EDR tree)} → GEN(verdict + evidence) → RTE: benign → ACT(close) | suspicious/malicious → ‖G-escalate‖ ; ‖G-sample‖ weekly`

**Execution**
1. Normalize the alert.
2. Run enrichment lookups in parallel.
3. Investigate as an analyst would.
4. Return a verdict with confidence and evidence.
5. Auto-close benign alerts with the evidence attached.
6. 🛑 **G-escalate**: send everything else to tier 2 as a prepared case.
7. 🛑 **G-sample**: QA auto-closed alerts weekly.

**Metric:** analyst minutes per alert.

#### *GovernedQuery golden-query* · AWF-0006
`TEC › DAT › ANALYTICS › analyze › data-answer` · **L3** · valid · ES · E3
**Formula:** `IN → CTX(semantic layer, schema, samples) → [GEN(SQL) → VAL(bounds, fan-out, canonical totals)]* → GEN(chart + summary) ‖G-artifact‖ → ‖G-signoff‖ PUB → LRN(golden query)`

**Execution**
1. Map business terms to governed metric definitions. If a term is ambiguous, ask instead of guessing.
2. Inspect the schema and sample rows.
3. Draft SQL, preferring the semantic layer.
4. Validate: sanity bounds, join fan-out (did row counts explode?), and reconciliation with a canonical dashboard total.
5. Chart the result and attach the SQL.
6. 🛑 **G-artifact**: an analyst reviews the logic.
7. 🛑 **G-signoff**: required before the result goes to execs.
8. Save the verified query to the golden set for reuse.

#### *FeedbackToPrototype variant-tested* · AWF-0007
`TEC › PRD › PROTO › create › prototype` · **L3** · valid · ES · E1
**Formula:** `IN(feedback) → GEN(theme clusters + quotes) ‖G-spec‖ → GEN(PRD) → CRIT(red-team) → FAN{GEN(prototype variant)} → [GEN]* ‖G-artifact‖ → VAL(5 user tests) → LRN`

**Execution**
1. Cluster tickets, call transcripts, and NPS verbatims into themes, each with counts and source-linked quotes.
2. 🛑 **G-spec**: the PM picks the problem to solve.
3. Draft the PRD: problem, users, non-goals, metrics, stories, edge cases. A critic red-teams it ("what would engineering push back on?").
4. Build 2–3 prototype variants (v0, Lovable, Bolt, Figma Make, Claude artifacts) from the PRD plus design tokens.
5. Iterate.
6. 🛑 **G-artifact**: design review.
7. Run 5 user tests and feed the transcripts back to step 1.

**Output:** the PRD and prototype become the input to AWF-0001 or AWF-0008.

#### *DesignToCode visual-diff* · AWF-0008
`TEC › PRD › DSYS › transform › ui-component-code` · **L3** · valid · ES · E3 [7]
**Formula:** `IN(frame link) → CTX(design context, variables, Code Connect map) → [GEN → VAL(render + screenshot diff)]* → ‖G-artifact‖ PUB`

**Execution**
1. Pull the frame's design context, variables (color, spacing, typography), and Code Connect mappings through the Figma MCP server [7].
2. Reuse mapped code components instead of re-creating them.
3. Use tokens only, with no hardcoded values.
4. Render, take a screenshot, compare with the Figma screenshot, and loop.
5. 🛑 **G-artifact**: designer review in a preview build.

**Output:** a PR. Token gaps are reported back to the design-system team.

### Kingdom PRO

#### *ScreenFunnel dual-llm-screen* · AWF-0009 · type of *ScreenFunnel*
`PRO › RES › LITREV › retrieve › systematic-review` · **L3** · valid · ES · E1/E2 [8][9]
**Formula:** `IN(PICO) → GEN(search strings) ‖G-spec‖ → FAN{ACT(database query)} → ASM(dedupe) → FAN{GEN(screen A), GEN(screen B)} → RTE: agree-exclude → sample | conflict or include → ‖G-sample‖ human → FAN{GEN(extract with quote + page)} ‖G-artifact‖ → GEN(synthesis) → VAL(citation resolver) → ‖G-signoff‖ PUB`

| Role | Tools |
|---|---|
| Search strategist | LLM + PubMed, Scopus, OpenAlex, and Semantic Scholar APIs |
| Screeners ×2 (independent) | Elicit, ASReview, Rayyan AI, or a custom classifier |
| Extractor | PDF parser (e.g. GROBID) → LLM into a fixed schema, quoting the source span |
| Verifier | Crossref DOI resolution + Zotero |

**Execution**
1. Draft Boolean and MeSH search strings. 🛑 **G-spec**: a librarian or PI approves, then the protocol is registered (PROSPERO, OSF).
2. Search, deduplicate, and log counts for the PRISMA flow diagram.
3. Two independent LLM screeners, each giving a reason per decision. **Tune for sensitivity, not accuracy.** A missed eligible study biases the result, and published sensitivity varies widely: a pooled 0.73 in one meta-analysis versus ~96% for dual-model ensembles in recent preprints [9]. 🛑 **G-sample**: calibrate against a human-screened set (sensitivity, Cohen's κ) before trusting the screeners at scale. Humans resolve all conflicts.
4. Full-text screening follows the same pattern with closer human involvement.
5. Extraction: every field quotes its source span and page. 🛑 **G-artifact**: humans verify 100% of the numbers that feed the meta-analysis.
6. Synthesis and draft: risk-of-bias table, meta-analysis script, narrative.
7. Resolve every reference and flag unsupported claims.
8. 🛑 **G-signoff**: authors take responsibility and disclose AI use. Under ICMJE, chatbots can't be authors and use must be disclosed [8].

**Output:** a PRISMA diagram, extraction dataset, draft manuscript, and an audit log of AI decisions.

#### *ResponseMatrix latexdiff* · AWF-0010
`PRO › RES › WRITE › transform › revised-manuscript` · **L2** · valid · ES · E1
**Formula:** `IN(reviews) → GEN(response matrix) ‖G-plan‖ → FAN{[GEN(edit / reanalysis) → VAL(compile, rerun scripts, cite keys)]*} → GEN(latexdiff + letter) → ‖G-artifact‖ → ‖G-signoff‖ PUB`

**Execution**
1. Parse the reviewer comments into `response.md` (comment → planned change → location).
2. 🛑 **G-plan**: the authors decide accept, rebut, or partial for each comment.
3. Run sub-agents per comment: text edits, re-run analyses and regenerate figures, add citations.
4. Compile and produce a `latexdiff` version.
5. Verify that every number matches the regenerated outputs and every citation key resolves.
6. Draft the response letter.
7. 🛑 **G-artifact/G-signoff**: the authors edit rebuttals for tone and substance.

#### *GroundedMemo cite-verified* · AWF-0025
`PRO › LEG › RESEARCH › retrieve › research-memo` · **L2** · valid · ES · E2 [24]
**Formula:** `IN ‖G-spec‖ → [CTX(grounded legal database) → GEN(IRAC memo)]* → FAN{VAL(cite exists, quote matches, holding supports, still good law)} → ‖G-signoff‖ PUB`

**Execution**
1. Frame the issue and jurisdiction. 🛑 **G-spec**.
2. Search primary law in a grounded database (Westlaw/CoCounsel, Lexis+ AI, Harvey), not the open web.
3. Draft an IRAC memo with pinpoint cites.
4. **Run a separate verification pass on every citation**, including a citator check.
5. 🛑 **G-signoff**: the attorney reads every authority cited.

**Why the `VAL` stage is mandatory:** in *Mata v. Avianca* (S.D.N.Y., sanctions June 22, 2023), counsel submitted ChatGPT-fabricated opinions with fake quotes and citations [24].

#### *PlaybookReview clause-parallel* · AWF-0024
`PRO › LEG › CONTRACT › verify › contract-redline` · **L3** · valid · ES · E2
**Formula:** `IN(.docx) → RTE(agreement type) → CTX(playbook) → FAN{GEN(clause vs. position: green/yellow/red)} → GEN(tracked changes + comments) → CRIT(defined terms, cross-references, caps vs. indemnities) → ‖G-artifact‖ → ‖G-signoff‖ ACT(send)`

**Execution**
1. Classify the agreement and load the matching playbook (standard positions, fallbacks, walk-away points per clause).
2. Segment the clauses, map each to a playbook entry, and flag missing clauses.
3. Analyze clauses in parallel for deviation.
4. Generate Word tracked changes with margin comments explaining each change.
5. Check internal consistency.
6. 🛑 **G-artifact**: an attorney reviews yellow and red items.
7. 🛑 **G-signoff**: the attorney sends.

**Strains:** `@harvey` · `@spellbook` · `@luminance` · `@claude-playbook-skill`

#### *ExtractMatchRoute three-way* · AWF-0022
`PRO › FIN › AP › operate › approved-payable` · **L4** · valid · DO · E3
**Formula:** `IN(invoice) → GEN(extract with per-field confidence) → VAL(vendor master, duplicates, bank-detail change) → VAL(PO ↔ receipt ↔ invoice) → GEN(GL coding) → RTE: matched under threshold → ACT(queue for payment) | exception → ‖G-escalate‖ ; ‖G-signoff‖ payment run`

**Rules:** a bank-detail change *always* escalates, because it's a fraud signal. Payment approval follows the delegation-of-authority matrix. The full audit trail is kept for SOX.

#### *EventDrivenUpdate cited-model* · AWF-0023
`PRO › FIN › INVEST › analyze › research-note` · **L3** · valid · ES · E2/E3 [23]
**Formula:** `CTX(consensus, guidance) → IN(release, filing, transcript) → FAN{GEN(KPI extract with citation)} → VAL(deltas vs. model) → ACT(Excel driver update, comment per cell) → GEN(transcript themes) → GEN(note) ‖G-artifact‖ → ‖G-signoff‖ (compliance) PUB`

**Strains:** `@claude-excel` (Claude for Excel beta since October 2025 [23]) · `@hebbia` · `@alphasense` · `@rogo`

#### *AmbientScribe linked-evidence* · AWF-0026 · type of *AmbientScribe*
`PRO › HLT › CLINDOC › transform › clinical-note` · **L3** · valid · DO · E2 [25][26]
**Formula:** `‖G-spec‖ (consent) IN(audio) → GEN(diarized transcript) → CTX(EHR problem list, meds) → GEN(specialty note + codes + patient summary) → VAL(sentence ↔ transcript links) → ‖G-artifact‖ → ‖G-signoff‖ PUB(EHR)`

**Execution**
1. 🛑 **G-spec**: patient consent to recording.
2. Ambient capture in the room or on a phone.
3. Diarized transcription, then a structured note in the specialty template.
4. Each note phrase links to its source audio or transcript. Abridge calls this "Linked Evidence," inside Epic Haiku → Hyperdrive [26].
5. 🛑 **G-artifact**: the clinician edits.
6. 🛑 **G-signoff**: the clinician signs and is the legal author.

**Strains:** `@abridge-epic` [26] · `@dragon-copilot` (launched March 2025; combines Dragon Medical One dictation with DAX ambient [25]) · `@nabla` · `@ambience`
**Habitat:** risk `high`, HIPAA, BAA required.

#### *BackwardDesign alignment-checked* · AWF-0027
`PRO › EDU › COURSE › create › course` · **L2** · valid · ES · E1
**Formula:** `IN(standards) → GEN(objectives by Bloom's level) ‖G-spec‖ → GEN(assessments + rubrics) → PLAN(modules) ‖G-plan‖ → FAN{GEN(lesson materials + differentiated versions)} → CRIT(every objective assessed; accuracy; accessibility) → ‖G-artifact‖ PUB(LMS import)`

#### *RubricGrader anchor-calibrated* · AWF-0028
`PRO › EDU › ASSESS › verify › graded-submission` · **L3** · valid · ES · E1
**Formula:** `‖G-spec‖ (rubric + 5–10 human-graded anchors) → [GEN(calibration grades) → VAL(agreement within 1 point)]* → FAN{GEN(score + evidence quote + feedback)} → RTE: low confidence → ‖G-sample‖ → ‖G-signoff‖ PUB`

Students can always request human review.

### Kingdom CRE

#### *BibleDrivenDraft continuity-checked* · AWF-0011 · type of *BibleDrivenDraft*
`CRE › WRI › FICTION › create › novel-manuscript` · **L2** · valid · ES · E1/E3 [10]
**Formula:** `IN(premise, voice samples) → GEN(bible via interview) ‖G-spec‖ → PLAN(beats → chapters → scene cards) ‖G-plan‖ → [CTX(scene card + bible entries + rolling summary + last ~2k words + voice samples) → GEN(scene) → CRIT(continuity) → CRIT(style sheet) → ‖G-artifact‖ → LRN(bible and summary)]*`

| Role | Responsibility | Strains |
|---|---|---|
| Bible keeper | Characters, places, timeline, rules | Sudowrite Story Bible, a guided pipeline from braindump → synopsis → outline → scenes [10]; NovelCrafter Codex, wiki entries linked into the manuscript with bring-your-own model [10]; Markdown vault + Claude Code |
| Outliner | Beats → scene cards (goal, conflict, outcome, POV, information revealed) | Same |
| Drafter | Scene prose | LLM with long context |
| Continuity checker | Fresh context; flags contradictions (eye color, travel time, premature knowledge) | Separate agent |
| Line editor | Style sheet: banned clichés, POV, tense | Critic agent |

**Gates:** 🛑 the author owns the bible (`G-spec`) and the outline (`G-plan`), where most creative control is exercised. The author also rewrites every chapter (`G-artifact`).
**Habitat note:** Amazon KDP requires disclosure of AI-*generated* text, images, and translations, even when heavily edited afterward. Purely AI-*assisted* work doesn't need disclosure [11]. Record which applies in each specimen.

#### *DailySerial xigang-driven* · AWF-0012
`CRE › WRI › SERIAL › create › serial-chapter` · **L3** · provisional · ES · E4 [12]
**Formula:** `CTX(top-ranked works: hooks, 爽点 cadence) → PLAN(大纲 → 卷纲 → 细纲, payoff every 1–3 chapters) ‖G-plan‖ → [CTX(细纲 + character sheet + previous summary) → GEN(~2,000-字 chapter) → VAL(names, power levels, timeline) → ‖G-artifact‖ PUB → IN(段评 reader comments) → LRN]*`
**Diagnosis vs. *BibleDrivenDraft*:** a different family (a cadenced chapter stream, not a manuscript), plus a reader-feedback `IN → LRN` loop inside every cycle.
**Habitat:** `lang:zh`. Platform risk: 番茄小说 faced an author boycott in 2024 over an AI-training supplementary agreement and added a way to opt out. In February 2025 it banned accounts for low-quality "water" (水文) content [12]. No explicit 起点 AI-content rule was found (§6). Status stays `provisional` until a specimen at E2 or better is deposited.

#### *BeatToScene coverage-read* · AWF-0013
`CRE › WRI › SCREEN › create › screenplay` · **L2** · valid · ES · E1 [13]
**Formula:** `IN(logline) → FAN{GEN(variants)} → CRIT ‖G-spec‖ → GEN(treatment → beat sheet → scene list) ‖G-plan‖ → [GEN(Fountain draft or writer draft) → CRIT(coverage persona) → GEN(multi-voice TTS table read) → ‖G-artifact‖]* → ‖G-signoff‖ PUB(Final Draft or Highland)`
**Compliance (WGA 2023 MBA, in effect through May 1, 2026; check successor terms):**
- AI-generated material is not "literary material" or "source material."
- Companies must disclose AI-generated material given to writers.
- Writers can't be required to use AI, but may choose to with company consent [13].

Log AI-assisted portions in each specimen.

#### *HookCadenceScript paywall-paced* · AWF-0014
`CRE › WRI › SCREEN › create › series-script` · **L3** · valid · DO (CN) · E2/E4
**Formula:** `CTX(top dramas: hooks, 反转 density, 卡点 placement) → GEN(core setup) ‖G-spec‖ → PLAN(60–100 one-line episodes, each ending on a cliffhanger) ‖G-plan‖ → FAN{batches of 10: GEN(episode)} → FAN{CRIT(3-second hook, end cliffhanger, line length, cast and location budget)} → ‖G-artifact‖ (head writer rewrites eps 1–10 + paywall ep) → VAL(content rules) → PUB(场次表)`
**Diagnosis vs. *BeatToScene*:** the family is a 60–100-episode series script with a monetization constraint (the paywall episode), and episodes are generated in parallel batches.
**Habitat:** domestic releases go through the NRTA's tiered review, with three categories by budget and subject. Platforms may not carry micro-dramas without a license or filing number [14]. **Downstream:** `uses` → AWF-0015, AWF-0016.

#### *ShotFactory character-locked* · AWF-0015 · type of *ShotFactory*
`CRE › MED › AIGCVIDEO › create › episode` · **L3** · valid · DO (CN) · E2 [15][16][17]
**Formula:** `IN(episode script) → PLAN(shot list) ‖G-spec‖ → CTX(character lock: turnaround sheets, references, LoRA) → FAN{[GEN(4 keyframes) → CRIT(VLM: identity match, artifacts) → SEL]*} → FAN{[GEN(image → video, 5–10 s) → VAL(morphing, physics)]*} → GEN(voice and lip-sync) → ASM(edit, captions, music) ‖G-artifact‖ → VAL(AI label) ‖G-signoff‖ PUB`

| Stage | Tools (CN / global) |
|---|---|
| Shot list (分镜: number, framing, camera move, action, dialogue, duration) | Doubao, DeepSeek, Claude, GPT |
| Character lock | 即梦 / Midjourney references; ComfyUI + per-character LoRA; Kling multi-image reference, 1–4 references per generation [17] |
| Keyframes | 即梦/Seedream, Flux, Midjourney |
| Motion | 可灵 Kling, 海螺 Hailuo, Vidu, Seedance, Veo, Runway |
| Voice and lip-sync | MiniMax, 火山引擎 TTS, ElevenLabs; lip-sync tools or native audio-video models |
| Assembly | 剪映/CapCut, Premiere |

**Execution**
1. Script → 20–40-shot list. 🛑 **G-spec**: the director approves the shot list and style frames.
2. Lock the characters. Practitioners generate front, side, and back views plus expression sheets, and use them as references in every later generation [16].
3. Generate 4 keyframe candidates per shot in parallel. A VLM critic filters, then a human selects.
4. Image → video per shot. Re-roll on morphing or physics breaks.
5. Generate voice per line with emotion tags, then lip-sync.
6. Assemble and check the first-3-seconds hook.
7. 🛑 **G-artifact**: the director lists re-rolls (loop back to step 3 or 4).
8. 🛑 **G-signoff**: compliance and labeling. CN rules require explicit and implicit labels on AI-generated content (in force since September 1, 2025 [15]). The draft 微短剧 regulation also requires a label in a visible position in every AI-generated episode [14].

**Reported economics (E3):** a brokerage report citing Ocean Engine data puts traditional 漫剧 at ¥2–5k per minute and AI-assisted production at ¥1–2.5k. It also reports one company cutting 11 production stages to 5 [16].
**Metrics to record in specimens:** usable-shot rate per generation, cost per finished minute, hours per episode.

#### *LiveActionAssist ad-cut-matrix* · AWF-0016
`CRE › MED › SHORTDRAMA › create › episode` · **L2** · valid · DO (CN) · E2/E4
**Formula:** `IN(script, uses AWF-0014) → GEN(场次表, cast, prop and location lists, location-optimized 7–10-day schedule) ‖G-spec‖ → GEN(previs keyframes) → [human shoot] → GEN(captions, rough-cut assembly from script alignment, color, VFX touch-ups) ‖G-artifact‖ → FAN{GEN(ad cuts × 20–50 hooks)} → ACT(投流 test) → SEL(by ROI) → ‖G-signoff‖ PUB`
**Diagnosis vs. *ShotFactory*:** the camera is human. AI occupies only the pre- and post-production stages, and the skeleton adds an ad-cut fan-out plus a market-selection loop.

#### *DubPipeline duration-fit* · AWF-0017
`CRE › MED › DUB › transform › localized-episode` · **L4** · valid · DO · E2/E3 [18]
**Formula:** `IN(episode + script) → GEN(diarized ASR, aligned to script) → CTX(per-series glossary + cultural notes) ‖G-spec‖ → FAN{lang: [GEN(translation) → VAL(fits line duration)]* → GEN(voice clone TTS) → GEN(lip-sync) → GEN(subtitles)} → ‖G-sample‖ (native QA: eps 1–10 in full, then sampled) → ‖G-signoff‖ PUB`
**Habitat:** overseas (出海) apps. ReelShort and DramaBox made roughly $130M and $120M in IAP in Q1 2025 [18]. Vendor claims for AI dubbing throughput (e.g. "120 minutes in 4–5 hours") are E3 and unverified.

### Kingdom COM

#### *ClusterBriefDraft editor-gated* · AWF-0018
`COM › MKT › CONTENT › create › web-article` · **L3** · valid · ES · E2 [19]
**Formula:** `IN(seed topics) → ACT(SEO API) → GEN(SERP-overlap clusters) ‖G-plan‖ → FAN{CTX(top-10 SERP) → GEN(brief) → CTX(product docs, SME input) → GEN(draft) → CRIT(facts, voice, links) → ‖G-artifact‖ ACT(CMS draft → publish)} → VAL(rank at 30/90 days) → LRN(refresh)`
**Constraint:** Google's March 2024 "scaled content abuse" policy targets mass-generated pages made mainly to rank, without adding value, whether automated or not [19]. That's why the `CTX(SME input)` stage and editor gate are part of this species' diagnosis.

#### *VariantMatrix performance-pruned* · AWF-0019
`COM › MKT › ADS › create › ad-variant-set` · **L3** · valid · ES · E3
**Formula:** `CTX(ad libraries, reviews, tickets) → GEN(angle × hook × format × persona matrix) ‖G-spec‖ → FAN{GEN(copy, static, avatar UGC video)} → VAL(claims and brand safety) ‖G-artifact‖ → ACT(bulk upload) → [IN(performance) → SEL(kill losers) → GEN(next matrix)]* weekly`

#### *ResearchThenPersonalize sampled* · AWF-0020
`COM › SAL › PROSPECT › operate › outbound-sequence` · **L3** · valid · ES · E3 [20]
**Formula:** `IN(ICP) → ACT(list build) → FAN{ACT(waterfall enrichment)} → FAN{GEN(research agent answers structured questions with source URLs)} → GEN(score and tier) → FAN{GEN(first line from research columns only)} ‖G-spec‖ (20-row sample) → ‖G-sample‖ 5–10% → ‖G-action‖ ACT(sequencer launch) → RTE(replies)`
**Practitioner pattern:** run cheap enrichment first, and spend agent-research credits (Claygent) only on accounts that fit the ICP [20].

#### *ProcedureAgent code-enforced-limits* · AWF-0021 · type of *ProcedureAgent*
`COM › CSX › RESOLVE › operate › resolved-conversation` · **L4** · valid · DO · E2/E3 [21][22]
**Formula:** `CTX(KB + procedures) → [IN(message) → RTE: info → GEN(answer) | transactional → VAL(authenticate) → ‖G-action‖ (limits in code) ACT(tool) | sensitive → ‖G-escalate‖]* → ‖G-sample‖ (QA scores every conversation; humans review flagged and random ones) → LRN(KB-gap clusters)`

**Execution**
1. Rewrite tribal knowledge as natural-language procedures with explicit conditions and limits. Decagon AOPs compile these into workflows where refunds and identity checks run in code [21]. Intercom Fin Procedures and Sierra journeys are equivalent strains.
2. Route each message by intent.
3. Authenticate before any account action.
4. 🛑 **G-action**: limits are enforced in code, not in the prompt.
5. 🛑 **G-escalate**: hand off with a summary.
6. 🛑 **G-sample**: QA.
7. Turn weekly KB-gap clusters into new articles.

**Metric caution:** resolution rates aren't defined the same way across vendors. Fin's site reportedly claims a 76% average, while independent and small-business tests cluster at 38–53% [22]. Decagon customer figures above 70% come from an analyst write-up [21]. All are E3.

### Kingdom ORG

#### *SourceScreenSchedule evidence-not-verdict* · AWF-0029
`ORG › BIZ › HR › operate › candidate-pipeline` · **L3** · valid · ES · E3 [27][28][29]
**Formula:** `IN(JD) ‖G-spec‖ → FAN{ACT(source)} → GEN(match rationale per criterion) → ‖G-action‖ ACT(outreach) → FAN{GEN(evidence summary, no reject decision)} → ACT(schedule) → GEN(interview kits) → ‖G-signoff‖ (human hiring decision)`
**Strains:** `@linkedin-hiring-assistant` (global English release by end of September 2025; sources candidates, screens via InMail Q&A, schedules [29]) · `@paradox` · `@juicebox`
**Why the species epithet matters (compliance):**
- **NYC LL144.** It requires an annual independent bias audit before an AEDT is used, a public summary of the results, and candidate notice 10 business days in advance. The employer is responsible, not the vendor [27].
- **EU AI Act.** It classifies recruitment AI as high-risk. Its obligations were originally due August 2, 2026, and the Digital Omnibus provisionally moves them to December 2, 2027. Confirm which date is legally in force [28].

Keeping the agent at *evidence*, never *verdict*, reduces exposure to both.

#### *IssueTreeResearch claims-table* · AWF-0030
`ORG › BIZ › STRAT › retrieve › research-deck` · **L3** · valid · ES · E1
**Formula:** `IN(key question) → PLAN(MECE issue tree) ‖G-spec‖ → FAN{GEN(deep research per branch)} → ASM(claims table: claim, number, source, date, confidence) → FAN{VAL(re-fetch source per number)} → GEN(so-what pages) ‖G-artifact‖ → GEN(deck from firm template)`

#### *DailyTriage draft-only* · AWF-0031
`ORG › XFN › INBOX › operate › triaged-inbox` · **L2** · valid · ES · E1
**Formula:** `IN(scheduled 07:00: email, calendar, DMs) → RTE(action / FYI / delegate / archive) → FAN{GEN(reply saved as draft)} → GEN(slot proposals) → GEN(top-5 brief) → ‖G-action‖ (human sends every message, accepts every invite)`
**Guard:** inbound email is untrusted input (prompt-injection surface). The agent may never send on its own.

---

## 4. Catalog Status

### 4.1 Genera described

| Kingdom | Phylum | Genera (type species ID) | Unoccupied classes (backlog) |
|---|---|---|---|
| TEC | SWE | *PlanGatedBuild* (0001), *FanOutCodemod* (0002), *DelegatedPR* (0003) | TEST, REVIEW, DEBUG, ARCH |
| TEC | ITS | *TriageThenRemediate* (0004), *EnrichAndAdjudicate* (0005) | INFRA, APPSEC, HELPDESK |
| TEC | DAT | *GovernedQuery* (0006) | DATAENG, DS, MLOPS |
| TEC | PRD | *FeedbackToPrototype* (0007), *DesignToCode* (0008) | PM, UXR, UI |
| TEC | ENG | none | all (niche, EM) |
| PRO | RES | *ScreenFunnel* (0009), *ResponseMatrix* (0010) | ANALYSIS, GRANT, PEER |
| PRO | LEG | *PlaybookReview* (0024), *GroundedMemo* (0025) | LITIG, REG, DD |
| PRO | FIN | *ExtractMatchRoute* (0022), *EventDrivenUpdate* (0023) | CLOSE, FPA, AUDIT, TAX |
| PRO | HLT | *AmbientScribe* (0026) | RCM, CLINTRIAL, DRUGDISC |
| PRO | EDU | *BackwardDesign* (0027), *RubricGrader* (0028) | TUTOR, LND |
| CRE | WRI | *BibleDrivenDraft* (0011), *DailySerial* (0012), *BeatToScene* (0013), *HookCadenceScript* (0014) | NONFIC, JOURN, TECHW, TRANS |
| CRE | MED | *ShotFactory* (0015), *LiveActionAssist* (0016), *DubPipeline* (0017) | POST, AUDIO, GAMEART |
| COM | MKT | *ClusterBriefDraft* (0018), *VariantMatrix* (0019) | SOCIAL, LIFECYCLE, MKTRES |
| COM | SAL | *ResearchThenPersonalize* (0020) | DEAL, RFP, REVOPS |
| COM | CSX | *ProcedureAgent* (0021) | QA, KB, CS |
| ORG | BIZ | *SourceScreenSchedule* (0029), *IssueTreeResearch* (0030) | PROC, PMO, ADMIN |
| ORG | GOV | none | all (niche, EM) |
| ORG | XFN | *DailyTriage* (0031) | MEET, PKM |

**Totals:** 5 kingdoms · 18 phyla (16 occupied) · 31 genera · 31 species (each currently the type of its genus) · 30 `valid` + 1 `provisional`.

### 4.2 Convergence view (trait query example)

`pattern: eval-opt` appears independently in SWE (0001, 0002), RES (0009), WRI (0011, 0014), MED (0015, 0017), MKT (0019), and EDU (0028). That's analogous evolution across five kingdoms, which confirms it belongs in the character matrix, not the rank hierarchy.

---

## 5. Implications for Phase 2

1. **Directory = taxonomy path down to genus.** Order and family live in front matter to keep paths shallow:
   `taxa/<KINGDOM>/<PHYLUM>/<CLASS>/<Genus>/<species-epithet>/{README.md, strains/, specimens/<date>-<slug>/}`
2. **CI can enforce the code mechanically:**
   - The formula grammar parses.
   - The genus signature equals the formula with its gates stripped.
   - The key answers in the PR template reproduce the claimed placement.
   - Serial IDs are unique.
   - `valid` requires a holotype folder.
3. **Contribution templates** are needed for three things: (a) new specimen of an existing species (the most common case), (b) new species, (c) taxonomic revision.
4. **Generated views** ("field guides") come from front matter: by profession (SOC crosswalk), by industry habitat, by trait (e.g. all `L4` with `risk:high`), and by region (CN 短剧/网文 guide).

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
| 16 | AI 漫剧 cost and market | ✓ (E3) ¥2–5k → ¥1–2.5k per minute. ⚠ Market-size estimates conflict (¥18.9B vs. ¥24.3B), so none is stated. | [16] |
| 17 | Kling supports character consistency | ✓ Multi-image reference (January 2025). ⚠ Kling-specific lip-sync not confirmed, so the wording is generalized. | [17] |
| 18 | ReelShort and DramaBox scale | ✓ ~$130M and ~$120M IAP in Q1 2025 | [18] |
| 19 | Google penalizes scaled AI content | ✎ Made precise: the "scaled content abuse" policy (March 2024) applies whatever the production method | [19] |
| 20 | Clay Claygent and waterfall enrichment | ✓ (E3) | [20] |
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
| — | Tools listed only in strain or role tables (Datadog Bits AI, incident.io, Dropzone, Hebbia, Rogo, Harvey, Spellbook, Arcads, Creatify, MagicSchool, Paradox, Juicebox, Hailuo, Vidu, Seedance, etc.) | ⚠ Not individually re-verified. They're used as strain labels only, and none of the claims depend on them. | — |

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
