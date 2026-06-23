## 安装前提
- Node.js 环境（推荐 LTS）
- 已安装 Codex 客户端
- （可选）OpenAI API 密钥（模型路由需要）

## 安装
```bash
npx lazycodex-ai install
```
自动安装全部组件。如需完全无人值守安装：
```bash
npx lazycodex-ai install --no-tui --codex-autonomous
```

## 验证安装
```bash
npx lazycodex-ai doctor
```
在 Codex 中输入 `$` 可查看已安装技能。

## 最小可用示例
1. 在项目根目录运行 `$init-deep` 生成记忆文件
2. 使用 `$ulw-plan "添加用户登录功能"` 生成计划
3. 执行 `$start-work [计划名]` 驱动智能体按计划实施
4. 如需保证验证完成，使用 `$ulw-loop "任务描述"`

## 卸载
```bash
npx lazycodex-ai uninstall
```