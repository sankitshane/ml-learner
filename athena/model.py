import youtube_dl
from pytube import YouTube
from transformers import pipeline


class Downloader:
    def download_video(self, url):
        yt = YouTube(url)

        # Get the highest quality audio stream
        audio_stream = yt.streams.filter(
            only_audio=True, file_extension="mp4").first()

        # Set the path where you want to save the audio file
        output_path = "downloads"

        # Download the audio
        audio_stream.download(output_path=output_path, filename="audio.mp4")

    def download_caption(self, url):
        options = {
            'writesubtitles': True,
            'allsubtitles': True,
            'skip_download': True,
        }
        video_caption = {"caption": []}
        with youtube_dl.YoutubeDL(options) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            if 'subtitles' in info_dict:
                for lang, captions in info_dict['subtitles'].items():
                    video_caption["lang"] = lang
                    for caption in captions:
                        video_caption["caption"].append(
                            f"Caption: {caption['ext']}, url: {caption['url']}"
                        )

        return video_caption


class Converter:
    def __init__(self):
        self.model = "facebook/wav2vec2-large-960h-lv60-self"

    def speech_to_text(self, path):
        pipe = pipeline(model=self.model)
        text = pipe(path, chunk_length_s=10)
        return text
