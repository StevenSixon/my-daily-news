## 安装
1. 克隆仓库：`git clone https://github.com/NotASithLord/peerd.git`
2. Chrome 打开 `chrome://extensions`，启用开发者模式。
3. 点击“加载已解压的扩展程序”，选择仓库内的 `extension/` 文件夹。
4. 点击工具栏扩展图标将其固定。

## 设置
1. 打开扩展面板，首次运行需创建本地保险库：使用 Touch ID / 安全密钥或设置恢复口令。
2. 进入设置（齿轮图标）→ API 密钥，添加 Anthropic 或 OpenRouter 的 API Key，或配置本地 Ollama 地址（无需密钥）。
3. 可选：在设置中开启“操作前确认”以手动批准每个自动化步骤。

## 最小使用
- 在聊天框中输入任务，例如“打开某个标签页并总结内容”，或“在这张页面上填写表单”。
- 代理会读取/驱动标签页，并在沙盒中执行相关计算。
- 可切换使用的模型（聊天框上方选择器）。

## 前置依赖
- Chrome 或 Firefox 浏览器（Firefox 临时加载支持，Chrome 为主要目标）。
- 至少一个模型提供商：Anthropic API 密钥、OpenRouter 密钥或本地运行的 Ollama。
- 无需 Node.js、无需构建步骤，直接加载扩展目录即可。

## 更新
- 在 `chrome://extensions` 中点击 peerd 旁的刷新图标即可应用代码更改。