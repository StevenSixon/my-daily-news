### 前提条件
- Node.js 24+
- AI 编码代理（推荐 Claude Code with Opus 4.7）

### 安装与启动
1. 从模板创建自己的仓库（GitHub 上点击“Use this template”）
2. 克隆新仓库：`git clone <你的仓库>`
3. 安装依赖：`npm install`
4. 启动 AI 代理：`claude --chrome`
5. 运行克隆命令：`/clone-website <目标网址>`

### 开发命令
```bash
npm run dev      # 启动开发服务器
npm run build    # 生产构建
npm run check    # lint + typecheck + build
```

如需其他 AI 代理，查阅 `AGENTS.md`。