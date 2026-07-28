### Claude Code
```bash
claude plugin marketplace add ayghri/i-have-adhd
claude plugin install i-have-adhd@i-have-adhd
```
输入 `/i-have-adhd` 即可应用该技能。

想每次会话自动生效：
```bash
touch ~/.claude/.i-have-adhd-always
```

### Codex
```bash
codex plugin marketplace add ayghri/i-have-adhd --ref main
codex plugin add i-have-adhd@i-have-adhd
```
输入 `$i-have-adhd` 显式调用，或由Codex在合适任务中隐式触发。

### 依赖
- Claude Code 或 Codex 等支持插件系统的编码代理。
- 无需本地安装额外依赖。