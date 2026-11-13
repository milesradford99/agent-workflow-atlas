---
id: AWF-0051
name: 受控题库的 RFP 应答草稿
summary: "基于已验证的资料库起草 RFP 答复并附来源；专家或合规人员审核标记项，最后由人签发。"
deliverable: RFP 应答草稿
shape: "接收 RFP/问卷 → 适配性检查（拒收不对口的文档）→ 拆解成问题 → 每个 问题：从已验证的资料库检索 + 起草并附来源追溯 → 标记无法回答的 → 🛑 review (专家/GRC 处理标记项) → (售前工程师（SE）评论 ⟲ 重新生成) → 🛑 sign-off → 按买方格式导出 → 把获批的修改回流到资料库"
source_hash: fa9260a0342e
---

# 受控题库的 RFP 应答草稿

**与相近工作流的区别：** 暂无相近者。AWF-0024 按手册审阅合同（Playbook contract review）依据手册审阅收到的合同；本工作流则基于获批的资料库起草对外的答复。
**工具变体：** `in-house-agentic-rag` · `conveyor` · `responsive`

## 步骤

1. 知识库只用经过验证、持续更新的产品文档和合规证书来构建 [[1]](#sources)。Zapier 把 434 条知识条目和 2,675 条历史答复接入同一个资料库 [[2]](#sources)。
2. 销售或售前工程师在销售日常工作的地方上传请求。智能体先检查自己能否回答这份文档，拒收不对口的文档，并告诉销售还需要什么 [[2]](#sources)。
3. 智能体检索对照获批语料检查每个问题，并把每条答复追溯到来源。智能体不能编造功能，也不能声称公司并不具备的合规资质 [[1]](#sources)。
4. 🛑 **审阅**：只有真正需要人工把关的地方，才会标记给安全/GRC 团队 [[2]](#sources)。售前工程师对草稿添加评论，AI 重新生成更新版本 [[1]](#sources)。
5. 🛑 **签发**：售前工程师根据客户的目标修改，并批准最终答复。系统从每次互动中学习 [[1]](#sources)。

**产出：** 一份按买方格式完成、可以提交的 RFP、RFI 或安全问卷，以及一个因获批修改而改进的资料库。
**失败模式 → 防护：** 过时或已弃用的规格进入答复 → 只使用受管控的语料，且每条答复都有溯源 [[1]](#sources)。智能体回答超出范围的文档 → 接收时做适配性检查 [[2]](#sources)。过度依赖掩盖缺口 → 把被标记的问题转给安全团队 [[2]](#sources)。

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。

- [Palo Alto Networks, From Weeks to Minutes](https://www.paloaltonetworks.com/perspectives/from-weeks-to-minutes-how-we-applied-an-ai-first-transformation-to-the-rfp-bottleneck/) (2026-03-26)。内部“头号客户（customer zero）”RFP 副驾；售前工程师修改并重新生成基于已验证语料的 AI 草稿。"delivering RFPs in days instead of weeks"。*第一手：是；可信度：高。*
- [Conveyor, Zapier playbook](https://www.conveyor.com/blog/steal-the-playbook-zapier) (2026-02-24)。Zapier 的 GRC 团队只审阅智能体起草的问卷中被标记的问题。"only 20% of security questions require a security team member which is down from 90%"。*第一手：厂商；可信度：中。*
