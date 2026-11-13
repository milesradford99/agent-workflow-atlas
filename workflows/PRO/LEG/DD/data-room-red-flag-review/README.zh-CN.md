---
id: AWF-0037
name: 数据室红旗风险审查
summary: "对照审查手册逐份审阅数据室文件并附引用，标出红旗风险；律师核实并分类。"
deliverable: 尽职调查红旗风险报告
shape: "交易背景提示词 (规模、辖区、债务) → 为数据室建立索引 + 缺失文件检查 → 索要缺失文件 → 每份文件：对照审查手册带引用审阅 + 外部检索 → 🛑 review (律师核实并分类风险) → 红旗风险摘要 + 尽职调查报告"
source_hash: 0a87542cd483
---

# 数据室红旗风险审查

**与相近工作流的区别：** AWF-0024 依手册审阅合同（Playbook contract review，CONTRACT）对单份合同出修订稿。本工作流并行覆盖整个数据室，索要缺失文件，并交付交易层面的红旗风险报告。
**工具变体：** `harvey` · `deeligence`

## 步骤

1. 审阅之前，先设置包含交易背景的系统提示词：公司规模、辖区和债务融资安排。这会触发相应的合规检查 [[1]](#sources)。
2. 带条件的 AI 检查找出缺失或归错类的文件，并起草向目标公司索要文件的请求 [[1]](#sources)。
3. 数据室中的每份文件都由提示词驱动做带引用的审阅，并检索法规数据库和公开来源以发现外部风险 [[1]](#sources)。
4. 🛑 **审阅**：律师对照引用核实、迭代并分类被标出的风险 [[1]](#sources)。律师助理把 AI 的审阅结果与原文并排核对 [[2]](#sources)。
5. 依据经核实的红旗风险生成红旗风险摘要和尽职调查报告 [[1]](#sources)。

**产出：** 一份经律师核实的红旗风险摘要和尽职调查报告，交付给交易团队和客户。
**失败模式 → 防护：** 过度依赖 AI 标出的风险 → 让律师核实并参与流程 [[1]](#sources)。数据室在交易中途发生变化 → 在平台中跟踪变更 [[2]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**薄弱**：只有匿名的、与厂商相关的或由记者转述的说法。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [Harvey, GSK Stockmann due diligence](https://www.harvey.ai/customers/gsk-stockmann) (2025-09-26)。为公司和房地产交易共同设计的尽职调查工作流，由律师核实所标出的风险。"up to 75% when applied to unstructured data rooms"。*第一手：厂商；可信度：中。*
- [Deeligence, Mayne Wetherell](https://www.deeligence.com/resources/mayne-wetherell-market-leading-due-diligence-practice-adopts-deeligence) (n.d.)。在一项大型交易中做 AI 重大合同审阅，并由律师助理复核。"75+ hours of lawyer time saved on a recent deal"。*第一手：厂商；可信度：中。*
