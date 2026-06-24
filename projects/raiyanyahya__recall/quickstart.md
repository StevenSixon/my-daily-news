## 安装

**从插件市场安装**（推荐）：
```bash
# 在 Claude Code 中输入
/plugin marketplace add raiyanyahya/recall
/plugin install recall@recall
```

**本地开发模式**（无需安装）：
```bash
claude --plugin-dir /path/to/recall
```

无需 `pip install`，插件自带总结器，numpy 可选。

## 最小可用示例

1. 在 Claude Code 中开始一次普通会话，修改项目文件。
2. 会话结束前运行 `/recall:save` 生成摘要。
3. 下次打开同一项目的新会话，Claude 会展示上次的上下文并询问是否继续。

**开启自动保存**（推荐）：在项目根目录创建 `recall.config.json`：
```json
{
  "auto_save_context": "on_end"
}
```
之后每次会话结束都会自动更新 `context.md`，省去手动 `/recall:save`。

## 依赖前提

- Claude Code 客户端（已安装并登录）
- Python 3.9+（Claude Code 运行环境自带即可）
- 无外部包依赖（numpy 可选）