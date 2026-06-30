**前置依赖**：Node.js >=18，项目中已有 git 仓库（或任意目录）

**安装**（无需全局安装，直接使用 npx）：

```bash
# 1. 初始化一个每日分诊循环（以 Grok 为例）
npx @cobusgreyling/loop-init . --pattern daily-triage --tool grok

# 2. 估算令牌成本（例如每日 L1 级别）
npx @cobusgreyling/loop-cost --pattern daily-triage --level L1 --cadence 1d

# 3. 审计项目就绪度并获取改进建议
npx @cobusgreyling/loop-audit . --suggest

# 4. 生成就绪度徽章
npx @cobusgreyling/loop-audit . --badge

# 5. 检测 STATE.md 与 LOOP.md 的配置漂移
npx @cobusgreyling/loop-sync .
```

**最小可用循环**：
在初始化后的项目中，打开 AI 编码代理并输入（以 Grok 为例）：
```
/loop 1d Run loop-triage. Update STATE.md. No auto-fix in week one.
```

详细文档参见 `docs/QUICKSTART.md`。