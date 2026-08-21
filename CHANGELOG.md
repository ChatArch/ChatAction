# Changelog

## 0.1.3 - 2026-08-21

### Added
- Add `chataction --tree-brief` for command trees without parameter signatures while retaining command nodes and descriptions.

### Changed
- Migrate the top-level tree flags to ChatStyle's shared `add_tree_option()` runtime and keep the public root name `chataction`.
- Keep parameter signatures in the default `chataction --tree` output.
- Update dependency windows to `chatstyle>=0.2.0,<0.3.0` and `chatenv>=0.2.10,<0.3.0`.

## 0.1.2 - 2026-08-12

### Changed
- Keep `chataction --tree` rooted at the public console command name even when invoked through `python -m chataction.cli`.
- Enable the MkDocs Material emoji renderer (`pymdownx.emoji` with Material `twemoji`/`to_svg`) for bilingual public docs.
- Harden tag-driven PyPI publishing with package-version, default-branch, and PyPI exact-version guards.
- Add CI smoke checks for installed `chataction --version` and `chataction --tree`.

## 0.1.1 - 2026-08-10

### Added
- Add top-level `chataction --tree` generated from the registered Click command tree.
- Add MkDocs command-tree documentation with Chinese and English pages.

### Changed
- Establish bounded ChatArch runtime dependencies for ChatStyle and ChatEnv.
- Document that template `hello` and documentation-only action commands are not part of the real CLI surface.

## 0.1.0 - 2026-07-05

### Added
- First tag-driven release through GitHub Actions and PyPI Trusted Publisher.

## 0.0.1 - 2026-07-05

### Added
- Placeholder release for PyPI name registration.
