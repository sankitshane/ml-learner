from pytube import YouTube

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
