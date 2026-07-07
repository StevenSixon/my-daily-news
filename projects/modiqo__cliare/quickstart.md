### 安装

```bash
# 使用 cargo 安装
cargo install cliare

# 或通过脚本安装（自动检测平台）
curl -fsSL https://github.com/modiqo/cliare/releases/latest/download/install.sh | sh
cliare metadata --format text
```

### 最小可用示例

1. 对一个已安装的 CLI 工具（如 `mycli`）进行标准测量：
   ```bash
   cliare measure mycli --out .cliare/mycli --profile standard --refresh
   ```

2. 快速查看总结：
   ```bash
   cliare summary --out .cliare/mycli
   ```

3. 查看命令索引：
   ```bash
   cliare describe .cliare/mycli --write
   ```

生成的 `command-index.json` 即是被测 CLI 的代理可用命令映射，可供下游代理框架加载。

### 依赖前提

- 被测 CLI 二进制可在 `PATH` 中访问或提供绝对路径。
- 某些上下文模式（如 `authenticated`、`host`）需要相应的运行环境。
- 没有其他系统级依赖。