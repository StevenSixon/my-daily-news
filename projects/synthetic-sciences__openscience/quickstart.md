### 安装
```bash
npm install -g @synsci/openscience
```
或者直接使用 npx 免安装运行：
```bash
npx synsci
```

### 最小可用示例
1. 设置 API 密钥（以 Anthropic 为例）：
```bash
export ANTHROPIC_API_KEY=sk-ant-...
```
2. 启动工作台：
```bash
openscience
```
浏览器会自动打开本地工作区界面。在输入框中给一个研究目标，代理即开始工作。

### 前置依赖
- Node.js 环境（无额外数据库或 Docker 要求）
- 至少一个 LLM 提供商的 API 密钥（支持 Anthropic、OpenAI、Google 等）
- 浏览器用于访问工作区 UI