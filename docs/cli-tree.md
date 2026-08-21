# CLI 树

`chataction --tree` 通过 ChatStyle 共享运行时输出当前安装版本的真实 Click 注册树，并默认保留命令参数签名。`chataction --tree-brief` 省略参数签名，但保留命令节点和描述。它们不是 README 手写示例；新增命令时应让运行时树、测试和文档同时更新。

```text
chataction
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

当前尚未注册带参数的业务子命令，因此详细树和简略树目前都显示上述相同的顶层选项节点。新增带参数命令后，详细树会显示其 argument/option 签名，简略树不会显示这些签名。

## 状态说明 {#status}

| 节点 | 状态 | 说明 |
| --- | --- | --- |
| `--help` | 已实现 | Click 自动生成帮助。 |
| `--version` | 已实现 | 读回 `chataction.__version__`。 |
| `--tree` | 已实现 | 由 ChatStyle `add_tree_option()` 从注册树渲染，默认包含参数签名。 |
| `--tree-brief` | 已实现 | 省略参数签名，保留命令节点和描述。 |
| `hello` | 不存在 | 模板演示命令不属于真实包接口。 |
| 业务 action 子命令 | 未实现 | 后续新增时必须有可复用 Python API 和 CLI 测试。 |

## 更新规则 {#update-rules}

- 新增 visible command 时，先实现可复用 Python API，再添加 CLI 适配。
- 顶层 Click group 必须继续使用 ChatStyle `add_tree_option()`，公开根名保持为 `chataction`。
- `--tree` 和 `--tree-brief` 必须继续从真实注册树渲染，不能复制静态示例。
- 测试至少覆盖 `--help`、`--version`、两种 tree 模式和代表性 leaf/group。
- README、MkDocs、CHANGELOG 和发布版本必须与命令树同步。
