---
name: meeting-minutes-analyzer
version: 0.1.0
last_updated: 2026-05-18
maintainer: <团队>
description: A 股 / 港股电话会议纪要分析 —— 提取语调 / Q&A / 口径变化，输出结构化点评
changelog:
  - 0.1.0: 初始骨架（教程 Ch17 对应）
---

# Skill: meeting-minutes-analyzer

> 这是 demo 结构骨架。实际落地要：(1) 替换 MCP 调用为真实 server 名；(2) 接入机构历史纪要库做口径对比；(3) 按合规要求调整黑名单。

## 输入

- `ticker`: 股票代码（必填）
- `period`: 财报期（必填，如 2025Q3）
- `file`: 纪要文件路径（必填）
- `mode`: brief（800-1200 字）/ full（1500-2500 字），默认 full

## 输出

- `output/{ticker}/{period}/minutes_note.md`
- `output/{ticker}/{period}/minutes_note.html`

## 步骤

### 步骤 1：数据查询清单（4 项 MCP）

- [ ] 公司基本面（mcp.<datasource>.query_company_profile）
- [ ] 最近 4 期财报数据（mcp.<datasource>.query_financials，用于口径对比）
- [ ] 历史 4 期纪要要点（mcp.<datasource>.query_minutes_history）
- [ ] 现有覆盖立场（mcp.coverage.query_coverage_status）

任一缺失 → 报 `MISSING_DATA: <字段>` 停下。

### 步骤 2：调用 Subagent 读纪要

`cn-meeting-minutes-reader` —— UNTRUSTED PDF / 文本输入，返回 schema JSON：

- `tone`: 管理层整体语调（cautious / neutral / confident）
- `qa_highlights`: Q&A 中关键问答（≤ 10 条）
- `guidance_changes`: 口径变化（vs 上一期）
- `kpi_mentions`: 提到的关键 KPI

### 步骤 3：横向对比历史口径

L3 Skill 自己做对比（不要让 Subagent 跨期计算）：

- 本期 guidance vs 上一期 guidance（diff）
- 本期 tone vs 历史 4 期 tone 序列
- 新出现 / 消失的关键词

### 步骤 4：生成点评草稿

1. 一句话定性（≤ 30 字，不出现"推荐 / 买入"）
2. 管理层语调表（本期 vs 历史 4 期）
3. 口径变化 diff（新增 / 删除 / 强化 / 弱化）
4. 3-5 条关键 Q&A 摘要 + 解读
5. Watch points（≤ 3 条，含触发条件）

### 步骤 5：双输出 + 检查

- MD + HTML，结构对齐
- 黑名单 grep（推荐 / 买入 / 建议加仓）
- 不复述纪要原文超过 50 字（fair use）

## 检查清单

- [ ] 不出现"推荐 / 买入 / 建议"
- [ ] 引用纪要原文片段 < 50 字 / 段
- [ ] 口径 diff 至少有 1 条具体内容
- [ ] HTML 字数 >= MD 字数 * 0.9
