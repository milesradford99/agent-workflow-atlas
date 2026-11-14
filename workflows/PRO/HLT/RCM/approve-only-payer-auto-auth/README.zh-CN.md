---
id: AWF-0156
name: 仅自动批准的预授权
summary: "对明确符合医疗政策的预授权请求自动批准；拒绝只能由持证临床人员作出，工具接受审计与监控。"
deliverable: 预授权决定
shape: "医疗机构提交预授权请求 (门户/ePA) → 引导式标准问题 → 对照医疗政策 + 既往记录核查请求 → 标准明确满足：自动批准 + 授权号 | 未满足 / 不完整：🛑 handoff (持证临床人员审阅；只有人可以拒绝) → 向医疗机构返回决定 → 🛑 sample (工具接受审计与监控)"
source_hash: 8538997c8038
---

# 仅自动批准的预授权

**工具变体：** `premera-clara` · `hcsc-blueapprovr` · `cohere-health` · `florida-blue-in-house`

## 背景

在美国，健康保险公司（支付方）常要求医生诊所或医院（医疗机构）在进行昂贵的治疗、检查或用药之前先征得同意：这就是预授权。保险公司对照自己成文的医疗政策，看这项医疗服务是否符合临床标准，然后批准、部分批准或拒绝。人工做这件事很慢，医疗机构要等上几天才有答复。在这里，智能体在请求到达时逐一核查，对明确符合标准的请求当场批准，这就免去了简单情形下的等待。它从不拒绝。凡是它不能批准的，都交给持证临床人员，因为拒绝关系到患者能否得到治疗，必须由有资质的人作出，保险公司要为此负责。人也会定期对这个工具做审计。

**术语：**
- **预授权（PA）**：保险公司在治疗、检查或用药之前给出的事先批准。
- **支付方、医疗机构**：为医疗费用买单的保险公司；提供医疗服务的医生诊所或医院。
- **ePA（电子预授权）**：通过在线门户或医疗机构的病历系统提交请求，而不是传真或电话。
- **医疗政策、临床标准**：保险公司成文的规则，规定在什么情况下承保某项服务。
- **授权号**：保险公司为获批的请求返回的编号。
- **决定（determination）**：保险公司的裁决：批准、部分批准或拒绝。
- **持证临床人员（保险计划的医疗管理人员）**：保险公司自己的护士和医师，审阅未被自动批准的请求。
- **自动批准**：无人查看请求就直接批准。
- **EHR**：电子健康档案，即医疗机构的患者病历系统。

## 用智能体搭建

**形态：** `service`。请求随时从门户到达，核查时没有人在键盘前；人只看到未获批准的请求和一份审计抽样。

**需要：** 作为参考文件供智能体读取的保险公司医疗政策和临床标准，每个服务或操作编码一份文件；对请求、引导式问题答案的读取权限，以及（对使用它的编码）对该参保人以往授权和理赔的读取权限；一个能记录批准并返回授权号的批准工具；一个供临床人员审阅的队列；一个供审计抽样的队列；一套经所在机构批准、可以处理可识别患者的健康信息的环境。不要给智能体任何能记录拒绝的工具。

| 步骤 | 搭建方式 |
|---|---|
| 医疗机构提交预授权请求 (门户/ePA) → 引导式标准问题 | 在智能体之外。门户向医疗机构提出每项服务所需的问题。每份填完的请求进入一个队列。 |
| 对照医疗政策 + 既往记录核查请求 | 由队列启动的 Agent SDK 程序或 `claude -p` 处理一份请求。一个 skill 承载核查流程：读取该编码对应的标准文件，对照答案，以及（对使用它的编码）参保人的既往记录，返回满足、未满足或不完整，并列出所依据的标准。 |
| 标准明确满足：自动批准 + 授权号 | 批准工具是唯一能写入决定的工具。一个 `PreToolUse` 钩子只在脚本确认所有必填项齐全、文件中每条标准都满足时才放行。 |
| 未满足 / 不完整：🛑 handoff | 请求进入临床人员队列，附上已核对的标准、所给答案和缺少的内容。 |
| 向医疗机构返回决定 | 程序把结果写回门户。批准来自批准工具；其他任何决定由临床人员在保险公司自己的系统里作出。 |
| 🛑 sample (工具接受审计与监控) | 见“检查点”。 |

**检查点：** `handoff`：智能体没有拒绝或部分批准的工具，所以每个不能明确满足的请求只能进入临床人员队列；只要有任何一条标准未满足或任何一项为空，批准工具上的钩子就会拦住批准。`sample`：固定比例的自动批准连同证据被复制到审计队列，由临床人员或质量人员审阅；审阅发现的问题和任何被推翻的批准都会记录下来，用来收紧标准文件和钩子的脚本。

