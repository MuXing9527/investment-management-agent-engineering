---
name: earnings
description: 一键季报点评 —— 自动调 earnings-note-cn Skill
---

# /earnings <ticker> [--quarter Q1|Q2|Q3|Q4] [--year YYYY]

Command 层只做 3 件事（参考 Ch10）：

1. **参数解析**：ticker 必填，quarter / year 默认取最近一期
2. **调用 Skill**：`earnings-note-cn` 接管业务逻辑
3. **输出整理**：把 Skill 产出的 MD + HTML 路径告诉研究员

业务逻辑全部在 Skill 里，Command 不要塞 prompt。

## 用法

```bash
/earnings 600519                  # 贵州茅台最近一期
/earnings AAPL --quarter Q2 --year 2026
```

## 反模式

- Command 里写"先拉财务数据，再算 variance..."—— 这是 Skill 该做的
- Command 之间互相调用（`/earnings` 调 `/valuation`）—— 容易循环依赖
