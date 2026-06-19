## 安装（以Claude Code为例）
```bash
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```
若使用桌面版，通过UI的Customize → +个人插件 → 创建插件并添加市场 → 添加仓库，输入仓库URL安装。

## 依赖前提
- 需Node.js在PATH上（用于生命周期钩子，非必须；若不满足，技能仍工作，仅激活提示静默）。

## 最小可用示例
安装后，代理启动时自动加载，开始对话即可体验。调用 `/ponytail ultra` 切换至极简模式，代理将更激进地减少代码。

其他代理安装见 README 各平台指引。