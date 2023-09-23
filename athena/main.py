from datetime import datetime

from model import Converter, Downloader, Result

video_urls = [
    "https://www.youtube.com/watch?v=TWdGj-Im5gg",
    "https://www.youtube.com/watch?v=UYk-gXv2-wc"
]


result = Result()


def get_caption(url):
    downloader = Downloader()
    if not downloader.check_for_caption(url):
        downloader.download_video(url)
        caption = Converter().speech_to_text()
        downloader.delete_video()
    else:
        caption = downloader.download_caption()

    return caption


def save_summary(url, summary, model):
    res = result.value
    if url not in res:
        res[url] = dict()

    res[url]["summary"] = summary
    res[url]["model"] = model
    res[url]["timestamp"] = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

    result.value = res


def process():
    for url in video_urls:
        caption = get_caption(url)
        summary = Converter().summarize(caption)
        save_summary(url, summary, Converter().summarize_model)
