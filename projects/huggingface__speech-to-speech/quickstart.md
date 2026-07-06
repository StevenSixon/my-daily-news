**安装**
```bash
# 需要 Python 3.10+
pip install speech-to-speech
# 可选后端：pip install "speech-to-speech[kokoro,pocket,chattts,faster-whisper,paraformer]"
```

**最小可用（云端 LLM）**
```bash
export OPENAI_API_KEY=your_key_here
speech-to-speech
# 启动 OpenAI Realtime 兼容服务在 ws://localhost:8765/v1/realtime
# 另开终端测试：
python scripts/listen_and_play_realtime.py --host 127.0.0.1 --port 8765
```

**完全本地（使用 llama.cpp 运行 Gemma 4）**
```bash
# 终端1：启动 LLM 服务器
llama-server -hf ggml-org/gemma-4-E4B-it-GGUF -np 2 -c 65536 -fa on --swa-full

# 终端2：启动语音管道
speech-to-speech \
    --model_name "ggml-org/gemma-4-E4B-it-GGUF" \
    --responses_api_base_url "http://127.0.0.1:8080/v1" \
    --responses_api_api_key ""
```

**在 macOS 上最优体验**
```bash
speech-to-speech --local_mac_optimal_settings
# 自动使用 MLX 后端进行 STT/LLM/TTS，并打开本地麦克风模式
```

**依赖前提**
- 安装前请确认 CUDA 版本（若使用 Qwen3-TTS GGML 后端，Linux 下可能需要手动安装对应 CUDA 版本的 `qwentts-cpp-python`）。
- 本地运行 LLM 需额外安装相应框架（如 llama.cpp、vLLM 或 transformers），非本工具包自带。