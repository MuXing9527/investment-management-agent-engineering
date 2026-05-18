---
name: digest
description: 卖方研报消化 —— 自动调 sell-side-research-digester Skill
---

# /digest <ticker> <period> <research_pdf_paths...>

Command 层只做 3 件事：

1. **参数解析**：ticker / period 必填，可传多份研报 PDF
2. **调用 Skill**：`sell-side-research-digester` 接管业务逻辑
3. **输出整理**：返回 MD 路径（无 HTML，研报消化是内部用）

## 用法

```bash
/digest 600519 2025Q3 ./raw/broker_a.pdf ./raw/broker_b.pdf ./raw/broker_c.pdf
```

## 反模式

- 在 Command 里指定具体券商名 —— Subagent 层会强制匿名化
- 输出 HTML —— 研报消化稿是内部材料，无需对外
