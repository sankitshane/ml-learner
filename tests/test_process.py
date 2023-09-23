import json
import os


def test_input_video_urls():
    # Testing the input is a list of urls

    from athena.main import video_urls

    assert type(video_urls) is list


def test_process_video_1_by_1():
    # Testing processing one video at a time

    from athena.main import process, video_urls

    process()

    assert os.path.exists('result/result.json')
    result = json.load(open('result/result.json'))
    assert type(result) is dict

    for url in video_urls:
        assert url in result


def test_cc_common_format(mock_url_with_cc):
    # Testing both downloaded cc and video to text have common format
    from athena.model import Downloader, Converter

    downloader = Downloader()
    downloader.download_video(mock_url_with_cc)

    path = "result/audio.mp4"
    assert os.path.exists(path) is True

    converter = Converter()
    cc_video_text = converter.speech_to_text(path)

    downloader.delete_video(path)
    
    caption_available = downloader.check_for_caption(mock_url_with_cc)
    cc_download_text = downloader.download_caption()

    assert type(cc_video_text) is str
    assert type(cc_download_text) is str
