---
id: AWF-0142
name: 上门走访录音生成照护评估
summary: "录制并转写照护走访或通话，起草评估或个案记录；从业人员审核修改后再归档。"
deliverable: 个案记录与评估
shape: "服务对象同意 → 录制从业人员的走访或通话 → 转写 → 起草评估或个案记录 → 🛑 review (从业人员检查并修改) → 归入个案档案"
source_hash: cc1780153aec
---

# 上门走访录音生成照护评估

**工具变体：** `magic-notes`

## 背景

在英格兰，市议会依据《照护法》（Care Act，关于成年人社会照护的法律）负有评估可能需要照护和支持的成年人的法定义务。社工或职业治疗师等从业人员上门走访或打电话，与对方谈清需求，再把谈话整理成评估或个案记录，存入议会的档案。整理要花好几个小时，靠的是记忆或匆忙的笔记；从业人员在走访时忙着打字，对服务对象的关注就会减少。智能体依据谈话录音工作：把录音转成文字稿，起草评估或个案记录。进行谈话的从业人员仍要阅读并修改每一份草稿，并负责归档：这份记录属于法定文件，从业人员对它负有职业责任，而且录音之前必须先征得对方同意。

**术语：**
- **从业人员（practitioner）**：进行谈话的社工、职业治疗师或评估人员。
- **服务对象（被服务对象）**：接受评估的人。
- **《照护法》谈话、评估**：围绕一个人的需求进行的结构化谈话，以及议会就此保存的书面记录。
- **个案记录（case note）**：记录与某人一次接触的带日期的文字，存放在其个案档案中。
- **法定（statutory）**：法律要求的；法定评估是议会依法必须开展的评估。
- **BASW**：英国社会工作者协会，即该职业的行业组织。
- **EHCP**：教育、健康与照护计划（Education, Health and Care Plan），一份说明儿童或青少年所需支持的法律文件。

## 用智能体搭建

**形态：** `platform`。把录音转成文字稿需要语音转写服务，通用智能体无法替代；归档则进入议会自己的个案档案系统。起草这一步可以作为 `skill` 运行。

**需要：** 在走访开始前记录下的服务对象同意；一套经议会批准、可用于照护记录的录音和转写服务，数据保存在议会要求的国家；议会的评估或个案记录模板，作为参考文件放在 skill 旁边；一套经批准可处理敏感个人信息的环境。不要给智能体个案档案系统的写入权限。

| 步骤 | 搭建方式 |
|---|---|
| 服务对象同意 → 录制从业人员的走访或通话 → 转写 | 平台。由从业人员征求同意并录音，服务生成文字稿。通用智能体做不了这一步。 |
| 起草评估或个案记录 | skill 读取文字稿和模板，按模板的标题写出草稿。文字稿没有涉及某个标题时，skill 写“谈话中未涉及”，不去填写。 |
| 🛑 review (从业人员检查并修改) → 归入个案档案 | 见“检查点”。 |

**检查点：** `review`：skill 把草稿与文字稿并排展示，然后停下，由从业人员检查并修改。归档是从业人员自己的操作：智能体没有写入个案档案的工具，所以除非从业人员亲自放进去，任何内容都进不了档案。

**与来源相比：** 来源和实例的时间为 2024-10 至 2026-01。它们描述的是一家厂商的产品，即 Beam 的 Magic Notes，由多个议会使用；公开材料看不到其内部步骤，所以这个设计把工作拆成录音服务和一个起草 skill。来源 5 无法打开（网站拒绝了页面读取器），两份 PDF 报告（来源 4 和一条公开实例）能打开但没有得到可读的文本，所以这里没有复核其中的数字。议会页面和厂商文章已读过。实例中多数节省时间的数字来自议会或厂商自己；唯一独立的评估是 Health Innovation KSS 的报告。上述搭建不作任何效果上的断言。

*以上是依据本条目的步骤和截至 2026-11 的工具文档做出的设计，不是已报道的实例。*

