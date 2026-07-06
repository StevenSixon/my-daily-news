## 安装要求
- Python 3.9+
- 本地运行 Ollama（`ollama pull llama3.1:8b` 拉取模型）
- 推荐 NVIDIA GPU，CPU 亦可用

## 安装
```bash
git clone <repo>
cd talos-worker
pip install -e .
```

## 配对账户
从 Talos 仪表盘获取设备配对码，然后：
```bash
talos-worker pair --code TALOS-XXXX-XXXX --server https://api.usetalos.xyz
```

## 启动 worker
```bash
talos-worker run --allocation 0.5
```
打开本地仪表板 http://127.0.0.1:8674 查看状态。

## 验证
```bash
talos-worker status
```
可查看 GPU 信息及可用模型列表。