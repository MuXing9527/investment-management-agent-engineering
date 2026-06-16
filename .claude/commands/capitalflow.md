# /capitalflow — 月度社会资金流向备忘录

触发 `monthly-capital-flow-memo` skill，整合信用货币层（Ch46）+ 金融市场层（Ch47），输出完整月度备忘录。

## 用法

```
/capitalflow [月份]
```

示例：
```
/capitalflow 2026年5月
/capitalflow 6月
```

## 运行流程

1. 触发 `macro-credit-flow` → 生成 Section 1（信用货币环境）
2. 触发 `equity-capital-flow` → 生成 Section 2（金融市场资金结构）
3. 拼合全文 + 写封头总结
4. 输出到 `output/日常记录/XXXX年X月社会资金流向备忘录.md`

## 说明

- 外资（EPFR）数据需用户手动提供，否则标「数据未提供」
- 官方点评（金融时报/央行）如有，请提前放入 `arcticle/` 文件夹
- 图表引用路径以当月 `data/` 文件夹为基准
