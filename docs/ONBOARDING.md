# 新研究员入职 Onboarding 流程

> 本文档对应教程 Ch27 模式 A（Cowork）的 5-15 人团队部署形态。

## Day 0 · IT 准备

- [ ] 给新研究员账号开通 Wind / FactSet / 内部数据库读权限
- [ ] 在团队凭证管理系统（Vault / 1Password 等）里生成对应的 token
- [ ] 邀请加入团队 git 组织 + 配套 GitHub repo 权限

## Day 1 · 本地环境

- [ ] 安装 Claude Code（参见 Anthropic 官方文档）
- [ ] clone 团队 git 仓库到本地
- [ ] 复制 `.env.example` → `.env`，填入 IT 给的凭证
- [ ] 复制 `CLAUDE.md.example` → `CLAUDE.md`，按个人覆盖板块做小幅调整（默认沿用团队版本）
- [ ] 运行 `pytest tests/hooks/test_check.py` 验证 hook 闸门可用

## Week 1 · 教程引导

按以下顺序在桌面上跑通 4 个 Skill，每个跑 1-2 次：

1. **earnings-note-cn**（Ch18 财报点评）—— 拿一份近期已公开财报跑通
2. **research-digest-cn**（Ch19 研报消化）—— 拿一份近期卖方研报跑通
3. **announcement-comment-cn**（Ch21 公告点评）—— 拿一份重要公告跑通
4. **thesis-debate**（Ch25 投委会预演）—— 用 base case 文档跑通辩论

跑通的标准：

- 双输出（MD + HTML）格式正确
- 黑名单 grep 不报错
- [VERIFY] 占位符在合适位置出现

## Week 2 · 自有方法论植入

研究员需要自己完成的部分：

- [ ] 在 `CLAUDE.md` 第 3 节"研究框架"里，写下你自己的行业 / 公司 / 估值偏好（参考 Part 5 序章）
- [ ] 在 `CLAUDE.md` 第 7 节"不要做的事"里，加入你自己的禁用词（个人风格）
- [ ] 找 1-2 份你过去写得最好的报告作为 few-shot 示例放进 `.claude/skills/<skill>/examples/`

## Month 1 · 进阶

- 学会写 PR——任何对 `.claude/skills/` 或 `.claude/agents/` 的修改走 PR + 同事 review，不直接 push 到 main
- 学会更新版本号 + changelog（参见 [`SKILL_VERSIONING.md`](SKILL_VERSIONING.md)）
- 如果遇到 hook 拦截 false positive，提 issue 而不是绕过 hook

## 红线（不可逾越）

- **MNPI / 客户数据 / 未公开持仓** 绝不输入任何 LLM
- **凭证（.env / API key）** 绝不 commit 到 git
- **绕过 hook** 任何形式都不允许——`--no-verify` 是开除事件，不是技术问题
- **AI 写出的内容直接对外发** 必须经过研究员人工审核

## 联系

- 团队 Skill / Agent 维护人：（待填）
- IT / 凭证支持：（待填）
- 合规问题：（待填）
