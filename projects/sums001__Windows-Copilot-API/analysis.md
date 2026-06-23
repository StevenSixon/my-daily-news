## 它是什么

一个逆向工程项目，将微软 Copilot 网页版 (copilot.microsoft.com) 的用户会话包装成 OpenAI 兼容的 REST API 和 Python 库。只需一个免费的微软账号登录一次，后续所有请求都复用该会话，无需 API Key、无配额账单。提供 `/v1/chat/completions` 和 `/v1/models` 两个端点，支持流式输出和多轮对话（通过 conversation_id），可直接替换 OpenAI 官方 SDK 的 `base_url`。

## 为什么火

Star 数 361，创建仅 3 天（2026-06-19）就获得关注，因为：
- **零摩擦免费**：开发者不必申请付费 API，利用已有 Copilot 账号即可获得 GPT-4 级别模型。
- **OpenAI 生态即插即用**：任何工具只要支持自定义 base_url 就能接入，兼容性极佳。
- **无需代理/网关**：本地一个进程启动，安全自控。

## 技术栈

- **Python 3.9+** 为主语言
- **Playwright** 驱动 Chromium 实现网页自动化及登录
- **FastAPI** 提供 OpenAI 兼容服务器
- **Token Bucket** 算法实现自限流（`server/ratelimit.py`）
- **Docker** 可选部署，需事先在宿主机完成人工登录

## 核心能力

1. **Python 客户端**：`CopilotClient.chat()` 返回完整回复和 `conversation_id`，`stream()` 逐 token 生成，可维持多轮对话。
2. **OpenAI 兼容服务器**：启动 `app.py` 后即可用官方 `openai` SDK 或任意 HTTP 调用，支持 `stream`、`conversation_id`。
3. **会话持久化**：浏览器登录后 cookie/token 保存在本地 `session/`，自动刷新，无需重复登录。
4. **并发与限流控制**：上游只支持单会话串行，服务器用锁序列化所有调用。内置 12 rpm 速率限制（可调），保护账号不被封。
5. **模型能力近似**：经 GPQA Diamond 测试得到 40.9% 准确率，定性为 GPT-4 级别，无推理模型（o1/o3）能力。

## 适用场景

- 个人开发者想用 GPT-4 级模型开发、测试但不想付费。
- 本地 AI 工具链需要一个免费后端。
- 轻量的一次性自动化任务，并发量极低。

**不适用**：高并发、生产级应用、需要多模型选择、商业用途（受微软服务条款限制）。

## 同类对比

- **OpenAI 官方 API**：无免费额度，需绑卡；本项目免费但依赖单个 Copilot 账号，响应速度与并发受限。
- **其他 Copilot 逆向（如 EdgeGPT）**：方法类似，但该项目强调 OpenAI 兼容格式和流式，部署更标准化。
- **本地模型（Ollama 等）**：硬件要求高，本项目不需要 GPU，利用云端 Copilot。

## 版本动态

- 2026-06-19 首版发布
- 2026-06-22 最近更新（示例、测试脚本）
- 目前尚无 release tag，早期快速迭代
---

## ℹ️ 置信度与信息盲区

- 置信度：**high**
- 信息盲区：未提供 GPQA Diamond 基准测试的详细设置（如温度、样本数、prompt 格式等）；未说明 Copilot 背后具体模型版本（GPT-4、4o 等）及其确参；未提及是否支持多模态（图片、文件上传等）；未披露会话 token 自动刷新的具体机制和有效期；未给出高并发下账号被封的风险边界或官方服务条款的可接受范围