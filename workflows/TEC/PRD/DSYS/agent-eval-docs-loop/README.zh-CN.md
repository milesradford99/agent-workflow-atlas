---
id: AWF-0194
name: 代理评测驱动的设计系统文档
summary: "让多个智能体依据设计系统文档构建界面并打分；维护者把失败归因为文档修改后重跑。"
deliverable: 经智能体测试的设计系统文档
shape: "设计系统变更 (组件、API 或文档) → (n 个智能体用同一提示词借助文档/MCP 构建界面 → 报告: 一次构建成功、修复、无障碍问题、视觉差异、token、成本 + 汇总的智能体反馈 → 🛑 review (维护者把症状转化为文档修复) → 编辑文档 ⟲ 重跑并对比前后) → 发布变更"
source_hash: c2b66f8eb0e2
---

# 代理评测驱动的设计系统文档

**与相近工作流的区别：** AWF-0008 设计转代码（Design to code）和 AWF-0122 带评分的 token 迁移（Scored token migration）交付的是产品代码。这里智能体是一群被测试对象，产出是经反复的智能体构建来衡量的、改进后的设计系统文档，人工检查点是把评测反馈转化为文档修复。
**工具变体：** `sanity-design-system-eval-tool` · `sanity-ailf` · `mcp-server`

## 步骤

1. 定义一项评测：哪个设计系统、安装说明、训练材料（markdown 或 MCP 服务器）、模型，以及自定义或由智能体生成的提示词 [[1]](#sources)。
2. 用同一个提示词启动 n 个智能体；每个都构建界面。衡量到成功构建所需的尝试次数、无障碍问题、代码行数、性能、每次迭代的视觉差异和 token 消耗；汇总智能体对哪里让它们困惑的反馈 [[1]](#sources)。
3. 每当发布组件、API 变化或文档更新时运行；3–5 次迭代通常就能给出信号，10 次可得到更确切的结果 [[1]](#sources)。
4. 🛑 **审阅**：维护者阅读报告；智能体的反馈 "more like a smoke detector than a dentist"（只有症状，没有原因），所以由人把它转化为具体的文档修改 [[1]](#sources)。
5. 修复文档（Sanity 从 markdown 换成了 JSON 文档 schema），重跑，并衡量前后变化 [[1]](#sources)。
6. 用第二套测试框架交叉验证：Sanity 内部的 AILF 套件分别测试没有文档、提供文档、以及自己查找文档这三种情况下的智能体 [[1]](#sources)。

**产出：** 设计系统文档（以及组件/API），附每个模型实测的智能体成功率，外加每次变更的前后对比报告。
**失败模式 → 防护：** 让智能体根据自己的反馈持续改写文档会失控（作者试过）→ 保留由人来转化反馈 [1]。在大规模运行上烧钱 → 少量迭代，跟踪 token/成本 [1]。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [PJ Onori, Sanity, How well do agents use your design system?](https://www.sanity.io/engineering/design-system-evals) (2026-08-26)。在 Sanity UI 上每天使用 4 个月；每个模型 n=30 次运行，对比当前文档与新文档。Sonnet 4.6 的成功构建率 "20%"（当前）对 "90%"（新）；"Across 76 test tasks, the library landed a 90/100 score"。*第一手：是；可信度：高。*