**与来源相比：** 来源出自 2023-03 至 2026-04。最新的一篇距本次核对不足 12 个月，所以没有另行查找更新的记述。来源描述的是保险公司自研或采购的工具，例如 Premera 的 CLARA、HCSC 的工具和 Cohere 的门户；它们给出了结果（批准，或转给临床人员），对工具如何作出判断着墨很少。因此这里的核查步骤，即一个 skill 对照标准文件比对答案，是一种设计，不是对这些工具的描述。有两个来源没能完整读到：Becker's Payer 页面拒绝访问，Geisinger 公告是一份没能转成文本的 PDF，所以条目中出自它们的内容仍按原样保留。预授权中关于自动化决定的规定因州和支付方而异；上面的搭建方式把拒绝留给人，对此不再多说。

*以上是依据本条目的步骤和截至 2026-11 的工具文档做出的设计，不是已报道的实例。*

## 步骤

*以下按来源所述。*

1. 医疗机构以电子方式提交预授权（PA）请求；工具只问评估该请求 'the precise number of questions required to evaluate'（平均约 6 分钟即可提交）[[2]](#sources)[[4]](#sources)。
2. 保险公司的引擎对照医疗政策/临床标准核查请求，对部分编码还会核对历史授权和理赔；它 'helps identify requests that clearly meet medical criteria' [[1]](#sources)[[2]](#sources)。
3. 标准满足且信息完整时，请求实时自动批准，授权号返回到门户 [[1]](#sources)[[4]](#sources)。
4. 🛑 **接手**：凡未自动批准的，都交给持证临床人员（保险计划的医疗管理人员/护士和医师审阅人）；工具从不拒绝：请求只会被批准，或转入 'only approved or advanced to a hands-on review by an HCSC clinician' [[1]](#sources)[[2]](#sources)[[3]](#sources)[[4]](#sources)。
5. 保险公司把最终决定（批准、部分批准或拒绝）发送给提交方 [[4]](#sources)。
6. 🛑 **抽检**：'Automated tools are regularly audited and monitored to ensure accuracy, fairness, and accountability' [[1]](#sources)。

**产出：** 返回医疗机构门户/EHR 的实时批准（授权号），或由临床人员作出的决定。
**失败模式 → 防护：** 自动化滑向拒绝 → 仅批准的设计，所有未批准的都转给持证临床人员。不完整的提交被自动挂起 → 引导式问题预先收集所需数据。模型漂移/偏见 → 定期审计和监控。
**与相近工作流的区别：** AWF-0032 按标准把关的预授权（Criteria-gated prior auth）是医疗机构一侧（辅助）：工作人员准备并提交请求。本工作流是保险支付方一侧，采用抽检：智能体无需逐项人工批准就发出批准，人只处理未获批准的余下部分，外加审计。产出是决定，而不是提交材料包。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Premera Blue Cross, Making prior authorization easier](https://healthsource.premera.com/your-premera-plan/prior-authorization-easier/) (2026-04-07)。自研的 CLARA 工具批准标准明确的请求；其余全部由临床人员审阅；工具接受审计。"about 85 percent of electronic prior authorization requests are now approved in real time"。*第一手：是；可信度：高。*
- [HCSC, Transforms Prior Authorization Process](https://www.hcsc.com/newsroom/news-releases/2023/artificial-intelligence-prior-authorization-process-helps-members-providers) (2023-07-13)。先试点，再扩展到住院/门诊各类别；采用批准或转入人工的设计，工具不做拒绝。"speed approvals were granted 80% of the time for behavioral health decisions and 66% for specialty pharmacy decisions"。*第一手：是；可信度：高。*
- [GuideWell/Florida Blue, AI in action](https://www.beckerspayer.com/leadership/ai-in-action-how-guidewell-is-improving-the-healthcare-experience/) (2025-07-31)。保险计划副总裁介绍自 2022 年起的 AI 批准，从不拒绝，并有人工监督。"processed nearly 3 million prior authorizations, with a remarkable 78% of cases receiving approval in under 90 seconds"。*第一手：是；可信度：高。*
- [Geisinger Health Plan, Ops Bulletin](https://www.geisinger.org/-/media/onegeisinger/files/pdfs/provider/navinet/opsbulletins/2023_03_15_ops_cohere_full_launch_v2.pdf?hash=6F68D56F947DACC613BBEF8E8EBE2A04&sc_lang=en) (2023-03-15)。Cohere 门户自动批准；未自动批准的请求转给保险计划的医疗管理部门。"Over 82% of those requests have been auto-approved"。*第一手：是；可信度：中。*
