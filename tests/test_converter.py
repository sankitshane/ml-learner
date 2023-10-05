import os


def test_convert_speech_to_text():
    from athena.model import Converter

    converter = Converter()
    path = "tests/fixtures/audio.mp4"
    text = converter.speech_to_text(path)
    assert type(text) is str


def test_download_and_convert(mock_url_without_cc):
    # Testing downloading and converting it into cc

    from athena.model import Converter, Downloader

    downloader = Downloader()
    downloader.download_video(mock_url_without_cc)

    path = "static/audio.mp4"
    assert os.path.exists(path) is True

    converter = Converter()
    text = converter.speech_to_text(path)
    assert type(text) is str

    downloader.delete_video(path)
    assert os.path.exists(path) is False


def test_summarise(mock_data):
    # Testing summarise function

    from athena.model import Converter

    summarised_data = Converter().summarize(mock_data)
    assert summarised_data is not None
    assert type(summarised_data) is dict
