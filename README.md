<div align="center">
    <a href="https://pypi.python.org/pypi/ChatAction">
        <img src="https://img.shields.io/pypi/v/ChatAction.svg" alt="PyPI version" />
    </a>
</div>

<div align="center">

[英文版](README.en.md) | [简体中文](README.md) | [文档](https://arch.gh.wzhecnu.cn/ChatAction/)
</div>

# ChatAction

ChatAction 是 ChatArch 的 action 编排命令面。当前版本提供稳定的基础 CLI 合同：`--version` 和从真实 Click 注册树生成的 `--tree`。

## 快速开始

```bash
pip install ChatAction
chataction --version
chataction --tree
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
chataction  # ChatAction action orchestration CLI.
├── --help  # Show this help message.
├── --version  # Show the installed package version.
└── --tree  # Print the registered command tree.
```

## CLI 规范

当前包没有模板 `hello` 命令，也没有文档-only 的伪 action 命令。后续新增真实 action 时应同步更新：

- 可复用 Python API；
- Click 命令注册；
- `chataction --tree` 输出；
- CLI 测试；
- README、MkDocs 和 CHANGELOG。

依赖窗口：`chatstyle>=0.1.1,<0.2.0`、`chatenv>=0.2.3,<0.3.0`。

## 文档

- 正式文档：https://arch.gh.wzhecnu.cn/ChatAction/
- CLI 树：https://arch.gh.wzhecnu.cn/ChatAction/cli-tree/

## 目录结构

- `src/`：包源码
- `tests/`：CLI 与版本测试
- `docs/`：MkDocs 文档源
