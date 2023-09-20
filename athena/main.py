import os
import json
from model import Downloader

video_urls = [
    "https://www.youtube.com/watch?v=TWdGj-Im5gg",
    "https://www.youtube.com/watch?v=UYk-gXv2-wc"
]

if not os.path.exists("result/result.json"):
    result = dict()
else:
    result = json.load(open("result/result.json")) 

def process():
    client = Downloader()

    for url in video_urls:
        result[url] = None

    json.dump(result, open("result/result.json", 'w'), indent=4)
