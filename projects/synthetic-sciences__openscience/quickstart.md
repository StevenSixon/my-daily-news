## 安装
```bash
npm install -g @synsci/openscience
```
或直接使用 npx：
```bash
npx synsci
```
要求 Bun 运行时（开发时），运行无需额外安装。

## 最小可用示例
1. 设置 API 密钥（如 Anthropic）：
```bash
export ANTHROPIC_API_KEY=sk-ant-...
openscience
```
2. 在打开的浏览器工作区中给代理下达研究目标，如“探索使用 transformer 模型预测蛋白质溶解度”。

## 依赖前提
- 对于开发：Bun 1.3+
- 运行环境：Linux 内核 5.1+ 或 glibc 2.17+，不支持 CentOS 7 默认内核。
- 浏览器访问工作区 UI。