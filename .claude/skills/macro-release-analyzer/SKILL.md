---
name: macro-release-analyzer
version: 0.1.0
last_updated: 2026-05-18
maintainer: <团队>
description: 中国宏观数据发布点评 —— 5 分钟出 800-1500 字，数据来自受信 MCP 无 untrusted 材料
changelog:
  - 0.1.0: 初始骨架（教程 Ch23 对应）
---

# Skill: macro-release-analyzer

> 这是 demo 结构骨架。实际落地要：(1) 接入 statistics_cn / pboc / mof 等真实数据源；(2) consensus 数据源按机构而定；(3) 资产含义部分慎写"建议"。

## 输入

- `indicator`: 指标名（CPI / PMI / 社融 / 工业增加值 / 出口 ...）
- `period`: 期间（如 2025-11）

## 输出

- `output/macro/{indicator}_{period}.md`
- `output/macro/{indicator}_{period}.html`

## 步骤

### 步骤 1：数据查询清单

- [ ] 最新值（mcp.macro_cn.query_indicator_latest）
- [ ] 历史序列（mcp.macro_cn.query_indicator_history）
- [ ] consensus 预测（mcp.macro_cn.query_indicator_consensus）
- [ ] 联动指标（mcp.macro_cn.query_related_indicators）
- [ ] 子项拆解（如 CPI → 食品 / 非食品 / 核心 CPI）

### 步骤 2：调 Subagent 做对比

`cn-macro-release-reader` —— 返回 actual / prior / consensus / surprise / 历史分位 / 子项。

### 步骤 3：跨指标联动判断

L3 Skill 自己判断（不让 Subagent 做宏观判断）：

- 本期数据 vs 相关高频指标是否一致
- 上下游指标的联动信号

### 步骤 4：起草点评

1. 一句话定调（≤ 30 字，避免"必然 / 一定"）
2. 数据表（actual / prior / consensus / surprise / YoY / MoM）
3. 子项拆解
4. 联动指标判断
5. 政策含义（央行 / 财政）
6. 资产含义（利率 / 汇率 / 股票 / 商品）—— 用"倾向于" / "历史上"等措辞

### 步骤 5：黑名单 grep

- 中文：推荐 / 买入 / 做多 / 做空 / 一定会 / 必然
- 英文：strongly bullish / definitely

## 检查清单

- [ ] 不出现"推荐 / 一定 / 必然"
- [ ] 数据表完整（actual / consensus / surprise）
- [ ] 资产含义部分用条件性措辞
