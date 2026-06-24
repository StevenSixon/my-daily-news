## 安装与前提
- Python 3.10+
- Chromium/Chrome 浏览器（渲染必须；Win/macOS 自动查找系统安装；Linux 可选自动下载 turbo 版本或指定路径）
- PDF 渲染需 `poppler`（使用 `pip install 'pixelrag[pdf]'`）
- 构建索引建议 GPU（CUDA 或 MPS），CPU 也可但较慢

```bash
# 基础安装（仅渲染与命令）
pip install pixelrag

# 或带索引功能
pip install 'pixelrag[index]'
```

## 最小可用示例
### 1. 直接使用托管 API 搜索（无需安装任何东西）
```bash
curl -X POST https://api.pixelrag.ai/search \
  -H "Content-Type: application/json" \
  -d '{"queries": [{"text": "What is the capital of France?"}], "n_docs": 5}'
```

### 2. 本地渲染一个网页
```bash
# 将 Wikipedia Python 页面渲染为截图块
pixelshot https://en.wikipedia.org/wiki/Python --output ./tiles
```

### 3. 本地构建索引并搜索
```bash
# 准备一个 PDF 文件
curl -L -o paper.pdf https://raw.githubusercontent.com/StarTrail-org/PixelRAG/main/assets/pixelrag-paper.pdf

# 创建配置文件 pixelrag.yaml
cat > pixelrag.yaml << 'EOF'
source:
  type: local
  path: ./paper.pdf

embed:
  model: Qwen/Qwen3-VL-Embedding-2B
  device: auto

output: ./paper_index
EOF

# 构建索引
pixelrag index build

# 启动搜索服务
pixelrag serve --index-dir ./paper_index --port 30001

# 查询
curl -X POST http://localhost:30001/search \
  -H "Content-Type: application/json" \
  -d '{"queries": [{"text": "Overview of PixelRAG"}], "n_docs": 1}'
```

### 4. 为 Claude Code 安装截图浏览插件
```bash
uv tool install pixelrag    # 或 pipx install pixelrag
claude plugin marketplace add StarTrail-org/PixelRAG
claude plugin install pixelbrowse@pixelrag-plugins
```
之后在 Claude 中直接使用 `/screenshot <URL>` 即可。