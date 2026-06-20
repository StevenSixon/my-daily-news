```bash
# 安装
pip install pixelrag

# 渲染网页为截图瓦片
pixelshot https://en.wikipedia.org/wiki/Python --output ./tiles

# 搜索托管Wikipedia索引（零配置）
curl -X POST https://api.pixelrag.ai/search \
  -H "Content-Type: application/json" \
  -d '{"queries": [{"text": "What is the capital of France?"}], "n_docs": 5}'

# 自建索引
cat > pixelrag.yaml << 'EOF'
source:
  type: local
  path: ./my_docs
embed:
  model: Qwen/Qwen3-VL-Embedding-2B
  device: cuda
  gpu_ids: [0]
output: ./my_index
EOF
pixelrag index build

# 服务启动
pixelrag serve --index-dir ./my_index --port 30001

# Claude Code插件
pip install pixelrag
claude plugin marketplace add StarTrail-org/PixelRAG
claude plugin install pixelbrowse@pixelrag-plugins
claude -p "screenshot https://news.ycombinator.com and summarize the top stories"
```
依赖：Python 3.10+, Chromium/Playwright自动安装。索引构建需CUDA GPU。