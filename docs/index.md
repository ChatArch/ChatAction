# ChatAction

ChatAction 是 ChatArch 的 action 编排命令面。当前包处在最小可用阶段：它提供稳定的顶层 CLI 入口、版本读回，以及由 ChatStyle 共享运行时生成的详细/简略命令树读回，后续真实 action 能力必须在同一命令树、测试和文档中同步出现。

<div class="grid cards" markdown>

-   **查看 CLI 表面**

    ---

    用 `chataction --tree` 查看带参数签名的命令树，或用 `chataction --tree-brief` 查看省略签名的简略树。

-   **安装与验证**

    ---

    用 `chataction --version` 和 `python -m pytest -q` 确认包版本与测试状态。

-   **边界**

    ---

    当前没有模板 `hello` 命令，也没有文档-only 的伪 action 命令。

</div>

## 快速开始 {#quickstart}

```bash
pip install ChatAction
chataction --version
chataction --tree
chataction --tree-brief
```

开发安装：

```bash
pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
```

## 当前能力 {#current-capabilities}

| 能力 | 状态 | 说明 |
| --- | --- | --- |
| 顶层 `--version` | 已实现 | 输出安装版本。 |
| 顶层 `--tree` | 已实现 | 通过 ChatStyle 从 Click 注册命令对象渲染 CLI 树，默认保留参数签名。 |
| 顶层 `--tree-brief` | 已实现 | 省略参数签名，但保留命令节点和描述。 |
| 业务 action 命令 | 未实现 | 后续新增真实 action 时必须补测试、README、MkDocs 和 changelog。 |

## 进一步阅读 {#next}

- [CLI 树](cli-tree.md)：查看当前已注册命令和维护规则。
