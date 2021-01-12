import sys
from typing import List
from unittest.mock import patch

import pytest
from poetry_pdf.cli import parse_cli
from poetry_pdf.exceptions import InvalidCommand
from poetry_pdf.exceptions import InvalidSourcePath


@pytest.mark.parametrize(
    "argv",
    [
        ["poetry-pdf", "tests/fixtures/the_raven.txt"],
        ["poetry-pdf", "tests/fixtures/the_raven.txt", "--output-dir", "."],
        ["poetry-pdf", "tests/fixtures/the_raven.txt", "--author", "Joel Lefkowitz"],
    ],
)
def test_parse_cli_valid_command(argv: List[str]) -> None:
    with patch.object(sys, "argv", argv):
        parse_cli()


def test_parse_cli_invalid_command() -> None:
    argv = ["poetry-pdf", "tests/fixtures/the_raven.txt", "123"]
    with patch.object(sys, "argv", argv), pytest.raises(InvalidCommand):
        parse_cli()


def test_parse_cli_invalid_source() -> None:
    argv = ["poetry-pdf", "tests/fixtures/not_the_raven.txt"]
    with patch.object(sys, "argv", argv), pytest.raises(InvalidSourcePath):
        parse_cli()


def test_parse_multiple_stylesheets() -> None:
    argv = [
        "poetry-pdf",
        "tests/fixtures/the_raven.txt",
        "--stylesheet",
        "sheet1",
        "--stylesheet",
        "sheet2",
    ]
    with patch.object(sys, "argv", argv):
        stylesheets = parse_cli()[3]
        assert stylesheets == ["sheet1", "sheet2"]
