<div align="center">
    <a href="https://pypi.python.org/pypi/ChatAction">
        <img src="https://img.shields.io/pypi/v/ChatAction.svg" alt="PyPI version" />
    </a>
</div>

<div align="center">

[英文版](README.en.md) | [简体中文](README.md) | [文档](https://arch.gh.wzhecnu.cn/ChatAction/)
</div>

# ChatAction

ChatAction 是 ChatArch 的 action 编排命令面。当前版本提供稳定的基础 CLI 合同：`--version`，以及由 ChatStyle 共享运行时从真实 Click 注册树生成的 `--tree` / `--tree-brief`。

## 快速开始

```bash
pip install ChatAction
chataction --version
chataction --tree
chataction --tree-brief
```

开发验证：

```bash
pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
python -m build
```

## CLI 树

```text
chataction
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

`--tree` 默认保留已注册子命令的参数签名；`--tree-brief` 省略参数签名，但保留命令节点和描述。当前包尚无业务子命令，因此两个模式的当前树都只包含相同的顶层选项节点。

## CLI 规范

当前包没有模板 `hello` 命令，也没有文档-only 的伪 action 命令。后续新增真实 action 时应同步更新：

- 可复用 Python API；
- Click 命令注册；
- `chataction --tree` 和 `chataction --tree-brief` 输出；
- CLI 测试；
- README、MkDocs 和 CHANGELOG。

依赖窗口：`chatstyle>=0.2.0,<0.3.0`、`chatenv>=0.2.10,<0.3.0`。

## 文档

- 正式文档：https://arch.gh.wzhecnu.cn/ChatAction/
- CLI 树：https://arch.gh.wzhecnu.cn/ChatAction/cli-tree/

## 目录结构

- `src/`：包源码
- `tests/`：CLI 与版本测试
- `docs/`：MkDocs 文档源
