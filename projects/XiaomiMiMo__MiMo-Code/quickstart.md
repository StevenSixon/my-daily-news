## 安装
```bash
# 一键安装
curl -fsSL https://mimo.xiaomi.com/install | bash

# 或通过 npm
npm install -g @mimo-ai/cli
```

## 启动
```bash
mimo
```
首次启动会引导配置，推荐选择 **MiMo Auto（限时免费）** 零配置开始。

## 最简使用
进入项目目录运行 `mimo`，直接输入任务描述，例如：
> Add a new API endpoint /users that returns a list of users

## 依赖前提
- Node.js 环境（npm 安装时）
- WSL 用户若遇剪贴板问题：`sudo apt install xsel`
- 语音输入需要 `sox`（macOS: `brew install sox`）