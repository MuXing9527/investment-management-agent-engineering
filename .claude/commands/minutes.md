---
name: minutes
description: 电话会议纪要分析 —— 自动调 meeting-minutes-analyzer Skill
---

# /minutes <ticker> <period> <file> [--mode brief|full]

Command 层只做 3 件事（参考 Ch10）：

1. **参数解析**：ticker / period / 纪要文件路径必填，mode 默认 full
2. **调用 Skill**：`meeting-minutes-analyzer` 接管业务逻辑
3. **输出整理**：返回 MD + HTML 路径

## 用法

```bash
/minutes 600519 2025Q3 ./raw/600519_2025Q3_call.pdf
/minutes NVDA Q1-FY27 ./raw/nvda_call.pdf --mode brief
```

## 反模式

- 把"先读纪要再对比口径"写到 Command —— 是 Skill 的事
- 默认值塞到 prompt 里 —— 应在 Command 层解析后传给 Skill
