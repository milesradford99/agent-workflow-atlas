# Conversion to the entry standard: status and remaining work

A handover note for whoever (person or agent) finishes converting the catalog to [STANDARD.md](STANDARD.md). Delete this file in the pull request that completes Part C.

State on 2026-11-14: **155 of 238 entries converted, 83 left.** `validate.py`, `build_index.py --check`, `build_diagrams.py --check` and `i18n.py status` all pass on this branch.

The aim behind the whole exercise: a reader must not be handed anything stale. Agent tooling changes monthly, so every entry's Build section is designed for today's tools, and every entry says what has changed since its sources.

## How to work

Everything an agent needs is in the repository. Do the parts in order: A, then B, then C.

**Setup, once per session**

```bash
pip install -r scripts/requirements.txt
```

```bash
python scripts/validate.py
```

The last line must read `OK: 238 workflows, N in the STANDARD.md format`. Note `N`.

The session needs open network access: source pages are spread over hundreds of sites. Read pages with `python scripts/read_page.py <URL>`. Some sites refuse automated readers (403 or 406 from uber.com, doordash, snowflake, openai.com, whatnot, faire, rocket, glovo, joinheadway). That is expected: flag the entry `source-unreachable` and carry on. Do not try to get round a refusal.

**One batch = one agent, one at a time.** No parallel agents; they are not needed and the batches were sized for a single cheap model (about 220,000 to 270,000 tokens and 8 to 10 minutes for 7 entries on a mid-size model).

For each batch in Part A:

1. Give the agent the text of [research/prompts/convert.md](research/prompts/convert.md) from the line "You are converting entries" to the end, with `<MONTH>` set to the current month (for example `2026-11`), `<CUTOFF>` set to twelve months earlier (`2025-11`), and `<ENTRIES>` set to the batch's lines from the table below. Add one line naming a converted entry from a nearby field as an extra example (suggestions are given per batch).
2. When it returns, run the four checks:

   ```bash
   python scripts/validate.py
   ```

   ```bash
   python scripts/build_index.py
   ```

   ```bash
   python scripts/build_diagrams.py --check
   ```

   ```bash
   python scripts/i18n.py status
   ```

   `validate.py` must end with `OK` and the count must have gone up by the batch size. `i18n.py status` must show `0 behind the English, 0 with problems, 0 missing`. If an entry fails, send the error text back to the same agent; do not fix it by weakening the check.
3. Check that only the batch's folders changed: `git status --short` should list only their `README.md` and `README.zh-CN.md`, plus `INDEX.md`.
4. Read one converted entry of the batch in full, English and Chinese. Reject and redo if: the Build section claims a result (time saved, accuracy); it names a tool or feature not in the STANDARD.md §3 table; the Background assumes the reader knows the field; the Chinese has fewer steps, or different numbers or links, than the English; a link was added to a page the agent says it did not open.
5. Update the count in the CHANGELOG.md line "N of the 238 entries are converted so far".
6. Copy the agent's report table into the "Batch reports" section at the end of this file, tick the batch below, commit, push. Commit message: `Convert <n> <field> entries to the entry standard`.

If a session is cut off mid-batch: run `python scripts/validate.py`. Entries that pass and whose `python scripts/i18n.py check <ID>` prints `OK` are finished and can be committed. Restore any other touched folder with `git checkout -- <folder>` and put it back in a batch.

To list what is still unconverted at any time:

```bash
grep -L '^build:' workflows/*/*/*/*/README.md workflows/unplaced/*/README.md
```

## Part A: convert the remaining 83 entries

Extra example for batches 5 to 7: `workflows/TEC/ITS/SRE/triage-then-remediate`. Batches 8 to 10: `workflows/TEC/DAT/DS/repo-grounded-analysis`. For the rest, pick an already converted entry in the same phylum (`grep -l '^build:' workflows/<K>/<P>/*/*/README.md`).

