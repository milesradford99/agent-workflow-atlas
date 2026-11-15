# 每条工作流的“一招”：全量提炼（2026-11-15）

接续 [试写记录](2026-11-context-moves-trial.md)。范围：最新来源或公开实例在 2025-11 及以后的条目（约 190 条）；更早的 50 条未提炼，列在文末。

方法同试写：只读每条的 summary、shape、“失败模式 → 防护”和“与相近工作流的区别”，没有通读全文；“一招”和分类是我的判断，数字出自条目原文。分类：放入、挡住、外验、回灌、分流、标准（定义见试写记录）。“标准”表示做法就是“AI 起草、人审阅或接手”，保留并标明。

试写的 20 条不在下表重复。

## TEC 技术

| 条目 | 分类 | 一招 |
|---|---|---|
| AWF-0192 Context-tested Slack analyst | 外验 | 不逐条审答案，改为端到端测试“上下文层”并抽看公开线程；只许用认可的数据集，答案附 SQL。 |
| AWF-0006 Governed query | 标准 | 载入指标定义，SQL 自检，分析师审阅后签发。条目没有防护一行。 |
| AWF-0123 Scheduled metric commentary | 外验 | 先用 6 个月标准差和同比判断波动是否有意义，再写评论；指标要在正确粒度上认证过。 |
| AWF-0063 Diff-proven dbt migration | 外验 | 每个模型用与生产数据的逐行 diff 证明；双向比对加不对称行数检查，抓出静默丢掉 NULL 和迟到行的增量水位。 |
| AWF-0124 Summoned dbt debugger | 挡住 | 查询用模板加上下文登记表，把编造路径导致的失败从约 25% 降到约 13%；83% 的诊断无需动作，所以修不修由人定。 |
| AWF-0191 Unprompted pipeline repair | 挡住 | 源数据问题按规则只报告不修，防止智能体用“有创意的过滤”掩盖坏数据；只读角色，沙箱里跑。 |
| AWF-0125 Multi-agent readout review | 放入 | 一行公司术语定义（内部的 DAU 指什么）消掉一整类误报；指标先预筛再交给评审智能体，整包给会把它搞晕。 |
| AWF-0064 Repo-grounded analysis | 挡住 | 只信已验证的表，未验证的表要分析师签字才能临时用；每条 Markdown 规则都配一段代码强制。 |
| AWF-0126 Calibrated-judge quality loop | 外验 | 评审模型先对照留出的人工标注校准，评分标准变了就重校；修复在固定夹具的模拟器上测。 |
| AWF-0065 Overnight experiment ratchet | 挡住 | 评测脚本只读、数据划分冻结，防止刷指标；20–30 轮后上下文会丢，用持久的实验记忆。 |
| AWF-0116 Agent-drafted PCB schematic | 外验 | 模型看不到全局（一个短接的开关引脚把 BOOT0 拉低，没被发现），所以要第二位工程师评审加上电调试；ERC 噪声多，用网表找真问题。 |
| AWF-0056 Phased preview build | 外验 | 每阶段出四视图渲染对照清单自查，再用真实切片器的反馈；布尔运算会静默失败。 |
| AWF-0058 Cited pre-screen checks | 外验 | 每项检查给出通过与否加法规条文引用，审查员逐项批准，并追踪“错放行率”；范围先限于简单建筑类型。 |
| AWF-0117 Pre-submittal plan check | 分流 | 约 4 个标记里只有 1 个是真问题，所以先由事务所分拣再改；用本所以往的审查清单做基准。 |
| AWF-0118 Zoning-rule study crew | 标准 | 逐条规则核对，建筑师签字。 |
| AWF-0059 Drawing-to-route draft | 回灌 | 班组长的修改进变更日志，反哺规则库。 |
| AWF-0057 Engineer-checked CFD run | 外验 | 边界条件错了也照样收敛（旋转壁面被留成 noSlip，叶片根本没转），所以加旋流探针和收敛交叉检查，工程师先审假设文档。 |
| AWF-0193 Unattended simulation campaign | 外验 | 求解器报成功却落在错误的平衡点，所以每次运行都做合理性检查；先用实测数据标定基础模型，再跑上千次。 |
| AWF-0151 First-pass submittal review | 标准 | 逐条要求核对并给出建议，PM 或工程师审阅。 |
| AWF-0235 Rule-set verdict review | 放入 + 外验 | 先由工程师确认通用规范与专用规范的冲突调和结果，再开始检查；每个判定带高亮证据，推翻要写理由。 |
| AWF-0190 Spec-to-submittal register | 标准 | 抽取要求、起草登记表，项目工程师逐行核对。 |
| AWF-0188 Scheduled vuln-fix PRs | 放入 | 每个代码库存自己的依赖模式、文件位置、构建命令和例外；工单、标签、分支和部署状态让重跑无害。 |
| AWF-0068 Slack IT request agent | 挡住 | 谁有权批准写在工作流或策略里，不让模型决定；置信阈值用数周真实流量来调。 |
| AWF-0066 Chat-to-IaC change | 外验 | 评审对象是 plan 输出而不是 HCL diff：看着很小的 diff 可能会替换或销毁资源。 |
| AWF-0186 Plan-verified drift fixes | 放入 | 一张导入 ID 格式表把 ID 错误从 13 个降到 5 个；仍有 12 个弱方案通过了干净的 plan，只被评审人抓到。 |
| AWF-0005 Alert enrich and adjudicate | 标准 | 富化、裁决，良性的自动关闭，其余转二线，每周抽检。条目没有防护一行。 |
| AWF-0128 Detonate-and-confirm detections | 外验 + 挡住 | 攻击模拟必须在实验主机上真跑，由验证智能体到 SIEM 查原始事件和规则命中；无人值守时智能体曾越界改了转发器配置，所以关进 devcontainer 并限制出站。 |
| AWF-0187 Purple-team detection build | 外验 | 每条规则至少用 5 个以上技术变体引爆，避免只能抓住那一个 PoC；送审前先对照真实运营遥测压误报。 |
| AWF-0185 Agent-run war room | 标准 | 调查、起草状态更新和复盘，P1/P2 不自主修复，后续事项同步进团队已用的工单系统。 |
| AWF-0127 Open-loop NOC root cause | 挡住 | 用确定的流程而不是开放的智能体循环，换来可复现的答案。 |
| AWF-0008 Design to code | 标准 | 载入令牌和组件映射，截图比对后设计师审阅。条目没有防护一行。 |
| AWF-0122 Scored token migration | 回灌 | 先分片试迁、工程和 UX 审，追问模型错在哪，改技能文件，直到规则稳定再锁定评分矩阵；简单映射交给 codemod。 |
| AWF-0060 Spec-to-ticket planning | 放入 | 拆任务时让智能体读代码库，票才不会脱离实现；它默认用户完全理性，会漏边缘情况。 |
| AWF-0232 In-codebase handoff prototype | 放入 | 开发者先给设计师备好仓库（设计师配置加 3 个技能文件），原型用真组件做在一条分支上，空状态和错误状态要写明。 |
| AWF-0121 Routed accessibility PR agent | 分流 | 约 36% 的 A 和 AA 级准则无法自动发现，所以超过复杂度阈值的直接转给无障碍团队，高风险模式列入拒绝清单。 |
| AWF-0062 Spec-bound screen options | 挡住 + 回灌 | 只许用组件库实例；每周重复的错误写进记忆（约 70 条），规格优先；QA 脚本报零错误设计师也要看。 |
| AWF-0120 Agent-run interviews | 标准 | 研究员定访谈提纲，智能体访谈并聚类，研究员共同分析后发布。 |
| AWF-0195 PR-reviewed research wiki | 回灌 | 每次访谈变成对研究 wiki 的一个 PR，研究员标出漏掉的再合并；带上分群背景，否则差异被抹平。 |
| AWF-0061 Quote-verified synthesis | 外验 | 引语会被编造（温度 0.1 也出现过），所以 100% 对照原文核对；不让模型判断情绪。 |
| AWF-0072 Guardrailed design spec | 放入 + 回灌 | 架构、安全、法务规则写成系统文件，每次运行都对照；每周用 PR 更新这些文件；规格分人读和智能体读两半。 |
| AWF-0184 Guideline-checked design review | 分流 | 安全团队先核实发现再给开发者看；160 多条内部准则逐条查，并标出缺失信息。 |
| AWF-0183 On-demand alert investigation | 标准 | 工程师点按钮才开始调查，出证据报告；修复 PR 另行选择。 |
| AWF-0071 Reproduce-first bug fix | 外验 | 先复现再修，修完用同样的样本量重跑同一个复现；另加一个换了说法的用例防止对报告措辞过拟合。 |
| AWF-0003 Delegated PR | 标准 | 贴标签的 issue 变成草稿 PR，人批准跑 CI 并审阅合并。条目没有防护一行。 |
| AWF-0179 Spec-PR then agent build | 外验 | 规格里的每条断言都对照真实代码核对（8 条里 7 条成立，第 8 条被标出），再过一道唱反调的裁决。 |
| AWF-0002 Fan-out codemod | 标准 | 试点后冻结方案，逐文件过 lint、类型、测试，抽检后分批 PR。条目没有防护一行。 |
| AWF-0180 Stale-flag cleanup PRs | 放入 | 开关的真实值取自平台的发布状态，不从代码里猜，再由人确认；50 次运行里 5 次干预全是调用链深度问题。 |
| AWF-0182 Risk-gated auto-approval | 挡住 + 外验 | 能否自动批准先由确定性规则决定（路径、大小、分支、标签）；提示词改动用历史 PR 回测，包括那次批错的。 |
| AWF-0181 Scenario release sweep | 外验 | 结果不确定，所以不拿它卡合并，单元测试照旧；另一个验证智能体确认并找原因，人再分拣。 |
| AWF-0132 Streak-verified flake fix | 外验 | 偶发失败重跑一次变绿不算数，要连续 N 次干净；每个修复者只试一个假设，专门的验证者只看目标测试。 |

