---
id: AWF-0209
name: 承运商电话订舱代理
summary: "接打承运商电话、核查合规并在线路价格区间内议价；团队主管确认后订舱。"
deliverable: 已订舱货载
shape: "货载在 TMS 中就绪 → 发布到货载信息板 + 为该线路给承运商排序 → 每个承运商电话 (呼入 | 呼出)：识别 MC → 合规核查 (Highway) → 匹配货载 → 在线路价格下限/上限内议价 → 无法识别 / 超出政策 / 承运商要求：🛑 handoff (业务员，附上下文) → 价格谈妥：🛑 sign-off (团队主管确认议价结果) → 在 TMS 中订舱 + 发送确认"
source_hash: f92d020ea928
---

# 承运商电话订舱代理

**与相近工作流的区别：** 最接近的是 AWF-0150（邮件转订单的货运智能体）：那是托运人一侧（邮件 → 报价/订单/预约，抽检并在异常时接手）。本工作流是承运商采购一侧：实时语音议价，交付物是按谈定价格订下的承运商，并且每次订舱都由团队主管确认。也不同于 AWF-0153（漏提货的补救电话，不涉及订舱）。
**工具变体：** `ten8` · `happyrobot` · `parade-codriver`

## 步骤

1. 货载在 TMS 中就绪后，智能体把它发布到相关的货载信息板，为该线路给经纪公司的承运商网络排序，并同时启动邮件和语音的外呼；已发布货载的承运商来电则全天候 24/7 接听 [[2]](#sources)。
2. 每通电话中，智能体通过 MC 号码识别承运商，在经纪公司的合规工具（Fura 和 Circle 用的是 Highway）中核查资质，并按起讫点或参考编号查找货载 [[1]](#sources)[[2]](#sources)[[3]](#sources)[[4]](#sources)。
3. 它告知货载详情，并在经纪公司按线路设定的价格下限和上限之内议价，与定价算法集成 [[1]](#sources)[[2]](#sources)。欺诈信号（调度员姓名、邮箱域名、银行信息变更）在后台交叉核对 [[2]](#sources)[[3]](#sources)。
4. 🛑 **接手**：当承运商或货载无法识别、缺少必填的货载字段、承运商要求转人工，或报价满足经纪公司的转接条件（例如等于或低于 Book Now / Max 价格）时，通话转给业务员，并附上 MC 号码和上下文摘要 [[2]](#sources)[[4]](#sources)。
5. 🛑 **签发**：在 Fura，智能体把谈完的结果交给团队主管确认后才订舱 [[1]](#sources)。
6. 智能体订下货载，并把每个数据点写回 TMS；运营人员保留对价格参数、滞留费争议和需要判断的货载的处理权 [[2]](#sources)[[3]](#sources)。

**产出：** TMS 中的已订舱货载（承运商、谈定价格、价格确认单），以及未订成货载的通话记录和已获取的报价。
**失败模式 → 防护：** 重复经纪 / 欺诈企图 → 后台合规和欺诈核查（Fura 的第一个月就拦下三起）[2]。承运商听到 AI 语音就挂断，或线路嘈杂 → 提供转接 [4]。智能体同意了不合理的价格 → 由人按线路设定上下限，并由团队主管确认 [1][2]。

## 公开实例

覆盖度（截至 2026-11-13）：**薄弱**：只有匿名、与厂商相关或经记者转述的说法。收集与复核见 [Third collection pass](../../../research/2026-11-third-pass.md)。

- [FreightWaves, Fura Freight: Next Year, Our AI Agent Will Book 90% of Loads](https://www.freightwaves.com/news/fura-freight-next-year-our-ai-agent-will-book-90-of-loads) (2026-11-11)。CEO 称智能体 Donna 从合规核查做到订舱；团队主管确认谈完的结果。"Donna, now handles more than 40% of the company’s load bookings"。*第一手：访谈；可信度：高。*
- [Ten8, Fura Freight case study results](https://www.ten8.ai/blog/fura-freight-case-study-results) (2026-04-03)。呼入语音、MC 核验、在每条线路的价格下限/上限内议价；边缘情况升级处理。"Carrier calls answered | 60% | 100%"。*第一手：厂商；可信度：中。*
- [HappyRobot, Circle Logistics case study](https://happyrobot.ai/blog/circle-logistics-x-happyrobot-case-study) (2026-02-25)。呼入承运商销售试点扩展为从报价到收款；集成 Transport Pro、DAT、Truckstop、Highway。"18% of all freight booked with zero human touch"。*第一手：厂商；可信度：中。*
