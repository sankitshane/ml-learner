import json
import os

from model import Downloader

result_file_name = "result/result.json"
video_urls = [
    "https://www.youtube.com/watch?v=TWdGj-Im5gg",
    "https://www.youtube.com/watch?v=UYk-gXv2-wc"
]


if not os.path.exists(result_file_name):
    result = dict()
else:
    result = json.load(open(result_file_name))


def process():
    client = Downloader()

    for url in video_urls:
        result[url] = None

    json.dump(result, open(result_file_name, 'w'), indent=4)
