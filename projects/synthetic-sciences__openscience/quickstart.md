### 安装
```bash
npm install -g @synsci/openscience
openscience
```
也可不全局安装，直接使用 npx：
```bash
npx synsci
```

### 最小可用示例
1. 设置 API 密钥（如 Anthropic）：
```bash
export ANTHROPIC_API_KEY=sk-ant-...
```
2. 启动工作区：
```bash
openscience
```
3. 在打开的浏览器界面中输入研究目标（例如“探索 AlphaFold3 在蛋白设计中的改进”），Agent 会自动规划并执行。

### 依赖前提
- Node.js（支持 npm）或直接从 GitHub Releases 下载平台二进制
- 至少一个 LLM 提供商的 API 密钥（也可选 Atlas 托管模型）
- 如需开发，需要 Bun 1.3+