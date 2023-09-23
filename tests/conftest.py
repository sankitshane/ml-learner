from os import path
from unittest import mock

import pytest

FIXTURUE_PATH = path.join(path.dirname(__file__), "fixtures")


@pytest.fixture(scope="session")
def mock_url_without_cc():
    yield "https://www.youtube.com/watch?v=HBz4pBSIsXI"


@pytest.fixture(scope="session")
def mock_url_with_cc():
    yield "https://www.youtube.com/watch?v=Ad_TEk94B9Q"


@pytest.fixture(scope="session")
def mock_data():
    with open(path.join(FIXTURUE_PATH, "example.txt")) as f:
        yield f.read()

@pytest.fixture(scope='session')
def mock_json():
    with open(path.join(FIXTURUE_PATH, "json_output.json")) as f:
        yield f.read().encode('utf-8')


@pytest.fixture(scope='session')
def mock_xml():
    with open(path.join(FIXTURUE_PATH, "xml_output.xml"), 'rb') as f:
        yield f.read()


@pytest.fixture(scope="session")
def mock_dw_video():
    from athena.main import Downloader
    with mock.patch.object(Downloader, "download_video") as mock_dw_video:
        yield mock_dw_video


@pytest.fixture(scope="session")
def mock_dw_caption():
    from athena.main import Downloader
    with mock.patch.object(Downloader, "download_caption") as mock_dw_caption:
        yield mock_dw_caption


@pytest.fixture(scope="session")
def mock_ck_caption():
    from athena.main import Downloader
    with mock.patch.object(Downloader, "check_for_caption") as mock_ck_caption:
        yield mock_ck_caption


@pytest.fixture(scope="session")
def mock_del():
    from athena.main import Downloader
    with mock.patch.object(Downloader, "delete_video") as mock_del:
        mock_del.return_value = None
        yield mock_del


@pytest.fixture(scope="session")
def mock_cv_video():
    from athena.main import Converter
    with mock.patch.object(Converter, "speech_to_text") as mock_cv_video:
        yield mock_cv_video
