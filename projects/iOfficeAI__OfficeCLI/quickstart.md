**安装（任选其一）**
- macOS/Linux: `curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash`
- Windows: `irm https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.ps1 | iex`
- 也可以直接下载 GitHub Release 的二进制并加入 PATH。

**最小可用示例（30 秒内）**
```bash
# 创建空白 PPT
officecli create deck.pptx

# 启动实时预览（浏览器自动打开）
officecli watch deck.pptx

# 另一个终端添加幻灯片
officecli add deck.pptx / --type slide --prop title="Hello"
```
浏览器中将立即看到新幻灯片，无需刷新。所有 `add`/`set`/`remove` 命令都会实时渲染。

**给 AI Agent 用**
只需在 Agent 对话中粘贴：
`curl -fsSL https://officecli.ai/SKILL.md`
Agent 将自动学习安装和使用全部命令。