- [ ] **Batch 5** (security, 6)
  - AWF-0005 workflows/TEC/ITS/SECOPS/alert-enrich-and-adjudicate
  - AWF-0128 workflows/TEC/ITS/SECOPS/detonate-and-confirm-detections
  - AWF-0187 workflows/TEC/ITS/SECOPS/purple-team-detection-build
  - AWF-0129 workflows/TEC/ITS/APPSEC/ai-fuzz-target-hunting
  - AWF-0067 workflows/TEC/ITS/APPSEC/sanitizer-bug-autopatch
  - AWF-0188 workflows/TEC/ITS/APPSEC/scheduled-vuln-fix-prs
- [ ] **Batch 6** (IT helpdesk, infrastructure, product planning and prototypes, 7)
  - AWF-0189 workflows/TEC/ITS/HELPDESK/self-repair-before-handoff
  - AWF-0068 workflows/TEC/ITS/HELPDESK/slack-it-request-agent
  - AWF-0066 workflows/TEC/ITS/INFRA/chat-to-iac-change
  - AWF-0186 workflows/TEC/ITS/INFRA/plan-verified-drift-fixes
  - AWF-0060 workflows/TEC/PRD/PM/spec-to-ticket-planning
  - AWF-0007 workflows/TEC/PRD/PROTO/feedback-to-prototype
  - AWF-0232 workflows/TEC/PRD/PROTO/in-codebase-handoff-prototype
- [ ] **Batch 7** (design systems and UI, 6)
  - AWF-0194 workflows/TEC/PRD/DSYS/agent-eval-docs-loop
  - AWF-0008 workflows/TEC/PRD/DSYS/design-to-code
  - AWF-0122 workflows/TEC/PRD/DSYS/scored-token-migration
  - AWF-0231 workflows/TEC/PRD/UI/designer-authored-ui-pr
  - AWF-0121 workflows/TEC/PRD/UI/routed-accessibility-pr-agent
  - AWF-0062 workflows/TEC/PRD/UI/spec-bound-screen-options
- [ ] **Batch 8** (user research and marketing, 7)
  - AWF-0120 workflows/TEC/PRD/UXR/agent-run-interviews
  - AWF-0195 workflows/TEC/PRD/UXR/pr-reviewed-research-wiki
  - AWF-0061 workflows/TEC/PRD/UXR/quote-verified-synthesis
  - AWF-0171 workflows/COM/MKT/MKTRES/backtested-synthetic-panel
  - AWF-0055 workflows/COM/MKT/MKTRES/routed-competitive-digest
  - AWF-0053 workflows/COM/MKT/SOCIAL/plan-to-calendar-drafting
  - AWF-0225 workflows/COM/MKT/LIFECYCLE/ranker-guided-creative-slate
- [ ] **Batch 9** (CAD, manufacturing, simulation, 6)
  - AWF-0116 workflows/TEC/ENG/CAD/agent-drafted-pcb-schematic
  - AWF-0056 workflows/TEC/ENG/CAD/phased-preview-build
  - AWF-0119 workflows/TEC/ENG/MFG/ai-first-cam-program
  - AWF-0059 workflows/TEC/ENG/MFG/drawing-to-route-draft
  - AWF-0057 workflows/TEC/ENG/SIM/engineer-checked-cfd-run
  - AWF-0193 workflows/TEC/ENG/SIM/unattended-simulation-campaign
- [ ] **Batch 10** (building codes and construction submittals, 6)
  - AWF-0058 workflows/TEC/ENG/CODECOMP/cited-pre-screen-checks
  - AWF-0117 workflows/TEC/ENG/CODECOMP/pre-submittal-plan-check
  - AWF-0118 workflows/TEC/ENG/CODECOMP/zoning-rule-study-crew
  - AWF-0151 workflows/TEC/ENG/SUBMITTAL/first-pass-submittal-review
  - AWF-0235 workflows/TEC/ENG/SUBMITTAL/rule-set-verdict-review
  - AWF-0190 workflows/TEC/ENG/SUBMITTAL/spec-to-submittal-register
- [ ] **Batch 11** (customer support and retail catalog, 7)
  - AWF-0021 workflows/COM/CSX/RESOLVE/procedure-agent
  - AWF-0108 workflows/COM/CSX/RESOLVE/resident-maintenance-triage
  - AWF-0175 workflows/COM/CSX/RESOLVE/supervised-voice-agent
  - AWF-0111 workflows/COM/RET/CATALOG/catalog-copy-factory
  - AWF-0112 workflows/COM/RET/CATALOG/confidence-sampled-attribute-extraction
  - AWF-0113 workflows/COM/RET/CATALOG/copilot-attribute-suggestions
  - AWF-0114 workflows/COM/RET/CATALOG/supplier-confirmed-catalog-fixes
