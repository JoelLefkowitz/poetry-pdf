import pytest


@pytest.fixture
def the_raven() -> str:
    with open("tests/fixtures/the_raven.txt", "r") as stream:
        return stream.read()
