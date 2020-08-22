import os
from typing import List, Optional

import pdfkit
from jinja2 import Environment, FileSystemLoader, StrictUndefined

from .utils import parent_dirs_exist, create_parent_dirs


def prepare_html(
    title: str,
    author: Optional[str],
    plaintext_lines: List[str],
    stylesheets: List[str],
) -> str:

    env = Environment(
        loader=FileSystemLoader(
            os.path.normpath(os.path.join(__file__, "../templates/"))
        ),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
        undefined=StrictUndefined,
    )

    render_context = {
        "title": title,
        "author": author,
        "plaintext_lines": plaintext_lines,
        "stylesheets": stylesheets,
    }

    return env.get_template("template.html").render(render_context)


def build(
    output_path: str,
    title: str,
    author: Optional[str],
    plaintext_lines: List[str],
    stylesheets: List[str],
) -> None:
    html = prepare_html(title, author, plaintext_lines, stylesheets)
    
    options = {
        "--enable-local-file-access": ""
    }

    if not parent_dirs_exist(output_path):
        create_parent_dirs(output_path)

    pdfkit.from_string(html, output_path, css=stylesheets, options=options)
