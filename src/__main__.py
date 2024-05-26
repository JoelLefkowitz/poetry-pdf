#!/usr/bin/env python
import os
from .builder import build
from .cli import parse_cli


def entrypoint() -> None:
    source_path, output_dir, author, stylesheets = parse_cli()
    filename = os.path.splitext(os.path.basename(source_path))[0]

    output_path = os.path.join(output_dir, filename + ".pdf")
    title = filename.replace("_", " ").title()

    with open(source_path, "r", encoding="utf8") as stream:
        plaintext_lines = stream.read().splitlines()

    if not stylesheets:
        stylesheets = [
            os.path.normpath(os.path.join(__file__, "../styles/default.css"))
        ]

    build(
        output_path,
        title,
        author,
        plaintext_lines,
        stylesheets,
    )


if __name__ == "__main__":
    entrypoint()
