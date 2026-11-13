---
id: AWF-0189
name: 先自修复再转人工
summary: "端到端诊断并用已知安全手段修复故障虚拟机；高风险或未知情况转交支持工程师。"
deliverable: 已解决的支持工单
shape: "用户报告无法访问托管虚拟机 → 程序化检查 → 只读诊断编排器 (资源健康、平台 API) → 原因明确: 停止 | 专项智能体通过串口控制台诊断 → 已知的安全修复: 自动修复 (重启、重置密码或网卡、控制台命令) → 验证修复 → 关闭 | 有风险或未知: 🛑 handoff (支持工程师拿到完整诊断) · 发布前: 弄坏测试虚拟机 + 评测"
source_hash: 78c549fe51e2
---

# 先自修复再转人工

**与相近工作流的区别：** AWF-0068 Slack IT 请求智能体（Slack IT request agent）只有在应用审批人对每个请求操作之后才开通权限。这里智能体端到端地诊断并修复基础设施，没有逐项审批，人只负责接手。自主程度是抽检而不是分段，产出物是修复后的系统，而不是授予的权限。
**工具变体：** `microsoft-foundry` · `microsoft-agent-framework` · `azure-serial-console` · `azure-ai-evaluation`

## 步骤

1. 把“如何做”类问题转给基于用户指南的 RAG 信息智能体。把连接问题转给故障排查智能体 [[1]](#sources)。
2. 用户选择虚拟机并报告 RDP 问题。智能体会实时显示它检测到什么、做了什么的摘要 [[1]](#sources)。
3. 先运行程序化检查。然后由只读诊断编排器决定要收集什么：Azure 资源健康、Managed Cloud Labs API，或转给通过串口控制台操作的专门的 Windows RDP 智能体。当早期信号显示原因明确时，它会提前停止 [[1]](#sources)。
4. 当问题是它可以安全处理的类型时，自动修复编排器会重启虚拟机、重置密码或网络接口，或发送串口控制台命令。然后它先验证修复，再结束这一循环 [[1]](#sources)。
5. 🛑 **接手**：当修复带有风险或超出已知场景时，智能体把完整的诊断上下文交给用户，由用户转交人工支持工程师 [[1]](#sources)。
6. 在发布前以及每次变更时，用几十种方式故意弄坏测试虚拟机，并运行评测，检查修复是否安全、一致 [[1]](#sources)。

**产出：** 一台已修复并验证的虚拟机，工单被避免或关闭。否则是交给支持工程师的诊断包。
**失败模式 → 防护：** 修复在不同操作系统版本上表现不同 → 对每个受支持的 Windows 版本做大量测试，并用故意弄坏的测试虚拟机加评测。不安全的修复 → 只执行已知的安全修复动作，有风险的情况转交人工。“如何做”类问题的知识陈旧 → 用户指南是唯一的事实来源。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Microsoft Inside Track, Resolving repetitive support tickets at Microsoft with AI automation](https://www.microsoft.com/insidetrack/blog/resolving-repetitive-support-tickets-at-microsoft-with-ai-automation/) (2026-08-13)。故障排查智能体在 150,000+ 台内部实验室虚拟机上运行的第一个月。"Reduce the average time to mitigate a common connectivity ticket from 16 hours to 15 minutes."。*第一手：是；可信度：高。*
