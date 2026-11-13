---
id: AWF-0152
name: 分层智能体安全审核
summary: "用文档、任务、报告三层智能体整理现场安全资料并生成审核报告；由人工审查全过程。"
deliverable: 安全审核报告
shape: "现场安全文档 (最多 400 页，多语言) → 文档智能体分析 + 创建任务 → 任务智能体拆解审核标准 → 报告智能体汇总合规发现 → 🛑 review (人在回路中审查过程) → 审核报告"
source_hash: 9c89967ae7b7
---

# 分层智能体安全审核

**与相近工作流的区别：** AWF-0040 全量内控测试（Full-population control testing）是对每项控制都留证据的财务审计。本工作流是基于现场文档的运营安全审核，由一名人工对智能体的过程做一次审查。
**未归类原因：** taxonomy.yaml 中目前没有涵盖此类的类别。在有三个类似的工作流足以支撑新类别 `EHS`（TAXONOMY.md 规则 2）之前，先归在这里。
**工具变体：** `claude-vertex`

## 步骤

1. 文档处理智能体分析审核文档并创建任务 [[1]](#sources)。
2. 任务拆解智能体把复杂的审核任务简化 [[1]](#sources)。
3. 报告生成智能体把结果汇总成最终的审核报告 [[1]](#sources)。
4. 🛑 **审阅**：智能体承担一半工作量；“the other half, which involves a human in the loop examining the process, remains in place”[[2]](#sources)。

**产出：** 安全管理计划审核报告（AES 每年约出 1,500 份）。
**失败模式 → 防护：** 在冗长的多语言文档中漏掉发现项 → 分层智能体加人工审查。检查点只有简略描述。

## 公开实例

覆盖度（截至 2026-11-06）：**薄弱**：只有匿名的、与厂商相关的或由记者转述的说法。收集与复核见 [Second collection pass](../../../research/2026-11-second-pass.md)。

- [Google Cloud, AES](https://cloud.google.com/customers/aes?hl=en) (n.d.)。已完成 50 多次智能体审核；引述 AES 数据科学人员的话。"Our auditors previously spent 14 days completing each audit process. Now, with our Claude-powered agents on Gemini platform, the same work is completed in just one hour"。*第一手：厂商；可信度：中。*
