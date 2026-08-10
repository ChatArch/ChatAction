from click.testing import CliRunner

from chataction import __version__
from chataction.cli import main


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chataction, version {__version__}" in result.output


def test_help_mentions_tree_option():
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0, result.output
    assert "--tree" in result.output
    assert "Print the registered command tree" in result.output


def test_tree_shows_base_registered_surface_with_purposes():
    result = CliRunner().invoke(main, ["--tree"])

    assert result.exit_code == 0, result.output
    assert "chataction  # ChatAction action orchestration CLI." in result.output
    assert "--help  # Show this help message." in result.output
    assert "--version  # Show the installed package version." in result.output
    assert "--tree  # Print the registered command tree." in result.output
    assert "#" in result.output


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
