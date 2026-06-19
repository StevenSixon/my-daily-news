## 安装
要求Python 3.10+。安装所有额外：
```bash
pip install "headroom-ai[all]"
```
Node环境：
```bash
npm install headroom-ai
```

## 最小可用示例
### Python库
```python
from headroom import compress

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Summarize: " + large_text}
]
compressed = compress(messages)
# 发送压缩后的messages给LLM
```

### 代理包装（Claude Code）
```bash
headroom wrap claude
```

### 独立代理服务器
```bash
headroom proxy --port 8787
```
配置应用使用该代理作为OpenAI兼容端点。

### 输出token缩减（可选）
```bash
export HEADROOM_OUTPUT_SHAPER=1
headroom proxy --port 8787
```

## 验证效果
```bash
headroom perf
```

## 依赖前提
- Python 3.10+（Python版）或Node环境（TypeScript版）
- 自动下载Hugging Face模型kompress-v2-base
- 可按需安装可选依赖：`[proxy]`、`[mcp]`、`[ml]`、`[code]`、`[memory]`、`[relevance]`、`[image]`、`[agno]`、`[langchain]`、`[evals]`、`[pytorch-mps]`（Apple GPU嵌入器卸载）