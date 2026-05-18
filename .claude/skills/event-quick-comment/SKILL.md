---
name: event-quick-comment
version: 0.1.0
last_updated: 2026-05-18
maintainer: <团队>
description: 关键事件快评 —— 30 分钟内出第一稿，分钟级时效 + 跨资产 + 禁止 AI 操作建议
changelog:
  - 0.1.0: 初始骨架（教程 Ch24 对应）
---

# Skill: event-quick-comment

> 这是 demo 结构骨架。实际落地要：(1) 历史先例 MCP 按机构数据情况调整；(2) urgency 阈值由机构内部 SLA 决定；(3) "操作建议"禁令是硬约束，黑名单 grep 必须严。

## 输入

- `title`: 事件标题（必填）
- `summary`: 事件摘要（必填）
- `timestamp`: 事件时间（必填）
- `source_docs`: 原始来源文件路径（可选）

## 输出

- 按 urgency 输出：
  - critical → `output/events/{ts}_critical.md`（800 字）
  - high → `output/events/{ts}_high.md`（1200 字）
  - medium → `output/events/{ts}_medium.md`（2000 字）

## 步骤

### 步骤 1：classifier 分类（5 秒）

调 `event-classifier`（haiku）：

- `category`: monetary_policy / geopolitical / regulatory / commodity / idiosyncratic
- `urgency`: critical / high / medium / low
- `affected_markets`: ...
- `ttl_minutes`: 此事件预计影响窗口

### 步骤 2：按 urgency 分流

- `low` → 不点评，进监控池
- `medium / high / critical` → 进入后续步骤

### 步骤 3：拉实时行情 + 历史先例 + 现有立场

- `mcp.bloomberg.query_realtime_prices`
- 同类事件历史先例（mcp.macro.query_similar_events_reactions）
- 内部已有的事件立场（mcp.coverage.query_existing_event_views）

### 步骤 4：调 category 专属 reader

按 category 分流到 `fed-event-reader` / `geopolitical-event-reader` / `regulatory-event-reader` / `commodity-event-reader` / `idiosyncratic-event-reader`。

### 步骤 5：调 cross-asset-correlation 拉历史统计

类似事件的历史跨资产反应分布（统计倾向，不是预测）。

### 步骤 6：按 urgency 选模板起草

- critical (800 字)：一句话定性 + 关键事实 + 跨资产反应表 + 我方现有立场
- high (1200 字)：+ 历史先例对比
- medium (2000 字)：+ 多场景演绎 + watch points

### 步骤 7：黑名单 grep（硬约束）

- 中文：推荐 / 建议 / 加仓 / 减仓 / 应该 / 离场 / 必然
- 英文：we recommend / should buy / should sell

任何命中 → 阻断输出。

## 检查清单

- [ ] 不出现"推荐 / 建议 / 加仓 / 减仓"
- [ ] urgency 与字数匹配
- [ ] 历史先例至少 1 条（或注明"无类似先例"）
- [ ] 跨资产反应用统计倾向措辞
