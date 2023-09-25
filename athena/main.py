from model import Converter, Downloader, Result

video_urls = [
    "https://www.youtube.com/watch?v=TWdGj-Im5gg",
    "https://www.youtube.com/watch?v=UYk-gXv2-wc"
]


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
    for url in video_urls:
        caption = get_caption(url)
        summary = Converter().summarize(caption)
        result.save_summary(url, summary, Converter().summarize_model)
