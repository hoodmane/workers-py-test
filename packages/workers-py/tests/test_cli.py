"""Tests for the pywrangler CLI."""

from click.testing import CliRunner

from pywrangler.cli import app


def test_help() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Pywrangler" in result.output


def test_version() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "pywrangler" in result.output


def test_sync_command() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["sync"])
    assert result.exit_code == 0


def test_types_command() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["types"])
    assert result.exit_code == 0


def test_info_command() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["info"])
    assert result.exit_code == 0
    assert "pywrangler version" in result.output
    assert "workers-runtime-sdk version" in result.output
