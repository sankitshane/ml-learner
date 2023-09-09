import os


def test_download_audio_file(mock_url_without_cc):
    # Testing audio file download given a audio file.

    from athena.model import Downloader

    downloader = Downloader()
    downloader.download_video(mock_url_without_cc)

    assert os.path.exists('downloads/audio.mp4')


def test_download_caption(mock_url_with_cc):
    # Testing downloading cc from a youtube video

    from athena.model import Downloader

    downloader = Downloader()
    caption_available = downloader.check_for_caption(mock_url_with_cc)

    if caption_available:
        caption = downloader.download_caption()
        assert caption is not None
        assert type(caption) is str


def test_caption_is_present(mock_url_without_cc, mock_url_with_cc):
    # Testing that caption is present in the video

    from athena.model import Downloader

    downloader = Downloader()
    is_caption_available = downloader.check_for_caption(mock_url_without_cc)

    assert is_caption_available is False

    is_caption_available = downloader.check_for_caption(mock_url_with_cc)

    assert is_caption_available is True