## PRO 专业服务

| 条目 | 分类 | 一招 |
|---|---|---|
| AWF-0167 AI-blended comparative judgement | 外验 | AI“80% 的时候对，偏偏在要紧处错”，所以看分歧的大小而不是一致率；人保留 10% 的比较，保证每份答卷都被人看过两次。 |
| AWF-0099 Data-informed IEP draft | 挡住 | 不知道的字段留空并标出，不许编内容；用学区审过的平台而不是通用聊天工具。 |
| AWF-0103 AI role-play practice | 放入 | 场景从最常见的真实对话里写出来，先批准场景集再让学员练。 |
| AWF-0043 SME-docs to e-learning | 标准 | 从专家资料出大纲和课程，教学设计师和专家审阅。 |
| AWF-0022 Invoice extract-match-route | 外验 | 明细行的数值会被编造，所以用业务规则检查（供应商、重复、银行信息、三单匹配）兜底；准确率低的供应商单独标记。 |
| AWF-0164 Exception-only reconciliation run | 挡住 + 回灌 | 自动清账有硬边界（金额上限、关联方除外），每季度按人工推翻率重新校准；上次的例外和阈值存在对话外的状态库。 |
| AWF-0218 Owner-confirmed PO accruals | 挡住 + 放入 | 分录一直停在“暂存”，经理批准才过账；业务逻辑放在可编辑的 SOP 里而不是写死，审阅中发现的缺口用来补 SOP。 |
| AWF-0038 Workpaper-matched close agents | 挡住 | 故意不给智能体银行权限；会计定规则，AI 只执行，主计长全部审阅。 |
| AWF-0039 Drafted variance narratives | 标准 | 按公司口吻起草预算差异说明，财务团队修改。 |
| AWF-0216 Agent-researched trading signals | 外验 | 想法量大带来多重检验问题，所以沿用同一套研究方法阈值；自动加人工检查“想法、代码、评估”三者是否一致。 |
| AWF-0166 Challenger-agent IC memo | 放入 | 初稿容易照搬标的公司自己的说法，所以另设一个挑战者智能体，用本所历史交易做依据来挑毛病。 |
| AWF-0023 Event-driven model update | 放入 + 外验 | 每个单元格带出处批注；多分部公司选错分部、月度当季度这类错靠分行业的消歧规则防。 |
| AWF-0098 Underwriter-finalized credit memo | 标准 | 抽取、分节起草，核保人定稿，走银行审批。 |
| AWF-0217 Expert-approved taxability rules | 回灌 | 现成的 RAG 免改准确率不到 65%；把专家以往的审阅意见传回去并微调；法规变了，监控会标出受影响的判定重审。 |
| AWF-0165 Issue-split notice reply | 放入 | 先把通知拆成一个个问题，每个问题套 13 点模板分别检索和作答，防止多问题通知漏答一点。 |
| AWF-0041 Review-ready 1040 prep | 分流 + 外验 | 低置信字段给报税员核对；用上年对比查漏表。 |
| AWF-0157 Nightly hospital-course drafts | 外验 | 摘要带行内出处，医生对照原文再用；遗漏占 25%、不准确占 20%，所以看 EHR 用时和倦怠，而不只看使用率。 |
| AWF-0033 Coordinator-reviewed prescreen | 外验 | 每条入组标准单独给标签、理由和出处，协调员逐条裁定；随机试验里每份病历用时 37.4 对 37.8 分钟，省时未必出现。 |
| AWF-0091 Writer-reviewed CSR draft | 外验 | 起草前先对数据表做映射和校验，起草后再跑自动检查，最后医学写作者全文审。 |
| AWF-0156 Approve-only payer auto-auth | 挡住 | 只能批准不能拒绝：凡是不批的都交给有执照的临床人员。 |
| AWF-0032 Criteria-gated prior auth | 外验 | 上线前按药品逐个用标准答案验证（Duke 评估 970 条标准里 7 个错）；病历材料由工作人员自己挑。 |
| AWF-0090 Exception-routed autonomous coding | 分流 | 有缺口或冲突的病历整份“掉出”给编码员；覆盖只是部分专科，所以保留编码员编制。 |
| AWF-0094 Agent-crew claim file | 挡住 | 没有任何智能体能付款；审计智能体把每个智能体的决定汇总给人工审批者。 |
| AWF-0095 Handler-accepted invoice recommendation | 回灌 | 理赔员标出缺失的药品或治疗知识，由资深人员把关后才更新进去。 |
| AWF-0096 Policy-grounded claim letters | 挡住 | 找不到支持的保单条文就拒绝生成拒赔信，直接显示“未找到相关保单条文”。 |
| AWF-0162 Subrogation alert triage | 放入 | 后台扫描所有案件（含已结案的），不靠理赔员记得转交；告警里直接套用各州的时效和过失规则。 |
| AWF-0149 Decision-ready submission triage | 分流 | 按抽取置信度决定直接入队还是先过人；整个收件箱都分诊，而不是核保人只看到一小部分。 |
| AWF-0163 Summarised GP-report underwriting | 外验 | 上线前测了 18 个月，按病种验证准确率，先从低风险案件做起，再扩到重疾险。 |
| AWF-0092 Business self-serve drafting | 挡住 | 只从法务批准的模板里填，超出范围就拒绝并转加急法务审。 |
| AWF-0159 Sample-tuned contract abstraction | 外验 + 回灌 | 先在有代表性的样本上抽取，律师据此改提示词，再全量跑；每个字段带回到原文的超链接。 |
| AWF-0161 Page-cited medical chronology | 外验 | 每个事件带页码引用，律师助理逐条对照原件。 |
| AWF-0035 Validated GenAI first-pass | 外验 | 全量跑完后抽样验证精确率和漏检率；把边缘文件算进去召回到 96.2% 但精确率掉到 58.4%，所以边缘政策要事先定。 |
| AWF-0036 Obligations register build | 标准 | 抓取法规、拆成义务并打标签，律师检查每项输出并签字。 |
| AWF-0160 Sampled DSAR disclosure | 外验 | 对被判“不相关”的文件做漏检抽样；收集前先和请求人谈范围（姓名缩写会撞上常用词）。 |
| AWF-0044 Gated replication run | 外验 | “代码跑通”不等于“结果复现”，所以单独设一个把系数与论文逐项比对的阶段；数据缺失记为不可复现，不记为代码失败。 |
| AWF-0168 Lab-in-the-loop discovery | 外验 | 同一份数据的分析每次跑都不一样，所以并行跑 8 条分析轨迹再做共识荟萃；实验全部由科学家做。 |
| AWF-0045 Critique-first grant draft | 分流 | 模拟评审只提意见不改稿，PI 逐条接受或拒绝后才整合；引用对照 PubMed 查（防止引了支持对立机制的论文）。 |
| AWF-0104 Hypothesis tournament | 外验 | Elo 排名是模型自评，不是事实；靠专家评估头部候选加实验验证。有一例其实是重新发现了已知但未发表的结果。 |
| AWF-0009 Screening funnel | 标准 | 两名独立筛选者筛每条记录，冲突和纳入项抽检，摘录带引文和页码。条目没有防护一行。 |
| AWF-0170 Added AI review | 分流 | AI 评审带标签、不打分，放在人工评审旁边；前 30% 批次由组织者抽看。 |
| AWF-0046 Review-of-review feedback | 外验 | 反馈先过可靠性测试才发给审稿人，而且只私下发、可忽略；两组的录用结果没有差别。 |
| AWF-0169 End-to-end AI paper | 分流 | 开放题目成功率低，所以生成很多、由人挑少数；3 篇里没有一篇达到作者自己对主会的标准。代码在沙箱容器里跑。 |
| AWF-0010 Reviewer-response revision | 标准 | 按每条审稿意见修改并起草回复，作者批准计划并签发。条目没有引用任何来源。 |

