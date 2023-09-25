import os


def test_input_video_urls():
    # Testing the input is a list of urls

    from athena.input import links

    assert type(links()) is list


def test_process_video_1_by_1(mock_caption, mock_sm_video, mock_save):
    # Testing processing one video at a time
    mock_caption.return_value = "dummy"
    mock_sm_video.return_value = "dummy summary"
    mock_save.return_value = None

    from athena.input import links
    from athena.main import process
    video_urls = links()
    process()

    assert mock_caption.call_count == len(video_urls)
    assert mock_sm_video.call_count == len(video_urls)
    assert mock_save.call_count == len(video_urls)


def test_cc_common_format(mock_url_with_cc):
    # Testing both downloaded cc and video to text have common format
    from athena.model import Converter, Downloader

    downloader = Downloader()
    downloader.download_video(mock_url_with_cc)

    path = "result/audio.mp4"
    assert os.path.exists(path) is True

    converter = Converter()
    cc_video_text = converter.speech_to_text(path)

    downloader.delete_video(path)

    downloader.check_for_caption(mock_url_with_cc)
    cc_download_text = downloader.download_caption()

    assert type(cc_video_text) is str
    assert type(cc_download_text) is str


def test_download_needed(mock_url_without_cc, mock_dw_video,
                         mock_cv_video, mock_del):
    # Testing video download only when cc is not present
    mock_cv_video.return_value = "dummy"

    from athena.main import get_caption

    caption = get_caption(mock_url_without_cc)
    assert type(caption) is str
    assert mock_dw_video.call_count == 1
    assert mock_cv_video.call_count == 1


def test_download_not_needed(mock_dw_caption, mock_url_with_cc):
    # Testing video download only when cc is not present
    mock_dw_caption.return_value = "dummy"

    from athena.main import get_caption

    caption = get_caption(mock_url_with_cc)
    assert type(caption) is str
    assert mock_dw_caption.call_count == 1
