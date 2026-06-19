## 安装

### 前提
- 已安装 **Claude Code**（推荐）、Cursor、Antigravity CLI、Gemini CLI 或支持指令文件的 AI 编码代理。
- （若通过 SSH 克隆）需配置 GitHub SSH Key，否则使用 HTTPS 地址。

### Claude Code 安装（推荐方式）
```bash
# 通过市场安装
/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills

# 若遇到 SSH 错误，改用 HTTPS
/plugin marketplace add https://github.com/addyosmani/agent-skills.git
/plugin install agent-skills@addy-agent-skills
```

### 本地开发安装
```bash
git clone https://github.com/addyosmani/agent-skills.git
claude --plugin-dir /path/to/agent-skills
```

### 其他工具
- **Antigravity CLI**: `agy plugin install https://github.com/addyosmani/agent-skills.git`
- **Gemini CLI**: `gemini skills install https://github.com/addyosmani/agent-skills.git --path skills`
- **Cursor**: 复制任意 `SKILL.md` 到 `.cursor/rules/`，或引用整个 `skills/` 目录。
- **Copilot**: 将 `agents/` 下的代理定义加入 `.github/copilot-instructions.md`。

## 最小可用示例

### 1. 定义需求
在 Claude Code 对话中输入：
```
/spec 我要做一个简单的待办事项 API，支持创建、完成和列表查询
```
代理将启动 `spec-driven-development` 技能，输出包含目标、结构、测试策略、技术边界的产品需求文档。

### 2. 拆解任务
```
/plan
```
将上一步的 PRD 分解为可验证的原子任务，按依赖排序。

### 3. 自动构建与交付
```
/build auto
```
一次性审批计划后，代理会按任务逐个增量实现、执行 TDD 测试、独立提交，并在失败或高风险步骤时暂停。完成后可直接 `/ship` 进入上线检查。

## 依赖与注意事项
- 技能本身无运行时依赖，但浏览器测试技能需要 Chrome/Edge 及 Chrome DevTools MCP 配置。
- 推荐在推理能力强的模型（如 Claude 4 系列、GPT-4.1 等）下使用，以保证复杂技能的遵循度。
- 可通过 `/using-agent-skills` 命令让代理自动路由当前任务适用的技能。