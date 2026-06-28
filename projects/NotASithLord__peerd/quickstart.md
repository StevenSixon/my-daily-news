## 安装
1. 克隆仓库：`git clone https://github.com/NotASithLord/peerd.git`
2. 打开 Chrome，进入 `chrome://extensions`，开启 **开发者模式**
3. 点击 **加载已解压的扩展**，选择项目内的 `extension/` 文件夹
4. 固定 peerd 图标到工具栏

## 最小示例
1. 首次启动需创建本地 vault：点击图标 → 设置 Touch ID/passkey 或恢复口令
2. 在 **设置 → API keys** 中填入 Anthropic 或 OpenRouter 密钥（或使用本地 Ollama 无需密钥）
3. 回到对话界面，输入自然语言指令，例如：“总结当前标签页的内容”或“打开 abc.com 并填充表单”
4. 如需安全审批，可在设置中开启“操作前确认”

## 依赖前提
- Chromium 内核浏览器（Chrome/Edge/Brave/Arc 等）
- 模型 API 密钥（Anthropic/OpenRouter）或已安装 Ollama 并在本地运行模型
- 无需 Node.js、npm，无构建步骤