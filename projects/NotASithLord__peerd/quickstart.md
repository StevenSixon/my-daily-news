## 安装
1. 克隆仓库：`git clone https://github.com/NotASithLord/peerd.git`
2. 在 Chrome 浏览器中，进入 `chrome://extensions`，开启“开发者模式”。
3. 点击“加载已解压的扩展程序”，选择仓库内的 `extension/` 文件夹。
4. 固定 peerd 图标到工具栏。
5. 打开 peerd 侧边栏，创建本地保管库（建议使用 Touch ID 或 Passkey 解锁）。
6. 在“设置” → “API 密钥”中添加 Anthropic (`sk-ant-...`) 或 OpenRouter (`sk-or-...`) 密钥；也可以使用本地 Ollama（无需密钥，无花费）。
7. 开始对话：peerd 可以读取和驱动标签页，运行沙盒命令等。可在设置中开启“操作前确认”。

**依赖前提**：Chrome 或 Edge/Arc 等 Chromium 内核浏览器；Firefox 亦可但尚在完善。需要相应模型 provider 的 API key，或本地已运行 Ollama。