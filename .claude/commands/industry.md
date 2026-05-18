---
name: industry
description: 行业深度研究 —— 自动调 industry-deep-dive-cn Skill
---

# /industry <industry_code> [--tickers ...] [--reports ...]

Command 层只做 3 件事：

1. **参数解析**：industry_code 必填，tickers 默认按申万一级取前 20 家
2. **调用 Skill**：`industry-deep-dive-cn` 接管业务逻辑
3. **输出整理**：返回 MD + HTML 路径

## 用法

```bash
/industry 801120                          # 食品饮料行业默认 N 家
/industry 801120 --tickers 600519,000858,000596
/industry 801120 --reports ./raw/r1.pdf,./raw/r2.pdf
```

## 反模式

- 在 Command 里写"先 MAP 再 REDUCE" —— 是 Skill 的事
- 默认 N 家公司硬编码到 prompt —— 应作为参数
