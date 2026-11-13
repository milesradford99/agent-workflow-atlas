---
id: AWF-0128
name: 攻击模拟验证检测规则
summary: "在实验室编写并执行攻击模拟，验证检测规则能否告警；每个 TTP 入库前都由人工审核。"
deliverable: 已验证的 TTP 目录
shape: "检测规则 → 编写 TTP 攻击模拟 YAML → 钩子校验 schema → (经 SSH 部署到实验室主机并运行 ⟲ 逐步检查) → 验证智能体轮询 SIEM 的原始事件 + 检测命中 → 超时：调试智能体对失败分类 → 🛑 review (逐个人工审查每个 TTP) → 加入已审阅目录 → 定时运行 → 健康度看板 → 🛑 review (团队决定修复项)"
source_hash: cb236516a767
---

# 攻击模拟验证检测规则

**与相近工作流的区别：** AWF-0005 告警富化与裁决：AWF-0005 对线上告警下判断（自动关闭或转交），并每周抽检审计。本工作流通过在实验室中引爆攻击来测试检测规则本身。它的产出是经验证的模拟目录和缺陷清单，每个产物在定时运行之前都经过人工审阅。
**工具变体：** `claude-code` · `codex` · `ttpforge` · `splunk`

## 步骤

1. 给智能体一条自定义检测规则。一个 Claude Code 插件（skill、钩子、参考资料）让它编写带检查和清理的 TTPForge 攻击模拟 YAML。[[1]](#sources)
2. PostToolUse 钩子在每次写入时运行 `ttpforge validate`，YAML 有效之前阻止继续推进。[[1]](#sources)
3. 智能体把 TTP 复制到一台由生产黄金镜像构建的隔离实验室主机，并通过 SSH 运行。某一步检查失败时，它重写并重新运行。[[1]](#sources)
4. 后台验证智能体每 2 分钟轮询一次 Splunk，超时为 10 分钟。成功需要同时满足：有原始遥测数据，且检测的 SPL 命中。[[1]](#sources)
5. 超时后，只做诊断的调试智能体对失败分类：主机静默、缺少事件类别、入库延迟，或规则谓词拒绝了该事件。[[1]](#sources)
6. 🛑 **审阅**：TTP 进入已审阅目录之前，由人对照检查清单逐个手工审查。[[1]](#sources)
7. 定时的 GitHub Actions 任务回放该目录，并向流水线健康度看板供数。🛑 **审阅**：由人决定检测规则或流水线要改什么。[[1]](#sources)

**产出：** 一份与检测规则对应、经审阅且可重复运行的攻击模拟目录，一个定时更新的健康度看板，以及一份待修复的检测和流水线缺陷清单。
**失败模式 → 防护：** 智能体在无人值守的运行中越出范围（它修改了实验室转发器的配置） → devcontainer 加出站规则，有风险的工作用交互式会话。薄弱的检查让 TTP 在未证明该技术的情况下就“通过” → skill 中的拒绝捷径规则加人工 TTP 审查。把入库延迟当成漏检 → 有限次轮询加调试分类器。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或检查点设在别处。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [DNB CDC, End-to-end detection validation using coding agents](https://blog.cauchy.org/blog/detection-validation/) (2026-06-16)。在实验室中端到端确认了 Netsh helper DLL 持久化（T1546.007）。"the detection matched on five events" after "about a three-minute ingestion lag"（文章称部分数字经过隐去或改动）。*第一手：是；可信度：中。*
