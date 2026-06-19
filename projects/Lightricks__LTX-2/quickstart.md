```bash
git clone https://github.com/Lightricks/LTX-2.git
cd LTX-2
uv sync --frozen
source .venv/bin/activate

# 下载模型权重（见 README 列表），放置到合适路径
# 然后运行管道示例（需根据实际配置调整参数）
# 例如使用 TI2VidTwoStagesPipeline
python -m ltx_pipelines.ti2vid_two_stages \
  --prompt "A cat walking on a piano, gentle lighting, slow-motion" \
  --checkpoint_path /path/to/ltx-2.3-22b-dev.safetensors \
  --spatial_upscaler_path /path/to/ltx-2.3-spatial-upscaler-x2-1.1.safetensors \
  --distilled_lora_path /path/to/ltx-2.3-22b-distilled-lora-384-1.1.safetensors \
  --gemma_path /path/to/gemma-3-12b-it-qat-q4_0-unquantized
```

**前提**：Python 环境、CUDA GPU（建议 Hopper 或更高，FP8 支持可降低显存）、通过 uv 安装的依赖、已下载上述所有模型文件。