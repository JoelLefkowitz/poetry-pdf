from typing import Any
from poetry_pdf.builder import prepare_html
from bs4 import BeautifulSoup
import re
from typing import List


def test_insert_stylesheets() -> None:
    stylesheets = ["styles.css"]
    html = prepare_html(
        title="", author="", plaintext_lines="", stylesheets=stylesheets
    )

    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("link", href=True)
    link_hrefs = [link["href"] for link in links]
    assert link_hrefs == stylesheets


def test_insert_plaintext(the_raven: str) -> None:
    plaintext_lines = the_raven.splitlines()
    html = prepare_html(
        title="", author="", plaintext_lines=plaintext_lines, stylesheets=[],
    )

    # Allows both group1 and group2 in <br>group1<br>group2<br>
    ends_in_break = r"(<br>)*?([^<>\n]+)(<br>)"

    # match.groups()[1] gives us only what ([^<>\n]+) captures
    split_lines = [match.groups()[1] for match in re.finditer(ends_in_break, html)]
    assert format_lines(split_lines) == format_lines(plaintext_lines)


def format_lines(lines: List[str]) -> List[str]:
    return [line.lstrip() for line in lines if not line.isspace() and not line == ""]