- [ ] **Batch 12** (video, 短剧, screenwriting, localisation, 7). Several sources are Chinese; keep Chinese industry terms as written and define them under Terms.
  - AWF-0138 workflows/CRE/MED/POST/autonomous-live-recap
  - AWF-0202 workflows/CRE/MED/POST/editor-curated-broadcast-clips
  - AWF-0077 workflows/CRE/MED/POST/transcript-first-video-edit
  - AWF-0016 workflows/CRE/MED/SHORTDRAMA/live-action-assist
  - AWF-0013 workflows/CRE/WRI/SCREEN/beat-to-scene-screenplay
  - AWF-0014 workflows/CRE/WRI/SCREEN/hook-cadence-drama-script
  - AWF-0136 workflows/CRE/WRI/TRANS/term-gated-game-localisation
- [ ] **Batch 13** (agriculture, strategy, government, 7)
  - AWF-0236 workflows/ORG/AGR/ADVISORY/agronomist-gated-push-advisories
  - AWF-0211 workflows/ORG/AGR/ADVISORY/extension-agent-mediated-advice
  - AWF-0154 workflows/ORG/AGR/ADVISORY/plot-registered-agronomy-advice
  - AWF-0228 workflows/ORG/BIZ/STRAT/qa-agent-competitive-brief
  - AWF-0143 workflows/ORG/GOV/CIVIC/officer-checked-planning-data-extraction
  - AWF-0204 workflows/ORG/GOV/POLICY/statute-mapped-regulatory-review
  - AWF-0080 workflows/ORG/GOV/POLICY/theme-sign-off-consultation-analysis
- [ ] **Batch 14** (education and medical coding, 5)
  - AWF-0103 workflows/PRO/EDU/LND/ai-role-play-practice
  - AWF-0043 workflows/PRO/EDU/LND/sme-docs-to-elearning
  - AWF-0102 workflows/PRO/EDU/TUTOR/guardrailed-course-tutor
  - AWF-0042 workflows/PRO/EDU/TUTOR/tutor-approved-ai-turns
  - AWF-0090 workflows/PRO/HLT/RCM/exception-routed-autonomous-coding
- [ ] **Batch 15** (legal and peer review, 7)
  - AWF-0035 workflows/PRO/LEG/LITIG/validated-genai-first-pass
  - AWF-0036 workflows/PRO/LEG/REG/obligations-register-build
  - AWF-0160 workflows/PRO/LEG/REG/sampled-dsar-disclosure
  - AWF-0025 workflows/PRO/LEG/RESEARCH/grounded-legal-memo
  - AWF-0170 workflows/PRO/RES/PEER/added-ai-review
  - AWF-0046 workflows/PRO/RES/PEER/review-of-review-feedback
  - AWF-0106 workflows/PRO/RES/PEER/submission-intake-screen
- [ ] **Batch 16** (research writing and unplaced, 7)
  - AWF-0169 workflows/PRO/RES/WRITE/end-to-end-ai-paper
  - AWF-0010 workflows/PRO/RES/WRITE/reviewer-response-revision
  - AWF-0221 workflows/unplaced/formulary-checked-discharge-supply
  - AWF-0215 workflows/unplaced/pharmacist-verified-script-entry
  - AWF-0212 workflows/unplaced/incident-to-signed-investigation
  - AWF-0152 workflows/unplaced/layered-safety-audit-agents
  - AWF-0147 workflows/unplaced/analyst-verified-lease-abstracts
- [ ] **Batch 17** (unplaced, 5). One unplaced entry is already converted and is a usable example: find it with `grep -l '^build:' workflows/unplaced/*/README.md`.
  - AWF-0234 workflows/unplaced/agent-built-replenishment-plans
  - AWF-0213 workflows/unplaced/cited-interconnection-readiness-review
  - AWF-0237 workflows/unplaced/cited-outage-revalidation
  - AWF-0214 workflows/unplaced/dispatcher-overridden-job-assignment
  - AWF-0238 workflows/unplaced/pre-arrival-troubleshooting-assist

