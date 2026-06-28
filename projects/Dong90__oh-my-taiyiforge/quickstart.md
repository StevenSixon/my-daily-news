## 安装与最小示例
**依赖前提**：Node.js（版本未明确，建议 LTS），npm，至少一个支持的 AI 终端（Claude Code/Cursor/OpenCode/Codex）。

```bash
# 1. 全局安装
npm install oh-my-taiyiforge

# 2. 同步 Skill 到所有 AI 终端
npx taiyi-forge-install --all

# 3. 在 AI 终端中创建第一个变更
/taiyi:new "优化登录流程"
/taiyi:status

# 或者从需求文档一键生成全栈骨架（auto 模式）
/taiyi:plan README.md --auto
```

自动生成的代码位于 `examples/<项目>/agent/` 目录，包含 FastAPI 后端、前端、测试及 Docker 配置。