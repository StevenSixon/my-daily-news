### 安装
无需克隆仓库，直接使用npm CLI：
```bash
# 初始化一个循环启动模板（如daily-triage，面向grok）
npx @cobusgreyling/loop-init . --pattern daily-triage --tool grok

# 估算该模式token花费
npx @cobusgreyling/loop-cost --pattern daily-triage --level L1

# 审计当前项目循环就绪度
npx @cobusgreyling/loop-audit . --suggest

# 生成就绪度徽章
npx @cobusgreyling/loop-audit . --badge
```

### 最小可用示例（Grok）
在项目根目录生成STATE.md后，用Grok运行只报告模式：
```
/loop 1d Run loop-triage. Update STATE.md. No auto-fix in week one.
```

### 依赖前提
- Node.js ≥ 18（用于运行npx CLI）
- 已配置的AI编码代理（Grok、Claude Code或Codex）且能访问项目仓库
- 建议先阅读项目Pattern Picker确定适合的起步模式（docs/pattern-picker.md）