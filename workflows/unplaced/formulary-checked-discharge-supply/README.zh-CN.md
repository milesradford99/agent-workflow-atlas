---
id: AWF-0221
name: 对照处方集的出院用药供应
summary: "对照接收机构的处方集检查每条出院用药；药师逐条验证后才供药。"
deliverable: 用药供应决定清单
shape: "为转入过渡护理机构的患者开具出院处方 → 把非结构化的医嘱清单粘贴进企业 AI 助手 → 智能体解析每条医嘱（药品、剂量、剂型） → 每条医嘱：对照接收机构的处方集匹配 → 每行给出供应 | 不供应建议 → 🛑 review (药师在配发前验证每一行；假阴性是最需要避免的错误) → 只打包并送出不在处方集内的药品 → 配药系统变更后，对处方样本定期重新验证 → 🛑 sign-off (质量团队确认准确率后才可继续使用)"
source_hash: a6f07c0222b2
---

# 对照处方集的出院用药供应

**与相近工作流的区别：** 现有唯一的药房条目 AWF-0215 药师核验的处方录入，是一个分段的 RPA 机器人，把处方录入药房管理系统，配发前有两次先后的药师核验（QV1/QV2）。替换测试不通过：本工作流的交付物是在护理过渡时，对照另一机构的处方集逐行给出供应/不供应决定（而不是录入完成的处方记录）；这里只有一次药师审阅，而不是两阶段核验链；自主程度是辅助（没有“跳过并记录”的自主档）；并且在系统变更后设有自己的重新验证关卡。
**工具变体：** `pair-govtech-assistant` · `pairchat-epic-assistants`

## 步骤

1. 医院药房收到一位转入过渡护理机构（社区医院或疗养院）的患者的出院处方，该机构的部分药品由自己的处方集供应。医嘱数据是从配药系统中复制出来的，没有结构，因此无法使用电子表格宏 [[1]](#sources)。
2. 药房工作人员——不具备编程技能——在 Pair（获准处理“受限/敏感-一般”级数据的政府 AI 平台）上配置了一个助手，存入接收机构的处方集和供应规则 [[1]](#sources)。
3. 粘贴进来的医嘱清单被解析，每一行药品都与该机构的处方集交叉核对；助手实时返回每行的供应 / 不供应建议 [[1]](#sources)。
4. 🛑 **审阅**：药师在供应决定敲定之前验证每条建议。论文明确指出，系统必须保持为决策支持，并强制人工监督，因为假阴性意味着本应供应的药品没有供应 [[1]](#sources)。
5. 转运时只配发建议的药品，减少接收机构的过量供应和浪费 [[1]](#sources)。
6. 🛑 **签发**：2025 年 6 月医院从 iPharm 迁移到国家统一综合药房系统后，药房在继续依赖该助手之前，用 100 张新抽取的处方重新做了技术评估；准确率保持在 99.4%，假阴性从三例降到零 [[1]](#sources)。
7. 同一家医院的并行部署表明这一模式可以推广：在同一平台上构建的两个 LLM 助手（EPIC Notes Analyser；Medication Change Identification）用于出院处方处理，遵循同样的强制验证规则，并通过 63 位独立用户的持续反馈进行监测 [[2]](#sources)。

**产出：** 针对转院患者出院处方的、经验证的逐行供应决定，用于打包转运药品；准确率和工时测量指标进入药房的质量审查。
**失败模式 → 防护：** 假阴性漏掉了需要的药品 → 强制药师逐行验证，并建立以假阴性为重点的错误分类。配药系统改变输出格式导致漂移 → 系统迁移后用新的 100 张处方样本做全面重新评估。员工高估节省的时间（92.3% 的人认为每张处方节省超过 3 分钟，而实测约 48 秒） → 采用工时测量，而不是自我报告。周末轮岗人员不熟悉机构规则 → 由助手承载处方集，而不是依赖人员名册。

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。收集与复核见 [Fourth collection pass](../../../research/2026-11-fourth-pass.md)。

- [Tan, Yew & Phua, Evaluation of an AI-Assisted Decision Support for Medication Supply in Stepdown Care Transitions](https://www.rescp.org/journal/view.html?uid=311&vmd=Full&year=) (2025-12-31)。医院的前瞻性评估，药师验证每一条建议。"The AI assistant achieved 99.5% overall accuracy in the former system and 99.4% in the new system"; "a 68.5% reduction in processing time per medication (median 5.4 to 1.7 seconds)". *第一手：是；可信度：高。*
- [Tan W.Q. et al., Integration of AI Powered Co-Pilot Tools for Discharge Prescription Processing Efficiency](https://www.rescp.org/journal/view.html?uid=218&vmd=Full&year=) (2025-12-31)。同一家医院，在出院处理中采用同样的强制验证规则。"an average of 17% reduction in processing time"; "analysis of 1,219 utilisations". *第一手：是；可信度：高。*
