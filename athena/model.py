from pytube import YouTube
from transformers import pipeline


class Downloader:
    def download(self, url):
        yt = YouTube(url)

        # Get the highest quality audio stream
        audio_stream = yt.streams.filter(
            only_audio=True, file_extension="mp4").first()

        # Set the path where you want to save the audio file
        output_path = "downloads"

        # Download the audio
        audio_stream.download(output_path=output_path, filename="audio.mp4")


class Converter:
    def __init__(self):
        self.model = "facebook/wav2vec2-large-960h-lv60-self"

    def speech_to_text(self, path):
        pipe = pipeline(model = self.model)
        text = pipe(path, chunk_length_s=10) 
        return text
