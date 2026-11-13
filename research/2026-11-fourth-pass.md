# Fourth Collection Pass

**Date:** 2026-11-13
**Question:** which of the catalog's weakest classes can gain a workflow backed by detailed first-hand evidence, and which unplaced fields can reach the three workflows a new class needs?

## Result

23 new draft workflows, AWF-0216 to AWF-0238, bring the catalog to 238. All 23 are evidence A: 20 have Strong public-run coverage and 3 have Partial. Five new categories opened, so the taxonomy now has 22 phyla and 92 classes.

| | Count |
|---|---|
| New, placed in an existing class | 17 |
| New, filed into a class opened in this pass | 3 |
| New, unplaced | 3 |
| Evidence A / B | 23 / 0 |
| Public runs: Strong / Partial | 20 / 3 |

## Quality bar

The third pass accepted vendor material as evidence B. This pass did not. A workflow went in only if a named organization or practitioner described its own production use or a completed run, with the steps, the human checkpoints and at least one measured number. Vendor case studies, product pages, demos and estimated figures could appear as extra sources but could not carry an entry. Each entry also had to pass the swap test against every workflow already in its class.

The research targeted the 37 classes that had no entry that was both evidence A and Strong. 13 of them now have one: AIGCVIDEO, CONTENT, CS, DEAL, DRUGDISC, INVEST, LIFECYCLE, LITIG, NONFIC, SRE, STRAT, SUBMITTAL and TAX. CLOSE and PROTO gained evidence-A entries with Partial coverage. INBOX, UI and PHARMACY gained second strong entries.

## New taxonomy

Each new class opened with three workflows (TAXONOMY.md rule 2). IDs did not change when folders moved.

| Class | Workflows | Opened by |
|---|---|---|
| `PRO/INS/UW` insurance underwriting | AWF-0149, 0155, 0163 | already had three |
| `ORG/LOG/FREIGHT` freight brokerage (new phylum `LOG`, logistics and supply chain) | AWF-0150, 0153, 0209 | already had three |
| `ORG/LOG/CUSTOMS` customs | AWF-0148, 0210, 0233 | Flexport's pre-transmission entry audit |
| `TEC/ENG/SUBMITTAL` construction submittals | AWF-0151, 0190, 0235 | the Hong Kong EMSD rule-set review pilot |
| `ORG/AGR/ADVISORY` farm advisory (new phylum `AGR`, agriculture) | AWF-0154, 0211, 0236 | PxD's PaddyAI advisories |

Still unplaced:
- pharmacy ×2 (AWF-0215, 0221);
- EHS ×2;
- energy ×2: interconnection review and outage revalidation, which may share a grid-operations class;
- field service ×2: dispatch and troubleshooting;
- real estate ×1 (lease abstraction; AWF-0108 sits in COM);
- supply planning ×1 (AWF-0234).

## Method

1. **Plan.** All 215 workflows were exported with their evidence grade and coverage. The work was split into eight groups and a maintainer approved the split: six aimed at the weak classes, one at logistics and one at physical-world fields. Agents were asked for 0–1 workflows per class.
2. **Research.** Eight agents worked in parallel from [research/prompts/collect.md](prompts/collect.md), with the stricter bar above added to the brief. They read pages through Exa. A usage limit stopped all eight partway through; they resumed from where they stopped.
3. **Drop.** Two candidates were dropped:
   - a social-reply workflow: the account was a vendor describing one day of using its own product;
   - a partner-onboarding workflow: the checkers found that both of its accounts were anonymous or third-person.
4. **Re-check.** Three separate checkers ([research/prompts/check.md](prompts/check.md)) re-opened all 49 cited links: 39 public runs and 10 sources.
   - Every claimed number matched its page and every link opened.
   - Six first-hand labels were changed, to interview or study.
   - One source did not describe the step it was first matched with. It is cited only for the retrospective audit service it does describe.
   - The pre-arrival step of the KONE workflow was confirmed by hand on KONE's own page.
5. **File.** Entries were generated in the standard format. Five classes were opened and their workflows moved. Chinese versions were written with `scripts/i18n.py` and the style guide, and every check passes.

## Coverage gaps

24 of the 37 classes still have no entry that is both evidence A and Strong:
- **Placed classes:** ADMIN, AP, ARCH, AUDIT, CLOSE, DD, FPA, LND, MEET, MFG, PKM, PMO, POST, PROC, PROTO, REG, RESEARCH, SCREEN, SERIAL, SHORTDRAMA and SOCIAL.
- **Unplaced fields:** EHS, energy interconnection and field-service dispatch.

For most of these the agents found only vendor case studies, press coverage, or workflows already in the catalog; the reasons and search lists are in the agents' output. Short drama and serial fiction have plenty of Chinese industry coverage, but no first-hand 复盘 with steps and numbers turned up.

## Caveats

- **Thin numbers.**
  - Several Strong entries rest on one first-hand account.
  - Knak's prototype handoff gives one developer's remark as its only number.
  - Rippling's QBR result comes from 15 test accounts.
