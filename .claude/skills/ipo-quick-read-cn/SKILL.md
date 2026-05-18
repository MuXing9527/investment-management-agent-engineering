---
name: ipo-quick-read-cn
version: 0.1.0
last_updated: 2026-05-18
maintainer: <团队>
description: A 股 / 港股招股书速读 —— PDF 分章节并行处理，30 分钟出 5000 字速读，客户/供应商强制匿名化
changelog:
  - 0.1.0: 初始骨架（教程 Ch22 对应）
---

# Skill: ipo-quick-read-cn

> 这是 demo 结构骨架。实际落地要：(1) PDF 分章节工具替换为真实 OCR + 目录解析；(2) 港股 / 美股招股书结构差异较大，需各自分支；(3) 客户匿名化 grep 兜底必须实测。

## 输入

- `prospectus_pdf_path`: 招股书 PDF 路径（必填）
- `market`: A股 / 港股 / 美股（默认 A股）

## 输出

- `output/{issuer}/ipo_quick_read.md`
- `output/{issuer}/ipo_quick_read.html`

## 步骤

### 步骤 1：PDF 分章节预处理

调 `mcp.pdf.split_by_toc` 把 600 页招股书按章节切分：

- 第 1 章 释义 + 概览 → 跳过
- 第 2 章 发行人基本情况 → `ipo-issuer-profile-reader`
- 第 3 章 业务与技术 → `ipo-business-reader`
- 第 4 章 关联交易 / 同业竞争 → `ipo-related-party-reader`
- 第 5 章 风险因素 → `ipo-risk-reader`
- 第 6 章 募集资金运用 → `ipo-use-of-proceeds-reader`
- 第 7 章 财务会计 → `ipo-financials-reader`

### 步骤 2：MAP 7 个章节并行

每个 Subagent 各自有最严的 output_schema，**强制匿名化客户 / 供应商为 A / B / C / D / E**。

### 步骤 3：拉行业 / 同行数据

- 行业基础数据
- 可对标的 A 股 / 港股同行

### 步骤 4：分 6 段子章节独立生成

每段 700-1000 字，独立调 LLM 写：

1. 一句话定性
2. 公司画像（业务 + 客户结构匿名化）
3. 财务（3 年完整数据 + 业务分部）
4. 行业地位
5. 募投合理性
6. 风险因素优先级

### 步骤 5：拼装 + 双输出 + 检查

- MD + HTML
- 黑名单 grep + 客户名 grep 兜底
- 不出现具体客户 / 供应商名（除非招股书披露允许）

### 步骤 6：grep 兜底确认匿名化

任何疑似客户名命中 → 阻断输出。

## 检查清单

- [ ] 客户 / 供应商已匿名化为 A / B / C
- [ ] 总字数约 5000
- [ ] 6 段子章节齐全
- [ ] 不出现"推荐 / 申购 / 必中"