## COM 商业

| 条目 | 分类 | 一招 |
|---|---|---|
| AWF-0174 Autonomous long-tail renewals | 挡住 | 折扣上限写在工作流里强制执行，不写在提示词里；联系客户前先给客户负责人一个否决窗口。 |
| AWF-0223 Confirmed-inputs QBR deck | 放入 | 用单一快照数据集，人确认过的判断存成结构化记录，跨多天的会话才不会丢决定；把客户已购产品的数据喂进去，免得推荐人家已有的模块。 |
| AWF-0049 Renewal-window risk brief | 外验 | 静态健康分会把正在流失的客户标成绿色；把多系统的非结构化信号合起来，用过去的流失案例回放检验。 |
| AWF-0173 Code-change doc refresh | 外验 | 只改段落不重写整篇（整篇重写会把错误藏起来），再由第二个模型对照代码 diff 核对；合并触发，客户可用时才发布。 |
| AWF-0048 Gap-match knowledge upkeep | 分流 | 先给来源完整度打分，素材太薄的转给人打电话补；要成簇才起草，一次性的修复不进知识库。 |
| AWF-0047 Calibrated conversation scoring | 外验 | 评审模型定期对照专家评分重新校准；各项标准分开报告并保留理由，否则一项出错会连带判几项不过。 |
| AWF-0172 Simulation release gate | 外验 | 先验证模拟器本身：看它对已上线版本的排序是否与生产一致；盲评的人仍能认出大多数模拟对话，所以排序一致才是要紧的检验。 |
| AWF-0107 Human-sent reply drafting | 分流 | 最有经验的坐席照着建议做反而掉质量，所以按技能水平衡量，允许老手不理会建议。 |
| AWF-0021 Procedure agent | 挡住 | 交易限额写在代码里。条目没有防护一行。 |
| AWF-0108 Resident maintenance triage | 标准 | 问诊分诊、派单，紧急情况转值班人员。来源对转交设计着墨很少。 |
| AWF-0175 Supervised voice agent | 分流 | 一个主管同时盯几路通话，按通话评分和告警排序决定听哪路；接管时由 AI 先介绍“同事”，避免声音突变。 |
| AWF-0115 Tiered-permission ads optimizer | 挡住 + 外验 | 按权限分级：否定词、出价等在限度内自动执行，预算和结构要批准；广告平台与分析工具的数据对不上时不执行（转化追踪出故障会让最好的系列看起来坏了）。 |
| AWF-0018 Cluster-brief-draft content | 外验 | 事实对照一手来源或专家核查（出现过不存在的以太坊升级）；30 天和 90 天回看排名。 |
| AWF-0224 Diffed article refresh | 外验 | 更新以与原文的并排 diff 呈现，加一道产品提及审计，编出来的产品功能一分钟就能抓到。 |
| AWF-0225 Ranker-guided creative slate | 外验 | 离线排序模型不当部署规则用（它的第一名线上排第 43），只用来凑一个高召回的候选集，由线上测试选赢家；对着代理指标只优化一轮。 |
| AWF-0171 Backtested synthetic panel | 外验 | 合成受访者先对照留出的真人研究回测，洞察负责人认可准确度后才用；直接要评分会偏窄偏正面，所以让它写自由文本再映射。 |
| AWF-0055 Routed competitive digest | 分流 | 设明确的入选门槛（重复出现的异议、已证实的公开动作、作战卡缺口），每条标给负责的产品营销，而不是压在一个分析师身上。 |
| AWF-0053 Plan-to-calendar drafting | 标准 | 按渠道起草进排期日历，人逐条审并批准发布（小红书对全自动发帖有风控）。 |
| AWF-0111 Catalog copy factory | 挡住 | 只跑数据完整的 SKU；规则检查器与写作简报出自同一份文本规范。 |
| AWF-0050 Call-to-CRM diff approval | 外验 | 每个字段都要能追溯到通话记录；写回前给销售看 diff，写后可回滚。 |
| AWF-0176 RFQ-to-quote drafting | 外验 | 先用确定性的编码匹配，匹配不上才用模型；每行带来源，低置信或偏离价格表的行标出来给销售确认。 |
| AWF-0222 Signed-contract validation | 分流 | 任何一点存疑就转交易台；编排和审计放在确定性的中间件里，与模型的校验逻辑分开。与 AWF-0110 做法几乎相同。 |
| AWF-0109 Inbound qualify-and-book agent | 外验 | 通话被打断的线索不直接判不合格，先做网站分析兜底；每天人工回看全部对话。 |
| AWF-0020 Research-then-personalize outbound | 外验 | 首句只许用调研结果，调研回答带来源 URL；邮箱瀑布流最后一步必须验证（退信率从 22% 到 1.3%）；上线前看 20 行样本。 |
| AWF-0110 Exception-only contract validation | 分流 | 只自动化有文档的“顺利路径”，存疑即转交易台，另设独立审计层。与 AWF-0222 做法几乎相同。 |
| AWF-0052 Propose-confirm pipeline sweep | 挡住 | 只读实时记录，提议与写回分开，人确认后才写。 |
| AWF-0051 Governed-library response draft | 放入 | 只从受管的答案库取材，每个答案带出处；先做文档适配检查，拒掉不该答的文件。 |

