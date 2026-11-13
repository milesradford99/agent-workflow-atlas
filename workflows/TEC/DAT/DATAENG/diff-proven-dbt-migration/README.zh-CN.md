---
id: AWF-0063
name: 差异验证的 dbt 迁移
summary: "将遗留代码迁移为 dbt 项目，每个模型都与生产数据比对验证；数据负责人逐表审批并签批切换。"
deliverable: 迁移完成的 dbt 项目
shape: "梳理血缘 + 遗留代码 + 文档 → 切分大型存储过程 → 每个 模型：翻译成 dbt → (与生产数据做 data diff ⟲ 智能体解释或修复差异) → 🛑 review (数据负责人通过行级 diff 审批该表) → 批量处理外观类修改 → 🛑 sign-off (全部审批通过后切换)"
source_hash: ab87adbe90bb
---

# 差异验证的 dbt 迁移

**与相近工作流的区别：** AWF-0002 扇出式代码迁移（fan-out codemod）：同样是并行改代码，但它的关卡是测试和 PR 评审。本工作流的关卡是生产数据行级一致，加上数据负责人逐表审批。
**工具变体：** `datafold-migration-agent` · `claude-code-skills` · `dbt-mesh` · `snowflake`

## 步骤

1. 智能体梳理完整的血缘、遗留代码库和语义层，并从 wiki 和会议录音中提取没有文档记录的背景信息 [[1]](#sources)。
2. 在逻辑边界处拆分过大的存储过程。一个 300K 字符的存储过程被拆成了约 400 个模型 [[2]](#sources)。翻译成职责清晰的模块化 dbt 项目，跨项目的部分使用 dbt Mesh [[1]](#sources)。
3. 用自动化的 data diff 把每个翻译后的模型与生产数据比对。对任何预期内的差异，智能体都必须结合遗留代码、新代码和需求来说明理由。无法解释的差异回到循环中，直到解决 [[1]](#sources)。单人变体在每次推送前运行双向 MINUS 一致性检查，以及 schema/CI 检查 [[3]](#sources)。
4. 🛑 **审阅**：数据负责人看过可视化的行级 diff 后，逐表审批。仅有文字说明是不够的 [[1]](#sources)。
5. 列重命名这类外观修改要批量处理，等数据验证完成后再做，因为每次修改都要消耗智能体调用 [[1]](#sources)。
6. 🛑 **签发**：只有每个维度表和事实表都经过评审并获批之后，才切换报表层背后的表 [[1]](#sources)。

**产出：** 一个纳入版本控制、与遗留输出验证一致的 dbt 项目，可在现有报表之后直接切换。
**失败模式 → 防护：** 负责人认为任何不一致都意味着“数据有问题”→ 展示行级 diff [[1]](#sources)。增量水位线悄悄丢掉 NULL 或迟到的行 → 双向一致性 diff，并检查两侧行数是否不对称 [[3]](#sources)。审阅人因过度检查成为瓶颈 → 让 diff 证据承担更多评审工作 [[1]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**薄弱**：仅有匿名、厂商相关或由记者转述的记录。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [dbt Labs, How Ecolab used an AI migration agent](https://www.getdbt.com/blog/ecolab-ai-agent-legacy-sql-migration) (2026-10-27)。Ecolab 把遗留的 Snowflake SQL 迁移为 40 多个 dbt 项目，经 diff 验证并由负责人审批。"roughly 90 tables were approved within the first four weeks of review"。*第一手：厂商（dbt 博客对 Ecolab 与 Datafold 演讲的总结）；可信度：高。*
