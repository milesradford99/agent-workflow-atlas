# Where Are the Real Runs? Public Evidence for the 31 Workflows

**Date:** 2026-11-06
**Key question:** for each of the 31 workflows, is there a public, detailed, first-hand write-up of a real run whose author could be invited to contribute an example?
**How it was made:** this is an [Issue-tree research (AWF-0030)](../workflows/ORG/BIZ/STRAT/issue-tree-research/) run. The method and the run log are in [Method](#method).

## Summary

| Coverage | Workflows | Count |
|---|---|---|
| **Strong**: a first-hand, detailed run that matches most of the shape | 0001, 0002, 0003, 0005, 0009, 0011, 0017, 0021, 0026, 0031 | 10 |
| **Partial**: first-hand, but only part of the shape or a different checkpoint | 0004, 0006, 0008, 0013, 0015, 0016, 0018, 0020, 0022, 0024, 0028, 0029, 0030 | 13 |
| **Weak**: only anonymous, vendor-linked or journalist-told accounts | 0012, 0014 | 2 |
| **None found** | 0007, 0010, 0019, 0023, 0025, 0027 | 6 |

**So what:**

1. **Coverage follows where engineers blog.** Software, ops and security have the most first-hand runs, with exact numbers and public repos. Law, finance, education and marketing have the fewest: four of the six "none found" are there. The other two are product (0007) and academic writing (0010). Example runs for those fields will have to come from practitioners directly.
2. **Real runs often put checkpoints in different places than our shapes do.** For example:
   - YC's recruiting agent sends rejections when the manager tells it to, but AWF-0029 says "no reject decision".
   - Ljubljana's grader releases final grades without a low-confidence sample (AWF-0028).
   - Socialstyrelsen replaces one of the two screeners with an LLM ensemble (AWF-0009).
   - One inbox agent (Murchison) can send mail, while AWF-0031 says a person sends every message.

   Under the swap test, some of these are new workflows, not examples. The shapes may also describe a stricter practice than most teams actually follow.
3. **短剧 and 网文 evidence is mostly second-hand.** Named studios appear only through journalist interviews, and the most detailed process accounts (lunxiao.com, tixiaolu.com) are anonymous. Dashverse (dubbing, AWF-0017) is the one first-hand engineering write-up.
4. **No consulting firm has published a run of AWF-0030 itself.** The nearest are a single-session data study (MKT1) and Anthropic's research-system build, and neither has a human plan gate. This run is the first public example.

## Top 10 outreach candidates

Ranked by shape match × detail × how easy it would be to contribute. Only public channels are listed. Nobody has been contacted.

| # | Who | Workflow | Why | Public channel |
|---|---|---|---|---|
| 1 | dotnet/runtime team, Stephen Toub (Microsoft) | 0003 Delegated PR | Near-exact shape and ten months of numbers, with a public repo and a public instructions file | github.com/dotnet/runtime |
| 2 | HumanLayer (BAML work) | 0001 Plan-gated build | Plan-gated research → plan → implement, with public prompts and public PRs | github.com/humanlayer |
| 3 | Databricks security incident response | 0005 Alert enrich and adjudicate | Enrich → verdict → auto-close or hand off, with strong numbers. They already plan to sample closed alerts, which fills the missing 🛑 sample | databricks.com blog |
| 4 | Socialstyrelsen (Fagerberg et al.) | 0009 Screening funnel | A national guideline deployment with a prespecified two-person audit. They plan an MIT / CC BY 4.0 release | medRxiv article page |
| 5 | UC Davis Health (Taylor, Adams et al.) | 0026 Ambient scribe | A peer-reviewed deployment with a reusable note-quality review, CC BY 4.0. They could add the consent step | JMIR Med Inform article page |
| 6 | Dashverse (Goel, Tetali) | 0017 Dubbing pipeline | First-hand engineering post with volumes and reviewer retention rates; close shape | insiders.dashverse.ai |
| 7 | Nubank (Gupta et al.) | 0021 Procedure agent | A regulated organization with authentication, handoff and human-labelled evaluation, CC BY 4.0 | arXiv 2606.08867 |
| 8 | Pedro Sant'Anna | 0031 Daily inbox triage | Scheduled, drafts-only triage with every action gated, in an MIT repo with an issue tracker | github.com/pedrohcgs/claude-code-my-workflow |
| 9 | Jon McNestrie | 0011 Bible-driven novel draft | Bible + locked voice + human-promoted critic notes, with a public template repo | github.com/jmcnestrie/novel-harness |
| 10 | FutureSearch (Daniel Hnyk) | 0018 Cluster-brief-draft content | A first-hand rank-check → refresh loop with a human PR gate and an open repo | github.com/futuresearch/example-cc-cronjob |

Strong alternates: Harper Reed (0031), Slack (0002), Pinecone (0021), Matt Garrett (0011), the YC software team (0029, as a possible new workflow).

## Claims table

Every row was re-opened by a second agent that didn't do the original search. **Number** is the page's own wording. **First-hand** means: `yes` (the organization or person describing its own run), `vendor` (a vendor writing about a customer, or about its own product), `interview` (a journalist relaying a named team), `anon`, or `no` (not a run). **Conf.** is confidence that the source shows a real run of this workflow.

### TEC

| AWF | Source | What the run shows | Number (page wording) | First-hand | Conf. |
|---|---|---|---|---|---|
| 0001 | [HumanLayer, *Advanced Context Engineering for Coding Agents*](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md) (no byline or date; images Aug 2025) | Research → plan → implement on a 300k-LOC Rust codebase; a human reviews the research and the plan | "shipping 35k LOC to BAML"; "spent 7 hours" | yes | high |
| 0001 | [Harper Reed, *My LLM codegen workflow atm*](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/) (2025-02-16) | Spec → prompt plan (TDD variant) → step by step, testing after each | "This entire process will take maybe 15 minutes." (planning) | yes | med |
| 0002 | [Sergii Gorbachov, Slack Engineering](https://slack.engineering/balancing-old-tricks-with-new-feats-ai-powered-conversion-from-enzyme-to-react-testing-library-at-slack/) (2024-05-22) | AST codemod + LLM with DOM context; rubric on sample files; humans verify | "80% of the content within these files was accurately converted"; "saving of 22% of developer time" | yes | high |
| 0002 | [Ziftci et al., Google, arXiv 2504.09691](https://arxiv.org/abs/2504.09691) (2025-04-13) | 39 int32→int64 migrations, edits per file with validation; failures go to people | "74.45% of the code changes and 69.46% of the edits were generated by the LLM" | yes | high |
| 0002 | [Anthropic, *How Anthropic runs large-scale code migrations*](https://claude.com/blog/ai-code-migration) (2026-07-16) | Rulebook → throwaway 3-file stress test → fan-out implement-review-fix → phase gates | "fanned out across all 1,448 files"; "Nineteen regressions surfaced after merge" | yes (own product) | med |
| 0002 / 0003 | [Charas & Bruggmann, Spotify Engineering](https://engineering.atspotify.com/2025/11/spotifys-background-coding-agent-part-1) (2025-11-06) | Fleet migrations in containers with an LLM judge; teams review the PRs | "merged more than 1500 pull requests"; "60–90%" time saving | yes | high |
| 0003 | [Stephen Toub, .NET Blog](https://devblogs.microsoft.com/dotnet/ten-months-with-cca-in-dotnet-runtime/) (2026-03-23) | Maintainers assign issues → agent PR → bot review → humans steer and merge | "all 878 CCA PRs"; "67.9% success rate"; "3 were reverted (0.6%)" | yes | high |
| 0004 | [Hsu, Neu, Farrag, Kindi, Meta Engineering](https://engineering.fb.com/2024/06/24/data-infrastructure/leveraging-ai-for-efficient-incident-response/) (2024-06-24) | Retriever + LLM ranker → top-5 suspect code changes for responders to check | "42% of these investigations had the root cause in the top five" | yes | med |
| 0004 | [Goutham Veeramachaneni, *I built an AI SRE in 60 mins*](https://www.gouthamve.dev/i-built-an-ai-sre-in-60mins-you-should-too/) (2026-04-21) | Replays recent pages against a knowledge base; opens runbook-update PRs that people review | "the false positive rate is less than 10% now" (no evals) | yes | med |
| 0004 | [Chatwoot, *Introducing Faultline*](https://faultline.chatwoot.com/blog/introducing-faultline) (2026-02-18) | A read-only agent investigates their own incidents across PagerDuty, New Relic, Sentry, AWS and GitHub | "typically makes 25-30 API calls" | yes | med |
| 0005 | [Shapton, Hanify, Pezzino, Databricks](https://databricks.com/blog/scaling-security-alert-triage-specialized-agents-databricks) (2026-07-06) | 17 per-source agents enrich → escalate / monitor / close; analysts decide escalations | "over 18,000 alerts with a 3.2% escalation rate"; "over 6,500 analyst hours in the first 30 days" | yes | high |
| 0005 | [Aaron Jewitt, Elastic Security Labs](https://www.elastic.co/security-labs/alert-triage-agentic-soc-elastic-workflows) (2026-07-02) | Deterministic checks → 20+ enrichment sources → triage and specialist agents → verdict | "30-minute manual alert triage into under 3 minutes" | yes (own product) | high |
| 0005 | [Mo & Stöckli, GitHub Security Lab](https://github.blog/security/ai-supported-vulnerability-triage-with-the-github-security-lab-taskflow-agent/) (2026-01-20) | Facts → false-positive audit → validated report → labelled issue | "~30 real world vulnerabilities" | yes | med |
| 0006 | [Xu, Suresh, Tang, OpenAI, *Inside our in-house data agent*](https://openai.com/index/inside-our-in-house-data-agent) (2026-01-29) | Schema, lineage and docs as context; SQL self-check; saved corrections; golden-SQL evals | "more than 3.5k internal users"; "70k datasets" | yes | med |
| 0006 | [Johnson, Busch, Khune, Uber, *QueryGPT*](https://www.uber.com/blog/query-gpt/) (2024-09-19) | Curated SQL samples → intent, table and column agents; the user confirms tables | "about 300 daily active users, with about 78%" reporting time saved | yes | med |
| 0007 | [Teresa Torres, Product Talk](https://www.producttalk.org/ai-prototyping-lovable/) (2025-08-13) | Interviews → scope → Lovable variants → internal user tests | "From idea to user validation, it just took us 11 days" | no (second-hand) | low |
| 0008 | [Jenny Xie, Figma blog, on Coinbase](https://www.figma.com/blog/how-coinbase-used-code-connect-to-shrink-token-costs/) (2026-09-02) | Frame link → MCP + Code Connect → agent implements; a designer checks components | "cost by 22.5%"; "time to implementation by 22.3%"; three runs | vendor | med |

### PRO

| AWF | Source | What the run shows | Number (page wording) | First-hand | Conf. |
|---|---|---|---|---|---|
| 0009 | [Fagerberg et al., Socialstyrelsen, medRxiv](https://www.medrxiv.org/content/10.64898/2026.06.02.26354724v1.full) (2026-06) | A locked LLM ensemble screens for 24 guideline reviews; two blinded methodologists audit a prespecified sample | "screened 74,679 records"; "415 to 34 person-days"; of 600 audited exclusions "none was confirmed as a final false negative" | yes | high |
| 0009 | [Gartlehner et al., RTI and partners, medRxiv](https://www.medrxiv.org/node/963738) (2025-03-21) | LLM first-pass extraction in six live reviews, verified by people, against human-only extraction | "9,341 data elements, extracted from 63 studies"; "precision of 98.9%"; "41 minutes per study" | yes | high |
| 0010 | [Pedro Sant'Anna, claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | Has a `/respond-to-referees` skill, but no real revision run is shown | "18 agents, 61 skills" | no (template) | low |
| 0022 | [Subudhi, Vagvala, Jain Devichand, Uber Engineering](https://www.uber.com/blog/advancing-invoice-document-processing-using-genai) (2025-04-17) | OCR → LLM extraction → rule checks → side-by-side human review → ERP | "overall accuracy rate of 90%"; handling time "by 70%"; "25-30% cost saving" | yes | med |
| 0023 | [Financial Datasets, *EarningsBench*](https://financialdatasets.ai/blogs/earningsbench) (2026-06-29) | KPI extraction from 60 releases, checked by hand: a benchmark, not a model update | "Opus 4.6 with Extended Thinking hit 99.3% accuracy" | no (benchmark) | low |
| 0024 / 0025 | [Ashurst, *Vox PopulAI*](https://www.ashurstperkinscoie.com/en/insights/vox-populai-lessons-from-a-global-law-firms-exploration-of-generative-ai) (2024-06-10) | Firm-wide trials; four expert lawyers blind-score AI against human work | "45% on creating first draft legal briefings"; "3 out of 5" vs "3.5 out of 5" | yes | med |
| 0026 | [Taylor … Adams, UC Davis Health, JMIR Med Inform 2026;14:e86474](https://escholarship.org/content/qt9r89g3sp/qt9r89g3sp.pdf) (pilot Jul–Aug 2024) | 31 physicians, 7,545 notes; 356 rated for omissions and hallucinations; physicians approve each note | "94.7% (337/356) free from significant errors"; "hallucinations (n=41, 11.5%)" | yes | high |
| 0028 | [Poličar, Špendl, Curk, Zupan, Ljubljana, arXiv 2501.14499](https://arxiv.org/html/2501.14499v1) (2025-01-24) | Rubric + up to 10 TA-graded examples, refined on 25% of submissions; LLM grades final unless a student appeals | "average CA scores ranging between 85% and 90%" | yes | high |
| 0028 | [Luke Korthals, UvA Teaching & Learning Centres](https://tlc.uva.nl/en/?p=51154) (undated) | Canvas submissions → AI feedback PDFs → upload; compared with four human graders | "the initial setup took about a month" | yes | med |

### CRE

| AWF | Source | What the run shows | Number (page wording) | First-hand | Conf. |
|---|---|---|---|---|---|
| 0011 | [Jon McNestrie, *Writing a novel with Claude Code*](https://medium.com/@JonMcNestrie/writing-a-novel-with-claude-code-a-ci-pipeline-for-prose-6f8f30c71bb1) (2026-07-07) | A bible repo with a locked voice file; critics write notes and the human picks which apply | "about ten rules extracted from your own edits"; "five in the core team" | yes | high |
| 0011 | [Matt Garrett, *How I Used AI To Write KDP GameLit Novel*](https://mattgarrett.com/how-i-used-ai-to-write-kdp-gamelit-novel/) (2026-09-10) | Story, world and continuity bibles; approved items locked as canon; batch revision; whole-book continuity audit | "102,737 words, 32 chapters"; "eight revision batches" | yes | high |
| 0011 | [George Saoulidis, *How to Write a Sequel Using AI*](https://georgesaoulidis.com/how-to-write-a-sequel-using-ai/) (2025-09-21) | Book 1 as context → bible → scene list → chapter by chapter → edits | "Asked for 40 scenes list"; "more than 100k words" | yes | med |
| 0012 | [提效录, *AI写小说进阶2026*](https://www.tixiaolu.com/posts/ai-novel-writing-advanced-2026/) (Advanced AI web-novel writing, 2026-03-28) | A claimed 180-day serial: 大纲 → 卷纲 → daily 细纲 → AI drafts → comment-driven plot changes | "总字数218万字，总收入达到了38万元" | anon | low |
| 0012 | [老高的AI研究室, WeChat](https://mp.weixin.qq.com/s/i2_RA8tdSVGy6LEf15Krdw) (Author with 570k readers reveals AI workflow, undated) | 章纲 → segment drafting → AI review → light human edit | "单月稿费成功突破 3 万元" | interview (unnamed author; carries a tool referral code) | low |
| 0013 | [Russell S.A. Palmer, *We Wrote a 100-Page Movie Script in 10 Days*](https://russellsapalmer.medium.com/we-wrote-a-100-page-feature-film-in-10-days-using-saga-and-chatgpt-316f45e0f4ad) (2025-10-28) | Logline → 40-beat outline → scenes drafted with a tool, then edited by people | "a 100-page first draft, written part-time over 10 days" | yes (reads like tool promotion) | med |
| 0013 | [Peter & David Luisi, *The Last Screenwriter*](https://lastscreenwriter.com/the-screenplay/) (2024) | The AI wrote the screenplay; people only selected and shortened scenes | (none) | yes | low |
| 0014 | [光影联盟编辑部, lunxiao.com](https://www.lunxiao.com/article.html?id=23310) (Producer's review of a micro-drama script process, 2026-09-21) | Study top dramas → hook-density table → paywall at eps 8–12 → ad-test eps 1–5 → rewrite | "台词通常在180到250字之间"; "ROI回升了0.2左右" | anon | low |
| 0014 | [小树 for GPLP, NetEase](https://m.163.com/dy/article/LAJ3VILB05118D5B.html) (A writer torn between AI and herself, 2026-10-31) | The AI makes the mind map and outline; lines and 爽点 timing stay human | "半个月上线一部AI短剧" (title) | interview | med |
| 0014 / 0015 | [新民周刊 p.41](https://img1.xinmin.cn/xmzk/2026-07-13/410713.pdf) (Xinmin Weekly, 2026-07-13) | AI review before human review; scripts expanded for AI production | "近七成都无法过审"; "5万字…可能要补充到8万字" | interview | med |
| 0015 | [毒眸 on 钛媒体](https://www.tmtpost.com/7712427.html) (How a 10-person team made an AI manhua drama in 45 days, 2025-10-02) | 珀乐互动: artist-drawn originals → AI video → edit; weekly director review | "一个仅10人的团队，用45天时间，完成了50集《明日周一》" | interview | high |
| 0015 | [PJ Ace, *I can't believe Disney allowed us to run this AI ad*](https://pjace.beehiiv.com/p/i-can-t-believe-disney-allowed-us-to-run-this-ai-ad-during-the-nba-finals-f77e73388ab4ca62) (2025-06-11) | Rough script → AI shot list and prompts → generate and re-prompt → edit | "300–400 generations to get 15 usable clips"; "One person, two days." | yes | high |
| 0015 | [金姬, 新民周刊](https://www.xinminweekly.com.cn/bianjituijian/2026/04/08/41135.html) (A one-person animation factory?, 2026-04-08) | Storyboard frames picked from many generations → image-to-video | "110多张分镜与定稿图的1700多次AI'抽卡'"; "近20人的团队" | interview | med |
| 0016 | [重庆日报 via 新华网](http://www.cq.xinhuanet.com/20260615/742fac2865f9486c86e0137a1e6993fe/c.html) (85 episodes shot in 10 days, 2026-06-15) | AI script breakdown and shoot plan → previs → live-action shoot | "85集的短剧，拍摄时间只用了10天…200万元"; breakdown "只需15分钟" | interview (studio's own tool) | med |
| 0016 | [子路, FoST未来叙事 via 观察者网](https://user.guancha.cn/main/content?id=1752038) (How 《行镖》 ran AI + live action) | Previs shoot → about half a month at 横店 → AI, live-action and post groups run in parallel | "第一集生成的图片资产，就达到了 300多张"; "30多位AI组成员" | interview | med |
| 0016 | [光影联盟, lunxiao.com](https://www.lunxiao.com/article.html?id=23821) (Review of ad-creative iteration, 2026-09-22) | Scenes graded S/A/B/C → several cuts each → 3-hour data refresh → kill by 3-second view rate | "接近900条视频素材"; ROI "0.17" → "2.3到2.8" | anon | low |
| 0017 | [Goel & Tetali, Dashverse](https://insiders.dashverse.ai/building-an-ai-dubbing-pipeline-for-micro-dramas/) (2026-10-12) | Diarized script rebuild → per-show glossary → duration-fit translation → cast TTS → human review of every show | "about 1,400 hours of micro-dramas across 16 languages"; reviewers kept "about 95%…89%…96%" | yes | high |
| 0017 | [传神语联 via 数据猿, Tencent Cloud](https://developer.cloud.tencent.com/article/2708997) (Transn multilingual short-drama case, 2026-07-14) | Story understanding → AI translation → post-edit with duration fit → voice-clone dubbing → AI and human QA | "每月配音短剧数量300部起，配音集数超2000集"; "AI负责约85%" | vendor | med |
| 0017 | [娱乐资本论 on 钛媒体](https://www.tmtpost.com/7526126.html) (Who holds the key to AI dubbing?, 2025-04-08) | A studio reruns a client drama through an AI dubbing tool, with human re-checks mandatory | "把一周的工作压缩到了一天" | interview (studio unnamed) | low |

### COM

| AWF | Source | What the run shows | Number (page wording) | First-hand | Conf. |
|---|---|---|---|---|---|
| 0018 | [Daniel Hnyk, FutureSearch](https://futuresearch.ai/blog/self-optimizing-seo-pipeline/) (2026-03-18) | Search Console → per-page analyzer agents → PR; a person picks which changes to make | "69 changes proposed"; "The human spends 20 minutes deciding" | yes | high |
| 0018 | [Victoria Olsina, *AI for SEO Content: 6-Month Test*](https://victoriaolsina.com/blog/ai-seo-content/) (2025-12-26) | Brief → AI draft → founder input → human edit and fact-check | "from 2-3 to 8-10 long-form articles monthly" | yes (site not named) | med |
| 0018 | [The SEO Agent Team](https://www.theseoagent.ai/blog/ai-seo-case-study) (updated 2026-09-19) | Keyword queue → 8 clusters → drafts → checks → published with no human gate stated | "61 new pages in roughly fifteen weeks" | vendor (own site) | med |
| 0019 | [Angad Singh, Segwise, on Curtis Howland's test](https://segwise.ai/blog/115k-ai-ugc-platform-test-findings.md) (2026-03-23) | Five AI-avatar UGC tools on the same offers and audiences | "2.42x ROAS at a $70 CPA"; "$115k experiment" | no (second-hand) | low |
| 0019 | [Arcads, Teknasyon use case](https://www.arcads.ai/usecases/teknasyon) (2025-12-17) | Bulk avatars to test angles, then scale the winners | "76% drop in Cost per Purchase and a 40% ROAS uplift" | vendor | low |
| 0020 | [Grigorij Altshuler, RevSculpt](https://revsculpt.com/articles/clay-for-outbound) (2026-10-05) | Signals → waterfall enrichment → research columns with evidence URLs → scoring → openers → CRM routing | "86% verified emails"; "bounced at 1.3%" vs "22%"; "About 48 held (55 booked)" | yes (unnamed clients) | med |
| 0020 | [Clay, Rippling customer story](https://clay.com/customers/rippling) (undated) | Enrich → persona segments → 12+ variants → sequencer | "2x year over year performance of our cold email channel in 2023" | vendor | low |
| 0020 | [Jack Jundanian, Lindy, *Clay review*](https://wf.lindy.ai/blog/clay-review) (updated 2026-10-19) | A four-week tool test; no Clay outcomes given | "the same 200-contact list" | no (tool review) | low |
| 0021 | [Gupta et al., Nubank, arXiv 2606.08867](https://arxiv.org/abs/2606.08867) (2026-06) | Five production deployments: routines, tools behind identity checks, escalation, human-labelled evaluation | "37 percentage-point improvement in AI transactional Net Promoter Score" | yes | high |
| 0021 | [Jackson Gold, Pinecone](https://www.pinecone.io/blog/support-agent-nexus/) (2026-09-01) | Ticket routing → account lookups → investigation → escalation brief for refunds and limits | "resolves 55.1% of the tickets"; "27 of the 49" | yes (early, small sample) | high |
| 0021 | [Decagon, Tremendous case study](https://decagon.ai/case-studies/tremendous) (undated) | Two-factor ownership check → resend, cancel or exchange → escalate with context | "92% CSAT… compared with 86% for its BPO team" | vendor | med |
| 0021 | [Intercom Community, Fin resolution thread](https://community.intercom.com/questions/3622) (2023–2026) | Practitioners report resolution rates and how they maintain their knowledge base | "around 55-60% from the past week, in around 3000 conversations" | yes (forum) | low |

### ORG

| AWF | Source | What the run shows | Number (page wording) | First-hand | Conf. |
|---|---|---|---|---|---|
| 0029 | [YC software team, yc-software/recruiting](https://github.com/yc-software/recruiting) | Claude Code commands for triage, outreach, scheduling and candidate briefs; the manager approves each step, **including rejections** | "27 inbox emails, 38 active candidates"; 8 applicants rated, "about 2 minutes" | yes | med |
| 0029 | [LinkedIn, Infinite Resource Solutions story](https://business.linkedin.com/hire/customer-stories/infinite-resource-solutions) (undated) | Sourcing → export to the ATS → scoring against recruiter criteria | "2–3 hours per day"; "48 hours to less than a day" | vendor | low |
| 0030 | [Emily Kramer, MKT1](https://newsletter.mkt1.co/p/state-of-marketing-report-part-3-how-to-research-in-claude-code) (2026-05-06) | 100 companies researched one data point at a time; the spreadsheet is the source of truth; spot-checks; published report | "100 high-growth B2B startups, 90+ data points each"; "burned 250 Clay credits" | yes | high |
| 0030 | [Hadfield et al., Anthropic Engineering](https://www.anthropic.com/engineering/multi-agent-research-system) (2025-06-13) | Lead agent → 3–5 parallel subagents → citation pass; humans only in evaluation | "outperformed single-agent Claude Opus 4 by 90.2%"; "about 15× more tokens" | yes (own product) | high |
| 0030 | [Graydon Trusler, claude-code-heavy](https://github.com/gtrusler/claude-code-heavy) | Worktrees → 2–8 parallel research assistants → synthesis | "Assistants: 6"; "~11,500 words" | yes | med |
| 0031 | [Harper Reed, *Getting Claude Code to do my emails*](https://harper.blog/2025/12/03/claude-code-email-productivity-mcp-agents/) (2025-12-03) | Mail, calendar and contacts over MCP → drafts only; he sends every message, after an unapproved send | "the past couple hundred emails I have sent" (voice training) | yes | high |
| 0031 | [Pedro Sant'Anna, `/triage-inbox`](https://github.com/pedrohcgs/claude-code-my-workflow) | Scheduled morning triage → buckets → drafts → proposed calendar holds; every outbound action needs confirmation | triage-inbox v2.0 (config, no run narrative) | yes | high |
| 0031 | [Mike Murchison, claude-chief-of-staff](https://github.com/mimurchison/claude-chief-of-staff) | `/gm` brief + three-tier triage with drafts; **sending is allowed**, with no approval step described | "from 90 minutes of morning inbox processing to about 5" | yes | med |

## Gaps

| AWF | What was searched for | What turned up instead |
|---|---|---|
| 0007 Feedback to prototype | PM write-ups that cluster feedback, write a PRD, prototype and test with users | Vendor guides; one second-hand interview |
| 0010 Reviewer-response revision | LLM-assisted revisions with a response letter and latexdiff, in blogs and preprints | Skill and prompt repos; systems papers |
| 0019 Ad variant matrix | Creative-strategist or brand write-ups of AI ad matrices with kill rules | Vendor case studies; a second-hand test report |
| 0023 Event-driven model update | Analyst posts on LLM model updates in Excel | Vendor pages; one benchmark |
| 0025 Grounded legal memo | Law-firm memo workflows with citation checks | A Stanford benchmark (not a run); sanctions news |
| 0027 Backward-design course | Teaching-centre reports of AI backward design with human review | Workshops; one design exercise with no course taught |

Pages that wouldn't open (Zhihu, a Bun post, a Pinterest post, the KP Division of Research, an EDUCAUSE piece) weren't counted. The Kaiser Permanente ambient-scribe work (NEJM Catalyst 2024) is probably strong for AWF-0026, but its primary pages failed to load.

## Method

This report is a run of AWF-0030. The steps below follow its shape.

1. **Key question → MECE issue tree.** The tree split by kingdom (TEC, PRO, CRE, COM, ORG), so every workflow sits in exactly one branch. Each workflow got four sub-questions: does a first-hand account exist, is it detailed, does it match the shape, and can its author contribute.
2. **🛑 Plan.** The maintainer approved the tree, the rules (first-hand only, public channels only, no contact) and the deliverables before any research started (2026-11-06 05:36 UTC).
3. **Each branch: deep research.** Five subagents ran in parallel, one per branch, and the CRE branch searched in Chinese too. In total: about 99 searches and about 101 page fetches.
4. **Claims table.** The results were merged into the tables above.
5. **Each number: re-fetch source.** Four separate checker agents re-opened all 65 sources:
   - every key number was found on its page;
   - about 20 author, date or wording corrections were made;
   - no source was dropped.
6. **So-what pages → 🛑 review → deck.** See the summary above and the deck. The maintainer's review is recorded in the example run.

Everything here is public information as of 2026-11-06. Numbers are as the sources state them, unaudited.
