---
name: earnings-note-cn
version: 0.1.0
last_updated: 2026-05-18
maintainer: <团队>
description: A 股 / 港股季报点评 —— 30 分钟出 1200-1500 字点评 + 双输出
changelog:
  - 0.1.0: 初始骨架（教程 Ch18 对应）
---

# Skill: earnings-note-cn

> 这是 demo 结构骨架。实际落地要：(1) 替换 MCP 调用为真实 server 名；(2) 按机构合规要求调整黑名单；(3) 接入机构内部的财务模板。

## 输入

- `ticker`: 股票代码（必填）
- `quarter`: Q1 / Q2 / Q3 / Q4（默认最近一期）
- `year`: 财报年份（默认最近一年）

## 输出

- `output/{ticker}/{year}{quarter}/earnings_note.md`
- `output/{ticker}/{year}{quarter}/earnings_note.html`

## 步骤

### 步骤 1：数据查询清单驱动

必须先查到以下数据才能进入步骤 2（参考 Ch12 / Ch15）：

- [ ] 本期 revenue / gross profit / net income / cash flow（mcp.<datasource>.financials）
- [ ] sell-side consensus（最近 30 天卖方一致预期）
- [ ] 上一期 + 去年同期同字段（QoQ / YoY 用）
- [ ] 业绩指引（如有）
- [ ] 重要会计政策变更（如有）

任一缺失 → 报 `MISSING_DATA: <字段>` 并停下，让研究员补充。

### 步骤 2：调用 Subagent 并行处理

- `financial-reader`：读财报原文，提取关键字段（参考 Ch11 output_schema）
- `consensus-reader`：读 sell-side consensus，标准化为 JSON
- `transcript-reader`：读电话会议纪要（如有）

3 个 Subagent 各自有 output_schema 强约束，禁止自由文本输出。

### 步骤 3：归并 + variance 表

L3 Skill 自己做 variance 计算（不要让 Subagent 做计算 → AI 容易算错）：

```text
variance_table = {
  revenue:   {actual, consensus, beat_miss},
  gross_pft: {actual, consensus, beat_miss},
  net_inc:   {actual, consensus, beat_miss},
  ...
}
```

所有计算结果标 `[VERIFY: variance_revenue_q1_2026]` 占位符。

### 步骤 4：生成点评草稿（强制结构）

1. 一句话结论（≤ 30 字，不出现"推荐 / 买入"）
2. 业绩 vs 共识表（步骤 3 的 variance 表）
3. 业绩拆分（按业务分部 / 地域）
4. 指引解读（如有 + 与历史指引对比）
5. 关键 watch points（≤ 3 条）

### 步骤 5：双输出 + 检查（参考 Ch9 / Ch13）

- 生成 MD + HTML，结构对齐
- 黑名单 grep（中文 + 英文，参考 check.py）
- 截断检查（HTML tag 平衡）
- [VERIFY] 占位符不能全部为空
- 不出现具体客户名

## 检查清单

- [ ] 标题不出现"推荐 / 买入 / 建议"
- [ ] variance 表所有数字标 [VERIFY] 或有 [SOURCE]
- [ ] HTML 字数 >= MD 字数 * 0.9
- [ ] 整体不超过 1500 字
