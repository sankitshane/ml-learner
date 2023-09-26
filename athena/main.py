from datetime import datetime, timedelta

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
        if url in result.value:
            renew = False
            if result.value[url]["model"] == Converter().summarize_model:
                renew = True

            last_pull = datetime.strptime(
                result.value[url]["timestamp"],
                "%Y-%m-%d %H-%M-%S"
            )
            if last_pull < datetime.now() - timedelta(days=10):
                renew = True

            if renew:
                continue

        caption = get_caption(url)
        summary = Converter().summarize(caption)
        result.save_summary(url, summary, Converter().summarize_model)


if __name__ == "__main__":
    process()
