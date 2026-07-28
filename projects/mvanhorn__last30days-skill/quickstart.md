## 安装
1. **Claude Code（推荐）**：
   ```
   /plugin marketplace add mvanhorn/last30days-skill
   /plugin install last30days
   ```
2. **其他Agent Skills主机**（Codex, Cursor, Copilot, Gemini CLI等）：
   ```
   npx skills add mvanhorn/last30days-skill -g
   ```
   （`-g` 为全局安装；省略则按项目安装）
3. **首次运行自动配置**：执行 `/last30days "test"`，向导会帮助设置X、YouTube等需要认证的源，提供浏览器cookie或API密钥。

## 最小可用示例
- 基本查询：
  ```
  /last30days OpenAI Sora
  ```
- 指定时间窗口：
  ```
  /last30days "AI robotics" --days 15
  ```
- 查看招聘信号：
  ```
  /last30days Anthropic --hiring-signals
  ```
- 直接对比：
  ```
  /last30days LangChain vs LlamaIndex
  ```

## 依赖前提
- 需要Node.js >=18（用于`npx`）或已安装Claude Code环境。
- Reddit、HN、Polymarket、GitHub来源无需额外配置。
- X、YouTube、TikTok等需提供API密钥或浏览器会话（向导引导完成）。
- arXiv、Techmeme、Digg源需本地安装对应CLI（首次运行向导可自动安装）。