---
id: AWF-0148
name: 报关单预录与经纪人复核
summary: "根据进口商单据预录报关单，每个字段附置信度和出处；录入员复核，报关经纪人最终确认申报。"
deliverable: 报关单
shape: "进口商单据 → 提取为报关单字段，附置信度 + 出处 → 匹配零件库 (HTS、原产地、Chapter 99 / Section 232 叠加) → 进口商专属的 SOP 规则 → 🛑 review (录入员 / 持证经纪人核对字段 + 置信度) → 推送到 ABI (NetCHB) → 🛑 sign-off (经纪人提交) → 关税变更：批量更新零件库"
source_hash: 1dbb6b17b1b8
---

# 报关单预录与经纪人复核

**与相近工作流的区别：** 形态上最接近的是 AWF-0041 可直接审阅的 1040 报税准备（Review-ready 1040 prep）（带置信度提取 → 报税员审阅 → 高级人员签发）。但它通不过互换测试：产出是带关税叠加逻辑和持续维护零件库的报关申报，由持证报关经纪人签发。
**未归类原因：** taxonomy.yaml 中目前没有涵盖此类的类别。在有三个类似的工作流足以支撑新类别 `CUSTOMS`（TAXONOMY.md 规则 2）之前，先归在这里。
**工具变体：** `cervo` · `avathon`

## 步骤

1. 接收商业单据并提取报关数据，每个字段都附置信度和出处 [[2]](#sources)[[3]](#sources)。
2. 应用动态零件库（HTS 编码、原产地拆分、Section 232/301/122 叠加）以及来自智能体工作室的进口商专属规则 [[1]](#sources)[[2]](#sources)。
3. 🛑 **审阅**：录入员在工具中审阅报关单，再推送到自己的 ABI，能看到 'confidence levels and source data for each field' [[3]](#sources)。
4. 🛑 **签发**：经纪人通过 NetCHB 始终 'fully in control of review and submission' [[2]](#sources)。
5. 规则变化时，在生效日期之前批量更新零件库 [[3]](#sources)。

**产出：** 由持证经纪人申报的报关单（CBP 表格 7501）。
**失败模式 → 防护：** 关税规则变化快于零件数据 → 批量更新零件库。归类错误的处罚 → 经纪人审阅每一份报关单；Krenz & Hannan 的审计已改为覆盖 100% 的报关单。

**近期实践（2026）：**
- 单据接收：收到的单据（来自发货人、承运人和政府机构，共四十多种类型）被拆分、分类并附到对应的货件上，系统会在提取完成前索要缺失的单据（C.H. Robinson，2026-10-26）。[[5]](#sources)

## 公开实例

覆盖度（截至 2026-11-13）：**充分**：有详细的第一手实例，与流程的大部分环节一致。更新见 [Third collection pass](../../../research/2026-11-third-pass.md)。

- [Cervo, Krenz & Hannan](https://usecervo.com/case-studies/krenz-and-hannan) (n.d.)。货运代理兼报关行；引述其进口部门经理的话。"15 - 60+ minutes per entry → 5 - 10 minutes"。*第一手：厂商；可信度：中。*
- [Cervo, M. J. Carrillo](https://usecervo.com/case-studies/m-j-carrillo) (n.d.)。边境报关行；引述其持证经纪人和运营副总裁的话。"70%+ of monthly shipments processed through Cervo within four weeks of go-live"。*第一手：厂商；可信度：中。*
- [Cervo, EMD Customs](https://usecervo.com/case-studies/emd-customs) (n.d.)。三人规模的报关行。"75% reduction in processing time"。*第一手：厂商；可信度：低。*
- [C.H. Robinson, Debuts Lean AI for Ocean Shipping, Air Freight and Customs](https://ir.chrobinson.com/news/press-releases/news-details/2026/C-H--Robinson-Debuts-Lean-AI-for-Ocean-Shipping-Air-Freight-and-Customs/default.aspx) (2026-10-26)。报关员拆分、分类并附上单据，提取数据，追补缺失单据；经纪人保留验证职责。"So far, time spent has been reduced 23%, allowing the company’s customs brokers to focus on critical validation and compliance steps."。*第一手：是；可信度：高。*
