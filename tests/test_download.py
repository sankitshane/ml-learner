import os

def test_download_audio_file(mock_url):
    # Testing audio file download given a audio file.

    from athena.model import Downloader

    downloader = Downloader()
    downloader.download_video(mock_url)

    assert os.path.exists('downloads/audio.mp4')


def test_download_caption(mock_url):
    # Testing downloading cc from a youtube video

    from athena.model import Downloader

    downloader = Downloader()
    caption = downloader.download_caption(mock_url)

    assert type(caption) is dict
