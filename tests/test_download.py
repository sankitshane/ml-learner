import os

def test_download_audio_file():
    # Testing audio file download given a audio file.

    from athena.model import Downloader

    url = "https://www.youtube.com/watch?v=IDB_3S1ezsc"
    downloader = Downloader()
    downloader.download(url)

    assert os.path.exists('downloads/audio.mp4')
