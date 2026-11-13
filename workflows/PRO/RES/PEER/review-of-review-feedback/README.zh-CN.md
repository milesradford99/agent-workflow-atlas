---
id: AWF-0046
name: 评审意见的再评审反馈
summary: "检查评审意见中的含糊、误读等问题并私下反馈；评审人可采纳、修改或忽略。"
deliverable: 修订后的同行评审意见
shape: "评审人提交评审意见 → 多个 LLM 检查含糊评论、误读和不专业的言辞 → 可靠性测试把关反馈 → 私下向评审人反馈 → 🛑 review (评审人采纳、修改或忽略)"
source_hash: b530e750d7ba
---

# 评审意见的再评审反馈

**与相近工作流的区别：** AWF-0010 审稿意见回复修订（Reviewer-response revision，WRITE）帮助作者回复评审意见。本工作流则在评审意见发布前，改进评审人自己写的评审。
**工具变体：** `review-feedback-agent`

## 步骤

1. 评审人提交后，由多个 LLM 组成的流水线针对含糊的评论、对内容的误解和不专业的言辞起草反馈 [[1]](#sources)。
2. 基于 LLM 的可靠性测试检查每条反馈的各项属性，只有通过的反馈才会发出 [[1]](#sources)。
3. 反馈只私下发给评审人。系统不会直接改动评审意见 [[1]](#sources)。
4. 🛑 **审阅**：评审人在评审意见发布前，自行决定忽略反馈或修改自己的评审 [[1]](#sources)。

**产出：** 一份更清晰、更可操作、由人类评审人写成的同行评审，进入正常的反驳和决定环节。
**失败模式 → 防护：** 反馈有幻觉或质量低 → 多 LLM 流水线加可靠性测试护栏 [[1]](#sources)。多数评审人不会更新 → 反馈保持可选；两组之间的录用结果没有差异 [[1]](#sources)。

**近期实践（2026）：**
- 反馈环节：反馈只发给评审人和程序主席（不发给领域主席或作者），在提交后几个小时内送达，且没有第二轮（ICLR blog 2024-10-09）。[[4]](#sources)

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。更多实例见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [ICLR Blog, LLM feedback at ICLR 2025](https://blog.iclr.cc/2025/04/15/leveraging-llm-feedback-to-enhance-review-quality/) (2025-04-15)。覆盖约 45k 份评审的随机对照研究；评审人在收到 AI 反馈后可选择性地修订。"26.6% of reviewers who received feedback updated their reviews"。*第一手：是；可信度：高。*
- [Thakkar et al., Nature Machine Intelligence](https://www.nature.com/articles/s42256-026-01188-x) (2026-02-23)。ICLR 2025 评审反馈智能体随机研究的同行评审发表版本。"27% of reviewers who received automated feedback updated their reviews, incorporating over 12,000 suggestions"。*第一手：是；可信度：高。*
