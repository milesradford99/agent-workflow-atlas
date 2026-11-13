---
id: AWF-0206
name: 自主闭环的 HR 服务台
summary: "回答 HR 问题并在人事系统中办理常规事务；敏感或超范围的情况转交 HR 伙伴。"
deliverable: 已办结的 HR 事务
shape: "员工或经理在聊天中提出请求 → 分类并路由到 HR 领域 (福利、薪酬、职业发展) → 依据本地政策和个人记录作答 | 在 HR 系统中办理事务 (证明信、休假、调动、晋升环节) → 敏感或超范围：🛑 handoff (HR 伙伴) → 满意度调查 → 增加自动化"
source_hash: bca4d4f18e17
---

# 自主闭环的 HR 服务台

**与相近工作流的区别：** AWF-0144（经理批准的招聘流程操作）和 AWF-0029（寻访-筛选-排期招聘）都是招聘类工作流，按批次或按决定审批。本工作流属于 HR 的员工服务一侧：智能体端到端办结大部分请求，人只接手 6% 的转交。交付物和自主程度都不同。
**工具变体：** `watsonx-orchestrate`

## 步骤

1. 员工和经理通过同一个聊天入口（AskHR）办理 HR 事务；IBM 关闭了 HR 电话热线和邮箱，使其成为唯一入口 [[1]](#sources)[[3]](#sources)。
2. 由 LLM 对提示词分类，并路由到相应的 HR 领域（福利、薪酬、职业与技能）[[2]](#sources)。
3. 对于提问，它结合本地薪酬和 HR 政策给出个性化答复；对于任务，它直接在后台系统（Workday、SAP SuccessFactors、Concur）中办理：在职证明信、休假申请、经理发起的员工调动、季度晋升中的环节、薪酬和组织变更 [[2]](#sources)[[3]](#sources)。2025 年起，它为多步骤的 HR 事务编排多个智能体 [[3]](#sources)。
4. 🛑 **接手**：它无法闭环处理的请求，以及低绩效或违纪等敏感事项，转交人类 HR 伙伴 [[1]](#sources)[[4]](#sources)。
5. 跟踪满意度（CSAT/NPS）并不断增加新的自动化；目前已有近 90 项 [[1]](#sources)[[3]](#sources)。

**产出：** 已回答的 HR 问题和在记录系统中办结的 HR 事务；其余情况转给 HR 伙伴。
**失败模式 → 防护：** 强制推行使满意度一度下滑（NPS -35）→ 不断改进答复并增加可办理的事务，直到 NPS 回升 [1]。机器人处理了敏感案例 → 按政策转交人工 [4]。办错事务 → 仅在发起请求的经理于 AskHR 内下达指令时才执行（确切的确认步骤未公开说明）。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [IBM CHRO, Embracing the future of HR](https://www.ibm.com/think/insights/embracing-future-of-hr-ai-first-enterprise) (2025-04-29)。IBM 自家的 HR 服务台：闭环率、转交占比、事务提速。"In 2024, AskHR handled more than 11.5 million interactions; 94% of those interactions were contained within the platform"。*第一手：是；可信度：高。*
- [IBM, HR | IBM Transformation](https://www.ibm.com/case-studies/ibm-transformation/ask-hr) (2026-07-16)。2025 年为 HR 事务做多智能体编排；业务量。"That same year, AskHR handled more than 16 million individual user messages."。*第一手：是；可信度：高。*