Part A is done when `grep -L '^build:' ...` prints nothing and `validate.py` reports `238 in the STANDARD.md format`. Then reword the CHANGELOG.md line to say every entry is converted.

## Part B: bring the first 132 conversions up to the same freshness rule

The first 132 entries were converted in an earlier session under a looser rule: a search for newer accounts was required only when the newest source was older than twelve months, and it is not recorded which source pages were actually opened. Only two of them state "No newer account found". The 23 entries converted after that (AWF-0133, 0070, 0182, 0130, 0180, 0069, 0131, 0181, 0132, 0063, 0124, 0191, 0192, 0006, 0123, 0125, 0064, 0126, 0065, 0185, 0127, 0230, 0004) and everything in Part A already follow the stricter rule and need no Part B pass.

List the 132:

```bash
git diff --name-only 7179c69 5083a9c -- workflows | grep '/README.md$' | xargs grep -l '^build:'
```

Work through them 8 per batch, grouped by class in the order that command prints, one agent at a time. The brief for each batch:

> You are re-checking entries in the Agent Workflow Atlas that are already in the STANDARD.md format. Month: `<MONTH>`. Entries: `<ENTRIES>`. Read STANDARD.md §3 (the building-block table and the Timeliness rules) first. For each entry: (1) open every link under Sources and Public runs with `python scripts/read_page.py <URL>`; a site that refuses stays unopened, do not get round it. (2) Run two or three web searches for newer accounts of the same practice and for each tool named in `variants` (renamed, withdrawn, superseded); open what you find. (3) Re-read the Build section against STANDARD.md §3: is the form still the smallest that works, does every named building block appear in the table? (4) Edit only the `## Build it with an agent` section: correct the form or a building block if wrong, and rewrite **Since the sources** so it gives the sources' date range, says which pages were opened this month, reports what is newer with month and link (or "No newer account found as of `<MONTH>`."), and says plainly where the sources' method has been superseded. Never link a page you did not open. If `build` changes, change the `build:` field and the **Form:** line together. (5) Set `method_checked: <MONTH>`. Set `last_verified: <MONTH>` only if every source and public run opened and still supports the entry. (6) Make the same edits in `README.zh-CN.md` and run `python scripts/i18n.py stamp <ID>`. (7) `python scripts/validate.py` and `python scripts/i18n.py check <ID>` must pass. Do not change steps, shape, Public runs or Sources; do not commit; do not run `build_index.py`. Never invent a source, number, tool or feature. Report a table: ID | Sources opened (n of m) | Form changed? | What changed in Since the sources | Problems found (a step the source does not support, a dead link, a citation fault).

After each batch run the four checks, read one entry, commit, push, and copy the report table to the end of this file.

## Part C: review and loose ends

These need judgement; give them to a stronger model or a person, after A and B.

- [ ] **`platform` verdicts.** List with `grep -l '^build: platform' workflows/*/*/*/*/README.md workflows/unplaced/*/README.md` (23 on 2026-11-14). For each, read the Build section: `platform` is right only if STANDARD.md §3's earlier rows truly do not fit. Downgrade where a `service` would do.
- [ ] **Entries flagged unsure of form.** Current verdict stands unless the review disagrees: AWF-0070 (service; kit is project-style), AWF-0132 (skill; one source is event-triggered), AWF-0063 (project; one source ran solo with skills), AWF-0124 (skill; source ran as a Slack bot), AWF-0125 (skill; source does not say how a run starts), AWF-0065 (project vs service).
- [ ] **AWF-0130** `profile-led-perf-fixes`: step 5 and the per-diff developer-review checkpoint are only partly supported. Uber's post says output feeds "downstream tools for code transformation or manual review by developers" and that validated suggestions flow into Optix; it does not say every diff is developer-reviewed before merge. Re-read the source and either soften the step or change the checkpoint (if the shape changes, rerun `build_diagrams.py`).
- [ ] **AWF-0006** `governed-query`: steps carry no citations and both public runs refuse automated readers (OpenAI 403, Uber 406). Open them in a browser, add citations or flag the entry.
- [ ] **AWF-0126** `calibrated-judge-quality-loop`: the Dropbox source lists a second author, Dmitriy Meyerzon, missing from the citation.
- [ ] **Sources no automated reader could open** (check by hand in a browser, then set `last_verified`): AWF-0180 (DoorDash, Glovo), AWF-0124 (Headway), AWF-0191 (Snowflake), AWF-0192 (Whatnot; Ramp returned only a title), AWF-0126 (DoorDash), AWF-0065 (Rocket, Faire), AWF-0006 (above), plus whatever Parts A and B add.
- [ ] **AWF-0185, AWF-0127, AWF-0230, AWF-0004** were converted in a batch that was stopped before its agent reported. They pass every check and each **Since the sources** says its sources were opened, but no flags were collected. Read all four in full.
- [ ] **AWF-0069**: a search suggested `qodo-cover` may be unmaintained; unconfirmed. Check its repository and update `variants` and **Since the sources**.
- [ ] Per research/prompts/convert.md, read three converted entries per batch in full before merging.
- [ ] Delete this file; reword the CHANGELOG.md entry; tick the pull request's checklist.

