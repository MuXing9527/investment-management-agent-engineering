---
name: macro
description: 中国宏观数据发布点评 —— 自动调 macro-release-analyzer Skill
---

# /macro <indicator> <period>

Command 层只做 3 件事：

1. **参数解析**：indicator（如 CPI / PMI / 社融）+ period（如 2025-11）必填
2. **调用 Skill**：`macro-release-analyzer` 接管业务逻辑（5 分钟出 800-1500 字）
3. **输出整理**：返回 MD + HTML

## 用法

```bash
/macro CPI 2025-11
/macro PMI 2025-12
/macro 社融 2025-11
```

## 反模式

- Command 里拉 consensus —— 是 Skill 的 step 1
- 在 Command 里写"先调宏观 Subagent" —— 编排在 Skill
