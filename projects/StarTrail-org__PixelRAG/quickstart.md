```bash
pip install pixelrag

# 渲染页面为截图瓦片
pixelshot https://en.wikipedia.org/wiki/Python --output ./tiles

# 直接调用公共搜索 API（无需 API Key）
curl -X POST https://api.pixelrag.ai/search \
  -H "Content-Type: application/json" \
  -d '{"queries": [{"text": "What is the capital of France?"}], "n_docs": 5}'

# 本地部署预建索引（需～217G 磁盘）
huggingface-cli download StarTrail-org/pixelrag-faiss-indexes \
  --repo-type dataset --include "search_index_normed_v2/*" --local-dir ./index
pip install 'pixelrag[serve]'
pixelrag serve --index-dir ./index/search_index_normed_v2 --port 30001
```