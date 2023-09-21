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
