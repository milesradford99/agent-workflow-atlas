---
id: AWF-0238
name: 到场前排障辅助
summary: "技术员到场前生成排障方案并在现场答疑；由技术员判断并完成修复，未解决的问题转技术支持台。"
deliverable: 排障方案
shape: "派出报修工单 → 确认设备 → 12 个月维保摘要 + 近期故障码 + 联网设备数据 → 到场前给出建议排障步骤 → 现场：(技术员提问 → 检索手册、往期支持台案例 → 带引用的步骤) → 🛑 action (技术员判断并完成修复) → 未解决：🛑 handoff (技术支持台) → 支持台解决的案例入档 → 知识库不断扩充"
source_hash: 889806fcaed2
---

# 到场前排障辅助

**与相近工作流的区别：** AWF-0214（调度员可改派的工单分配，dispatcher-overridden job assignment）决定由哪位技术员接单，调度员抽查任务看板。本工作流从派单之后开始：为诊断做计划，并指导一位技术员完成维修，每一步由技术员决定（辅助），并可交接给人工支持台。交付物、用户和检查点都不同。AWF-0108（住户报修分诊，resident maintenance triage）把住户的报修请求分诊成工单，不指导维修。
**工具变体：** `amazon-bedrock-claude` · `fluid-topics-rag`

## 步骤

1. 技术员被派去处理一个报修工单。在现场服务管理工具中，Technician Assistant 先确认技术员处理的是正确的设备 [[1]](#sources)[[3]](#sources)。
2. 它汇总该设备过去 12 个月的维保记录和近期故障数据，包括联网设备（24/7 Connect）的信号，并把不清楚的故障码解读为可能的根因和修复办法 [[1]](#sources)[[3]](#sources)。
3. 技术员到达前，它生成建议的排障步骤，让技术员能带上合适的零件 [[1]](#sources)[[2]](#sources)。
4. 到现场后，技术员提出后续问题（部件更换、参数设置、进入方式）。助手检索经批准的手册、支持文档和已验证的往期支持台案例，返回简短、带引用的步骤，有时附手册中的图片。显示前用 LLM-as-judge / 护栏检查相关性和依据 [[1]](#sources)[[3]](#sources)。
5. 🛑 **操作**：由技术员决定怎么做并完成工作。KONE 称该工具支持决策，“同时始终把最终判断留给他们”（'while always leaving the final judgment to them'） [[1]](#sources)。
6. 🛑 **接手**：如果问题仍未解决，技术员升级给技术支持台（Technical Helpdesk，由经验丰富的现场服务工程师组成）。支持台解决的案例会被记录并加入知识库，知识库“每天都在增长”（'is growing on a daily basis'） [[1]](#sources)[[3]](#sources)。

**产出：** 针对一次报修的排障方案和带引用的现场指导。仍未解决的案例转给技术支持台，每个已解决的支持台案例都会成为下一次报修的新知识。
**失败模式 → 防护：** 不安全的指示 → 只检索经批准的文档和已验证的案例（“我们不能让 AI 给出不安全的指示”，'We cannot make instructions by AI that are not safe to use'）。过长的回答在现场无法使用 → 技术员反馈后缩短了输出。双手占用 → 已有语音转文字的需求，并列入路线图。各市场术语不一 → 技术员改进了翻译。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Fourth collection pass](../../../research/2026-11-fourth-pass.md)。

- [KONE, How an AI tool helps service technicians stay one step ahead](https://www.kone.com/global/en/newsroom/stories/technician-assistant-ai-elevator-maintenance.html) (2026-08-19)。在 KONE 技术员中推广；报修前预诊断；最终判断由技术员做出。"Already available to approximately 15,000 KONE service technicians across 60 countries"; "80% of surveyed technicians report being satisfied with the tool"。*第一手：是；可信度：高。*
- [KONE Singapore, Living tall with Singapore's vertical nervous system](https://www.kone.sg/stories-and-references/stories/living-tall-with-singapore-vertical-nervous-system.aspx) (undated)。Technician Assistant 在新加坡/马来西亚的试点；升级案例方面的早期结果。"a 6% decrease in call-out rates and 30% fewer escalated cases"。*第一手：是；可信度：中。*
