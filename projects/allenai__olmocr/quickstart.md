## 安装
```bash
# 系统依赖（Ubuntu/Debian）
sudo apt-get install poppler-utils ttf-mscorefonts-installer msttcorefonts fonts-crosextra-caladea fonts-crosextra-carlito gsfonts lcdf-typetools

# Python 环境
conda create -n olmocr python=3.11 -y
conda activate olmocr

# 本地 GPU 推理（需 12GB 显存及以上）
pip install olmocr[gpu] --extra-index-url https://download.pytorch.org/whl/cu128
pip install https://download.pytorch.org/whl/cu128/flashinfer/flashinfer_python-0.2.5%2Bcu128torch2.7-cp38-abi3-linux_x86_64.whl

# 纯远程推理（无需 GPU 驱动）
pip install olmocr
```

## 最小可用示例
```bash
# 下载示例 PDF
curl -o sample.pdf https://olmocr.allenai.org/papers/olmocr_3pg_sample.pdf

# 本地转换
olmocr ./workspace --markdown --pdfs sample.pdf

# 查看结果
cat workspace/markdown/sample.md
```

## 使用远程服务器
```bash
olmocr ./workspace --server http://your-vllm:8000/v1 --model allenai/olmOCR-2-7B-1025-FP8 --markdown --pdfs *.pdf
```