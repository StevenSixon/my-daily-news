## 前提
- 已安装并配置 Codex CLI（支持插件系统）
- Node.js 18+（用于 npx 安装）
- OpenAI API 访问（模型路由需要）

## 安装
```bash
npx lazycodex-ai install
```
安装完成后，启动 Codex，同意加载的钩子。

## 验证
```bash
npx lazycodex-ai doctor
```

## 最小可用示例
1. 打开 Codex，输入 `$init-deep` 初始化项目记忆。
2. 使用 `$ulw-plan "优化登录流程"` 制定计划。
3. 执行 `$start-work` 完成计划。
4. 或直接使用 `$ulw-loop "修复所有类型错误"` 让代理自动循环直至完成。

如果使用自主模式：
```bash
npx lazycodex-ai install --no-tui --codex-autonomous
```