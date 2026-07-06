### 安装
```bash
git clone https://github.com/NotASithLord/peerd.git
# 无构建，直接加载扩展
```
- Chrome：进入 `chrome://extensions`，开启开发者模式，加载 `extension/` 文件夹
- Firefox：在 `about:debugging#/runtime/this-firefox` 中加载 `extension/manifest.json`

### 设置
1. 打开扩展侧边栏，首次创建本地保险库（推荐Touch ID/Passkey）
2. 进入 Settings → API keys，添加 Anthropic 或 OpenRouter 密钥（或使用本地 Ollama）
3. 选择默认模型

### 最小示例
在聊天框中发送指令：“阅读当前标签页的标题，并总结为三个要点”，peerd 会驱动目标标签页执行。开启 `Confirm before actions` 可手动审批每一步。

### 依赖前提
- Chromium 浏览器或 Firefox
- 一个 LLM API 密钥或本地 Ollama 服务（非必须，但无密钥只能使用有限功能）
- 无外部运行时依赖，不安装 Node/Python