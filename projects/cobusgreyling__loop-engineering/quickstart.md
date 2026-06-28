## 安装
无需安装，直接使用 npx 运行 CLI 工具（需要 Node.js 环境），或者克隆仓库从源码构建。

## 最小可用示例
### 1. 脚手架一个每日分类循环
```bash
npx @cobusgreyling/loop-init . --pattern daily-triage --tool grok
```
### 2. 估算令牌成本
```bash
npx @cobusgreyling/loop-cost --pattern daily-triage --level L1
```
### 3. 审计准备状态
```bash
npx @cobusgreyling/loop-audit . --suggest
```
### 4. 开始循环（以 Grok 为例）
```bash
/loop 1d Run loop-triage. Update STATE.md. No auto-fix in week one.
```
## 前提
- 拥有可用的 AI 编码代理环境（Grok、Claude Code、Codex 或 Cursor）
- 基本了解目标工具的指令语法
- 项目已初始化 Git（部分循环依赖版本控制）