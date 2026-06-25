### 安装
```bash
# 基础安装（vLLM 后端）
pip install lift-pdf

# 或含 HuggingFace 后端
pip install lift-pdf[hf]
```

### 启动 vLLM 服务（推荐）
```bash
lift_vllm   # 默认针对 H100 GPU 配置
# 或指定 GPU 类型，如：lift_vllm --gpu a10
```
此命令将拉取 Docker 镜像并启动优化过的推理服务。

### 准备 Schema
创建一个 `schema.json` 文件：
```json
{
  "type": "object",
  "properties": {
    "invoice_number": {"type": "string", "description": "发票号"},
    "total": {"type": "number", "description": "总金额"}
  },
  "required": ["invoice_number", "total"]
}
```

### 提取数据
```bash
lift_extract input.pdf ./output --schema schema.json
```
输出将在 `./output` 下生成 `<filename>.json` 和 `<filename>_metadata.json`。

### 使用 HuggingFace 后端（无需 vLLM 服务）
```bash
lift_extract input.pdf ./output --schema schema.json --method hf
```
确保有 GPU 且已安装 `pip install lift-pdf[hf]`，模型将自动下载。

### 依赖前提
- Python 3.10+（推测）
- 对于 vLLM 模式：Docker 与 NVIDIA GPU（支持 H100/A100/L40S/4090 等）
- 对于 HF 模式：torch、transformers，建议安装 Flash Attention