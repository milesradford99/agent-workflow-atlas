---
id: AWF-0219
name: 智能体团队的结合蛋白设计
summary: "科学家智能体团队设计蛋白结合体流水线和候选序列；研究员把关方案，实验室验证设计。"
deliverable: 经验证的结合体序列
shape: "人类设定议程(靶点 + 约束) → PI 智能体召开 5 场并行的单独会议来挑选科学家团队 → 合并会议 → 就项目方案召开团队会议(科学家智能体 + Scientific Critic) → 🛑 plan (人类研究员对方案和工具选择给出高层反馈) → 智能体为每个流水线组件编写代码(ESM | AlphaFold-Multimer | Rosetta)并经评审循环(代码 ⟲ 评审) → (运行突变轮次 + 排序 ⟲ 下一轮) → 筛出候选序列 → 🛑 sign-off (人类研究员批准送去合成的名单) → 🛑 handoff (湿实验室：表达、抗原芯片、多重 ELISA) → 结合数据回传团队"
source_hash: 24299b390acd
---

# 智能体团队的结合蛋白设计

**与相近工作流的区别：** 最接近的是同类的 AWF-0034 化学家把关的 DMTA 循环。替换测试不通过：AWF-0034 的交付物是高通量实验的反应网格和操作步骤，由化学家在运行前修正，并在每个循环中挑选候选清单；本工作流的交付物是由智能体自己设计的流水线产出的蛋白序列，人工检查点是会议层面的议程反馈（约占 1% 的字数）加合成前的一次签发，验证则是交给独立的湿实验室团队做 ELISA，而不是由提出方案的化学家在实验台上小规模重复。自主程度也更宽松：检查点之间，智能体自己编写并运行工具。
**工具变体：** `virtual-lab-gpt4o` · `esm-alphafold-multimer-rosetta`

## 步骤

1. 人类研究员说明研究目标和约束（针对近期 SARS-CoV-2 变异株设计纳米抗体结合体），并创建一个 LLM 首席研究员（PI）智能体 [[1]](#sources)。
2. 通过五场并行的单独会议，询问 PI 智能体项目需要哪些专业智能体；再由一场合并会议把五份答案整合成一个团队。在已发表的实例中，产生了计算生物学家、机器学习专家和免疫学家，外加一个常驻的 Scientific Critic 智能体 [[1]](#sources)[[3]](#sources)。
3. 一场团队会议确定项目方案（纳米抗体还是抗体；从头设计还是改造已知结合体），另一场确定工具栈。🛑 **计划**：人类研究员只在这些会议上给出高层反馈——在项目方案会议中，人类写的内容占 0.5% 的字数，在带评审的单独会议中约占 1% [[3]](#sources)。
4. 由一位科学家智能体加上 Scientific Critic 开单独会议，产出各个流水线组件；评审提出的异议会驱动多轮修改，之后代码才被接受 [[1]](#sources)[[3]](#sources)。
5. 智能体运行自己设计的流水线（ESM-1b 对数似然比打分、AlphaFold-Multimer 复合物预测、Rosetta 能量打分），从四个野生型纳米抗体（Ty1、Nb21、H11-D4、VHH-72）出发，进行四轮迭代突变，每轮引入一个突变 [[1]](#sources)[[4]](#sources)。
6. 🛑 **签发**：人类负责人接受排名靠前的突变序列清单（92 个新纳米抗体）送去合成，并加上供实验使用的序列标签 [[1]](#sources)[[4]](#sources)。
7. 🛑 **接手**：独立的湿实验室团队针对原始株和近期的刺突 RBD，进行纳米抗体表达、RBD 表达、抗原芯片打印和多重 ELISA；结果连同计算打分和完整的智能体对话记录一并发表 [[1]](#sources)[[2]](#sources)。

**产出：** 一组排好序的设计结合体序列，以及产生它们的计算流水线，交给湿实验室；ELISA 结合数据和完整的会议记录公开发布。
**失败模式 → 防护：** 智能体停留在含糊的角色定义或过于激进的从头设计 → 并行会议加合并会议，并在每场会议中设置 Scientific Critic 智能体。智能体写出看似合理但有误的代码或打分公式 → 组件级的评审循环，以及人工审阅最终流水线。计算打分无法预测结合 → 以湿实验室 ELISA 作为唯一被接受的结论（92 个设计中，有两个对 JN.1 或 KP.3 的结合有所改善）。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Fourth collection pass](../../../../../research/2026-11-fourth-pass.md)。

- [Swanson, Wu, Bulaong, Pak & Zou, The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies](https://www.nature.com/articles/s41586-025-09442-9) (2025-07-29)。智能体团队设计了自己的流水线；设计经湿实验室 ELISA 确认。"designed 92 new nanobodies"; "two new nanobodies exhibit improved binding to the recent JN.1 or KP.3 variants". *第一手：是；可信度：高。*
- [Swanson et al., Supplementary Information, Supplementary Note 3](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-025-09442-9/MediaObjects/41586_2025_9442_MOESM1_ESM.pdf) (2025)。量化了人类在每个检查点的贡献有多少。"with the human researcher only writing 0.5% of the words" (project specification team meeting). *第一手：是；可信度：高。*
