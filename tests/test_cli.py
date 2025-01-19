from click.testing import CliRunner
from nextstep.cli import cli


def test_generate_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["generate", "Build authentication system"])
    assert result.exit_code == 0
    assert "Generating tasks for: Build authentication system" in result.output
