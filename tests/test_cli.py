from click.testing import CliRunner

from chataction import __version__
from chataction.cli import main


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chataction, version {__version__}" in result.output
