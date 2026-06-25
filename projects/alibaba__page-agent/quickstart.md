### 安装
**CDN 直接体验（限评估）**
```html
<script src="https://cdn.jsdelivr.net/npm/page-agent@1.10.0/dist/iife/page-agent.demo.js"></script>
```
该脚本会自动初始化一个 Agent，使用阿里巴巴提供的免费测试 LLM（需同意条款）。`?autoInit=false` 可阻止自动运行，之后手动 `new window.PageAgent(...)`。

**NPM 集成**
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

await agent.execute('点击登录按钮')
```

### 依赖前提
- 现代浏览器（支持 ES2020+）
- 有效的 LLM API 端点（兼容 OpenAI 格式），或使用免费 CDN 测试端点
- 若需跨页面任务，安装 Chrome 扩展（可选）