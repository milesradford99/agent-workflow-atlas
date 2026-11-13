---
id: AWF-0034
name: 化学家把关的 DMTA 循环
summary: "生成并排序候选化合物，编写高通量实验方案；化学家筛选、修正流程并在台架规模复现。"
deliverable: 经验证的实验结果
shape: "开放目标 + 引导提示词 → 生成并排序方案 → 🛑 plan (化学家选定候选清单) → 智能体编写 HTE 实验网格 → 🛑 review (化学家修正实验流程) → (运行 HTE + 分析 ⟲ 提出下一轮) → 🛑 sign-off (化学家在台架规模复现) → 预印本"
source_hash: f39118abaf34
---

# 化学家把关的 DMTA 循环

**与相近工作流的区别：** 暂无相近的。AWF-0023 事件驱动的模型更新（Event-driven model update，INVEST）属于不同领域。
**工具变体：** `gpt-5-4-maria-lab` · `generative-model-robotic-synthesis`

## 步骤

1. 科学家写下目标以及引导/评分提示词。模型生成研究方案并排序 [[1]](#sources)[[2]](#sources)。
2. 🛑 **计划**：化学家审阅排名靠前的方案，并批准要测试哪些 [[1]](#sources)[[2]](#sources)。
3. 实验室智能体把选定的想法转成高通量实验流程 [[1]](#sources)。
4. 🛑 **审阅**：在运行之前，化学家对实验流程做修正（被描述为小幅修改）[[1]](#sources)[[2]](#sources)。
5. 实验室运行并分析实验。模型重新分析数据并提出下一轮 [[1]](#sources)。
6. 🛑 **签发**：化学家在台架规模手工重复有代表性的反应，在撰写报告前验证结果 [[1]](#sources)[[2]](#sources)。

**产出：** 一个经验证的反应或分子结果，附 HTE 数据和台架规模的确认，整理成预印本供外部专家评审。
**失败模式 → 防护：** 微量规模的假象 → 台架规模的人工重复 [[1]](#sources)。夸大自主性或通用性 → 实验方自己说明结果可能无法推广到其他反应或底物 [[2]](#sources)。安全范围 → 由人控制哪些方案进入实验室 [[2]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或检查点设在别处。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [R&D World, OpenAI + Molecule.one near-autonomous chemist](https://www.rdworldonline.com/openai-and-molecule-one-report-a-near-autonomous-ai-chemist-that-improved-a-stubborn-coupling-reaction/) (2026-06-22)。两轮 HTE，均经化学家批准并在台架规模验证；CEO 介绍了人的角色。"Maria ran 10,080 reactions in total"。*第一手：访谈；可信度：中。*
- [Google, Aptamers lab-in-the-loop agentic discovery](https://research.google/pubs/aptamers-as-a-sandbox-for-lab-in-the-loop-agentic-molecular-discovery/) (2026)。针对适配体结合物的智能体式设计—测试—改进轮次；摘要中未描述人工关口。"from 0.0% in Round 1 to 26.0% in Round 2 and 42.1% in Round 3 on α-thrombin"。*第一手：是；可信度：低。*
