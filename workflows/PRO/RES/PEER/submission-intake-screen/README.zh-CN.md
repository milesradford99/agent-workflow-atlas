---
id: AWF-0106
name: 投稿入口筛查
summary: "筛查投稿的抄袭、图像完整性、利益冲突和论文工厂迹象；被标记的稿件由编辑决定是否送审。"
deliverable: 已筛查的投稿
shape: "每份 投稿：AI 检查 (语言、图像完整性、抄袭、利益冲突、论文工厂信号) → 最多 20 条建议 → 无问题：交给编辑 | 被标记：🛑 review (编辑决定是否送审) → 专家更正 → 重新训练模型"
source_hash: a5cdb7d88bf4
---

# 投稿入口筛查

**与相近工作流的区别：** 最接近的是 AWF-0046 评审意见的再评审反馈（PEER），它检查审稿人写的评审意见，并私下向审稿人反馈。本工作流在入口处筛查稿件本身，服务于编辑部，且在评审开始之前进行。产出和检查点的负责人不同。
**工具变体：** `frontiers-aira`

## 步骤

1. 每份来稿一到达，就由内置于出版方同行评审平台的 AIRA 自动检查 [[1]](#sources)。
2. 检查涵盖语言质量、图表和图像完整性、抄袭及利益冲突，速度为“每秒最多 20 项检查” [[1]](#sources)[[2]](#sources)。
3. AIRA 最多给出 20 条建议并标出问题；它还会推荐编辑和审稿人 [[1]](#sources)。
4. 🛑 **审阅**：编辑和审稿人根据结果决定论文是否送交同行评审；AI 标出疑点，由人来决定 [[1]](#sources)[[2]](#sources)。
5. 专家反馈（包括被更正的错误）成为训练数据，模型定期重新训练 [[1]](#sources)。

**产出：** 每份投稿在同行评审开始之前，附带完整性和质量标记送达负责编辑。
**失败模式 → 防护：** 图像误报，被标记的图像中只有约 10% 确有问题 → 每条标记都由人来决定 [[1]](#sources)。欺诈手法变化导致模型漂移 → 用专家更正的结果重新训练 [[1]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或检查点位置不同。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [IEEE Spectrum, Peer Review of Scholarly Research Gets an AI Boost](https://spectrum.ieee.org/peer-review-of-scholarly-research-gets-an-ai-boost) (2020-07-27)。Frontiers 对每份投稿运行 AIRA；报道引述了高管对标记精确度的说法。"About 10 percent of our flagged images have some sort of problem"。*第一手：访谈；可信度：中。*
