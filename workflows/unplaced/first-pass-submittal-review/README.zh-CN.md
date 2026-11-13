---
id: AWF-0151
name: 施工提交件初审
summary: "将施工提交件与规格书及既往批复比对并给出处理建议；项目经理或工程师复核，最终由审批责任人批准。"
deliverable: 提交件审查回复
shape: "收到提交件 → 匹配适用的规格章节 + RFI + 既往批复 → 逐项核对要求 → 标出不合规 / 缺失项 → 结构化建议 → 🛑 review (PM/PE 确认并修改) → 回复分包商 | 转交建筑师 → 🛑 sign-off (建筑师/责任工程师作出处置)"
source_hash: 5d67cdc556ab
---

# 施工提交件初审

**与相近工作流的区别：** AWF-0058 带引用的预审检查（Cited pre-screen checks）是对许可申请人的图纸集做规范合规预审。本工作流则是承包商对照项目规格书，检查分包商的产品资料和施工详图。产出不同（提交件审查回复），审批人也不同（先是 PM，再是责任建筑师）。
**未归类原因：** taxonomy.yaml 中目前没有涵盖此类的类别。在有三个类似的工作流足以支撑新类别 `SUBMITTAL`（TAXONOMY.md 规则 2）之前，先归在这里。
**工具变体：** `trunk-tools` · `procore-datagrid` · `buildsync`

## 步骤

1. 提交件到达时，将其与项目规格书、相关的 RFI 回复和此前已批准的提交件比对 [[1]](#sources)。
2. 标出不合规的条目，并 'in minutes' 生成结构化建议 [[1]](#sources)。
3. 🛑 **审阅**：助理项目经理或项目工程师依据分析采取行动，并回复分包商 [[1]](#sources)。
4. 🛑 **签发**：批准权仍在责任审批人手中；Procore 的智能体 'require human consent before actions are finalized' [[2]](#sources)。

**产出：** 经过修正的提交件送交建筑师，避免被退回要求修改并重新提交（Revise and Resubmit）。
**失败模式 → 防护：** 漏检的不合规问题到现场才暴露 → 逐项要求核对。规格书已被取代 → 从项目管理系统读取当前的项目文件集。

**近期实践（2026）：**
- 逐项核对要求：把每一项标为合规、部分合规或不合规，让审阅人集中处理例外项（ENR 2026-06-17）。
- 回复分包商：返还 AI 报告和自动标注，并附上审阅人的指示；转交建筑师时，附上合规对照表（BuildSync；ENR 2026-06-17）。[[5]](#sources)

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：第一手实例只覆盖流程的一部分，或检查点设在别处。收集与复核见 [Second collection pass](../../../research/2026-11-second-pass.md)。更多实例补充见 [Third collection pass](../../../research/2026-11-third-pass.md)。

- [Trunk Tools, Cleveland Construction](https://trunktools.com/content/customers/pdfs/cleveland.pdf) (n.d.)。电气提交件当天完成；引述助理 PM 的话。"estimated savings of 790+ hours and $60K+ across four projects"。*第一手：厂商；可信度：中。*
- [ENGtechnica, Procore/Datagrid](https://engtechnica.com/procore-embeds-datagrid-ai-agents-in-construction-workflows/) (2026-05-22)。Level 10 Construction 自建了提交件智能体。"We ran 10 submittal reviews in an hour using our agent, easily saving 12 hours of work"。*第一手：访谈；可信度：中。*
- [Bryan Gottlieb, ENR, Trunk Tools Launches Cortex AI Platform](https://www.enr.com/articles/63178-trunk-tools-launches-cortex-ai-platform-to-interpret-construction-drawings) (2026-06-17)。Cleveland Construction 的高级副总裁：提交件先经 AI 处理再由员工审阅；合规对照表发送给建筑师。"reducing average submittal cycle times from 55 days to 13 days"；"from roughly two hours to less than 10 minutes"。*第一手：访谈；可信度：中。*
- [Jeff Yoders, ENR, Gilbane Rolls Out Trunk Tools AI Agents Across Its Jobsites](https://www.enr.com/articles/61435-gilbane-rolls-out-trunk-tools-ai-agents-across-its-jobsites) (2025-09-26)。30 个 Gilbane 项目；多数收到的提交件在送交建筑师前就被标为不合规。"review more than 2,000 submittals"；"72% of submittals received ... were non-compliant, 25% partially compliant, and only 3% fully compliant"。*第一手：否；可信度：中。*
- [Trunk Tools, Torcon case study](https://trunktools.com/customers/case-study-how-torcon-project-team-save-time-reduce-risk/) (2026-03-12)。两个项目的试点；为项目工程师做提交件合规审查。"64 submittal reviews completed with ~43.5 minutes saved per review (~46 hours)"。*第一手：厂商；可信度：中。*
- [BuildSync, Monteith Construction: Blueprints to Bedside](https://buildsync.ai/case-studies/blueprints-to-bedside) (n.d.)。PM 在每份产品资料提交件提交后，立即在 Procore 内运行 AI 审查。"I spend 70% less time reviewing submittals"；"Our failure rate has dropped by around 50%"。*第一手：厂商；可信度：中。*
