from input import links
from model import Converter, Downloader, Result


def get_caption(url):
    downloader = Downloader()
    if not downloader.check_for_caption(url):
        downloader.download_video(url)
        caption = Converter().speech_to_text()
        downloader.delete_video()
    else:
        caption = downloader.download_caption()

    return caption


def process():
    result = Result()
    for url in links():
        caption = get_caption(url)
        summary = Converter().summarize(caption)
        result.save_summary(url, summary, Converter().summarize_model)
