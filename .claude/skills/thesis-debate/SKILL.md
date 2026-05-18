---
name: thesis-debate
version: 0.1.0
last_updated: 2026-05-18
maintainer: <团队>
description: 投委会预演 —— 3 Agent 并行对辩 base case + 5 估值误区强制核对，输出攻防点表（第 3 列留空）
changelog:
  - 0.1.0: 初始骨架（教程 Ch25 对应）
---

# Skill: thesis-debate

> 这是 demo 结构骨架。实际落地要：(1) 攻防点表第 3 列**必须留空给研究员手填**（不让 AI 替答）；(2) 5 估值误区是 schema 硬约束，不允许 Subagent 跳过；(3) 5/5 都 not_applicable 时需 warn。

## 输入

- `base_case_path`: 研究员的 base case 文档（必填）
- `context_docs`: 持仓 / 历史观点 / 行业资料（可选）

## 输出

- `output/debate/{ticker}/{date}_debate.md`（仅 MD，第 3 列空白）

## 步骤

### 步骤 1：装载 + 生成 thesis 摘要

读 base_case，生成结构化 thesis 摘要（≤ 5 个核心论点）。

### 步骤 2：并行调 bull / bear

`bull-case-agent` + `bear-case-agent` 并行运行：

- 各自锁定立场（独立 system prompt + 独立 Subagent 实例）
- 各自输出 ≤ 5 条最强论据
- 各自带 `attack_surface` 自暴薄弱点

### 步骤 3：调 devil-advocate

输入：thesis 摘要 + bull 论据 + bear 论据
输出：bull / bear 都没意识到的共同盲区 + **强制核对 5 个估值误区**：

- `growth_premium`（高景气溢价）
- `resource_value`（资源价值）
- `replacement_cost`（重置成本）
- `low_pb_cheap`（低 PB 即便宜）
- `dcf_undervalue`（DCF 算便宜）

每条必须返回 `applicable / partial / not_applicable` + severity。
**5 条 minItems = maxItems = 5，强制全部返回**。

### 步骤 4：consolidator 归并

L3 Skill 自己做归并（不让 Subagent 跨自身视角整合）：

- 按 severity 分级：`thesis_breaker > weakener > watch`
- 同类合并
- 5 估值误区作为独立模块保留（不要合并进攻防点表）

### 步骤 5：生成攻防点表（3 列）

| # | 攻击点 | 严重性 | 我方现有回应 | 应答盲区（留空） |
|---|---|---|---|---|

**第 3 列必须由研究员手工填**，AI 不填。

### 步骤 6：强制检查

- 不生成 HTML（debate 是内部讨论材料）
- 第 3 列必须全空（grep "应答盲区" 后续列必须为空）
- 5 估值误区核对表必须 5/5
- 若 5/5 都 not_applicable → warn 研究员可能 over-confident

## 检查清单

- [ ] 攻防点表"应答盲区"列全空
- [ ] 5 估值误区核对完整（5 项）
- [ ] bull / bear 论据 ≤ 5 条
- [ ] 不生成 HTML
- [ ] 输出不含"推荐 / 建议"
