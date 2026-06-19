## 安装

**前置依赖**：
- Node.js（推荐 LTS 版本，README 未指定最低版本）
- 可选：sox（用于语音输入）
- WSL 用户需安装 `xsel`（解决剪贴板乱码）

**一键安装**：
```bash
curl -fsSL https://mimo.xiaomi.com/install | bash
```

**或通过 npm**：
```bash
npm install -g @mimo-ai/cli
```

**开发构建**（需要 Bun）：
```bash
bun install
bun run dev
```

## 首次运行
```bash
mimo
```
启动后按终端引导配置：
- **MiMo Auto（限时免费）**：匿名通道，零配置
- **Xiaomi MiMo 平台**：OAuth 登录
- **从 Claude Code 导入**：一键迁移认证
- **自定义提供商**：在 TUI 中添加任何 OpenAI 兼容 API

## 最小可用示例
进入项目目录，运行 `mimo`，选择 build Agent，直接开始对话：
```text
> 帮我重构 api/user 模块，添加输入校验
```
Agent 读取项目结构、记忆中的规则后生成代码。任务会自动分配 ID，下次打开相同项目时，上下文和进度会被记忆系统恢复。

## 常用命令
- `/voice`：激活语音输入
- `/goal [条件]`：设定本次会话停止条件
- `/dream`：从对话中提炼知识到项目记忆
- `/distill`：发现并封装重复工作流
- 按 `Tab` 切换主 Agent（build/plan/compose）

**注意**：语音功能需 MiMo 账号且安装 `sox`，WSLg 音频配置见 README 详情。