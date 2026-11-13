---
id: AWF-0069
name: 筛选式测试补充
summary: "为已有测试类生成补充单测，只保留通过多重过滤的，以 diff 提交；代码负责人逐个决定采纳与否。"
deliverable: 单元测试 diff
shape: "挑选已有测试的类 → 每个提示词 × 温度：生成补充测试 → 能编译 → 首次运行通过 → 5 次重跑都通过 → 提高覆盖率 → 每个留存测试一个 diff → 🛑 sample (工具作者) → 🛑 review (工程师采纳或拒绝)"
source_hash: 3e038380829f
---

# 筛选式测试补充

**与相近工作流的区别：** AWF-0002 扇出式代码迁移（Fan-out codemod）是在大量文件上改写已有代码。本工作流只新增测试，以实测的覆盖率提升为门槛，每个测试一个小 diff。
**工具变体：** `testgen-llm` · `meta-ach-mutation-guided` · `qodo-cover`

## 步骤

1. 选定一个已有的、由人编写的测试类：工程师刚提交的 diff 所在目录，或最近有人补过测试的目录 [[1]](#sources)。
2. 用多种提示词策略（extend_test、extend_coverage、corner_cases、statement_to_complete）生成补充测试用例。可选地在 0.0–1.0 之间扫描温度，或组合两个 LLM [[1]](#sources)。
3. 依次过滤，任何一关不过就丢弃：必须能编译、首次运行通过、5 次重跑全部通过（不是不稳定测试），并且相对已有测试实测提高覆盖率。失败的测试一律丢弃，因为无法区分是真 bug 还是断言写错了 [[1]](#sources)。
4. 每个留存的测试单独作为一个 diff 提交，附摘要和测试计划，进入正常的代码评审 [[1]](#sources)。
5. 🛑 **抽检**：在 12 月的几轮运行中，工具的两位作者先审阅推荐结果，再交给工程师 [[1]](#sources)。
6. 🛑 **审阅**：负责该代码的工程师逐个接受、拒绝或放弃每个 diff，最终合入什么由他们决定 [[1]](#sources)。

**产出：** 合入的单元测试 diff，每个都保证提高覆盖率且稳定通过，扩充了原有测试类。
**失败模式 → 防护：** 没有断言或断言写着 TODO 的测试、只测简单 getter 的测试、近乎重复的测试、依赖薄弱 mock 的测试 → 在评审时拒绝并去重；覆盖率过滤要严格。只有约 4–5% 的生成尝试能留存下来，所以要跑大量低成本的尝试 [[1]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [Meta, Automated Unit Test Improvement using LLMs at Meta](https://arxiv.org/abs/2402.09171) (2024-02-14)。Instagram 和 Facebook 的 test-a-thon 活动；每个过滤后的测试作为 diff 交给工程师接受或拒绝。"73% of its recommendations being accepted for production deployment by Meta software engineers"。*第一手：是；可信度：高。*
