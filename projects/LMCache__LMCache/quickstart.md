### 安装
```bash
pip install lmcache
```

### 快速体验
1. 根据 [Quickstart 文档](https://docs.lmcache.ai/getting_started/quickstart.html) 准备配置文件（示例见 `examples/cache_with_configs`）。
2. 启动 LMCache 守护进程：`lmcache_server --config /path/to/config.yaml`
3. 在 vLLM 启动参数或环境变量中启用 LMCache connector（如 `--lmcache-config` 或 `LMCACHE_CONFIG_FILE`）。
4. 发送请求，观察缓存命中效果。

> 详细步骤和不同后端（Redis、NIXL 等）的配置见[文档](https://docs.lmcache.ai/recipes/index.html)。

### 依赖前提
- Python ≥ 3.9
- PyTorch（版本需匹配推理框架）
- vLLM 或其他推理引擎（若使用）
- 若使用远程存储，需对应的服务（如 Redis）和网络权限