## 安装

```bash
# 一键安装（无需 Node 预装）
curl -fsSL https://opencode.ai/install | bash

# 或通过 npm（需 Node.js，推荐 v18+）
npm i -g opencode-ai@latest
```

## 启动

```bash
opencode
```

## 最小示例
1. 进入任何项目目录，终端执行 `opencode`。
2. 默认使用 **build** 代理，直接输入编码指令（如 “创建一个 hello world 函数”）。
3. 按 `Tab` 切换到 **plan** 代理进行只读探索或规划。
4. 输入 `@general` 可调用通用子代理执行多步搜索任务。

## 桌面应用（Beta）
从 [releases page](https://github.com/anomalyco/opencode/releases) 下载对应平台安装包，或使用 Homebrew Cask：`brew install --cask opencode-desktop`。