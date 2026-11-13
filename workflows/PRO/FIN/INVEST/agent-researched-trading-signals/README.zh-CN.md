---
id: AWF-0216
name: 智能体研究的交易信号
summary: "智能体提出、编码并回测交易假设；技术团队审查代码，投资委员会签发后才上线交易。"
deliverable: 获批的交易信号
shape: "创意智能体提出可检验的假设 → 实现者基于公司研究数据编写 Python → 回测 → 评估者（显著性、风险、经济逻辑、创意与代码一致性） → 不通过：丢弃 | 通过：记录完整轨迹 → 🛑 review (技术团队：代码审查，单元/集成/情景测试) → 🛑 sign-off (投资委员会：假设、逻辑、结果) → 上线交易"
source_hash: 8fa92b238c30
---

# 智能体研究的交易信号

**与相近工作流的区别：** AWF-0166（挑战者智能体投委会备忘录）和 AWF-0023（事件驱动的模型更新）都是针对已有交易或模型，产出供人决策的文档；本工作流的交付物是全新的、已编码并回测的交易信号，上线交易前要过技术团队的代码审查和投资委员会签发两道关。替换测试在交付物和检查点上不通过。
**工具变体：** `alphagpt` · `claude-code-skills`

## 步骤

1. “创意人”智能体头脑风暴出可检验的投资假设（例如订单失衡、招聘效率）；Man Group 称它能“在几分钟而不是几天内产出几十个可行的想法” [[1]](#sources)。
2. “实现者”智能体借助 Man Group 的研究工具和自有数据库，把每个想法写成生产级 Python 代码，并运行回测 [[1]](#sources)[[2]](#sources)。
3. “评估者”智能体沿用与人工研究相同的门槛：统计显著性检验、风险评估和经济逻辑检查；内置的一致性检查会对比所述想法与实际代码，以发现偏离和 p-hacking [[1]](#sources)。
4. 工作流编排器协调这三个角色；日志系统记录每个假设、前提和决策，供事后审阅 [[1]](#sources)。
5. 🛑 **审阅**：技术团队对信号做代码审查，运行单元、集成和情景测试，并评估实现风险 [[1]](#sources)。
6. 🛑 **签发**：投资委员会按人工信号同一套框架审阅假设、经济逻辑和研究结果；只有获批的信号才进入实盘交易 [[1]](#sources)[[3]](#sources)。

**产出：** 一个获批上线交易的信号，附带代码、回测和决策日志；它与人工研究的信号一样并入系统化组合。
**失败模式 → 防护：** 想法数量大导致多重检验 / p-hacking → 沿用同样的研究方法门槛并持续监控；想法与代码偏离或幻觉 → 在想法、实现和评估之间做自动加人工的一致性检查；各自为政的本地技能导致回测不一致 → 共享的、由负责人审阅并经评测的技能库 [1][2]。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Fourth collection pass](../../../../../research/2026-11-fourth-pass.md)。

- [Man Group, What AI Can (and Can't Yet) Do for Alpha](https://www.man.com/insights/what-ai-can-do-for-alpha) (2025-11-12)。公司自述的三智能体研究循环及双轨人工验证。"It has been observed to produce dozens of viable concepts within minutes rather than days.". *第一手：是；可信度：高。*
- [Hedgeweek / Bloomberg, Man Group deploys agentic AI for quant signal discovery](https://hedgeweek.com/news/man-group-deploys-agentic-ai-for-quant-signal-discovery) (2025-07-11)。资深基金经理称 AI 生成的信号经检查点后获批实盘。"AlphaGPT has already produced several dozen investment signals that have been approved for live trading". *第一手：访谈；可信度：高。*
- [Man Group, Building signals that trade themselves](https://www.youtube.com/watch?v=EOg4gY0Yln0) (2026-05-21)。由 AI 提出、回测并投入生产的信号现已交易真实资金；人工审阅全部产出。"we now have 750 of them using Claude Code". *第一手：是；可信度：中。*
