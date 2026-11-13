---
id: AWF-0070
name: 分级打分的 PR 评论
summary: "在代码变更上发布带置信度分级的评审评论；作者将每条标记为有用或无用，并决定是否处理。"
deliverable: PR 评审评论
shape: "diff → 过滤符合条件的文件 → 构建上下文（附近的函数、类、import）→ 各助手（缺陷、最佳实践、安全）起草评论 → 置信度打分 → 去重 → 剔除低价值类别 → 以行内评论发布 → 🛑 review (作者评价并修复) → 在最终提交上重跑 5 次以衡量是否已处理"
source_hash: aeb0bf42f090
---

# 分级打分的 PR 评论

**与相近工作流的区别：** AWF-0003 委派式 PR 是在智能体自己的编写循环内使用机器人评审。本工作流评审全公司每一个由人编写的 diff，产出的是评论而不是代码。
**工具变体：** [`claude-code` kit](variants/claude-code.md) · `ureview` · `coderabbit` · `github-copilot-code-review` · `graphite-diamond`

## 步骤

1. 对每个 diff，跳过配置文件、生成的代码和实验性目录。用附近的函数、类定义和 import 构建提示词 [[1]](#sources)。
2. 并行运行各专门的助手：Standard（缺陷、异常处理、逻辑）、Best Practices（内部规范）和 AppSec（安全漏洞）[[1]](#sources)。
3. 第二个提示词为每条评论的置信度打分。按助手、语言和类别分别设定阈值来剪枝。用语义相似度过滤器合并重叠的评论。屏蔽历史上对开发者价值较低的类别 [[1]](#sources)。
4. 把留下的评论以行内评论的形式发布到评审平台，每个提交在 CI 中的耗时中位数为 4 分钟 [[1]](#sources)。
5. 🛑 **审阅**：作者把每条评论标为有用或无用，并决定是否处理。评价数据流入数据仓库，用于重新调整阈值 [[1]](#sources)。
6. 度量：在最终提交上把评审器重跑 5 次。如果没有任何一次重跑复现某条评论，就算它已被处理。对照人工标注的基准跟踪精确率和召回率，并以这些数字作为推广的关卡 [[1]](#sources)。

**产出：** 每个 PR 上与人工评审并行的行内评审评论，有用率和已处理率这两项指标会反馈用于调整阈值。
**失败模式 → 防护：** 嘈杂、低价值的评论损害信任 → 分类别的置信度阈值、去重，并屏蔽历史表现差的类别；在有用率持续偏高之前，暂缓推广到新语言 [[1]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [Uber, uReview](https://www.uber.com/us/en/blog/ureview/) (2025-08-12)。三个助手、一个打分器和一个去重过滤器发布行内评论；已处理率与人工评论对比衡量。"Engineers who interact with the tool mark 75% of its comments as useful"; 65% addressed vs 51% for human comments。*第一手：是；可信度：高。*
