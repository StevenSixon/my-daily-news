## 安装
```bash
curl -fsSL https://raw.githubusercontent.com/1jehuang/jcode/master/scripts/install.sh | bash
```
（需要 Linux/macOS 环境，Windows 及其他安装方式见仓库文档）

## 配置 LLM Provider
设置所需 API key，例如：
```bash
export OPENAI_API_KEY="sk-..."
# 或 ANTHROPIC_API_KEY, AWS 凭证等
```
详细认证方式参考 `AUTH_CREDENTIAL_SOURCES.md`。

## 启动会话
在项目目录下运行：
```bash
jcode
```
即进入终端交互界面，可直接用自然语言描述任务，或利用 `/` 命令进行高级操作。侧面板、记忆等功能默认自动生效，无需额外配置。