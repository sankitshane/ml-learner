import json
import os


def test_input_video_urls():
    # Testing the input is a list of urls

    from athena.main import video_urls

    assert type(video_urls) is list


def test_process_video_1_by_1(mock_caption, mock_sm_video):
    # Testing processing one video at a time
    mock_caption.return_value = "dummy"
    mock_sm_video.return_value = "dummy summary"

    from athena.main import process, video_urls
    path = 'result/result.json'
    process()

    assert os.path.exists(path)
    result = json.load(open(path))
    assert type(result) is dict

    for url in video_urls:
        assert url in result


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


def test_save_summary(mock_url_without_cc):
    # Testing saving the generated summary in result

    from athena.main import save_summary

    path = 'result/result.json'
    summary = "Dummy summary of the video"
    model = "facebook/cnn"
    save_summary(mock_url_without_cc, summary, model)

    assert os.path.exists(path)
    result = json.load(open(path))
    assert type(result[mock_url_without_cc]) is dict
    assert result[mock_url_without_cc]["summary"] == summary
    assert result[mock_url_without_cc]["model"] == model
    assert "timestamp" in result[mock_url_without_cc]
    assert result[mock_url_without_cc]["timestamp"] is not None
