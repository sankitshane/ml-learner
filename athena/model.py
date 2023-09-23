import json
import os
import xml.etree.ElementTree as ET

import requests
import youtube_dl
from pytube import YouTube
from transformers import pipeline


class Downloader:
    def __init__(self):
        self.cc_url = None
        self.cc_file_type = None

    def delete_video(self, path="result/audio.mp4"):
        os.remove(path)

    def download_video(self, url):
        yt = YouTube(url)

        # Get the highest quality audio stream
        audio_stream = yt.streams.filter(
            only_audio=True, file_extension="mp4").first()

        # Set the path where you want to save the audio file
        output_path = "result"

        # Download the audio
        audio_stream.download(output_path=output_path, filename="audio.mp4")

    def convert_xml(self, binary):
        xml_text = binary.decode('utf-8')
        root = ET.fromstring(xml_text)
        sentences = []
        for child in root:
            if child.tag == 'text' and child.text:
                sentences.append(child.text)

        return sentences

    def convert_json(self, binary):
        json_text = json.loads(binary.decode('utf-8'))
        sentences = []

        for child in json_text["events"]:
            for seg in child['segs']:
                if "utf8" in seg:
                    sentences.append(seg['utf8'])

        return sentences

    def download_caption(self):
        response = requests.get(self.cc_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Get the content of the response
            file_content = response.content

            if self.cc_file_type == "srv":
                text = self.convert_xml(file_content)
            elif self.cc_file_type == 'json':
                text = self.convert_json(file_content)

        return " ".join(text)

    def check_for_caption(self, url):
        cc_link = dict()
        with youtube_dl.YoutubeDL() as ydl:
            info_dict = ydl.extract_info(url, download=False)
            if "en" in info_dict['subtitles']:
                english_cc = info_dict['subtitles']['en']
                for cc_file in english_cc:
                    if cc_file['ext'].startswith('json'):
                        cc_link["json"] = cc_file['url']
                    elif cc_file['ext'].startswith('srv2'):
                        cc_link['srv'] = cc_file['url']

                if "json" in cc_link:
                    self.cc_file_type = "json"
                    self.cc_url = cc_link['json']
                elif 'srv' in cc_link:
                    self.cc_file_type = "srv"
                    self.cc_url = cc_link['srv']

        return self.cc_url is not None


class Converter:
    def __init__(self):
        self.model = "facebook/wav2vec2-large-960h-lv60-self"

    def speech_to_text(self, path="result/audio.mp4"):
        pipe = pipeline(model=self.model)
        text = pipe(path, chunk_length_s=10)
        return text['text']
