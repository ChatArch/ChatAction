# CLI 树

`chataction --tree` 输出当前安装版本的真实 Click 注册树。它不是 README 手写示例；新增命令时应让运行时树、测试和文档同时更新。

```text
chataction  # ChatAction action orchestration CLI.
├── --help  # Show this help message.
├── --version  # Show the installed package version.
└── --tree  # Print the registered command tree.
```

## 状态说明 {#status}

| 节点 | 状态 | 说明 |
| --- | --- | --- |
| `--help` | 已实现 | Click 自动生成帮助。 |
| `--version` | 已实现 | 读回 `chataction.__version__`。 |
| `--tree` | 已实现 | 从 `chataction.cli.main` 注册树渲染。 |
| `hello` | 不存在 | 模板演示命令不属于真实包接口。 |
| 业务 action 子命令 | 未实现 | 后续新增时必须有可复用 Python API 和 CLI 测试。 |

## 更新规则 {#update-rules}

- 新增 visible command 时，先实现可复用 Python API，再添加 CLI 适配。
- `--tree` 必须继续从真实注册树渲染，不能复制静态示例。
- 测试至少覆盖 `--help`、`--version`、`--tree` 和代表性 leaf/group。
- README、MkDocs、CHANGELOG 和发布版本必须与命令树同步。
