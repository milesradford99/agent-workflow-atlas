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
