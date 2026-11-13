---
id: AWF-0023
name: 事件驱动的模型更新
summary: "依据新发布的财报和文件更新模型驱动项并逐格引用来源；分析师复核，合规签核后发布。"
deliverable: 研究笔记
shape: "加载一致预期 + 业绩指引 → 新的财报、文件或电话会记录 → 每个 KPI：提取并附引用 → 与模型对比 → 更新 Excel 驱动项并逐格加批注 → 电话会主题 → 笔记 → 🛑 review → 🛑 sign-off (合规) → 发布"
source_hash: 30dd5a482ea5
---

# 事件驱动的模型更新

**工具变体：** `claude-excel`（Claude for Excel 自 2025 年 10 月起公测 [[23]](#sources)） · `hebbia` · `alphasense` · `rogo`

## 步骤

1. 在事件发生前，通过数据连接器加载一致预期和业绩指引：LSEG 分析师预测、S&P Capital IQ、Daloopa、FactSet，以及 financial-analysis 插件中的其他来源 [[23]](#sources) [[25]](#sources)。
2. 财报、文件或电话会记录发布后将其拉取进来；Aiera 提供实时的财报电话会记录 [[23]](#sources)。
3. 对每个 KPI，使用带提取规则的行业分类体系提取数值并附上来源文档的引用。编写适用于整个行业的消歧规则，涵盖业务分部、期间（月度还是季度）、口径（合并还是按比例）、监管框架，以及 GAAP 还是调整后口径 [[24]](#sources)。
4. 把每个实际值和任何业绩指引变化与模型及一致预期对比；earnings-analysis 技能涵盖“metrics, guidance changes” [[23]](#sources)。
5. 直接在原 Excel 中更新驱动项。Claude for Excel 会保留公式依赖关系，“tracks and explains its changes”，并链接到它引用的单元格 [[23]](#sources)。每个被改动的驱动项都加一条单元格批注，写明来源和原因。
6. 从电话会记录中提炼主题并起草笔记；`/earnings [company] [quarter]` 可生成财报后更新报告 [[25]](#sources)。
7. 🛑 **审阅**：分析师对照来源检查每个改动的单元格和每个被引用的 KPI。先看模型或规则结果不一致的数值，因为一致预期只是确定优先级的信号，不是证据 [[24]](#sources)。即使提取准确率达到 99.3%，原始的模型输出也不应直接发布 [[24]](#sources)，AI 生成的分析“should always be reviewed by a qualified professional” [[25]](#sources)。
8. 🛑 **签发（合规）**：合规部门在分发前批准笔记。
9. 发布笔记并保存更新后的模型。

**产出：** 一份更新后的模型，每个改动的驱动项都带有来源和原因；以及一份研究笔记，经合规签发后即可分发。
**失败模式 → 防护：** 多业务分部公司选错分部、把月度数字当成季度数字、REIT 取到小计或用错口径、银行比率套用错误的监管框架 → 全行业统一的消歧规则和 Extended Thinking [[24]](#sources)。部分行业（保险、工业、REIT、零售）准确率较低 → 在这些行业加强复核 [[24]](#sources)。悄悄的改动破坏模型 → 变更跟踪以及到引用单元格的链接 [[23]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**暂无**：目前还没有公开的第一手实例。一个真实的实例将是第一个。来自 [Where are the real runs?](../../../../../research/2026-11-real-runs.md)；每个数字都已对照原页面复核。

- [Financial Datasets, *EarningsBench*](https://financialdatasets.ai/blogs/earningsbench) (2026-06-29)。从 60 份财报中提取 KPI，并经人工核对：这是一个基准测试，不是模型更新。"Opus 4.6 with Extended Thinking hit 99.3% accuracy"。*第一手：否（基准测试）；可信度：低。*
