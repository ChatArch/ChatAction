<div align="center">
    <a href="https://pypi.python.org/pypi/ChatAction">
        <img src="https://img.shields.io/pypi/v/ChatAction.svg" alt="PyPI version" />
    </a>
</div>

<div align="center">

[English](README.en.md) | [简体中文](README.md) | [Documentation](https://arch.gh.wzhecnu.cn/ChatAction/)
</div>

# ChatAction

ChatAction is the ChatArch action-orchestration command surface. The current version provides a stable base CLI contract: `--version` plus `--tree` / `--tree-brief`, generated from the real Click command registry by the shared ChatStyle runtime.

## Quick Start

```bash
pip install ChatAction
chataction --version
chataction --tree
chataction --tree-brief
```

Development verification:

```bash
pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
python -m build
```

## CLI Tree

```text
chataction
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

`--tree` includes parameter signatures for registered subcommands by default. `--tree-brief` omits those signatures while preserving command nodes and descriptions. Because the package does not yet register business subcommands, both modes currently contain the same top-level option nodes.

## CLI Contract

The package does not expose a template `hello` command or documentation-only pseudo action commands. Future real actions should update these surfaces together:

- reusable Python API;
- Click command registration;
- `chataction --tree` and `chataction --tree-brief` output;
- CLI tests;
- README, MkDocs, and CHANGELOG.

Dependency windows: `chatstyle>=0.2.0,<0.3.0`, `chatenv>=0.2.10,<0.3.0`.

## Documentation

- Documentation: https://arch.gh.wzhecnu.cn/ChatAction/
- CLI tree: https://arch.gh.wzhecnu.cn/ChatAction/cli-tree/

## Layout

- `src/`: package source code
- `tests/`: CLI and version tests
- `docs/`: MkDocs documentation source
