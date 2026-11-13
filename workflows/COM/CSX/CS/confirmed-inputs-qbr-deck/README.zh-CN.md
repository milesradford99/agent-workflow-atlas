---
id: AWF-0223
name: 确认输入后的 QBR 演示稿
summary: "为客户账户评估产品使用情况并生成 QBR 演示稿；客户经理确认判断项后修改并汇报。"
deliverable: QBR 幻灯片
shape: "账户快照（CRM、通话、采用度、续约、支持） → 每个产品：评估使用率 → 规则覆盖：提出状态 | 需判断：🛑 review (TAM 确认) → 保存已确认的输入 → ROI 计算 → 填入 Slides 模板 → (修正 ⟲ 对照已确认输入做 QA) → 🛑 review (TAM 修改并汇报)"
source_hash: debe48418e63
---

# 确认输入后的 QBR 演示稿

**与相近工作流的区别：** 最接近的是 AWF-0049 续约窗口风险简报（其中提到了 QBR 草稿）。AWF-0049 交付的是内部风险简报和挽留方案，由 CSM 验证风险标记并批准外联；本工作流交付的是面向客户的演示稿，运行中途对各产品的判断项设有检查点，终审前还有自动 QA 循环。AWF-0174 是自主的续约流程（抽检），交付物和自主程度都不同。
**工具变体：** `rippling-ai` · `google-slides` · `salesforce` · `gong`

## 步骤

1. 在模型接触数据之前先准备数据：把 Salesforce、Gong 通话、采用度指标、规划文档和支持历史合并为一份账户快照（归属、续约、健康信号、订阅、工单、活动） [[1]](#sources)。
2. 评估产品使用率；已批准的规则能覆盖的情况，AI 提出状态，证据不全或依赖上下文的情况，则标记出来 [[1]](#sources)。
3. 🛑 **审阅**：技术客户经理（TAM）确认被标记的评估（例如某功能采用率低是否要紧），机械性的步骤则异步运行 [[1]](#sources)。
4. 把已确认的输入保存为结构化记录（产品、状态、原因、confirmed_by_team）写入 Drive 文档，这样次日可以从 ROI 和演示稿生成继续工作 [[1]](#sources)。
5. 由不同技能分别收集上下文、分析通话、评估使用率和计算 ROI；演示稿构建器按结构化的逐页指令写入固定的 Google Slides 模板 [[1]](#sources)。Handshake 的版本会对照与客户经理共同制定的 54 项评分标准给演示稿打分 [[2]](#sources)。
6. QA 技能对照已确认的输入回读演示稿（占位符、数字不一致、状态错误）；明确的错误直接修正并复查，需判断的修改则交回团队 [[1]](#sources)。
7. 🛑 **审阅**：客户经理审阅完成的演示稿，并向客户汇报 [[1]](#sources)[[2]](#sources)。

**产出：** 每个账户一份原生 Slides 格式的 QBR 演示稿，基于已确认的输入生成，TAM 可直接汇报；已确认的输入保存在 Drive 中。
**失败模式 → 防护：** 数字过时或冲突、跨多天会话丢失决定、内容放错幻灯片 → 单一快照数据集、结构化的保存记录、固定模板加 QA 回读。推荐客户已拥有的模块 → 把已拥有产品的数据送入叙述环节 [2]。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Fourth collection pass](../../../../../research/2026-11-fourth-pass.md)。

- [Rippling, Taking QBRs from hours to minutes](https://www.rippling.com/blog/taking-qbrs-from-hours-to-minutes) (2026-10-30)。Rippling TAM 的 QBR 工作流，判断项由团队确认并带演示稿 QA，在 15 个账户上测试。"Across 15 test accounts, prep time fell from two to three hours per review to under 20 minutes.". *第一手：是；可信度：高。*
- [Handshake, The QBR agent that gave sellers a week back every quarter](https://joinhandshake.com/blog/enterprise/building-agents-that-require-judgment/) (2026-08-25)。Handshake 客户经理的 QBR 智能体，对照 54 项评分标准逐步爬坡优化。"our agent reduced preparation time from 45 minutes per account to around 10". *第一手：是；可信度：高。*
