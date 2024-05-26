import pytest
import sys
from src.cli import parse_cli
from src.exceptions import InvalidCommand, InvalidSourcePath
from typing import List
from unittest.mock import patch


@pytest.mark.parametrize(
    "argv",
    [
        ["poetry-pdf", "test/the_raven.txt"],
        ["poetry-pdf", "test/the_raven.txt", "--output-dir", "."],
        ["poetry-pdf", "test/the_raven.txt", "--author", "Joel Lefkowitz"],
    ],
)
def test_parse_cli_valid_command(argv: List[str]) -> None:
    with patch.object(sys, "argv", argv):
        parse_cli()


def test_parse_cli_invalid_command() -> None:
    argv = ["poetry-pdf", "test/the_raven.txt", "123"]
    with patch.object(sys, "argv", argv), pytest.raises(InvalidCommand):
        parse_cli()


def test_parse_cli_invalid_source() -> None:
    argv = ["poetry-pdf", "test/not_the_raven.txt"]
    with patch.object(sys, "argv", argv), pytest.raises(InvalidSourcePath):
        parse_cli()


def test_parse_multiple_stylesheets() -> None:
    argv = [
        "poetry-pdf",
        "test/the_raven.txt",
        "--stylesheet",
        "sheet1",
        "--stylesheet",
        "sheet2",
    ]
    with patch.object(sys, "argv", argv):
        stylesheets = parse_cli()[3]
        assert stylesheets == ["sheet1", "sheet2"]
