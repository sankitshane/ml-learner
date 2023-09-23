import json
import os
from datetime import datetime

from model import Converter, Downloader

result_file_name = "result/result.json"
video_urls = [
    "https://www.youtube.com/watch?v=TWdGj-Im5gg",
    "https://www.youtube.com/watch?v=UYk-gXv2-wc"
]


if not os.path.exists(result_file_name):
    result = dict()
else:
    result = json.load(open(result_file_name))


def get_caption(url):
    downloader = Downloader()
    if not downloader.check_for_caption(url):
        print("no caption")
        downloader.download_video(url)
        caption = Converter().speech_to_text()
        downloader.delete_video()
    else:
        print("caption exists")
        caption = downloader.download_caption()

    return caption


def save_summary(url, summary, model):
    if url not in result:
        result[url] = dict()

    result[url]["summary"] = summary
    result[url]["model"] = model
    result[url]["timestamp"] = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

    json.dump(result, open(result_file_name, 'w'), indent=4)


def process():
    for url in video_urls:
        caption = get_caption(url)
        summary = Converter().summarize(caption)
        save_summary(url, summary, Converter().summarize_model)

    json.dump(result, open(result_file_name, 'w'), indent=4)
