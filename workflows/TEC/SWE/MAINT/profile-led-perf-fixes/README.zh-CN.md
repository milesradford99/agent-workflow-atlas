---
id: AWF-0130
name: 基于性能剖析的优化
summary: "依据线上性能剖析定位热点函数中的反模式，给出带置信度的修复建议；开发者评审后才合并。"
deliverable: 性能修复 diff
shape: "每日全机群 CPU/内存剖析 → 每个服务取前 30 个热点函数 → 静态过滤 (剔除开源库 + 运行时) → 每个函数：对照目录检测反模式 → LLM 陪审团 + 基于规则的校验器 → 置信度评分 + 建议修复 → 🛑 review (开发者) → 合并 diff"
source_hash: 40812a950e8e
---

# 基于性能剖析的优化

**与相近工作流的区别：** AWF-0002 扇出式代码迁移：AWF-0002 在各处应用同一项事先规划好的重构，并由试点计划把关。本工作流由生产环境的剖析数据决定改什么，每个 diff 是不同的修复，关卡是开发者对照实测热点路径逐个 diff 审阅。
**工具变体：** `uber-perfinsights` · `optix`

## 步骤

1. 从每日运行的全机群剖析器获取 CPU 和内存剖析数据，采样于流量高峰期。[[1]](#sources)
2. 每个服务按 flat CPU 保留前 30 个函数。当 runtime.mallocgc 超过 CPU 的 15% 时，加入内存剖析。用静态过滤剔除开源库和运行时函数。[[1]](#sources)
3. 对每个热点函数，把完整源码和一份精选的反模式清单发给 LLM。提示词采用少样本示例、角色设定，要求修复可运行，并要求给出置信度评分。[[1]](#sources)
4. LLM 陪审团独立检查反模式是否存在、修复是否有效。随后 LLMCheck 基于规则的校验器捕获误报，并记录检测准确率。[[1]](#sources)
5. 🛑 **审阅**：diff 合入 Go monorepo 之前，由开发者审阅带评分的建议。经验证的建议还会输入 Uber 的持续优化工具（Optix）。[[1]](#sources)

**产出：** 合入 monorepo 的优化 diff，以及一份随时间跟踪的热点代码中反模式数量。
**失败模式 → 防护：** LLM 的误报和幻觉损害工程师的信任 → 陪审团校验加 LLMCheck（误报率 'from over 80% to the low teens'）。时间花在冷代码上 → 先用基于剖析的热点路径过滤。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [Uber, PerfInsights](https://www.uber.com/us/en/blog/perfinsights/) (2025-07-22)。已在顶级 Go 服务中投入生产；合入了数百个 diff。每个问题 "from 14.5 hours to almost 1 hour of tool runtime"；"93.10% time savings"。*第一手：是；可信度：高。*
