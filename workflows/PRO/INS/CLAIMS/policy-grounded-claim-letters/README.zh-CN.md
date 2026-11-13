---
id: AWF-0096
name: 基于保单条款的理赔函件
summary: "起草引用保单条款的理赔函件，无依据条款时拦截；由理赔员复核，保险公司批准后发出。"
deliverable: 保障范围决定函
shape: "理赔档案 + 保单声明页 + 估损单 → 生成引用保单条款的函件 → 没有支持条款：拦截 ('no relevant policy language found') → 🛑 review (内勤理赔员) → 🛑 sign-off (保险公司批准) → 发出"
source_hash: 7236f3a2c5a7
---

# 基于保单条款的理赔函件

**与相近工作流的区别：** AWF-0024 依据审查手册的合同审阅（Playbook contract review）是对照审查手册给合同做批注。这里的产出是以保单为依据、对外发出的保障范围函件，检查点是保险公司的批准。
**工具变体：** `voltaire`

## 步骤

1. 系统分析理赔档案、保单声明页和估损单，然后从头生成拒赔、部分拒赔或赔付函件 [[1]](#sources)。
2. 如果理赔员试图在没有有效保单条款的情况下拒赔，工具会返回“no relevant policy language found”[[1]](#sources)。
3. 🛑 **审阅**：内勤理赔员修改函件 [[1]](#sources)。
4. 🛑 **签发**：函件交保险公司批准；在使用该工具之前，函件常因保单措辞或语法有误而被“退回”[[1]](#sources)。

**产出：** 经保险公司批准、发给投保人的保障范围函件。
**失败模式 → 防护：** 引用了错误的保单措辞 → 生成器拒绝生成它无法找到依据的拒赔。巨灾期间业务激增、新入职的内勤理赔员多 → 内置各保险公司专用的格式。

## 公开实例

覆盖度（截至 2026-11-06）：**薄弱**：只有匿名、与厂商相关或由记者转述的说法。收集与复核见 [Second collection pass](../../../../../research/2026-11-second-pass.md)。

- [Voltaire, PC360 webcast with TSI Adjusters](https://voltaire.claims/blog/actionable-ai-that-adjusters-actually-adopt-about-voltaires-recent-pc360-webcast-with-tsi-adjusters/) (2025-11-18)。TSI 在飓风 Helene 和 Milton 期间为一家保险公司使用该工具，并让 60 多名内勤理赔员上手。"One adjuster reported saving two hours daily.". *第一手：厂商（Voltaire 对其网络研讨会的回顾；未点名理赔员）；可信度：中。*
