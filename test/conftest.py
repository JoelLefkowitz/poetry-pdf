import pytest
import sys

sys.path.append("..")


@pytest.fixture
def the_raven() -> str:
    with open("test/the_raven.txt", "r", encoding="utf8") as stream:
        return stream.read()
