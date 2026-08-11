# Changelog

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
- Update ChatArch internal dependency lower bounds to `chatstyle>=0.1.1,<0.2.0` and `chatenv>=0.2.3,<0.3.0`.
- Document that template `hello` and documentation-only action commands are not part of the real CLI surface.

## 0.1.0 - 2026-07-05

### Added
- First tag-driven release through GitHub Actions and PyPI Trusted Publisher.

## 0.0.1 - 2026-07-05

### Added
- Placeholder release for PyPI name registration.
