# methodology-as-asset

《方法论资产化：从 Prompt 到 Agent 的投研工程》配套结构骨架。

## 这个 repo 是什么

教程 27 章 + Part 5 序章里所有 CLAUDE.md / Skill / Subagent / Command / Hook 的 **结构骨架**——按 5 层架构组织，方便研究员开新项目时直接 clone 改名上手。

## 这个 repo 不是什么

- **不是开箱即跑的成品**——所有 MCP server 名、Subagent 名、API 路径都是 demo 占位，需要替换成你机构内部的真实工具
- **不是完整可跑的代码包**——Claude Code / Anthropic SDK 在持续演进，语法以官方最新文档为准
- **不是合规审核过的生产模板**——黑名单 / 信任边界规则需要按你机构合规部门要求重写
- **不是教程本身**——只看 repo 不看书，等于看了食谱目录但没看食谱

## 目录结构

```text
methodology-as-asset/
├── README.md                                  # 本文件
├── CLAUDE.md.example                          # 项目级 CLAUDE.md 模板（脱敏）
├── .gitignore                                 # 忽略 .env / 日志 / 缓存
├── .env.example                               # MCP 凭证模板
├── .claude/
│   ├── settings.json                          # Hook 配置
│   ├── commands/
│   │   ├── earnings.md                        # Ch18 季报点评入口
│   │   ├── minutes.md                         # Ch17 纪要分析入口
│   │   ├── digest.md                          # Ch19 研报消化入口
│   │   ├── industry.md                        # Ch20 行业深度入口
│   │   ├── announcement.md                    # Ch21 公告点评入口
│   │   ├── ipo.md                             # Ch22 IPO 速读入口
│   │   ├── macro.md                           # Ch23 宏观数据点评入口
│   │   ├── policy.md                          # Ch23 政策文件解读入口
│   │   ├── event.md                           # Ch24 事件快评入口
│   │   └── debate.md                          # Ch25 投委会预演入口
│   ├── skills/
│   │   ├── earnings-note-cn/SKILL.md          # Ch18
│   │   ├── meeting-minutes-analyzer/SKILL.md  # Ch17
│   │   ├── sell-side-research-digester/SKILL.md  # Ch19
│   │   ├── industry-deep-dive-cn/SKILL.md     # Ch20
│   │   ├── announcement-comment-cn/SKILL.md   # Ch21
│   │   ├── ipo-quick-read-cn/SKILL.md         # Ch22
│   │   ├── macro-release-analyzer/SKILL.md    # Ch23
│   │   ├── policy-doc-analyzer/SKILL.md       # Ch23
│   │   ├── event-quick-comment/SKILL.md       # Ch24
│   │   └── thesis-debate/SKILL.md             # Ch25
│   ├── agents/
│   │   ├── financial-reader.yaml              # Ch18 / Ch11 教学样例
│   │   ├── cn-meeting-minutes-reader.yaml     # Ch17
│   │   ├── sell-side-research-reader.yaml     # Ch19（强制匿名化券商名）
│   │   ├── cn-company-snapshot.yaml           # Ch20 MAP 单家公司画像
│   │   ├── industry-aggregator.yaml           # Ch20 REDUCE 行业聚合
│   │   ├── cn-announcement-classifier.yaml    # Ch21 classifier（haiku）
│   │   ├── equity-incentive-reader.yaml       # Ch21 category reader 示例
│   │   ├── ipo-business-reader.yaml           # Ch22（客户匿名化）
│   │   ├── ipo-financials-reader.yaml         # Ch22 财务三年数据
│   │   ├── cn-macro-release-reader.yaml       # Ch23 数据发布对比
│   │   ├── cn-policy-document-reader.yaml     # Ch23 政策措辞 diff
│   │   ├── event-classifier.yaml              # Ch24 classifier（haiku）
│   │   ├── fed-event-reader.yaml              # Ch24 FOMC reader 示例
│   │   ├── bull-case-agent.yaml               # Ch25 多头立场
│   │   ├── bear-case-agent.yaml               # Ch25 空头立场
│   │   └── devil-advocate-agent.yaml          # Ch25 5 估值误区核对
│   └── hooks/
│       ├── check.py                           # Ch26 PreToolUse
│       ├── stop_check.py                      # Ch26 Stop
│       └── audit_log.py                       # Ch27 可选
├── docs/
│   ├── ONBOARDING.md                          # 新研究员入职流程（Ch27）
│   └── SKILL_VERSIONING.md                    # Skill 版本管理规范（Ch27）
├── tests/
│   └── hooks/test_check.py                    # Ch26 hook 单测
└── output/                                    # .gitignore 默认包含
    └── （研究员产出落地目录）
```

## 怎么用这个 repo

### 第一次落地

1. clone 这个 repo 到你机构 git
2. 把 `CLAUDE.md.example` 复制为 `CLAUDE.md`，按 Ch6（卖方版）或 Ch7（买方 Long Only 版）改成你自己的方法论
3. 把 `.env.example` 复制为 `.env`，填入 MCP 凭证（Wind / FactSet / 自有库）
4. 按章节顺序读教程，每读完一章把对应的 skill / agent 改成你机构语境

### 团队推广

Ch27 模式 A（Cowork）的最小落地形态——团队 git 仓库就是这个 repo 的 fork，每个研究员本地 `git pull` 即同步最新 Skill。

参见 [`docs/ONBOARDING.md`](docs/ONBOARDING.md) 与 [`docs/SKILL_VERSIONING.md`](docs/SKILL_VERSIONING.md)。

## 重要声明

- 本 repo 的所有规则、黑名单词表、合规检查只是 **示意**，**不能直接作为机构合规标准使用**
- MNPI / 客户数据 / 未公开持仓 **绝不能** 输入任何 LLM 系统——本 repo 不防御此类违规，机构内部合规流程必须独立兜底
- 模型升级 / Anthropic SDK 变更可能让本 repo 的语法过期，**以 Anthropic 官方文档为准**

## 反馈

教程仓库地址：（待填）
本 repo issue：（待填）

— Jovian Research
