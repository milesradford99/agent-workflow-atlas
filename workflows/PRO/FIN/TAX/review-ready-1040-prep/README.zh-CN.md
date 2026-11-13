---
id: AWF-0041
name: 可供复核的 1040 报税准备
summary: "从客户资料提取字段，生成底稿并导入报税软件；经办人核验，高级复核人签字报送。"
deliverable: 已复核的纳税申报表
shape: "客户上传原始资料 → 提取字段并给出置信度 → 🛑 review (经办人核验低置信度字段和科目映射) → 生成底稿并导入报税软件 → AI 二次复核（缺失表单、同比、事务所自定检查）→ 🛑 review (经办人处理标记项) → 🛑 sign-off (高级复核人签字并报送)"
source_hash: 278597ae5135
---

# 可供复核的 1040 报税准备

**与相近工作流的区别：** AWF-0022 发票提取—匹配—路由（Invoice extract-match-route，AP）提取发票用于付款。本工作流准备的是受监管的申报文件，需要经办人和注册会计师（CPA）签字。
**工具变体：** `juno` · `filed`

## 步骤

1. 客户把 W-2、1099、K-1 和券商对账单上传到事务所的门户 [[1]](#sources)。
2. AI 提取字段，并为每个字段给出置信度分数 [[1]](#sources)。
3. 🛑 **审阅**：经办人对照源 PDF 核对提取的值，先看低置信度字段。对于企业申报表，经办人还要确认科目表映射 [[1]](#sources)。
4. 系统生成底稿，并把数据导入报税软件。数据录入和诊断检查由 AI 完成 [[1]](#sources)[[2]](#sources)。
5. 申报表草稿回到 AI 复核环节，由它把缺失表单、同比波动和事务所自定检查标记出来，形成复核计划 [[1]](#sources)。
6. 🛑 **审阅**：经办人逐项处理并解决这些标记项 [[1]](#sources)。
7. 🛑 **签发**：高级复核人或 CPA 全面复核、修正、签字并报送 [[1]](#sources)[[2]](#sources)。

**产出：** 一份经 CPA 签字并电子报送的申报表，附有证据可追溯的底稿和已处理完毕的复核清单。
**失败模式 → 防护：** 源字段读错 → 置信度分数加人工核验 [[1]](#sources)。漏掉表单 → 与上年对比检查 [[1]](#sources)。把 AI 当作初级经办人看待：所有内容都要复核 [[2]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**薄弱**：只有匿名、与厂商相关或由记者转述的说法。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [Filed, Teel Accounting](https://www.filed.com/cases/teel-accounting) (2026)。独立执业的 CPA 让申报表经过 AI 数据录入和诊断检查，并在 ProConnect 中逐份复核。"processing 50% of all returns through Filed for data entry and diagnostics"。*第一手：厂商；可信度：中。*
- [Juno, How AI tax preparation works](https://juno.tax/blog/how-ai-tax-preparation-works) (2026-03-06)。厂商创始人介绍事务所内部实际使用的分步工作流。*第一手：厂商；可信度：低。*
