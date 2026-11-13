---
id: AWF-0004
name: 先分诊后处置
summary: "对告警展开调查、给出带证据的假设排序并起草复盘；任何运行手册操作均由值班工程师批准。"
deliverable: 事件处置结果
shape: "告警 → 路由到运行手册 → 每个信号：调查 (指标、日志、链路追踪、部署) → 假设排序 → 🛑 action → 执行运行手册步骤 → 检查 SLO → 起草复盘 → 🛑 review → 更新运行手册"
source_hash: a446ca4fe3c5
---

# 先分诊后处置

## 步骤

1. 告警触发智能体，智能体按服务标签路由到对应的运行手册。
2. 并行进行只读调查：错误激增、时间窗口内的部署、典型链路追踪，以及可疑的 diff。
3. 把带证据链接的假设排序发到事件频道。
4. 🛑 **操作**：值班工程师批准某条具体的运行手册命令（回滚、扩容、重启）。
5. 对照 SLO 验证是否恢复。
6. 起草复盘。🛑 **审阅**：事件负责人修改，尤其是根因和后续行动项。
7. 更新运行手册。

**防护：** 写操作工具限制在运行手册命令的白名单内，由代码强制执行。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或检查点设在别处。来自 [Where are the real runs?](../../../../../research/2026-11-real-runs.md)；每个数字都已对照原页面复核。

- [Hsu, Neu, Farrag, Kindi, Meta Engineering](https://engineering.fb.com/2024/06/24/data-infrastructure/leveraging-ai-for-efficient-incident-response/) (2024-06-24)。检索器加 LLM 排序器 → 给出前 5 个可疑代码变更供响应人员核查。"42% of these investigations had the root cause in the top five"。*第一手：是；可信度：中。*
- [Goutham Veeramachaneni, *I built an AI SRE in 60 mins*](https://www.gouthamve.dev/i-built-an-ai-sre-in-60mins-you-should-too/) (2026-04-21)。对照知识库重放近期的告警；提交运行手册更新 PR，由人评审。"the false positive rate is less than 10% now"（没有评测）。*第一手：是；可信度：中。*
- [Chatwoot, *Introducing Faultline*](https://faultline.chatwoot.com/blog/introducing-faultline) (2026-02-18)。只读智能体跨 PagerDuty、New Relic、Sentry、AWS 和 GitHub 调查他们自己的事件。"typically makes 25-30 API calls"。*第一手：是；可信度：中。*