## 步骤

*以下按来源所述。*

1. 从业人员获得被服务对象的同意。Kingston 把这个工具描述为以“data safety and service user consent at its absolute heart”构建 [[2]](#sources)。
2. 从业人员用 Magic Notes 录制日常走访或《照护法》（Care Act）谈话。数据存储在英国 [[1]](#sources)[[2]](#sources)。
3. 工具转写音频，并生成详细的评估、报告或个案记录 [[1]](#sources)[[2]](#sources)。
4. 🛑 **审阅**：从业人员检查并修改草稿。Kingston 的一位资深社工形容自己得到了“a really accurate and detailed record and summary for me to review”[[2]](#sources)。
5. 审阅后的记录或评估成为个案档案 [[2]](#sources)。

**产出：** 经从业人员确认的法定评估或个案记录，存入市议会的社会照护档案。
**失败模式 → 防护：** 音频质量差导致转写不准（见于 Kingston 评估的二手报道，未查阅原文）→ 从业人员审阅每一份草稿。过度依赖和技能退化 → BASW 已呼吁加强评估。厂商夸大节省的时间 → 优先采用市议会的数据（Swindon、Kingston），而非 Beam 的预测。

**近期实践（2026）：**
- 审阅步骤：Kent 的主管反映，AI 起草的报告需要的修改变少了，审计也发现评估更加一致（HI-KSS 评估）。

**与相近工作流的区别：** AWF-0081 摘要辅助的个案决定（Summary-aided casework decision）是对庇护面谈做摘要，供另一位官员作决定。本工作流则是为进行谈话的从业人员起草法定评估或个案记录，用于归档，没有决定环节。跨类别看，它与 AWF-0026 医患对话环境记录员（Ambient scribe）和 AWF-0086 会议纪要相似，但产出是社会照护评估，而非临床记录或会议纪要。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。更多实例补充见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Swindon Borough Council, AI trial](https://www.swindon.gov.uk/news/article/1071/council_completes_ai_trial_to_enhance_adult_social_care_services) (2024-10-01)。2024 年 4 月至 7 月，19 名社工在 184 次一线会面中试用。"the time taken to write up these assessments was reduced from four hours to one hour 30 minutes."。*第一手：是；可信度：高。*
- [Kingston Council launch](https://www.kingston.gov.uk/news/2024/kingston-council-launches-ai-tool-free-time-frontline-social-workers) (2024-11-20)。先试点，再推广到更多成人社会照护工作人员；从业人员审阅每份记录。"saves each frontline social worker at least 4 hours a week"（同一页面也写作 "up to four hours"）。*第一手：是；可信度：中。*
- [Beam via techUK, Kent rollout](https://www.techuk.org/resource/how-local-government-is-using-ai-to-transform-social-care.html) (2025-12-10)。Kent 先由 29 名从业人员试点，后扩大到 1,000 多名员工。"seven hours per week"。*第一手：厂商；可信度：低。*
- [Health Innovation KSS, Evaluation of test and learn of Magic Notes in Kent County Council adult social care](https://healthinnovation-kss.com/wp-content/uploads/2026/01/Magic-Notes-Evaluation-Report-HI-KSS-final.pdf) (2026-01)。独立评估；29 名员工，2025 年 5 月至 6 月，涵盖照护需求评估和职业治疗（OT）评估。"an average reduction of 2.7 hours per assessment (48%)"。*第一手：研究；可信度：高。*
- [St Helens Borough Council, rolls out AI tool to 450 frontline staff](https://news.sthelens.gov.uk/article/14316/St-Helens-Borough-Council-rolls-out-innovative-AI-tool-to-450-frontline-staff) (2025-11-26)。市议会先试点（17 名从业人员），再推广到 450 名员工，包括 EHCP 报告。"able to submit reports and assessments 71 per cent faster"。*第一手：是；可信度：高。*
