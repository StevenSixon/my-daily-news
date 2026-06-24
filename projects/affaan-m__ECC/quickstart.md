## 安装

### 前置依赖
- Node.js（推荐 20+）
- 至少一个受支持的 AI harness 已安装（如 Claude Code、Cursor、Codex）

### 从 npm 安装（推荐）

```bash
npm install -g ecc-universal ecc-agentshield
```

### 从 GitHub 安装

```bash
git clone https://github.com/affaan-m/ECC.git
cd ECC
npm install
```

### 验证安装

```bash
ecc status
```

## 最小可用示例

1. **查看可用技能**

```bash
ecc skills list
```

2. **启动控制面板（v2.0.0）**

```bash
node scripts/control-pane.js
```

此面板展示本地 session、工作项看板、MCP 库存状态。

3. **使用 Session 适配器查询当前 agent 状态**

```bash
ecc sessions list
```

4. **生成操作者状态快照**

```bash
ecc status --markdown --write status.md
```

此命令将本地状态写入 Markdown 文件，包含就绪检查、活跃 session、技能运行健康度、待处理治理事件等。

> **注意**：详细配置请参阅仓库内的 [The Shorthand Guide](./the-shortform-guide.md) 和 [Hermes Setup Guide](docs/HERMES-SETUP.md)。README 声明“本仓库只含原始代码，指南解释一切”。