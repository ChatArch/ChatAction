import click
from click.testing import CliRunner

from chataction import __version__
from chataction.cli import main


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chataction, version {__version__}" in result.output


def test_help_mentions_tree_options():
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0, result.output
    assert "--tree" in result.output
    assert "Print the registered CLI tree and exit." in result.output
    assert "--tree-brief" in result.output
    assert "without parameter signatures" in result.output


def test_tree_shows_base_registered_surface_with_purposes():
    result = CliRunner().invoke(main, ["--tree"])

    assert result.exit_code == 0, result.output
    assert result.output.splitlines()[0] == "chataction"
    assert "--help  # Show this message and exit." in result.output
    assert "--version  # Show the version and exit." in result.output
    assert "--tree  # Print the registered CLI tree and exit." in result.output
    assert (
        "--tree-brief  # Print the registered CLI tree without parameter signatures and exit."
        in result.output
    )
    assert "#" in result.output


def test_tree_defaults_to_signatures_and_brief_omits_them():
    @click.command(name="inspect-action", help="Inspect one action.")
    @click.argument("action_id")
    @click.option("--format")
    def inspect_action(action_id: str, format: str | None) -> None:
        del action_id, format

    main.add_command(inspect_action)
    try:
        tree_result = CliRunner().invoke(main, ["--tree"])
        brief_result = CliRunner().invoke(main, ["--tree-brief"])
    finally:
        main.commands.pop("inspect-action", None)

    assert tree_result.exit_code == 0, tree_result.output
    assert brief_result.exit_code == 0, brief_result.output
    assert (
        "inspect-action <ACTION-ID> [--format FORMAT]  # Inspect one action."
        in tree_result.output
    )
    assert "inspect-action  # Inspect one action." in brief_result.output
    assert "<ACTION-ID>" not in brief_result.output
    assert "[--format FORMAT]" not in brief_result.output


def test_template_hello_command_is_not_registered():
    help_result = CliRunner().invoke(main, ["--help"])
    tree_result = CliRunner().invoke(main, ["--tree"])
    missing_result = CliRunner().invoke(main, ["hello"])

    assert help_result.exit_code == 0, help_result.output
    assert tree_result.exit_code == 0, tree_result.output
    assert "hello" not in help_result.output.lower()
    assert "hello" not in tree_result.output.lower()
    assert missing_result.exit_code != 0
    assert "No such command" in missing_result.output


def test_tree_root_uses_public_console_command_even_in_python_module_mode():
    result = CliRunner().invoke(main, ["--tree"], prog_name="python -m chataction.cli")

    assert result.exit_code == 0, result.output
    assert result.output.splitlines()[0] == "chataction"
    assert "python -m chataction.cli" not in result.output
