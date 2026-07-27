## 安装与上手

### 环境要求
- 项目内要有 AI 编码代理（如 Claude Code、Cursor、Codex CLI、Grok Build 等）
- Node.js 环境（用于执行 npx 命令）

### 最快开始
1. 在项目根目录运行：
   ```bash
   npx impeccable install
   ```
   安装器会自动检测已配置的工具链并安装技能和钩子。

2. 在 AI 编码工具中执行：
   ```
   /impeccable init
   ```
   根据引导完成设计上下文设定（品牌/产品类型、受众、色彩、字体等）。

3. 开始使用任意命令，例如：
   ```
   /impeccable critique 首页
   /impeccable polish 结账页
   /impeccable audit
   ```

### 最小示例
- 审阅设计：`/impeccable critique landing`
- 润色页面：`/impeccable polish settings`
- 强化边缘情况：`/impeccable harden checkout`
- 直接指令：`/impeccable 重做这个英雄区域`

### 其他安装方式
- **Git 子模块**：团队可固定版本
- **插件市场**：Claude Code（`/plugin marketplace add`）、Grok Build（`grok plugin install`）
- **手动复制**：从 `dist/` 目录复制到对应工具的技能文件夹

### 配置说明
- 在 `.gitignore` 添加推荐块，避免提交缓存、截图等临时文件。
- 使用 `/impeccable pin <command>` 可将常用命令提升为独立快捷指令。
- `npx impeccable update` 更新已有安装。