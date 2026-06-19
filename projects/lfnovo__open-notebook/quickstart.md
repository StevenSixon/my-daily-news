## 前提
- 安装 [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- （可选）获取 AI 供应商 API 密钥：OpenAI、Anthropic、Google 等，或使用 Ollama 免费本地运行

## 安装与启动
1. 获取编排文件：
   ```bash
   curl -o docker-compose.yml https://raw.githubusercontent.com/lfnovo/open-notebook/main/docker-compose.yml
   ```
2. 编辑 `docker-compose.yml`，将 `OPEN_NOTEBOOK_ENCRYPTION_KEY` 改为自定义密值。
3. 启动服务：
   ```bash
   docker compose up -d
   ```
4. 等待约 15–20 秒，浏览器打开 `http://localhost:8502`。

## 最小可用配置
1. 进入界面后，导航至 **Models**。
2. 选择一个 AI 供应商，点击 **+ Add Configuration**，粘贴 API Key 等必要信息。
3. 点击 **Test** 测试连通性，然后 **Sync Models** 并勾选需要启用的模型。
4. 在 **Default Model Assignments** 中点击 **Auto-Assign Defaults** 或手动分配聊天、嵌入等模型。
5. 创建第一个笔记本，上传 PDF 或添加网页链接，即可开始搜索和对话。

## 完全本地免费方案
使用 Ollama 示例文件代替默认编排：
```bash
curl -o docker-compose.yml https://raw.githubusercontent.com/lfnovo/open-notebook/main/examples/docker-compose-ollama.yml
docker compose up -d
```
在 Models 中选择 Ollama，配置本地端点（默认 `http://host.docker.internal:11434`），拉取模型后即可使用。