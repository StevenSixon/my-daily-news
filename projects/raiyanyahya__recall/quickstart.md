## 安装

**通过插件市场安装**（仓库即市场）：
```
/plugin marketplace add raiyanyahya/recall
/plugin install recall@recall
```

**本地开发模式**：
```
claude --plugin-dir /path/to/recall
```

无需 `pip install`，摘要器已内置并仅依赖标准库（numpy 可选）。

## 最小可用示例
1. 正常使用 Claude Code 工作，会话活动会自动追加到 `.recall/history.md`。
2. 会话结束时，在 Claude Code 中输入 `/recall:save`，本地摘要器会生成/更新 `context.md`。
3. 下次启动 Claude Code 时，插件会自动加载 `context.md` 并询问是否从上次上下文继续。

## 依赖
- Python 3.9+（运行时环境）
- 无强制第三方包，选择安装 numpy 可加速大型会话摘要

## 配置（可选）
在项目根目录创建 `recall.config.json` 可调整输出目录、捕获开关、自动保存模式、摘要句数、脱敏、Git 包含等，完整选项见 README。