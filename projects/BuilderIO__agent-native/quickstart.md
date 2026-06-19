## 快速上手

**前提**：Node.js 18+、pnpm（推荐）。

1. 创建项目

```bash
npx @agent-native/core@latest create my-platform
```

2. 进入目录并安装

```bash
cd my-platform
pnpm install
```

3. 启动开发服务器

```bash
pnpm dev
```

此时访问 `http://localhost:3000` 即可看到模板应用。

你也可以单独创建一个应用（非 monorepo）：
```bash
npx @agent-native/core@latest create my-app --standalone --template mail
```

**使用技能**（无需完整项目）：
```bash
npx @agent-native/core@latest skills add visual-plan
```

然后就可以在 Claude Code 等编码代理中使用 `/visual-plan` 和 `/visual-recap`。

更多模板见官网：https://agent-native.com/templates