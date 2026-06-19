## 它是什么
`container` 是 macOS 上原生的容器运行时，它以轻量级虚拟机的方式运行 Linux 容器，完全由 Swift 编写，并深度优化 Apple Silicon。它兼容 OCI 镜像标准，可从任何标准注册表拉取镜像，并在本地构建、运行和推送容器镜像。

## 为什么火
- **Apple Silicon 原生体验**：不是基于 QEMU 的模拟，而是直接利用 macOS 的虚拟化框架，性能损失极小，启动快。
- **苹果级工程品质**：代码由 Apple 维护，遵循严格的安全与稳定性要求，作为系统扩展集成到 macOS 26 中，与系统网络、文件系统深度绑定。
- **打破 Docker Desktop 限制**：无订阅费用，无商业许可证烦恼，对开发者友好，且针对 M 系列芯片的能效比做了特殊调教。

## 技术栈
- **语言**：Swift（包括系统级 API 调用）。
- **底层依赖**：`Containerization` Swift 封装包，直接调用 macOS 26 的 `Virtualization.framework` 和网络扩展。
- **兼容性**：遵循 OCI 镜像、分层、配置规范，输出标准容器镜像。
- **配置管理**：TOML 文件替代旧的 UserDefaults 属性，更透明、版本化。

## 核心能力
- `container machine`：长期运行的 Linux 环境，与主机文件、网络、VS Code 等紧密集成，替代传统开发环境。
- 完整的镜像生命周期：`pull`、`run`、`build`（通过 Dockerfile 或直接挂载）、`push`、`cp`。
- 网络与存储：支持自定义网络，防止 IP 泄露；`system df` 精确统计空间占用。
- 结构化输出：支持 JSON/YAML/TOML 格式的 `ls` 和 `inspect`，适合脚本编程。
- 安全升级路径：提供升级/降级脚本，保留用户数据。

## 适用场景
- 需要在 Mac 上运行 Linux 微服务或数据库的本地开发测试。
- CI/CD 流程中利用 Mac 原生虚拟化批量运行 Linux 作业。
- 构建多架构镜像（x86_64 可能受限，但 Apple Silicon 原生支持）。
- 寻求 Docker Desktop 免费且更紧密系统集成的替代方案的用户。

## 同类对比
- **Docker Desktop**：功能最完备，但在 Apple Silicon 上通过虚拟机运行 Linux，有额外资源开销和许可证限制。`container` 更轻量，系统集成更深。
- **Podman**：无守护进程架构，可在 Mac 上通过 Podman Machine 运行，但同样依赖外部虚拟机。`container` 原生虚拟化效率更高。
- **Lima**：同样是虚拟机方案，但配置灵活。`container` 作为 Apple 官方工具，与 macOS 特性（如安全隔离、网络扩展）的协同更好。
- **Finch**：基于 Lima 的 Amazon 容器工具，仍有虚拟层。`container` 直接从系统层面接管，资源占用更低。

## 版本动态
- **1.0.0 里程碑**（2026-06-09）：项目满一年，正式引入 `container machine` 特性，配置全面转向 TOML 文件，清理了结构化输出格式，增加 `cp` 命令，修复多个稳定性问题。
- **破坏性变更**：移除了对 0.x 版本 XPC API 的兼容，CLI 子命令（如系统属性设置）被替换。
- **未来方向**：将持续增强长期环境集成，提升对 IDE 和开发工具链的支持，维持 patch 版本内的稳定性。