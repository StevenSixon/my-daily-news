## 安装
选择你使用的 AI 代理平台，执行对应命令（需 Node.js 在 PATH 中）：

**Claude Code**
```
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```

**Codex**
```bash
codex plugin marketplace add DietrichGebert/ponytail
codex
# 在 /plugins 菜单中安装，/hooks 中信任钩子
```

**Gemini CLI**
```bash
gemini extensions install https://github.com/DietrichGebert/ponytail
```

**仅规则方式**
将本仓库的 `AGENTS.md` 复制到项目根目录，任何读取该文件的代理（如 CodeWhale、Swival）即生效。

## 最小可用示例
启动代理，下达任务：“实现一个日期选择器”。
代理会输出：
```html
<!-- ponytail: browser has one -->
<input type="date">
```
不再额外安装 flatpickr 或编写组件。

## 依赖前提
- Node.js（用于部分平台的钩子）
- 对应 AI 代理平台的 CLI 或桌面版
- 如果使用 nvm/nix，确保非交互 shell 的 PATH 可访问 node