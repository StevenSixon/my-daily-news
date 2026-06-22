### 安装
```bash
pip install pixelrag
```
### 最小渲染示例
```bash
pixelshot https://en.wikipedia.org/wiki/Python -o ./tiles
```
### 即时搜索（无需部署）
```bash
curl -X POST https://api.pixelrag.ai/search \
  -H "Content-Type: application/json" \
  -d '{"queries":[{"text":"Python creator"}],"n_docs":3}'
```
### 本地索引与搜索
```bash
pip install 'pixelrag[index]'
# 准备 pixelrag.yaml 指定本地文档目录
pixelrag index build
pixelrag serve --index-dir ./my_index --port 30001
curl -X POST http://localhost:30001/search \
  -H "Content-Type: application/json" \
  -d '{"queries":[{"text":"test"}],"n_docs":1}'
```
依赖：Python 3.10+；渲染网页需 Chromium（Playwright 自动下载）；PDF 处理需 `poppler`（通过 `pip install 'pixelrag[pdf]'` 安装）。