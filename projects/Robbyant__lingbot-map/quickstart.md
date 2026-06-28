### 环境
- Python 3.10
- PyTorch 2.8.0 + CUDA 12.8
- FlashInfer（推荐，否则回退到PyTorch SDPA）
- viser（可选可视化）、onnxruntime（可选天空分割）

### 安装
```bash
conda create -n lingbot python=3.10 -y && conda activate lingbot
pip install torch==2.8.0 torchvision==0.23.0 --index-url https://download.pytorch.org/whl/cu128
pip install -e .
pip install flashinfer-python
# 可选：pip install -e ".[vis]" && pip install onnxruntime
```
### 下载模型
从[HuggingFace](https://huggingface.co/robbyant/lingbot-map)或ModelScope获取`lingbot-map-long.pt`。

### 最小运行
```bash
python demo.py --model_path /path/to/lingbot-map-long.pt --image_folder example/courthouse --mask_sky
```
浏览器打开`http://localhost:8080`查看实时重建结果。