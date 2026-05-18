---
name: sell-side-research-digester
version: 0.1.0
last_updated: 2026-05-18
maintainer: <团队>
description: 卖方研报消化 —— 提取核心观点 + 标记 vs consensus 差异，禁止输出具体券商名
changelog:
  - 0.1.0: 初始骨架（教程 Ch19 对应）
---

# Skill: sell-side-research-digester

> 这是 demo 结构骨架。实际落地要：(1) 配置真实 consensus MCP；(2) 维护券商名黑名单 grep；(3) 接入机构现有覆盖立场库。

## 输入

- `ticker`: 股票代码（必填）
- `period`: 财报期 / 时间窗口（必填）
- `research_pdf_paths`: 一份或多份卖方研报路径（必填）

## 输出

- `output/{ticker}/{period}/research_digest.md`（仅 MD，内部使用）

## 步骤

### 步骤 1：数据查询清单

- [ ] sell-side consensus（最近 30 天）
- [ ] consensus 预测分布（spread / std）
- [ ] 内部现有覆盖立场（mcp.coverage.query_existing_views）

### 步骤 2：每份研报独立调 Subagent

对每份 PDF 调一次 `sell-side-research-reader`，并行执行。
**Subagent 层强制匿名化**：所有"中信 / 中金 / 海通 / 招商"等券商名 → `broker_anonymous_1 / 2 / 3`。

### 步骤 3：横向比对识别共识 / 少数派 / 离群

L3 Skill 计算：

- 共识假设（≥ 60% 研报一致的论点）
- 少数派假设（1-2 份研报提出，其他没提）
- 离群假设（明显偏离的预测，标 outlier）

### 步骤 4：起草消化稿

1. 一句话 thesis 共识总结（≤ 30 字）
2. 共识假设清单（来源标 anonymous_N）
3. 少数派假设（含理由）
4. 离群预测与差异原因
5. 与内部现有立场对照（同 / 异 / 互补）

### 步骤 5：黑名单 grep 兜底

- 中文券商名（中信 / 中金 / 海通 / 招商 / 国泰 / 申万 / 长江 ...）
- 英文 broker 名（Goldman / MS / JPM / UBS / CS ...）

任何命中 → 阻断输出，让研究员手工脱敏后重跑。

## 检查清单

- [ ] 不出现任何具体券商名（grep 兜底）
- [ ] 至少标 1 个"少数派假设"或注明"无少数派"
- [ ] 引用单份研报内容 < 80 字