- **Who wrote it.**
  - Rivian's accrual workflow is published on the AWS blog, co-written by Rivian engineers.
  - Flexport's customs audit rests on its CEO's posts and a product broadcast. Flexport runs the brokerage itself, so these count as first-hand.
- **Not peer-reviewed.** JD.com's planning workflow comes from a preprint written with JD staff, so it is graded a study.
- **Risk.** Judicial drafting, pharmacy and grid outages are tagged `high`.

## New workflows

| ID | Workflow | Class | Evidence | Public runs |
|---|---|---|---|---|
| AWF-0216 | [Agent-researched trading signals](../workflows/PRO/FIN/INVEST/agent-researched-trading-signals/) | PRO › FIN › INVEST | A | strong |
| AWF-0217 | [Expert-approved taxability rules](../workflows/PRO/FIN/TAX/expert-approved-taxability-rules/) | PRO › FIN › TAX | A | strong |
| AWF-0218 | [Owner-confirmed PO accruals](../workflows/PRO/FIN/CLOSE/owner-confirmed-po-accruals/) | PRO › FIN › CLOSE | A | partial |
| AWF-0219 | [Agent-team binder design](../workflows/PRO/HLT/DRUGDISC/agent-team-binder-design/) | PRO › HLT › DRUGDISC | A | strong |
| AWF-0220 | [Judge-decided opinion drafting](../workflows/PRO/LEG/LITIG/judge-decided-opinion-drafting/) | PRO › LEG › LITIG | A | strong |
| AWF-0221 | [Formulary-checked discharge supply](../workflows/unplaced/formulary-checked-discharge-supply/) | unplaced (proposed PRO › HLT › PHARMACY) | A | strong |
| AWF-0222 | [Signed-contract validation](../workflows/COM/SAL/DEAL/signed-contract-validation/) | COM › SAL › DEAL | A | strong |
| AWF-0223 | [Confirmed-inputs QBR deck](../workflows/COM/CSX/CS/confirmed-inputs-qbr-deck/) | COM › CSX › CS | A | strong |
| AWF-0224 | [Diffed article refresh](../workflows/COM/MKT/CONTENT/diffed-article-refresh/) | COM › MKT › CONTENT | A | strong |
| AWF-0225 | [Ranker-guided creative slate](../workflows/COM/MKT/LIFECYCLE/ranker-guided-creative-slate/) | COM › MKT › LIFECYCLE | A | strong |
| AWF-0226 | [Animatic-gated AI commercial](../workflows/CRE/MED/AIGCVIDEO/animatic-gated-ai-commercial/) | CRE › MED › AIGCVIDEO | A | strong |
| AWF-0227 | [Dictation-to-memoir manuscript](../workflows/CRE/WRI/NONFIC/dictation-to-memoir-manuscript/) | CRE › WRI › NONFIC | A | strong |
| AWF-0228 | [QA-agent competitive brief](../workflows/ORG/BIZ/STRAT/qa-agent-competitive-brief/) | ORG › BIZ › STRAT | A | strong |
| AWF-0229 | [Ledger-earned inbox actions](../workflows/ORG/XFN/INBOX/ledger-earned-inbox-actions/) | ORG › XFN › INBOX | A | strong |
| AWF-0230 | [Team-agent incident triage](../workflows/TEC/ITS/SRE/team-agent-incident-triage/) | TEC › ITS › SRE | A | strong |
| AWF-0231 | [Designer-authored UI PR](../workflows/TEC/PRD/UI/designer-authored-ui-pr/) | TEC › PRD › UI | A | strong |
| AWF-0232 | [In-codebase handoff prototype](../workflows/TEC/PRD/PROTO/in-codebase-handoff-prototype/) | TEC › PRD › PROTO | A | partial |
| AWF-0233 | [Pre-transmission entry audit](../workflows/ORG/LOG/CUSTOMS/pre-transmission-entry-audit/) | ORG › LOG › CUSTOMS | A | partial |
| AWF-0234 | [Agent-built replenishment plans](../workflows/unplaced/agent-built-replenishment-plans/) | unplaced (proposed ORG › LOG › PLANNING) | A | strong |
| AWF-0235 | [Rule-set verdict review](../workflows/TEC/ENG/SUBMITTAL/rule-set-verdict-review/) | TEC › ENG › SUBMITTAL | A | strong |
| AWF-0236 | [Agronomist-gated push advisories](../workflows/ORG/AGR/ADVISORY/agronomist-gated-push-advisories/) | ORG › AGR › ADVISORY | A | strong |
| AWF-0237 | [Cited outage revalidation](../workflows/unplaced/cited-outage-revalidation/) | unplaced (proposed ORG › ENE › OUTAGECOORD) | A | strong |
| AWF-0238 | [Pre-arrival troubleshooting assist](../workflows/unplaced/pre-arrival-troubleshooting-assist/) | unplaced (proposed ORG › FSV › TROUBLESHOOT) | A | strong |
