## 安装与运行
1. **环境要求**：Chromium 内核浏览器（Chrome、Edge、Brave 等）；如需要本地模型可安装 [Ollama](https://ollama.com)。
2. **获取代码**：`git clone https://github.com/NotASithLord/peerd.git && cd peerd`
3. **加载扩展**：
   - 打开 `chrome://extensions`，启用“开发者模式”
   - 点击“加载已解压的扩展程序”，选择仓库内的 `extension/` 文件夹（包含 `manifest.json`）
4. **设置代理**：
   - 点击浏览器工具栏的 peerd 图标，在侧边面板中创建本地 Vault（推荐使用 Touch ID 或 Passkey 解锁）
   - 进入 Settings → API keys，添加至少一个模型提供商的密钥（Anthropic `sk-ant-...`、OpenRouter `sk-or-...` 或保持本地 Ollama 无需添加）
5. **开始对话**：返回聊天界面，输入消息即可让 peerd 读取/操作标签页、运行沙箱。可在设置中开启“操作前确认”以逐步审核。

**最小可用示例**：
- 在浏览器中打开某个网页，然后向 peerd 提问：“总结这个页面的核心内容”。它会自动读取当前标签页内容并生成摘要。
- 或输入：“在 JS Notebook 里写一段代码计算斐波那契数列前 20 项并打印结果”，peerd 会启动沙箱执行并返回输出。

如需更新代码，直接在 `chrome://extensions` 卡片上点击刷新图标。Firefox 临时加载方式请参考 README 说明。