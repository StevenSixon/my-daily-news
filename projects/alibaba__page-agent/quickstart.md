### CDN 一键体验
```html
<script src="https://cdn.jsdelivr.net/npm/page-agent@1.11.0/dist/iife/page-agent.demo.js" crossorigin="true"></script>
```
使用免费测试 LLM，适合快速评估。添加 `?autoInit=false` 可手动初始化。

### NPM 安装
```bash
npm install page-agent
```

```javascript
import { PageAgent } from 'page-agent'

const agent = new PageAgent({
    model: 'qwen3.5-plus',
    baseURL: 'https://dashscope.aliyuncs.com/compatible-mode/v1',
    apiKey: 'YOUR_API_KEY',
    language: 'en-US',
})

await agent.execute('Click the login button')
```
**依赖前提**：Node.js 环境（若使用 npm）；若通过 CDN 方式，可直接在现代浏览器中运行，无需任何构建工具。需要有效的 LLM API key（推荐阿里云 DashScope 或兼容接口）。