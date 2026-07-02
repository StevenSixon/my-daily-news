## 安装与最小示例
**前提**：
- Node.js 18.18+
- ChatGPT订阅或OpenAI API密钥
- Claude Code已安装

**安装**：
```bash
# 添加插件市场
/plugin marketplace add openai/codex-plugin-cc
# 安装插件
/plugin install codex@openai-codex
# 重载插件
/reload-plugins
# 运行设置
/codex:setup
```
若Codex未安装，`/codex:setup`会提示通过npm安装，或手动执行：
```bash
npm install -g @openai/codex
codex login
```

**最小可用示例**：
```bash
# 在Claude Code中运行一次标准审查（后台）
/codex:review --background
# 查看任务状态
/codex:status
# 获取审查结果
/codex:result
```

**快速后台救援**：
```bash
/codex:rescue --background investigate why the tests failed
```
稍后通过`/codex:result`查看结论。