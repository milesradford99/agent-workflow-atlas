---
id: AWF-0124
name: 按需召唤的 dbt 排障助手
summary: "工程师在 Slack 中召唤后诊断 dbt 生产故障；是否修复由工程师决定，修复 PR 由其审核合并。"
deliverable: 流水线故障诊断
shape: "Slack 中的 dbt 故障告警 → 🛑 action (工程师 @ 智能体) → 对照已知故障特征分类 → (对某一层执行模板化行数查询 ⟲ 上移一层) → 根因发在 Slack 串中 → 🛑 action (工程师决定是否修复) → 智能体起草修复 PR + Jira 工单 → 🛑 review (工程师批准并合并)"
source_hash: a6f716e56922
---

# 按需召唤的 dbt 排障助手

**与相近工作流的区别：** 最接近的是 AWF-0063（经 diff 验证的 dbt 迁移），它把遗留代码翻译成 dbt，并在切换前用行级 diff 加以证明。本工作流诊断的是已在生产中运行的流水线的故障。每次运行由人发起，每项修复由人决定。
**工具变体：** `claude-agent-sdk` · `dbt` · `snowflake` · `slack` · `jira` · `kestra`

## 步骤

1. dbt 生产故障发布到数据通知频道。🛑 **操作**：值班工程师通过 @ 智能体来启动排查。团队有意选择了手动触发 [[1]](#sources)。
2. 把错误与 11 种已知故障特征的查找表进行匹配来分类。不要从第一性原理出发做诊断 [[1]](#sources)。
3. 按固定的层级顺序向上游追溯：mart、intermediate、staging、base、source。运行预先写好的行数查询，智能体只需填入模型名和日期。找到行数开始出现差异的第一层，阅读该层的 SQL，再上移一层重复。编造的列名会让查询失败，智能体随后用修正后的 schema 路径重试 [[1]](#sources)。
4. 几分钟内在同一个 Slack 串中回帖诊断结果，标明是常规修复还是需要判断的情况 [[1]](#sources)。
5. 🛑 **操作**：由工程师决定是否继续。只有此时，修复 skill 才会起草修复、开 PR 并创建 Jira 工单。🛑 **审阅**：工程师阅读、批准并合并 [[1]](#sources)。
6. 随着新模式出现，持续更新故障分类和数据仓库上下文注册表 [[1]](#sources)。

**产出：** 告警串中的根因诊断；工程师提出要求时，再加上修复 PR 和 Jira 工单。
**失败模式 → 防护：** 数据仓库的瞬时错误若由修复流程自行处理，会产生不必要的工单和 PR → 每项修复都由人决定（83% 的诊断无需任何操作）。编造的 schema 路径（起初约 25% 的查询失败） → 模板化查询加上下文注册表，把失败率降到约 13% [[1]](#sources)。上游 API 漂移等边缘情况 → 仍交给人处理。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [Headway, De-Bug-T: an AI copilot for dbt debugging](https://headway.co/blog/headway-engineering-de-bug-t) (2026-05-07)。上线五周；大多数诊断无需修复，因此有理由让人保留修复决定权。"Of the diagnoses over five weeks, 83% required no action at all."。*第一手：是；可信度：高。*