## Batch reports

Paste each batch's report table here, newest last.

**Batch 1 (2026-11-14), network blocked at the time; sources re-read in batch 3**

| ID | Form | Why this form | Flags |
|---|---|---|---|
| AWF-0133 | skill | One author, one comment at a time, in the conversation | outdated-method (2023 fine-tuned in-house model; build uses a general agent) |
| AWF-0070 | service | Runs on every commit in CI, nobody present | unsure-of-form (service vs project) |
| AWF-0182 | service | A PR-opened event starts the run unattended | |
| AWF-0130 | service | Daily scheduled batch; developers see scored diffs | step 5 only partly supported (Part C) |
| AWF-0180 | service | Daily cron with tickets; two stops answered later | source-unreachable (DoorDash, Glovo) |

**Batch 2 (2026-11-14)**

| ID | Form | Why this form | Sources opened | Flags |
|---|---|---|---|---|
| AWF-0069 | skill | One engineer, one class at a time | 1 of 1 | `qodo-cover` status unconfirmed |
| AWF-0131 | skill | Engineer states one concern, works class by class | 1 of 1 | |
| AWF-0181 | skill | Developer starts the sweep and triages the report | 1 of 1 | |
| AWF-0132 | skill | One engineer per flaky test | 2 of 2 | unsure-of-form (skill vs service) |
| AWF-0063 | project | Per-model parity and no-cutover rules need hooks | 3 of 3 | unsure-of-form (skill vs project) |
| AWF-0124 | skill | Engineer starts each investigation and decides on the fix | 0 of 1 | source-unreachable (Headway); unsure-of-form (skill vs service) |
| AWF-0191 | service | Starts from failure webhook or timer, nobody present | 1 of 2 | source-unreachable (Snowflake) |

**Batch 3 (2026-11-14)**

| ID | Form | Why this form | Sources opened | Flags |
|---|---|---|---|---|
| AWF-0192 | service | Slack questions from many people; data team samples answers | 1 of 3 | source-unreachable (Whatnot, Ramp body) |
| AWF-0006 | skill | One analyst, one question, present for review | 0 of 2 | source-unreachable; steps carry no citations |
| AWF-0123 | service | Scheduled run, owner reviews after publish | 1 of 1 | |
| AWF-0125 | skill | One data scientist reviews one readout | 1 of 1 | unsure-of-form (skill vs service) |
| AWF-0064 | project | Multi-day analysis needs hooks and standing repo knowledge | 1 of 1 | |
| AWF-0126 | service | Daily judging, nobody present | 1 of 2 | source-unreachable (DoorDash); second author missing |
| AWF-0065 | project | Unattended loop; a hook must lock the eval code | 1 of 3 | source-unreachable (Rocket, Faire); unsure-of-form (project vs service) |

**Batch 4 (2026-11-14), stopped early: 4 of 7 finished, no report (see Part C)**

AWF-0185, AWF-0127, AWF-0230, AWF-0004 converted. AWF-0005, AWF-0128, AWF-0187 moved to batch 5.
