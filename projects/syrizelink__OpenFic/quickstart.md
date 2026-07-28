## 快速上手

### Docker（推荐）
```bash
docker run -d -p 8000:8000 -v "openfic:/data" --name openfic ghcr.io/syrizelink/openfic:latest
```
访问 `http://localhost:8000`。

### pip 安装
1. 确保 Python 3.12+
2. 安装：`pip install openfic`
3. 启动：`openfic serve`

### 桌面应用
从 [Releases](https://github.com/syrizelink/OpenFic/releases) 下载对应平台安装包即可。

所有数据保存在本地，无额外依赖。