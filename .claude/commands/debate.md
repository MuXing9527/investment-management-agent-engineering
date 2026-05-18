---
name: debate
description: 投委会预演 —— 自动调 thesis-debate Skill（多 Agent 对辩 + 5 估值误区核对）
---

# /debate <base_case_path> [--context ...]

Command 层只做 3 件事：

1. **参数解析**：base_case 文档路径必填，context 可选（持仓 / 历史观点）
2. **调用 Skill**：`thesis-debate` 接管业务逻辑
3. **输出整理**：返回攻防点表 MD（第 3 列空白，由研究员手填）

## 用法

```bash
/debate ./holdings/600519_base_case.md
/debate ./holdings/xyz_base_case.md --context ./holdings/historical_views/
```

## 反模式

- Command 里写"先多头再空头" —— 是 Skill 编排
- 输出 HTML —— debate 是内部讨论材料，无 HTML
- 让 AI 替研究员填"应答盲区" —— 必须留空
