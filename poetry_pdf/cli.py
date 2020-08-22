import os
import sys
from inspect import cleandoc
from typing import List, Optional, Tuple

from docopt import DocoptExit  # type: ignore
from docopt import docopt

from .exceptions import InvalidCommand, InvalidSourcePath

docopts_cli = cleandoc(
    """
    Usage:
        poetry-pdf <source_path> 
                   [--output-dir=<output_dir>]
                   [--author=<author>]
                   [--stylesheet=<stylesheet>]... 
    """
)


def parse_cli() -> Tuple[str, str, Optional[str], List[str]]:
    try:
        cli_arguments = docopt(docopts_cli)
    except DocoptExit:
        raise InvalidCommand(sys.argv[1:], docopts_cli)

    source_path = cli_arguments["<source_path>"]

    if not os.path.exists(source_path):
        raise InvalidSourcePath(source_path)

    output_dir = (
        cli_arguments["--output-dir"]
        if cli_arguments["--output-dir"]
        else os.getcwd()
    )
    
    author = cli_arguments["--author"]

    stylesheets = cli_arguments["--stylesheet"]
    return source_path, output_dir, author, stylesheets
