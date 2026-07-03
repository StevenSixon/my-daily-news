## 安装
**前提**：Python 3.10+，建议使用 `uv` 或 `pipx` 隔离。
```bash
# 使用 uv（推荐）
uv tool install graphifyy

# 或 pipx
pipx install graphifyy

# 注册技能到 AI 助手（如 Claude Code）
graphify install
```

## 最小使用
在你的 AI 编码助手中输入：
```
/graphify .
```
工具会自动扫描当前目录并生成三个文件：
- `graph.html`: 浏览器中交互查看图谱
- `GRAPH_REPORT.md`: 亮点、关键联系和建议问题
- `graph.json`: 完整图谱数据，可随时查询

## 命令行直接使用
```bash
graphify extract .                # 从代码提取符号与关系
graphify cluster-only graph.json  # 社区发现
graphify export callflow-html     # 生成调用流架构图
```

## 可选功能安装
```bash
uv tool install "graphifyy[pdf,video,neo4j]"   # 示例：支持 PDF、视频转录和 Neo4j 推送
```