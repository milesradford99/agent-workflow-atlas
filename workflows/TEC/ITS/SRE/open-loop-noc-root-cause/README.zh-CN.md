---
id: AWF-0127
name: 网络故障根因分析（NOC）
summary: "分析网络告警，在故障工单中标注根因和建议措施；NOC 工程师采纳或修改，复杂问题升级至二线。"
deliverable: 故障工单标注
shape: "网络告警 / 故障情形 → 收集网元数据 → 根因分析 (检索、标注) → 建议措施 → 整理成工单 → 🛑 review (NOC 工程师采纳或修改标注) | 复杂：🛑 handoff (二线运维人员)"
source_hash: 2b1ea214c54d
---

# 网络故障根因分析（NOC）

**与相近工作流的区别：** 与 AWF-0004 同属一类，但这里智能体从不执行任何 runbook 步骤（没有操作检查点）。产出是给人工运维人员看的工单标注。
**工具变体：** `docomo-agentic-ai` · `langgraph-mcp`

## 步骤

1. 告警到达；智能体确认告警并从网元收集数据 [[1]](#sources)。
2. 多智能体根因分析；Atsky 采用固定的四步流程：检索 → 标注 → 建议 → 格式化 [[1]](#sources)[[2]](#sources)。
3. 提出建议措施并发布分析报告 [[1]](#sources)[[2]](#sources)。
4. 🛑 **接手**：升级给二线运维人员（DOCOMO）[[1]](#sources)。🛑 **审阅**：'the agent recommends, the NOC decides'（Atsky）[[2]](#sources)。

**产出：** 带标注的故障工单，含排序后的根因和一条建议措施。
**失败模式 → 防护：** 告警噪声 → 抑制。答案不可复现 → 用确定性流程，而不是开放的智能体循环。

## 公开实例

覆盖度（截至 2026-11-06）：**部分**：有第一手实例，但只覆盖流程的一部分，或检查点设在别处。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [NTT DOCOMO, AI-Centric Network](https://www.docomo.ne.jp/english/binary/pdf/info/media_center/event/mwc26/AI-Centric_Network.pdf?ver=1772615651) (2026, MWC)。覆盖 1M+ 台设备的商用网络运维。"Reduces recovery time by more than 50%"。*第一手：是；可信度：中。*
- [Atsky, Tier-1 NOC](https://www.atsky.io/case-study/aiops-telco-network-operations) (n.d.)。北欧运营商，经由 Nokia；MVP 在 250 个历史情形上测试。"84% of annotations accepted as written by NOC engineers"。*第一手：厂商；可信度：中。*
