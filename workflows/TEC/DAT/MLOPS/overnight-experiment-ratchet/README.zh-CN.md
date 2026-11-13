---
id: AWF-0065
name: 通宵实验迭代
summary: "通宵循环修改代码、训练和评估，产出改进的候选模型；协议由人制定，晋级前由科学家审查日志。"
deliverable: 改进后的候选模型
shape: "🛑 plan (人编写协议：指标、优先级、约束) → 冻结评估框架和数据划分 → (修改代码 → 提交 → 训练 → 评估 → 保留或回退) ⟲ 直到人叫停 → 智能体撰写结果报告 → 🛑 review (科学家审计日志) → 🛑 sign-off (晋级)"
source_hash: bdb4c487891e
---

# 通宵实验迭代

**与相近工作流的区别：** AWF-0023 事件驱动的模型更新是根据新闻事件更新投资模型。本工作流是针对冻结的留出指标做 ML 训练的棘轮式迭代。AWF-0004 先分诊再修复属于运维，不是训练。
**工具变体：** `autoresearch` · `git` · `weights-and-biases`

## 步骤

1. 🛑 **计划**：由人编写协议（program.md）：主要指标、尝试方向的优先顺序（先特征后超参数，先简化后复杂化）、约束和命令 [[1]](#sources)[[2]](#sources)。
2. 把评估代码和训练/测试划分设为只读，让智能体无法钻指标的空子 [[1]](#sources)[[3]](#sources)。Faire 在发现损失函数的改动让指标无法比较之后，增加了明确的防护规则 [[2]](#sources)。
3. 循环：修改代码 → git commit → 在严格的挂钟时间预算内训练 → 评估 → 有提升就保留，否则回退。把每次结果追加到结构化日志中 [[1]](#sources)[[2]](#sources)。
4. 维护一份持久的 experiments.md，记录假设、结果和长期计划，这样长时间运行也不会忘记已放弃的想法。科学家可以随时查看并重新引导方向，无需停止运行 [[2]](#sources)。
5. 运行停止后，智能体撰写报告，说明尝试了什么、什么失败了以及原因，还有最优配置是如何形成的 [[1]](#sources)。
6. 🛑 **审阅**：科学家在第二天早上审计完整的结果日志和 git 历史 [[1]](#sources)。
7. 🛑 **签发**：问题的界定和指标的选择由人负责，上线哪个模型也由人决定 [[2]](#sources)。

**产出：** 一个更好的候选模型，附带 git 记录、实验日志和书面报告，交由人做晋级决定。
**失败模式 → 防护：** 钻指标的空子 → 评估框架只读 [[1]](#sources)[[3]](#sources)。迭代 20-30 轮后丢失上下文 → 持久的实验记忆 [[2]](#sources)。智能体过早断定搜索已穷尽 → 持续提供新想法，并由人引导 [[2]](#sources)。对离线指标过拟合 → 晋级前由人审阅候选模型 [[1]](#sources)[[2]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [Rocket, What 200+ autonomous ML experiments taught us](https://careers.rocket.com/blog/technology-and-product/autonomous-ml-experiments-model-tuning) (2026-04-15)。在生产分类模型上通宵运行的智能体循环；人在第二天早上审阅日志。"220+ experiments, a 14% success rate, and a roughly 3% improvement to our primary metric"。*第一手：是；可信度：高。*
- [Faire, Autoscience](https://craft.faire.com/autoscience-how-we-built-agent-driven-ml-exploration-at-faire-f3183e7deb29) (2026-07-22)。带框架约束的 autoresearch 循环已推广到 Faire 大部分 ML 团队。"improve production model accuracy, in some cases by double-digit percentages"。*第一手：是；可信度：高。*
