# Skill / Subagent 版本管理规范

> 本文档对应教程 Ch27 的 "Skill 工程化" 部分。

## 为什么要做版本管理

3 个月后没人记得这个 Skill 上次跑得好这次不行是因为改了什么。版本号 + changelog 是研究员体系最基础的可追溯性。

## 版本号规则（semver 简化版）

`major.minor.patch`，例如 `1.4.2`。

| 升哪一位 | 触发条件 | 例子 |
|---|---|---|
| `patch` | 修 bug、调小细节，不改输出结构 | 1.4.1 → 1.4.2：修正 [VERIFY] 在 HTML 里的转义 |
| `minor` | 新增字段 / 新增 Subagent / 新增检查规则，向后兼容 | 1.4.2 → 1.5.0：新增"季度变化分析"子段 |
| `major` | 输出结构变化、字段重命名、删除字段 | 1.5.0 → 2.0.0：输出从 5 段重构为 6 段 |

## SKILL.md / agent.yaml 头部格式

```yaml
---
name: earnings-note-cn
version: 1.4.2
last_updated: 2026-05-12
maintainer: <团队 / 个人>
changelog:
  - 1.4.2: 修正 [VERIFY] 在 HTML 输出中的转义问题
  - 1.4.1: 增加港股 ADR 处理分支
  - 1.4.0: 新增季度变化分析 Subagent
  - 1.3.x: ...（保留近 5 条）
---
```

changelog 保留近 5 条，再之前的版本进 git 历史即可。

## PR 流程

任何对 `.claude/skills/` 或 `.claude/agents/` 的修改：

1. 开新分支 `skill/<skill-name>-<change-brief>`
2. 改 SKILL.md / agent.yaml 本体 + 同步更新 version + changelog
3. 提 PR，模板要求：
   - 改动摘要（1-2 句）
   - 对哪个 Skill / Agent / Hook 有影响
   - 是否会影响已经在跑的研究员工作流（向后兼容性）
4. 至少 1 个同事 review——最好是写过类似 Skill 的
5. CI 跑 hook 单测（`pytest tests/hooks/`）
6. merge 到 main，团队 git pull 时统一更新

## 兼容性原则

- **major 升级前必须邮件 / Slack 通知全团队**，给出迁移指引
- **minor 升级默认向后兼容**——如果不兼容，应该走 major
- **patch 升级随时可发**

## 配套 Skill 模板

新建 Skill 时建议从这个最小骨架开始：

```yaml
---
name: <skill-name>
version: 0.1.0
last_updated: YYYY-MM-DD
maintainer: <你的名字>
description: <一句话，能让别人一眼看懂这个 Skill 干什么>
changelog:
  - 0.1.0: 初始版本
---

# 步骤 1：装载输入
# 步骤 2：数据查询清单驱动（参考 Ch12 / Ch15）
# 步骤 3：Subagent 并行处理（参考 Ch11 / Ch14）
# 步骤 4：归并 + 生成主文档
# 步骤 5：双输出 + 黑名单 grep + [VERIFY] 计数（参考 Ch9 / Ch13）
```

## Anti-pattern

- **直接改 main 分支的 Skill** —— 一个研究员"自己改一下"全团队跟着倒霉。修法：PR + review
- **不更新 version / changelog** —— 出问题没法定位。修法：CI 检查 version 是否 bump
- **changelog 只写"优化代码""修 bug"** —— 等于没写。修法：每条都说清楚改了哪个字段 / 增删什么行为
