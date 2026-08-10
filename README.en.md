<div align="center">
    <a href="https://pypi.python.org/pypi/ChatAction">
        <img src="https://img.shields.io/pypi/v/ChatAction.svg" alt="PyPI version" />
    </a>
</div>

<div align="center">

[English](README.en.md) | [简体中文](README.md) | [Documentation](https://arch.gh.wzhecnu.cn/ChatAction/)
</div>

# ChatAction

ChatAction is the ChatArch action-orchestration command surface. The current version provides a stable base CLI contract: `--version` and `--tree`, generated from the real Click command registry.

## Quick Start

```bash
pip install ChatAction
chataction --version
chataction --tree
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
chataction  # ChatAction action orchestration CLI.
├── --help  # Show this help message.
├── --version  # Show the installed package version.
└── --tree  # Print the registered command tree.
```

## CLI Contract

The package does not expose a template `hello` command or documentation-only pseudo action commands. Future real actions should update these surfaces together:

- reusable Python API;
- Click command registration;
- `chataction --tree` output;
- CLI tests;
- README, MkDocs, and CHANGELOG.

Dependency windows: `chatstyle>=0.1.1,<0.2.0`, `chatenv>=0.2.3,<0.3.0`.

## Documentation

- Documentation: https://arch.gh.wzhecnu.cn/ChatAction/
- CLI tree: https://arch.gh.wzhecnu.cn/ChatAction/cli-tree/

## Layout

- `src/`: package source code
- `tests/`: CLI and version tests
- `docs/`: MkDocs documentation source
