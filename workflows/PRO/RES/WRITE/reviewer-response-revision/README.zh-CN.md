---
id: AWF-0010
name: 审稿意见回复与稿件修订
summary: "按审稿意见逐条修改稿件并起草回复信；作者审定修改方案、审改反驳并最终签发。"
deliverable: 修订稿
shape: "审稿意见 → 回复对照表 → 🛑 plan → 每个 意见：(修改或重新分析 ⟲ 编译、重跑、引用检查) → latexdiff + 回复信 → 🛑 review → 🛑 sign-off"
source_hash: 88eea1844381
---

# 审稿意见回复与稿件修订

## 步骤

1. 把审稿意见解析进 `response.md`（意见 → 计划的修改 → 位置）。
2. 🛑 **计划**：作者对每条意见决定接受、反驳还是部分接受。
3. 为每条意见分别运行子智能体：修改文字、重跑分析并重新生成图表、补充引用。
4. 编译，并生成 `latexdiff` 版本。
5. 核实每个数字都与重新生成的输出一致，每个引用键都能解析。
6. 起草回复信。
7. 🛑 **审阅**：作者从语气和实质内容两方面修改反驳。
8. 🛑 **签发**：通讯作者在重新投稿前批准修订稿、`latexdiff` 和回复信。

## 公开实例

覆盖度（截至 2026-11-06）：**暂无**：暂无公开的第一手实例，一个真实的示例运行将是第一个。来自 [Where are the real runs?](../../../../../research/2026-11-real-runs.md)；每个数字都已对照原页面复核。

- [Pedro Sant'Anna, claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)。含有 `/respond-to-referees` 技能，但没有展示真实的修订运行。"18 agents, 61 skills"。*第一手：否（模板）；可信度：低。*
