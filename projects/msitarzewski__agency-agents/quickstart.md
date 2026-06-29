## 安装与使用

### 方式1：桌面应用（推荐）
下载 [Agency Agents 应用](https://github.com/msitarzewski/agency-agents-app/releases/latest)，可视化选择代理安装到目标IDE。

### 方式2：脚本安装
```bash
# 克隆仓库
git clone https://github.com/msitarzewski/agency-agents.git
cd agency-agents

# 生成集成文件
./scripts/convert.sh

# 交互式安装（自动检测已安装的AI工具）
./scripts/install.sh

# 或指定工具和部门
./scripts/install.sh --tool claude-code --division engineering,security
```

### 方式3：手动复制
直接将 `engineering/`、`design/` 等目录下的 `.md` 文件复制到AI工具的代理配置目录（如 Claude Code 的 `~/.claude/agents/`）。

## 最小可用示例
安装后，在 Claude Code 对话中输入：
> “激活 Frontend Developer 模式，帮我用 React 实现一个响应式导航栏。”

AI将代入前端开发专家角色，交付符合该角色标准的代码和说明。

### 依赖前提
- Git（若通过克隆获取）
- Bash 环境（运行脚本）
- 目标AI工具已安装（如 Claude Code CLI、Cursor 编辑器等）