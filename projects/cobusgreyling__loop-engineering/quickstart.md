## 安装与使用

**前提条件**：Node.js环境，可通过npx直接使用CLI工具，或克隆仓库进行开发。

**快速上手（无克隆）**：

```bash
# 1. 生成启动模板
npx @cobusgreyling/loop-init . --pattern daily-triage --tool grok

# 2. 估算令牌花费
npx @cobusgreyling/loop-cost --pattern daily-triage --level L1

# 3. 审计项目准备情况
npx @cobusgreyling/loop-audit . --suggest

# 4. 运行演示：查看分数变化
bash scripts/before-after-demo.sh
```

**开发模式（monorepo）**：

```bash
git clone https://github.com/cobusgreyling/loop-engineering.git
cd loop-engineering
cd tools/loop-init && npm ci && npm test && node dist/cli.js /path/to/project --pattern daily-triage --tool grok
cd tools/loop-audit && npm ci && npm test && node dist/cli.js /path/to/project --suggest
cd tools/loop-cost && npm ci && npm test && node dist/cli.js --pattern ci-sweeper --cadence 15m
```

**最小示例**：使用Grok运行日常分诊，只报告不自动修复：

```
/loop 1d Run loop-triage. Update STATE.md. No auto-fix in week one.
```

**注意**：首次使用建议L1级别（仅报告），逐步升级到L2（辅助修复）和L3（无人值守）。详细信息请参阅[模式选择器](https://cobusgreyling.github.io/loop-engineering/#interactive)。
