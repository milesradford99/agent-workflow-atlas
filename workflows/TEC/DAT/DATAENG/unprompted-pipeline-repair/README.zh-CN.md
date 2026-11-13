---
id: AWF-0191
name: 主动修复数据管道
summary: "主动接手数据管道故障，提交经测试的修复 PR 或根因报告；由工程师合并或处理。"
deliverable: 经测试的修复 PR
shape: "管道故障告警 | 定时代码异味扫描 → 拉取日志 + 代码 + 已知修复知识库 → 对故障分类 → 代码问题: (在开发沙箱中应用修复 ⟲ 运行受影响的测试) → 带完整上下文开 PR | 源数据问题: 根因报告 + 给源数据负责人的说明草稿 → 🛑 review (工程师合并 PR 或根据报告处理) → 新的故障模式写入知识库"
source_hash: 61976f3d1bfc
---

# 主动修复数据管道

**与相近工作流的区别：** AWF-0124 被召唤的 dbt 调试员（Summoned dbt debugger）只有在工程师 @ 它时才启动（🛑 action），并且只有在工程师决定修复后才起草修复（第二个 🛑 action）。这里智能体在每次故障时主动运行，并按计划运行以做改进工作，直接产出经沙箱测试的 PR，唯一的检查点是合并审阅：检查点安排不同，首个产出物也不同（是 PR，而不是诊断线程）。
**工具变体：** `snowpark-container-services` · `dbt-cloud` · `dbt-mcp` · `notion-kb` · `bigquery` · `claude-code-headless`

## 步骤

1. 每次受监控的管道故障（来自调度器的 webhook）都会触发，也按计划触发（例如每 12 小时），扫描管道中的代码异味和性能问题；无需工程师来召唤智能体 [[1]](#sources)[[2]](#sources)。
2. 由确定性脚本而不是智能体收集上下文：克隆仓库、下载运行产物、只把失败的测试提取成紧凑的摘要、把团队的已知故障知识库渲染成 markdown，并把生产数据克隆到开发沙箱 [[2]](#sources)。
3. 智能体先搜索知识库，匹配到文档化的修复时就严格照做；否则从头调查日志、DAG 血缘和数据，在上游修复，而不是逐个给下游测试打补丁 [[2]](#sources)。
4. 对每个故障分类：CODE（可在项目内修复）或 SOURCE（上游数据有问题）。SOURCE 问题只出报告：智能体用诊断查询记录根因，为源数据负责人起草一段通俗英文说明，绝不在代码里加变通办法 [[2]](#sources)。
5. 对 CODE 修复，应用改动并在沙箱中运行受影响的模型/测试直到通过；生产保持只读，由数据仓库角色强制执行 [[2]](#sources)。Snowflake 的智能体在 "before anything touches production" 之前测试修复 [[1]](#sources)。
6. 带完整上下文开 PR 并通知团队频道；Snowflake 报告从检测到 PR 平均不到 16 分钟 [[1]](#sources)。
7. 🛑 **审阅**：工程师审阅并合并 PR（或根据源数据报告采取行动）；"The agent proposes the repair. A person still decides what ships." [[1]](#sources)。输出是 PR 而 "not an auto-merged commit"，因为 CODE/SOURCE 分类并不完美 [[2]](#sources)。
8. 出现新的故障模式时，由人在知识库中添加一条记录；下一次运行就会遵循它 [[2]](#sources)。

**产出：** 每天早上有一个经测试的修复 PR（或带起草的干系人说明的源数据根因报告）等着值班工程师；以及已合并的 PR 和知识库条目。
**失败模式 → 防护：** 智能体用一个取巧的过滤条件掩盖糟糕的源数据 → 按规则 SOURCE 问题只出报告 [2]。智能体逐个给失败的测试打补丁 → 提示词要求在上游修复 [2]。智能体把 CODE 与 SOURCE 分错类 → 人工审阅 PR，不自动合并 [2]。智能体触碰生产环境 → 只读角色、沙箱中的 dbt 运行 [2]。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Snowflake, How Snowflake Built an Agent to Fix Broken Data Pipelines](https://www.snowflake.com/en/blog/ai-agent-fixes-data-pipeline-failures/) (2026-10-19)。在内部团队的管道上已在生产环境运行 5 个月；每个受监控的故障都被调查；PR 由人合并。"Under 16 minutes from incident detection to PR creation."; "100s of PRs merged."; "500+ pipelines improved."。*第一手：是；可信度：高。*
- [Hiflylabs, Agentic System for DataOps](https://hiflylabs.com/blog/2026/3/5/ai-agent-for-data-pipeline-ops) (2026-03-05)。咨询公司为客户的 dbt Cloud 作业搭建的生产系统；先查知识库的修复、CODE/SOURCE 分流、PR 审阅。"Total elapsed time: maybe an hour. The fix itself took two minutes." (人工基线)。*第一手：是；可信度：中。*
