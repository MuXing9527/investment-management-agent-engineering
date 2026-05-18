---
name: announcement-comment-cn
version: 0.1.0
last_updated: 2026-05-18
maintainer: <团队>
description: A 股公告分类 + 快速点评 —— 3-5 分钟出第一稿，按 importance 分流
changelog:
  - 0.1.0: 初始骨架（教程 Ch21 对应）
---

# Skill: announcement-comment-cn

> 这是 demo 结构骨架。实际落地要：(1) 扩展 category 专属 reader（教程列了 7 种）；(2) 调整每类公告的字数和模板；(3) classifier 用 haiku 控制成本。

## 输入

- `announcement_pdf_path`: 公告 PDF 路径（必填）

## 输出

- 若 importance = ignore → 返回"不点评"标记
- 若 importance = note_only → `output/{ticker}/{date}/note.md`（一行摘要）
- 若 importance = comment_needed | urgent → `output/{ticker}/{date}/announcement_comment.md`

## 步骤

### 步骤 1：classifier Subagent 分类（10 秒）

调 `cn-announcement-classifier`（haiku，最便宜）：

- `category`: equity_incentive / m_and_a / shareholding_change / lockup_expiry / related_party / outbound_investment / litigation / other
- `importance`: ignore / note_only / comment_needed / urgent
- `suggested_action`: ...

### 步骤 2：按 importance 分流

- `ignore` → 直接返回，不进入后续步骤
- `note_only` → 写一行摘要 → 退出
- `comment_needed | urgent` → 进入步骤 3

### 步骤 3：拉补充数据

按 category 调相关 MCP（如 equity_incentive → 总股本 / 历史授予；shareholding_change → 历史减持记录等）。

### 步骤 4：调 category 专属 reader

每类公告有专属 reader Subagent（参考 Ch21 表，本 repo 提供 equity-incentive-reader 作为示例，其余待团队按需补充）。

### 步骤 5：按 category 模板起草

每类公告的点评结构不同：

- 股权激励 → 行权价 / 业绩条件 / 摊薄影响
- 重大重组 → 标的估值 / 协同 / 商誉风险
- 增减持 → 占比 / 历史规律 / 暗示信号
- 限售解禁 → 解禁规模 / 解禁股东类型 / 历史减持倾向

### 步骤 6：黑名单 grep

- 中文：推荐 / 买入 / 加仓 / 摊薄影响巨大 / 一定 / 必然
- 英文：strongly recommend / definitely / guaranteed

## 检查清单

- [ ] importance 为 ignore / note_only 时不生成正式点评
- [ ] 不出现"推荐 / 买入 / 一定 / 必然"
- [ ] 不出现具体券商名
