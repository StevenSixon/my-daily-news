## 安装
```bash
# 一键安装（推荐）
curl -fsSL https://mimo.xiaomi.com/install | bash

# 或通过 npm（需 Node.js ≥18）
npm install -g @mimo-ai/cli
```

## 首次运行
```bash
mimo
```
启动时自动引导配置，可选：
- MiMo Auto（限时免费，匿名零配置）
- 小米 MiMo 平台 OAuth 登录
- 导入 Claude Code 认证
- 自定义 OpenAI 兼容 API

## 最小使用示例
进入项目目录后运行 `mimo`，即可用自然语言指令：
```
> 帮我添加一个用户登录接口
> /plan 分析当前项目结构
> /goal 完成接口和单元测试
```

## 依赖前提
- 操作系统：macOS / Linux / WSL
- Node.js ≥18（二选一，npm 安装需要）
- 可选：`sox`（语音输入需要，macOS `brew install sox`，Linux `apt install sox`）
- WSL 用户建议安装 `xsel` 以解决剪贴板问题