---
id: AWF-0126
name: 校准评审的质量闭环
summary: "用经人工校准的评审器给线上智能体会话打分并为失败类别起草修复；评分细则、标注和修复审核均由人负责。"
deliverable: 智能体质量评分与修复
shape: "🛑 plan (人为每项评测撰写评分细则) → 🛑 review (人标注校准会话) → (优化评审器提示词 ⟲ 与留出的人工标注的一致度) → 每日 追踪记录 → 对话记录构建器 → 对生产会话逐条评审每项适用标准 → 按标准聚类失败 → 编码智能体调查 → 修复明确：起草 PR | 提示词改动：诊断 + 提案 → 🛑 review → 离线模拟器回归 → 上线"
source_hash: d876ab63025b
---

# 校准评审的质量闭环

**与相近工作流的区别：** 最接近的是 AWF-0065（通宵实验棘轮），它在人工撰写的协议和晋升签发之下，通宵对冻结的评测运行训练改动。本工作流中，评测本身就是产品：经人工标注校准的评审器每天给线上生产会话打分，由此引出的修复要经过人工审阅和离线回归。产出和检查点都不同。
**工具变体：** `gepa` · `dspy` · `opentelemetry` · `clickhouse` · `dropbox-dash-judges` · `netflix-explanation-judge`

## 步骤

1. 🛑 **计划**：由人为每项评测撰写评分细则（护栏，加上各领域智能体的能力检查）。每项检查都是通过/不通过，并且可以从会话本身验证，这样人和评审器能用同样的方式评分 [[1]](#sources)。
2. 🛑 **审阅**：人工审阅者标注一组校准会话。用 GEPA 优化评审器提示词，保留那些在留出集上提高了与人工标注一致度的修改。每当评分细则变化就重新校准 [[1]](#sources)。
3. 每个会话都通过 OpenTelemetry 追踪并写入 ClickHouse。对话记录构建器重建每个会话，并只给每项标准它所需的证据。评审器先判断某项标准是否适用，再附简短理由打分 [[1]](#sources)。
4. 每天对生产会话运行评审器。按违反的标准对失败聚类，并按出现频率给各主题排序 [[1]](#sources)。
5. 编码智能体针对一个聚类开展工作：阅读失败的追踪记录、代码和近期改动。修复明确时，它起草 PR。对于提示词改动，它撰写诊断和提案。🛑 **审阅**：由工程师审阅二者之一 [[1]](#sources)。
6. 上线前，用固定的工具夹具和模拟用户运行离线模拟器，例如 50 个场景 × 8 次试验。使用与生产相同的评分细则和评审器 [[1]](#sources)。

**产出：** 生产智能体每天一份经人工校准的质量评分、按频率排序的失败主题，以及在发布前经离线验证的、已审阅的修复。
**失败模式 → 防护：** 评审器与人的判断不一致 → 对照人工标注校准，评分细则演进时重新运行。最近的一则个案左右了修复 → 按评分标准聚类。改动无法在真实用户身上测试 → 固定夹具的模拟器。skill 把某个聚类分错了类 → 更新 skill，而不是只修这一次运行 [[1]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [DoorDash, Building Ask DoorDash (Part 3): Evaluation](https://careersatdoordash.com/blog/building-ask-doordash-part-three-evaluation/) (2026-06-30)。在全国上线前，对生产会话使用校准评审器，并做模拟器回归。"from an average of 1 employee-submitted feedback to 2,000 auto-graded sessions per day"。*第一手：是；可信度：高。*
- [Dropbox, How we used DSPy to turn AI evaluations into better responses in Dash Chat](https://dropbox.tech/machine-learning/how-we-turned-ai-evaluations-into-better-responses-in-dash-chat) (2026-06-25)。评审器经人工标注校准后，再通过回放用于优化智能体提示词。"26% reduction in incomplete answers"。*第一手：是；可信度：中。*
