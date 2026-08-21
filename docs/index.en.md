# ChatAction

ChatAction is the ChatArch action-orchestration command surface. The current package is intentionally minimal: it provides a stable top-level CLI entry point, version readback, and detailed/brief command-tree readback through the shared ChatStyle runtime. Future action capabilities must appear in the runtime tree, tests, and documentation together.

<div class="grid cards" markdown>

-   **Inspect the CLI surface**

    ---

    Use `chataction --tree` for command parameter signatures or `chataction --tree-brief` for a signature-free overview.

-   **Install and verify**

    ---

    Use `chataction --version` and `python -m pytest -q` to confirm package identity and tests.

-   **Boundary**

    ---

    The package does not expose a template `hello` command or documentation-only pseudo action commands.

</div>

## Quick Start {#quickstart}

```bash
pip install ChatAction
chataction --version
chataction --tree
chataction --tree-brief
```

Development install:

```bash
pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
```

## Current Capabilities {#current-capabilities}

| Capability | Status | Notes |
| --- | --- | --- |
| Top-level `--version` | Implemented | Prints the installed package version. |
| Top-level `--tree` | Implemented | Uses ChatStyle to render the Click command tree with parameter signatures by default. |
| Top-level `--tree-brief` | Implemented | Omits parameter signatures while preserving command nodes and descriptions. |
| Business action commands | Not implemented | Future real actions must update tests, README, MkDocs, and changelog together. |

## Next {#next}

- [CLI Tree](cli-tree.md): current registered commands and maintenance rules.
