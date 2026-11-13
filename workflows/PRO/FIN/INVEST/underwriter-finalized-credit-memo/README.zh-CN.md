---
id: AWF-0098
name: 承销人定稿的信贷备忘录
summary: "提取交易文件信息并逐节起草信贷备忘录；承销人定稿，并经银行信贷审批流程签核。"
deliverable: 信贷备忘录
shape: "上传交易文件 (数千页、多种文件类型) → 提取字段 (Document AI) → 每个备忘录章节：总结并起草 → 汇编备忘录草稿 → 🛑 review (承销人在 Docs 中修改并定稿) → 🛑 sign-off (银行的信贷审批流程) → 把每一步归档到共享 Drive"
source_hash: 483faf53e6be
---

# 承销人定稿的信贷备忘录

**与相近工作流的区别：** 最接近的是 AWF-0023 事件驱动的模型更新（Event-driven model update，INVEST），它更新股票模型，并在合规签发后发布研究报告。本工作流产出的是单笔贷款的信贷备忘录，由承销人定稿，并输入受监管的信贷决策，因此产出物、检查点负责人和风险都不同。分类说明：FIN 下没有贷款/信贷类别，所以 INVEST 是最接近的。
**工具变体：** `gemini-vertex-docai` · `moodys-credit-memo` · `ncino-banking-advisor`

## 步骤

1. 承销人上传某笔交易的贷款档案。在 Banesco USA，每笔交易有数千页，涉及多种文件类型 [[1]](#sources)。
2. Document AI 从非结构化文件中提取细节。部署在 Vertex AI 上的 Gemini 对材料做总结，并逐节起草，这原本是承销人一节一节手工完成的工作 [[1]](#sources)。
3. 智能体在几分钟内汇编出信贷备忘录草稿；人工流程大约要一周 [[1]](#sources)。穆迪（Moody's）介绍了同样的模式，数据来自其评级、公司概况、股权结构、财务数据和申报文件，并使用银行的模板 [[2]](#sources)。
4. 🛑 **审阅**：承销人在 Google Docs 中审阅、修改并定稿 [[1]](#sources)。
5. 🛑 **签发**：定稿的备忘录进入银行既有的信贷审查和审批流程。两个来源都没有详细描述这一步；智能体从不作出信贷决定。
6. 承销人通过 Gmail 与相关方沟通，共享 Drive 文件夹保存每一步的记录 [[1]](#sources)。

**产出：** 每笔贷款申请对应一份定稿的信贷备忘录，交信贷审批，并与交易档案一起保存。
**失败模式 → 防护：** 通用模板无法满足各组合细分领域的需求 → 那家欧洲银行为一个重点细分领域做了定制模板，并计划制作各行业专用的模板 [[2]](#sources)。摘要可能把提取错误带进信贷档案 → 承销人在审批前修改并定稿每一份备忘录 [[1]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**薄弱**：只有匿名、与厂商相关或由记者转述的说法。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [Google Workspace, Banesco USA customer story](https://workspace.google.com/customers/banescousa) (undated)。一家资产 50 亿美元的社区银行用 Gemini 起草信贷备忘录；承销人在 Docs 中定稿。"280 credit memos we annually process"。*第一手：厂商；可信度：中。*
- [Moody's, Major European bank transforms credit analysis](https://www.moodys.com/web/en/us/insights/ai/major-european-bank-transforms-credit-analysis-with-moodys-agentic-solutions.html) (2026-04-20)。一家未具名的欧洲银行用基于模板的智能体草稿取代了外包的备忘录起草。"first drafts in less than 15 minutes"。*第一手：厂商；可信度：中。*
