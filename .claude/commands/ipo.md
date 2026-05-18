---
name: ipo
description: IPO 招股书速读 —— 自动调 ipo-quick-read-cn Skill
---

# /ipo <prospectus_pdf_path> [--market A股|港股|美股]

Command 层只做 3 件事：

1. **参数解析**：招股书 PDF 路径必填，market 默认 A 股
2. **调用 Skill**：`ipo-quick-read-cn` 接管业务逻辑（30 分钟出 5000 字）
3. **输出整理**：返回 MD + HTML 路径

## 用法

```bash
/ipo ./raw/xxx_prospectus.pdf
/ipo ./raw/yyy_prospectus.pdf --market 港股
```

## 反模式

- 在 Command 里 split PDF —— 是 Skill 的 step 1
- 把 7 个章节 Subagent 都写到 Command —— Skill 编排即可
