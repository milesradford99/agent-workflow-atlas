---
id: AWF-0060
name: 从需求文档到工单规划
summary: "把需求文档拆解成工单项目计划并录入任务系统；拆解方案由人反复修改，产品和研发共同评审工单。"
deliverable: 带工单的项目计划
shape: "文档中的需求 → 智能体读取需求和代码库 → 拆解草案（任务、顺序、依赖、涉及文件）→ 🛑 plan (提出异议、反复修改) → 通过 MCP 在任务系统中创建项目和工单 → 🛑 review (产品经理 + 研发) → 🛑 handoff (交给实施者)"
source_hash: 89e808f5b732
---

# 从需求文档到工单规划

**工具变体：** `claude-code-linear-mcp` · `notion-mcp` · `gh-cli-issues`

## 背景

产品经理描述问题和团队要交付的结果，工程师则需要范围合适、能够按合理顺序实施的工作项。把这两种视角连接起来，需要了解现有代码，也要找出产品描述中没有明说的依赖。本工作流让智能体起草拆解方案，创建双方同意的工单。发布之前先由人检查计划，产品和研发再共同审阅工单。优先级、范围和遗漏仍由他们负责。

**术语：**
- **Spec / PRD**：规格或产品需求文档，写明问题、预期行为和约束。
- **PM / 依赖**：产品经理，以及另一项任务开始前必须完成的工作。
- **任务系统 / 工单（tracker / ticket）**：共享的工作规划系统，以及其中的单个工作项。
- **MCP / CLI**：连接智能体工具与其他系统的协议，以及命令行界面。
- **数据建模 / 边界情况**：定义信息的表示方式，以及实现必须处理的少见条件。

## 用智能体搭建

**形态：** `skill`。产品经理或工程师在对话中规划一个项目，不需要独立的无人值守控制器。

**需要：** 需求文档及代码库只读权限；工单模板；获批的文档和任务系统 MCP server (connector) 工具，或议题 CLI。写入范围限定在目标项目内，保密计划留在获批系统中。

| 步骤 | 搭建方式 |
|---|---|
| 需求 → 读取需求和代码库 → 拆解草案 | Skill 读取需求及相关源码，写出任务、顺序、依赖、涉及文件和未决问题。 |
| 🛑 plan → 创建项目和工单 | Skill 展示提议的工单集合并停下。批准后，通过权限受限的 MCP server (connector) 工具只创建该集合。 |
| 🛑 review → 🛑 handoff | Skill 列出已创建工单链接与未决问题；产品和研发修改后，再分配实施工作。 |

**检查点：** `plan`：Skill 写工单之前，由人审阅拆解方案及目标任务系统。`review`：智能体向产品经理和研发交出已创建的集合后停下。`handoff`：实施者收到双方同意的工单，并再次检查需求；规划 Skill 不启动实施。

**与来源相比：** 条目列出的证据为 2026-04 及未标日期的记录。2026-11 打开 Matos 页面时只有标题；Every 页面只能读到订阅边界，因此未重新核实所引的工单数量。Every 现在显示发布于 2026-05、更新于 2026-11。检索发现 [Anthropic 当前的 Skill 规划指南](https://claude.com/resources/guides/the-complete-guide-to-building-skills-for-claude/planning-and-design)，已于 2026-11 打开，将基于任务系统的迭代规划列为 Skill/MCP 用例。这支持所提的打包方式，不能验证受限页面中的结果。流程不需要专门的规划平台，优先级与验收仍需由人确定。

*以上是依据本条目的步骤和截至 2026-11 的工具文档做出的设计，不是已报道的实例。*

## 步骤

*以下按来源所述。*

1. 产品经理照常在 Notion 中撰写需求文档（问题、目标、指标、用户故事、约束）[[1]](#sources)。单人变体中则是一份路线图 README [[2]](#sources)。
2. 产品经理或工程师通过 Notion MCP 让 Claude Code 读取需求文档，并请它给出项目计划。智能体提出任务、顺序、依赖，以及每个任务在代码库中涉及的部分 [[1]](#sources)。
3. 🛑 **计划**：人阅读拆解方案，并提出异议（“为什么要拆 X 和 Y？它们改的是同一个文件”“你漏了迁移这一步”），来回几轮直到方案严密 [[1]](#sources)。
4. 智能体通过 MCP 把计划推送到 Linear：建一个项目，每个工单都带有优先级、描述，以及产品和技术两方面的背景 [[1]](#sources)。变体则通过 gh CLI 使用 GitHub issues [[2]](#sources)。
5. 🛑 **审阅**：产品经理和研发共同评审创建好的工单。他们移动、删除或重新排定工单优先级，并指出遗漏的部分 [[1]](#sources)。
6. 🛑 **接手**：工单交给工程师或编码智能体。实现某个工单之前，负责人要再次审阅其需求，关注数据建模和边界情况 [[2]](#sources)。

**产出：** 一个结构化的 Linear（或 GitHub）项目，工单范围明确、优先级清晰，可直接用于迭代排期或交给智能体领取。
**失败模式 → 防护：** 工单拆分时不了解代码库 → 智能体在拆解时读取仓库。默认用户完全理性，遗漏边界情况和微交互 → 实现前由人再次审阅 [[2]](#sources)。智能体速度快但不担责 → 强制产品经理 + 研发评审 [[1]](#sources)。

**与相近工作流的区别：** AWF-0001 计划把关式构建（plan-gated build）：其计划关卡通向代码 PR。本工作流的交付物止于任务系统中已评审的工单集合，代码工作随后交接出去。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [João Matos, The bottleneck has moved](https://joaomatos.me/notes/bottleneck-moved-fixed-it) (2026-04-10)。通过 Claude Code 和 MCP，把 Notion 需求文档变成经过评审的 Linear 项目。"The review usually takes 15–30 minutes"; "Total time from Notion doc to ready-to-work Linear project: under an hour."。*第一手：是；可信度：高。*
- [Marcus Moretti, Claude Code for Product Managers](https://every.to/source-code/claude-code-for-product-managers) (n.d.)。从路线图 README 生成 GitHub issues；产品经理在实现前逐个重新审阅工单。"Claude produced about 100 detailed tickets"。*第一手：是；可信度：高。*
