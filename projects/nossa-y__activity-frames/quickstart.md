### 安装
确保 Python 3.10+，安装：
```bash
pip install activity-frames
```
（可选）安装 YAML 支持：
```bash
pip install "activity-frames[yaml]"
```

### 开始录制
```bash
aframes record
```
首次运行会自动下载并验证 nocta-recorder 构建（macOS Apple Silicon；Intel/Linux 也可用）。录制会在后台进行，屏幕捕捉，音频默认关闭。

### 查看今日活动
```bash
aframes today
```
（输出结构化 YAML 或 JSON）

### 生成代理上下文
```bash
aframes context          # 最近 2 小时
aframes context --hours 3
```

### 启用 MCP 服务器
与 Claude Code 等集成：
```bash
claude mcp add activity-frames -- aframes mcp
```
或直接启动：
```bash
aframes mcp
```
此后代理可调用 5 个工具：get_context, get_activity, get_day_summary, get_patterns, get_communications。

### Python 快速示例
```python
from activity_frames import ActivityLog

log = ActivityLog()
print(log.context(hours=2))  # 文本上下文
doc = log.day()               # 结构化今日文档
```

### 依赖前提
- 操作系统：macOS（Apple Silicon 推荐，Intel 支持但测试较少）、Linux x64（有限测试）。Windows 未提及。
- 若已有兼容的捕获数据库，可设置环境变量 `AFRAMES_DB` 跳过 recorder。
- 无外部服务或 LLM 依赖。