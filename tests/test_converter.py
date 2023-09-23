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

    path = "result/audio.mp4"
    assert os.path.exists(path) is True

    converter = Converter()
    text = converter.speech_to_text(path)
    assert type(text) is str

    downloader.delete_video(path)
    assert os.path.exists(path) is False
