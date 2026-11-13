---
id: AWF-0156
name: 仅自动批准的预授权
summary: "对明确符合医疗政策的预授权请求自动批准；拒绝只能由持证临床人员作出，工具接受审计与监控。"
deliverable: 预授权决定
shape: "医疗机构提交预授权请求 (门户/ePA) → 引导式标准问题 → 对照医疗政策 + 既往记录核查请求 → 标准明确满足：自动批准 + 授权号 | 未满足 / 不完整：🛑 handoff (持证临床人员审阅；只有人可以拒绝) → 向医疗机构返回决定 → 🛑 sample (工具接受审计与监控)"
source_hash: b00198dbd6d6
---

# 仅自动批准的预授权

**与相近工作流的区别：** AWF-0032 按标准把关的预授权（Criteria-gated prior auth）是医疗机构一侧（辅助）：工作人员准备并提交请求。本工作流是保险支付方一侧，采用抽检：智能体无需逐项人工批准就发出批准，人只处理未获批准的余下部分，外加审计。产出是决定，而不是提交材料包。
**工具变体：** `premera-clara` · `hcsc-blueapprovr` · `cohere-health` · `florida-blue-in-house`

## 步骤

1. 医疗机构以电子方式提交预授权请求；工具只问评估该请求 'the precise number of questions required to evaluate'（平均约 6 分钟即可提交）[[2]](#sources)[[4]](#sources)。
2. 引擎对照医疗政策/临床标准核查请求，对部分编码还会核对历史授权和理赔；它 'helps identify requests that clearly meet medical criteria' [[1]](#sources)[[2]](#sources)。
3. 标准满足且信息完整：请求实时自动批准，授权号返回到门户 [[1]](#sources)[[4]](#sources)。
4. 🛑 **接手**：凡未自动批准的，都交给持证临床人员（保险计划的医疗管理人员/护士和医师审阅人）；工具从不拒绝：请求只会被批准，或转入 'only approved or advanced to a hands-on review by an HCSC clinician' [[1]](#sources)[[2]](#sources)[[3]](#sources)[[4]](#sources)。
5. 最终决定（批准、部分批准或拒绝）发送给提交方 [[4]](#sources)。
6. 🛑 **抽检**：'Automated tools are regularly audited and monitored to ensure accuracy, fairness, and accountability' [[1]](#sources)。

**产出：** 返回医疗机构门户/EHR 的实时批准（授权号），或由临床人员作出的决定。
**失败模式 → 防护：** 自动化滑向拒绝 → 仅批准的设计，所有未批准的都转给持证临床人员。不完整的提交被自动挂起 → 引导式问题预先收集所需数据。模型漂移/偏见 → 定期审计和监控。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Premera Blue Cross, Making prior authorization easier](https://healthsource.premera.com/your-premera-plan/prior-authorization-easier/) (2026-04-07)。自研的 CLARA 工具批准标准明确的请求；其余全部由临床人员审阅；工具接受审计。"about 85 percent of electronic prior authorization requests are now approved in real time"。*第一手：是；可信度：高。*
- [HCSC, Transforms Prior Authorization Process](https://www.hcsc.com/newsroom/news-releases/2023/artificial-intelligence-prior-authorization-process-helps-members-providers) (2023-07-13)。先试点，再扩展到住院/门诊各类别；采用批准或转入人工的设计，工具不做拒绝。"speed approvals were granted 80% of the time for behavioral health decisions and 66% for specialty pharmacy decisions"。*第一手：是；可信度：高。*
- [GuideWell/Florida Blue, AI in action](https://www.beckerspayer.com/leadership/ai-in-action-how-guidewell-is-improving-the-healthcare-experience/) (2025-07-31)。保险计划副总裁介绍自 2022 年起的 AI 批准，从不拒绝，并有人工监督。"processed nearly 3 million prior authorizations, with a remarkable 78% of cases receiving approval in under 90 seconds"。*第一手：是；可信度：高。*
- [Geisinger Health Plan, Ops Bulletin](https://www.geisinger.org/-/media/onegeisinger/files/pdfs/provider/navinet/opsbulletins/2023_03_15_ops_cohere_full_launch_v2.pdf?hash=6F68D56F947DACC613BBEF8E8EBE2A04&sc_lang=en) (2023-03-15)。Cohere 门户自动批准；未自动批准的请求转给保险计划的医疗管理部门。"Over 82% of those requests have been auto-approved"。*第一手：是；可信度：中。*
