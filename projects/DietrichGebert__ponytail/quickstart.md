### 安装（以 Claude Code 为例）
1. 确保 `node` 加入 PATH（非交互式 shell 同样可用）。
2. 在 Claude Code 中依次发送以下两个独立消息：
   ```
   /plugin marketplace add DietrichGebert/ponytail
   ```
   ```
   /plugin install ponytail@ponytail
   ```
3. 桌面版：在 UI 的 Customize → 个人插件 → 从仓库添加 → 输入 `https://github.com/DietrichGebert/ponytail`。

### 最小可用示例
- 新建会话后，规则自动激活（默认 `full` 模式）。你可以直接提出需求，代理将自行遵循决策阶梯。
- 使用 `/ponytail ultra` 开启极度懒惰模式，或 `/ponytail off` 关闭。
- 可通过环境变量 `PONYTAIL_DEFAULT_MODE=ultra` 全局设置默认模式。

### 其他代理的快速接入
- **OpenCode**：在 `opencode.json` 中添加 `"plugin": ["@dietrichgebert/ponytail"]`。
- **Cursor**：复制 `.cursor/rules/` 下的规则文件到项目的 `.cursor/rules/`。
- **Copilot CLI**：`copilot plugin marketplace add DietrichGebert/ponytail && copilot plugin install ponytail@ponytail`。
详细支持列表和安装说明见 README。

### 前提依赖
- 除 Claude Code / Codex 需要 Node.js 外，其他代理仅需复制对应的规则文件，无其他运行时依赖。