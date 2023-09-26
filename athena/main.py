from datetime import datetime, timedelta

from input import links
from log import logger
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
        logger.debug(f"Working on url: {url}")
        if url in result.value:
            logger.debug(f"url: {url} already present in DB")
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
                logger.debug(
                    f"url: {url} can't be summarised yet as its cached"
                )
                continue

        caption = get_caption(url)
        summary = Converter().summarize(caption)
        result.save_summary(url, summary, Converter().summarize_model)


if __name__ == "__main__":
    logger.debug("Start process ...")
    process()
