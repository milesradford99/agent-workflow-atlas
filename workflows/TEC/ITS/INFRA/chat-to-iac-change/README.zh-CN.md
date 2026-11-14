---
id: AWF-0066
name: 对话驱动的 IaC 变更
summary: "把 Slack 请求或告警转成附带 plan 结果的基础设施即代码 PR；CODEOWNERS 审批人通过后合并才会生效。"
deliverable: 已应用的基础设施变更
shape: "Slack 请求或监控告警 → 读取 IaC 仓库的既有写法（MCP）→ 生成 Terragrunt/OpenTofu 变更 → 开 PR → PR 上运行 plan，结果发到 PR 和 Slack → 🛑 review (CODEOWNERS 审批 plan) → 合并后 apply → 每日漂移检查"
source_hash: c15d05432b42
---

# 对话驱动的 IaC 变更

**工具变体：** `opentofu-terragrunt-mcp` · `terraform-atlantis` · `hcp-terraform`

## 背景

基础设施工程师配置应用依赖的机器、网络和监控。一句简单的扩容请求可能改变正在运行的资源，因此团队需要精确记录将创建、修改或删除什么。本工作流让智能体把聊天请求或监控告警转化为配置变更提案。交付系统执行前，审阅人先检查预期效果。人工审阅不能省去，因为看起来合理的代码修改仍可能销毁数据或中断服务。

**术语：**
- **IaC / HCL**：基础设施即代码，以及描述资源的配置语言。
- **PR / diff / CI**：提议的仓库修改、被修改的行，以及变更时运行的自动检查。
- **Plan / apply / state**：预览基础设施改动、实际执行，以及保存代码与部署资源对应关系的状态。
- **漂移 / CODEOWNERS**：声明配置与运行基础设施的差异，以及指定必需代码审阅人的文件。
- **MCP / SSH**：智能体工具连接协议，以及远程命令连接。

## 用智能体搭建

**形态：** `service`。聊天与监控事件均可启动无人值守运行，人收到变更提案后审阅。

**需要：** 基础设施仓库及资源示例；限定权限的代码托管和聊天 MCP server (connector) 工具；已有 plan/apply 流水线；分支保护与必需审阅人。Plan 凭据必须只读；起草智能体既没有 apply 凭据，也不能合并。共享 plan 之前应移除密钥。

| 步骤 | 搭建方式 |
|---|---|
| Slack 请求或监控告警 → 读取仓库写法 → 生成变更 | 事件接收器调用 `claude -p` (headless)；Skill 读取仓库示例并起草相同风格的配置。 |
| 开 PR → plan 发到 PR 和 Slack | Skill 通过 MCP server (connector) 工具开 PR；已有流水线生成并报告 plan。 |
| 🛑 review → 合并后 apply | 智能体在 PR 处停下。代码托管平台的必需审阅与受保护合并规则把关，之后才进入单独的 apply 流水线。 |
| 每日漂移检查 | 已有调度器运行只读 plan 命令并报告差异；Skill 可以准备后续审阅项。 |

**检查点：** `review`：必需审阅人收到 diff、plan、原始请求与告警背景。代码托管权限阻止智能体合并或绕过必需审阅；只有获批的交付流水线能 apply。对已审阅版本的实质修改需要重新生成 plan 并批准。

**与来源相比：** 来源出自 2026-06，已于 2026-11 打开。针对更新实例及所列工具的检索，截至 2026-11 未找到更新实例。无界面编码 Skill 可以准备配置，不需要重建来源的机器人内部实现。OpenTofu/Terragrunt、云资源提供方和 plan/apply 流水线仍然必需，通用智能体不能替代。来源中的分工仍然适用：智能体提出变更，基础设施 plan 展示影响，必需的人工审阅把关部署。

*以上是依据本条目的步骤和截至 2026-11 的工具文档做出的设计，不是已报道的实例。*

## 步骤

*以下按来源所述。*

1. 入口有两种：有人在 Slack 里用大白话提出请求（例如“给服务 A 加两个实例”），或者监控告警直接发给智能体 [[1]](#sources)。
2. 智能体通过 MCP 访问 OpenTofu 仓库，找到这类资源已有的代码写法，并以相同风格写出 Terragrunt 变更 [[1]](#sources)。
3. 智能体开一个 PR。若由告警触发，PR 会记录原因、告警和 plan 输出，这样“谁加了服务器、为什么加”就有据可查 [[1]](#sources)。
4. PR 一打开，CI 就自动运行 `plan`，并把结果评论到 PR 上，同时发到 Slack [[1]](#sources)。
5. 🛑 **审阅**：CODEOWNERS 中指定的必需审阅人阅读 plan 和 diff。未经审阅的合并在技术上被禁止。无论变更是人写的还是智能体写的，规则都一样 [[1]](#sources)。
6. 交付流水线在合并后自动执行 apply，因此只有获批的变更才能进入基础设施 [[1]](#sources)。
7. 每日漂移检查把代码与线上基础设施比对，发现有人在控制台改动就在 Slack 告警。有意为之的例外写进 `.driftignore` [[1]](#sources)。

**产出：** 一个已合并的 IaC PR，附 plan 输出，已应用到云上，并以请求或告警作为变更记录。
**失败模式 → 防护：** 审阅人批准了看似很小、实际会替换或销毁资源的 HCL diff → 把 plan 输出作为审阅对象，发在 PR 上。控制台的紧急修复与代码产生漂移 → 每日漂移扫描，加上紧急改动必须回写代码的规则。状态被锁 → 每个项目都有强制解锁的工作流，而不是登录 SSH [[1]](#sources)。

**与相近工作流的区别：** AWF-0001 计划把关式构建和 AWF-0003 委派式 PR 产出的是以测试为关卡的应用代码 PR。这里的请求来自聊天或告警，人工检查点是基础设施的 plan（将创建、修改或销毁什么），而合并本身就是部署。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或把检查点放在了别处。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [LY Corporation, From IaC to AI: Adopting OpenTofu and ChatOps](https://techblog.lycorp.co.jp/en/techverse2026-86) (2026-06-22)。Slack 机器人开 Terragrunt PR，plan 发到 Slack，由人审批，合并后 apply，覆盖 7 个服务。"about 1,500 resources" declared as code (no metric for the agent part itself)。*第一手：是；可信度：中。*
