---
id: AWF-0172
name: 模拟对话发布闸门
summary: "每次客服代理变更都先在模拟客户对话上与现版本对比评判；人工复核失败案例并签字放行。"
deliverable: 代理发布决定
shape: "候选变更（提示词、知识库、模型）+ 假设 → 对照真实对话检验模拟器 → (修订代理 ⟲ 每个 场景 × 人设：模拟客户对话，工具已模拟 → LLM 评判相对现版本通过/失败) → 🛑 review (失败的对话记录) → 🛑 sign-off (发布负责人/客户质检) → 线上 A/B → 上线"
source_hash: 3cb203bf56f1
---

# 模拟对话发布闸门

**与相近工作流的区别：** 最接近的是 AWF-0047 校准式对话评分：那是事后对线上对话评分并抽样；本工作流在任何客户看到之前就测试变更，以发布签字和 A/B 测试收尾。交付物（发布决定与质检发现）和检查点（上线前签字与持续抽样）都不同。
**工具变体：** `snowglobe` · `intercom-fin-evals` · `claude-code`

## 步骤

1. 说明待测的变更（提示词、知识库、模型）和预先约定的成功标准，例如减少不必要的转人工 [[2]](#sources)。
2. 在信任模拟器之前先检验它：把真实对话分成开发集（用于配置模拟器）和测试集，并确认模拟分数对已上线版本的排序与生产环境一致 [[2]](#sources)。DoorDash 比较了 302 条模拟对话和 175 条生产对话，升级率相近 [[1]](#sources)。
3. 根据场景和人设生成多轮对话（配送延误、政策边缘情形、语言切换）；模拟工具输出，不触及任何生产后端或客户记录 [[1]](#sources)[[2]](#sources)[[4]](#sources)。
4. 用负责团队定义的二元通过/失败评分标准给每条对话打分；比较候选版本与现版本，反复修改直到通过率达到退出标准 [[1]](#sources)[[2]](#sources)。
5. 🛑 **审阅**：工程师阅读失败的对话记录和预期与实际的执行轨迹，找出修复办法 [[3]](#sources)。
6. 🛑 **签发**：客户的质检团队（Delight.ai）或业务负责人（Telonic：前台经理）在测试环境试用后批准发布 [[3]](#sources)[[4]](#sources)。
7. 只有明显胜出者才进入线上 A/B 测试，比较自助解决率和满意度，然后上线 [[2]](#sources)。

**产出：** 针对一次代理变更的放行/不放行决定，并保存模拟对话记录和评判结果，用于回归跟踪。
**失败模式 → 防护：** 模拟客户的行为与真实客户不同 → 先用已上线版本验证模拟器；Nubank 的盲审人员仍能识别出大多数模拟对话，所以排序一致性才是关键检验 [2][5]。评判漂移 → 固定的回归套件加针对具体功能的评分标准 [1]。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [DoorDash, one-click simulation and evaluation platform](https://careersatdoordash.com/blog/doordashs-one-click-simulation-and-evaluation-platform-for-support-chatbots/) (2026-06-01)。模拟的订单状态对话与生产升级率吻合；用作上线前闸门。"Simulation: 302 conversations in five minutes, with a 46% escalation rate"。*第一手：是；可信度：高。*
- [Nubank, arXiv 2609.30137](https://arxiv.org/html/2609.30137v1) (2026-09-24)。经模拟筛选的卡片管理代理随后赢得线上 A/B 测试并上线。"Simulation-guided iteration increased transactional net promoter score (tNPS) by 36.69 points in a live A/B test"。*第一手：是；可信度：高。*
- [Anthropic, Delight.ai case study](https://claude.com/customers/delightai-qa) (undated)。为每个客户的代理做人设加场景的回归运行；客户质检团队给出放行。"it used to take us about a week to fix issues, test, and deploy. Now it takes just one or two days max"。*第一手：厂商；可信度：中。*
