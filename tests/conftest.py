import pytest


@pytest.fixture(scope="session")
def mock_url():
    yield "https://www.youtube.com/watch?v=HBz4pBSIsXI"
