---
id: AWF-0066
name: 对话驱动的 IaC 变更
summary: "把 Slack 请求或告警转成附带 plan 结果的基础设施即代码 PR；CODEOWNERS 审批人通过后合并才会生效。"
deliverable: 已应用的基础设施变更
shape: "Slack 请求或监控告警 → 读取 IaC 仓库的既有写法（MCP）→ 生成 Terragrunt/OpenTofu 变更 → 开 PR → PR 上运行 plan，结果发到 PR 和 Slack → 🛑 review (CODEOWNERS 审批 plan) → 合并后 apply → 每日漂移检查"
source_hash: 33fbf8740625
---

# 对话驱动的 IaC 变更

**与相近工作流的区别：** AWF-0001 计划把关式构建和 AWF-0003 委派式 PR 产出的是以测试为关卡的应用代码 PR。这里的请求来自聊天或告警，人工检查点是基础设施的 plan（将创建、修改或销毁什么），而合并本身就是部署。
**工具变体：** `opentofu-terragrunt-mcp` · `terraform-atlantis` · `hcp-terraform`

## 步骤

1. 入口有两种：有人在 Slack 里用大白话提出请求（例如“给服务 A 加两个实例”），或者监控告警直接发给智能体 [[1]](#sources)。
2. 智能体通过 MCP 访问 OpenTofu 仓库，找到这类资源已有的代码写法，并以相同风格写出 Terragrunt 变更 [[1]](#sources)。
3. 智能体开一个 PR。若由告警触发，PR 会记录原因、告警和 plan 输出，这样“谁加了服务器、为什么加”就有据可查 [[1]](#sources)。
4. PR 一打开，CI 就自动运行 `plan`，并把结果评论到 PR 上，同时发到 Slack [[1]](#sources)。
5. 🛑 **审阅**：CODEOWNERS 中指定的必需审阅人阅读 plan 和 diff。未经审阅的合并在技术上被禁止。无论变更是人写的还是智能体写的，规则都一样 [[1]](#sources)。
6. 合并后自动执行 apply，因此只有获批的变更才能进入基础设施 [[1]](#sources)。
7. 每日漂移检查把代码与线上基础设施比对，发现有人在控制台改动就在 Slack 告警。有意为之的例外写进 `.driftignore` [[1]](#sources)。

**产出：** 一个已合并的 IaC PR，附 plan 输出，已应用到云上，并以请求或告警作为变更记录。
**失败模式 → 防护：** 审阅人批准了看似很小、实际会替换或销毁资源的 HCL diff → 把 plan 输出作为审阅对象，发在 PR 上。控制台的紧急修复与代码产生漂移 → 每日漂移扫描，加上紧急改动必须回写代码的规则。状态被锁 → 每个项目都有强制解锁的工作流，而不是登录 SSH [[1]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或把检查点放在了别处。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [LY Corporation, From IaC to AI: Adopting OpenTofu and ChatOps](https://techblog.lycorp.co.jp/en/techverse2026-86) (2026-06-22)。Slack 机器人开 Terragrunt PR，plan 发到 Slack，由人审批，合并后 apply，覆盖 7 个服务。"about 1,500 resources" declared as code (no metric for the agent part itself)。*第一手：是；可信度：中。*
