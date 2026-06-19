## 依赖前提
- Mac 搭载 Apple 芯片（M 系列）。
- macOS 26 或更高版本（利用了新版虚拟化和网络增强特性）。

## 安装
1. 从 [GitHub Release 页面](https://github.com/apple/container/releases) 下载最新签名安装包。
2. 双击 `.pkg` 文件，按提示输入管理员密码，文件将安装到 `/usr/local`。
3. 启动系统服务：
   ```bash
   container system start
   ```

## 最小可用示例
运行一个 Alpine Linux 容器并打印 hello：
```bash
container run --rm alpine echo "Hello from Apple container"
```

拉取并交互式运行 Ubuntu：
```bash
container run -it ubuntu bash
```

创建长期开发机器（类似功能虚拟机）：
```bash
container machine create --name devbox
container machine start devbox
```

## 后续步骤
- 阅读[入门教程](https://github.com/apple/container/blob/main/docs/tutorials/start-here.md)构建和发布 web 服务器镜像。
- 查阅[命令参考](https://github.com/apple/container/blob/main/docs/command-reference.md)了解更多命令。