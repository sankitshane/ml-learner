import json
from datetime import datetime, timedelta
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


@pytest.fixture(scope='session')
def mock_result():
    with open(path.join(FIXTURUE_PATH, "dummy_result.json"), 'rb') as f:
        data = json.loads(f.read().decode('utf-8'))
        curr = datetime.now()
        for key in data:
            data[key]["timestamp"] = curr.strftime("%Y-%m-%d %H-%M-%S")
            if key == "url_4":
                data[key]["timestamp"] = (curr - timedelta(days=11)).\
                    strftime("%Y-%m-%d %H-%M-%S")
        yield data


@pytest.fixture()
def mock_dw_video():
    from athena.main import Downloader
    with mock.patch.object(Downloader, "download_video") as mock_dw_video:
        yield mock_dw_video


@pytest.fixture()
def mock_dw_caption():
    from athena.main import Downloader
    with mock.patch.object(Downloader, "download_caption") as mock_dw_caption:
        yield mock_dw_caption


@pytest.fixture()
def mock_ck_caption():
    from athena.main import Downloader
    with mock.patch.object(Downloader, "check_for_caption") as mock_ck_caption:
        yield mock_ck_caption


@pytest.fixture()
def mock_del():
    from athena.main import Downloader
    with mock.patch.object(Downloader, "delete_video") as mock_del:
        mock_del.return_value = None
        yield mock_del


@pytest.fixture()
def mock_cv_video():
    from athena.main import Converter
    with mock.patch.object(Converter, "speech_to_text") as mock_cv_video:
        yield mock_cv_video


@pytest.fixture()
def mock_sm_video():
    from athena.main import Converter
    with mock.patch.object(Converter, "summarize") as mock_sm_video:
        yield mock_sm_video


@pytest.fixture()
def mock_save():
    from athena.main import Result
    with mock.patch.object(Result, "save_summary") as mock_save:
        yield mock_save


@pytest.fixture()
def mock_caption():
    with mock.patch("athena.main.get_caption") as mock_caption:
        yield mock_caption


@pytest.fixture()
def mock_json_load():
    import json
    with mock.patch.object(json, "load") as mock_load, \
            mock.patch.object(json, "dump") as mock_dump:
        mock_load.return_value = {"hello": "world"}
        mock_dump.return_value = 100
        yield mock_load, mock_dump


@pytest.fixture
def mock_open_file():
    # Create a mock for the 'open' function using mock_open
    mock_open = mock.mock_open()
    with mock.patch('builtins.open', mock_open):
        yield mock_open


@pytest.fixture
def mock_links():
    # Creating mock links for input
    with mock.patch("athena.main.links") as mock_links:
        yield mock_links
