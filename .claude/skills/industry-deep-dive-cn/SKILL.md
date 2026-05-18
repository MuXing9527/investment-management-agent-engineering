---
name: industry-deep-dive-cn
version: 0.1.0
last_updated: 2026-05-18
maintainer: <团队>
description: A 股行业深度 —— MAP/REDUCE 并行处理 N 家公司，分章节生成避免长输出幻觉
changelog:
  - 0.1.0: 初始骨架（教程 Ch20 对应）
---

# Skill: industry-deep-dive-cn

> 这是 demo 结构骨架。实际落地要：(1) 接入真实 Wind / FactSet MCP；(2) 按机构内部分类调整 industry_code；(3) 分章节字数按机构研报要求调整。

## 输入

- `industry_code`: 申万一级行业代码（必填）
- `tickers`: 公司列表（默认按 industry 取前 20 家）
- `report_paths`: 卖方研报 PDF（可选）

## 输出

- `output/{industry}/{date}/industry_deep_dive.md`
- `output/{industry}/{date}/industry_deep_dive.html`

## 步骤

### 步骤 1：行业数据查询清单

- [ ] 行业基础数据（mcp.<datasource>.query_industry_data）
- [ ] 成分股清单（mcp.<datasource>.query_industry_constituents）
- [ ] 产业链关联（mcp.<datasource>.query_industry_associations）
- [ ] 相关政策（mcp.macro.query_related_policies）

### 步骤 2：MAP —— N 个 cn-company-snapshot 并行

每家公司一个 Subagent，并行调用。每个返回标准化"公司画像"（财报 / 分部 / 对标）。

### 步骤 3：REDUCE —— industry-aggregator 聚合

N 份 snapshot 输入 → `industry-aggregator` 计算：

- CR5 / CR10
- 财务指标分布（毛利率 / ROE 分位）
- 增长 / 估值散点

### 步骤 4：（可选）调研报消化 Skill

若有研报 → 调 `sell-side-research-digester` 拿到 consensus 共识 / 少数派。

### 步骤 5：分 5 个子章节独立生成（防长输出幻觉）

按 Ch20 拆 5 段，每段独立调用 LLM 写 1500-2500 字：

1. **行业全景** —— 市场规模 / 增速 / 驱动因素
2. **竞争格局** —— CR5 / CR10 / 头部尾部
3. **产业链拆解** —— 上下游 / 议价能力
4. **估值与盈利** —— 横向对标 / 历史分位
5. **关键变量与 watch list** —— 触发条件

### 步骤 6：拼装 + 双输出 + 检查

- MD + HTML，结构对齐
- 黑名单 grep
- 截断检查（HTML tag balance）

## 检查清单

- [ ] 总字数 5000-10000
- [ ] 5 个子章节齐全
- [ ] 不出现具体券商名
- [ ] HTML 字数 >= MD 字数 * 0.9
