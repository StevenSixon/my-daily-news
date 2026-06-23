**安装**
```bash
pip install pixelrag
# 如需索引构建或服务
pip install 'pixelrag[index]'
```

**渲染网页为截图瓦片**
```bash
pixelshot https://en.wikipedia.org/wiki/Python --output ./tiles
```

**使用官方托管 API 搜索**（无需密钥或索引）
```bash
curl -X POST https://api.pixelrag.ai/search \
  -H "Content-Type: application/json" \
  -d '{"queries": [{"text": "What is the capital of France?"}], "n_docs": 5}'
```

**本地自建索引（示例：索引 PDF）**
```bash
# 下载示例 PDF
curl -L -o paper.pdf https://raw.githubusercontent.com/StarTrail-org/PixelRAG/main/assets/pixelrag-paper.pdf

# 编写配置
cat > pixelrag.yaml << 'EOF'
source:
  type: local
  path: ./paper.pdf
embed:
  model: Qwen/Qwen3-VL-Embedding-2B
  device: auto
output: ./paper_index
EOF

# 构建索引并启动服务
pixelrag index build
pixelrag serve --index-dir ./paper_index --port 30001

# 搜索
curl -X POST http://localhost:30001/search \
  -H "Content-Type: application/json" \
  -d '{"queries": [{"text": "Overview of PixelRAG and the diagram"}], "n_docs": 1}'
```

**前提要求**：Python 3.10+，Linux（CUDA）或 macOS（Apple Silicon）可加速嵌入；PDF 渲染需安装 poppler；服务器依赖 FastAPI。