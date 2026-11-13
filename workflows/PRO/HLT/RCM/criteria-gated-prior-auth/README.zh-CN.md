---
id: AWF-0032
name: 按标准把关的预授权申请
summary: "对照支付方标准核查病历，起草文件清单和申请信；工作人员修改并提交申请或申诉。"
deliverable: 预授权申请材料包
shape: "病历号 + 药品 + 支付方标准 → 提取病历数据 → 逐条核查标准 → 满足 | 不满足 (停止，列出未满足项) → 文件清单 + 申请信 → 🛑 review (预授权人员选择病历、修改申请信) → 🛑 action (工作人员提交申请或申诉)"
source_hash: 288c44faaef4
---

# 按标准把关的预授权申请

**与相近工作流的区别：** AWF-0026 诊室环境语音病历助手（Ambient scribe，CLINDOC）根据对话生成就诊病历。本工作流生成的是提交给支付方的材料，在标准不满足时可以停止，并由人提交。
**工具变体：** `epic-maestro-care-llm` · `nds-appeals-ai` · `notable-sidekick` · `latent-health`

## 步骤

1. 按药品逐一设置：用回顾性的批准和拒付记录建立基准文件。把 LLM 按条标准的输出与之对比。优化提示词和源数据并重新测试，直到输出一致 [[1]](#sources)。
2. 工作人员输入患者的病历号（MRN）、药品和日期。修改日期会让工具从新的授权申请切换为拒付申诉 [[1]](#sources)。
3. 工具实时从电子病历中提取医生记录、体征记录表、检验、医嘱、用药和 ICD 编码，并与支付方的预授权及医学必要性标准结合 [[1]](#sources)。
4. LLM 逐条评估标准。只要有一条标准未满足，工具就提示用户停止，并列出哪些标准已满足、哪些未满足 [[1]](#sources)。
5. 所有标准都满足时，工具生成文件清单，并起草一封引用支持性临床信息的申请信 [[1]](#sources)。
6. 🛑 **审阅**：医学必要性与拒付团队的工作人员依照清单，在信息公开（release-of-information）流程中选择病历并修改申请信 [[1]](#sources)。在申诉的变体中，工作人员阅读并修改每份 AI 起草的申诉，然后批准或驳回。对于医学必要性案件，医生审阅其中的临床论证 [[2]](#sources)。
7. 🛑 **操作**：工作人员把材料包或申诉提交给支付方。复杂的、高金额的医学必要性拒付仍由人工团队处理 [[2]](#sources)。

**产出：** 一份可直接提交给支付方的预授权或申诉材料包（申请信加所选病历），由工作人员提交。已分类的拒付数据回流给前端授权团队。
**失败模式 → 防护：** 支持性文件不匹配（在 Duke 评估的 970 条标准中有 7 处错误）→ 上线前按药品做基准验证，并由工作人员自己挑选病历 [[1]](#sources)。超出范围的复杂拒付 → 划出范围，转交人工和医生 [[2]](#sources)。

**近期实践（2026）：**
- 异常处理步骤：自动化出错（缺少过敏信息、材料包生成失败）时，创建带有明确说明的员工任务，而不是悄悄留下缺口（Notable/MIT Health）。[[3]](#sources)

## 公开实例

覆盖度（截至 2026-11-06）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [New workflows for empty categories](../../../../../research/2026-11-new-workflows.md)。更多实例见 [Third collection pass](../../../../../research/2026-11-third-pass.md)。

- [Duke DIHI, Medical Prior Authorization Assistant](https://dihi.org/project/using-ai-to-reduce-the-burden-of-prior-authorizations-2/) (2026-04-01)。按药品的 LLM 标准核查先在回顾性病例上验证，再与拒付团队一起上线。"the LLM correctly assessed the authorization status for all 83 cases across the three medications"。*第一手：是；可信度：高。*
- [NDS InfoServ, AI-generated appeals case study](https://www.ndsinfo.com/case-studies/appeals) (n.d.)。根据 835 文件和电子病历起草申诉信，工作人员修改并批准后才提交。"Reviewing and approving an AI-generated appeal took 8–12 minutes"。*第一手：厂商；可信度：中。*
- [Northwestern Medicine, AI Helps Improve Access to Specialty Medication](https://nmventures.org/en/latent) (n.d.; pilot early 2025)。专科药房试点：工具从 Epic 提取病历证据，支持工作人员提交预授权。"the average time to complete a PA decreased by 67%, from 17 minutes to 5 minutes and 20 seconds"。*第一手：是；可信度：中。*
- [Notable, MIT Health cut prior auth time in half](https://www.notablehealth.com/customer-stories/mit-health-cut-prior-auth-time-in-half-with-ai) (2026-11-10)。智能体预先组装临床材料包并回答支付方的问卷；出现失败时创建人工任务。"completed in an average of 6 minutes, an estimated 45% reduction from the previous average ~11-minute handling time"。*第一手：厂商；可信度：中。*
