import re
from bs4 import BeautifulSoup
from src.builder import prepare_html
from typing import List


def test_insert_stylesheets() -> None:
    stylesheets = ["styles.css"]

    html = prepare_html(
        title="",
        author="",
        plaintext_lines="",
        stylesheets=stylesheets,
    )

    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("link", href=True)
    link_hrefs = [link["href"] for link in links]
    assert link_hrefs == stylesheets
