from os import path

import pytest

FIXTURUE_PATH = path.join(path.dirname(__file__), "fixtures")


@pytest.fixture(scope="session")
def mock_url_without_cc():
    yield "https://www.youtube.com/watch?v=HBz4pBSIsXI"


@pytest.fixture(scope="session")
def mock_url_with_cc():
    yield "https://www.youtube.com/watch?v=Ad_TEk94B9Q"


@pytest.fixture(scope='session')
def mock_text():
    with open(path.join(FIXTURUE_PATH, "json_output.txt")) as f:
        yield f


@pytest.fixture(scope='session')
def mock_xml():
    with open(path.join(FIXTURUE_PATH), "xml_output.xml") as f:
        yield f
