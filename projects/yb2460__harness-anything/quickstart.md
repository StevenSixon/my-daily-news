### 环境要求
- Windows 10/11
- Python 3.10+ 及 pywin32 (`pip install pywin32`)
- 目标软件：WPS Office 2019+ 或 MS Office 2016+ / Zotero 7+ （可选）Adobe Illustrator 2023+ / Photoshop 2023+

### 安装
```bash
# WPS/Office操控
pip install git+https://github.com/yb2460/cli-anything-wps.git

# Zotero学术工具（需进入对应目录安装）
cd cli-anything-zotero  # 按实际目录
pip install -e .

# Illustrator操控
cd illustrator-harness/agent-harness
pip install -e .

# Photoshop操控
cd photoshop-harness/agent-harness
pip install -e .
```

### 最小示例
```bash
# 创建一个空白演示文稿并导出
cli-anything-wps document new --type impress --name "示例"
cli-anything-wps export render output.pptx -p pptx

# 查看学术Skill并运行论文写作流水线
cli-anything-zotero skills list
cli-anything-zotero skills pipeline thesis

# 用Illustrator生成简易LOGO并导出SVG
cli-anything-illustrator project new logo.ai -w 500 -h 500
cli-anything-illustrator text add "Brand" --x 100 --y 100 --font "Arial" --size 72
cli-anything-illustrator export svg output.svg

# 用Photoshop创建横幅并导出PNG
cli-anything-photoshop project new banner.psd -w 1920 -h 1080
cli-anything-photoshop export png banner.png
```