### 安装依赖
- Python 3.8+（推荐使用虚拟环境）
- 系统依赖：可能需要 `libreoffice`（用于 Office 文档解析），参阅官方文档。

### 安装 MinerU
```bash
pip install mineru
```

### 模型下载（自动）
首次运行时，MinerU 会自动从网络下载所需模型文件（约 1~2GB），也可手动下载后配置离线缓存。

### 最小示例
```bash
# 解析 PDF 输出 Markdown
mineru -p document.pdf -o output_dir
```
更复杂的用法（VLM 引擎、API 接口）请参考官网文档：https://opendatalab.github.io/MinerU/