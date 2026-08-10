# ChatAction

ChatAction is the ChatArch action-orchestration command surface. The current package is intentionally minimal: it provides a stable top-level CLI entry point, version readback, and command-tree readback. Future action capabilities must appear in the runtime tree, tests, and documentation together.

<div class="grid cards" markdown>

-   **Inspect the CLI surface**

    ---

    Use `chataction --tree` to audit the commands exposed by the installed version.

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
| Top-level `--tree` | Implemented | Renders the current CLI tree from the Click command object. |
| Business action commands | Not implemented | Future real actions must update tests, README, MkDocs, and changelog together. |

## Next {#next}

- [CLI Tree](cli-tree.md): current registered commands and maintenance rules.