## ORG 组织与公共部门

| 条目 | 分类 | 一招 |
|---|---|---|
| AWF-0236 Agronomist-gated push advisories | 外验 | 扩大前先做 A/B：AI 写的脚本收听率比人写的低 2–3.5 个百分点，项目页上“略高”的初步说法没有成立；农艺师逐稿比对。 |
| AWF-0154 Plot-registered agronomy advice | 放入 | 农户先在地图上核对自己地块的多边形，后面的土壤数据和养分计划都以它为准。 |
| AWF-0085 Policy-checked expense audit | 放入 | 政策库由团队自己维护、每周同步，防止用错版本；先并行跑，再逐步放权。准确率数字是厂商自报。 |
| AWF-0029 Source-screen-schedule hiring | 挡住 | 智能体永远不做拒绝决定；一句“全部拒掉”曾在约 2 分钟内发出 8 封拒信，所以按每个候选人签字而不是按批。 |
| AWF-0084 Data-pulled status report | 标准 | 拉数据起草状态报告，项目经理对照源数据后发出。证据只有工具作者的一份自述。 |
| AWF-0030 Issue-tree research | 外验 | 每个数字重新抓取来源核对；允许答“未知”，因为智能体会用看着合理的整数填空（两期通讯发布后被更正过）。 |
| AWF-0228 QA-agent competitive brief | 外验 | 另设一个 QA 智能体逐条对照来源和内部文档，不让研究智能体自己批改自己的作业；每个来源必查日期。 |
| AWF-0141 Gap-checked benefits form fill | 放入 + 外验 | 填表前先做缺口分析，社工和当事人把缺的补齐；每个字段标明数据从哪来、为什么填它。 |
| AWF-0142 Visit-recorded care assessment | 标准 | 录音转写后起草评估，从业者核对修改后归档。 |
| AWF-0205 Exemption-cited records redaction | 外验 + 挡住 | 每处遮蔽都附豁免条款引用，由档案官员逐处批准；哪些请求类型可以自动放行要显式配置。 |
| AWF-0143 Officer-checked planning data extraction | 外验 | 边界用 IoU 和中心距离检查；准确率看着高之后更容易过度信任，所以全量复核而不是抽检（日期 94% 正确）。 |
| AWF-0204 Statute-mapped regulatory review | 标准 | 逐条对照授权法律并分类，分类只当路线图，机构协调员和律师决定删什么。 |
| AWF-0080 Theme sign-off consultation analysis | 外验 | 先让两个人互相比对，得到人与人之间的基线（F1 0.710），再拿模型去比；审阅者可以标“没有合适的主题”，据此回头改主题表。 |
| AWF-0148 Broker-reviewed entry prep | 放入 | 零件库是关键输入：关税规则变得比零件数据快，所以要能批量更新零件库；每个字段带置信度和来源。 |
| AWF-0233 Pre-transmission entry audit | 外验 | 每票报关单在传输前都过一遍规则审计，规则集集中维护；只标规则或法规违规，干净的直接放行。归类本身对不对不在这道审计里。 |
| AWF-0209 Carrier-call booking agent | 挡住 | 每条线路的运价上下限由人设定，智能体只在其间谈；后台做合规和欺诈检查（第一个月抓到 3 起）。 |
| AWF-0150 Email-to-order freight agents | 放入 | 含糊的委托（“周二有一车货”）靠该客户的历史记录补全。 |
| AWF-0031 Daily inbox triage | 挡住 | 只给草稿权限，不给发送工具，而不是靠提示词约束（原型曾自作主张答应了一个写书邀约）。 |
| AWF-0229 Ledger-earned inbox actions | 挡住 + 回灌 | 每类动作各自从主人的批准记录里挣自主权，记在台账里，有升级和降级规则；另有每小时和每天的上限（曾有 37 个删除请求被上限拦下）。 |
| AWF-0208 Confidence-routed meeting tickets | 分流 + 回灌 | 负责人置信度低或没人认领的事项进 Slack 等批准；用少样本示例教它“我们大概应该……”不算任务；用编辑距离做反馈。 |
| AWF-0086 Template-driven meeting minutes | 标准 | 转写后按模板生成纪要，工作人员改正后分发。 |
| AWF-0087 Diff-reviewed vault upkeep | 回灌 | 主人审 git diff 并写行内批注；再从会话日志里挖摩擦点，更新 CLAUDE.md。 |
| AWF-0146 Pick-then-summarise research digest | 分流 | 只给读者自己存下的论文做深度摘要；另有一个 QA 定时任务修小毛病、拦大问题。 |
