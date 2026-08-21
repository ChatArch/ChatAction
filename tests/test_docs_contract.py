from pathlib import Path


def test_mkdocs_material_i18n_public_domain_and_icon_renderer():
    mkdocs = Path("mkdocs.yml").read_text(encoding="utf-8")
    pyproject = Path("pyproject.toml").read_text(encoding="utf-8")

    assert "site_url: https://arch.gh.wzhecnu.cn/ChatAction/" in mkdocs
    assert "repo_url: https://github.com/ChatArch/ChatAction" in mkdocs
    assert "name: material" in mkdocs
    assert "- i18n:" in mkdocs
    assert "docs_structure: suffix" in mkdocs
    assert "mkdocs-static-i18n" in pyproject
    assert '"chatstyle>=0.2.0,<0.3.0"' in pyproject
    assert '"chatenv>=0.2.10,<0.3.0"' in pyproject
    assert "pymdownx.emoji" in mkdocs
    assert "material.extensions.emoji.twemoji" in mkdocs
    assert "material.extensions.emoji.to_svg" in mkdocs


def test_cli_tree_docs_are_bilingual_and_use_public_command():
    zh = Path("docs/cli-tree.md").read_text(encoding="utf-8")
    en = Path("docs/cli-tree.en.md").read_text(encoding="utf-8")

    assert "chataction --tree" in zh
    assert "chataction --tree" in en
    assert "chataction --tree-brief" in zh
    assert "chataction --tree-brief" in en
    assert "python -m chataction.cli" not in zh
    assert "python -m chataction.cli" not in en
