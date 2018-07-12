import requests
from urllib.parse import parse_qs
import shutil


VID = "AQsAuvGIP9U"


def parse(qs):
    d = parse_qs(qs)
    stream_list = d["url_encoded_fmt_stream_map"][0].split(',')
    d2 = parse_qs(stream_list[0])
    url = d2["url"]
    return url


def main():
    params = {
        "playlistId": "PLDYAvKPeZGgC1HGrJ-0oNftx5Ry9u0Nne",
        "part": "snippet,contentDetails",
        "key": "AIzaSyCyLSmcEDJt3HaLFK0_LdJYPkq0RFAVzKA",
        "maxResults": "50",
    }
    resp = requests.get(
        "https://www.googleapis.com/youtube/v3/playlistItems", params=params)
    print(resp.text)


def download_video():
    resp = requests.get(
        "https://www.youtube.com/get_video_info?video_id={}".format(VID))
    url = parse(resp.text)[0]
    res = requests.get(url, stream=True)  # video url
    res.raw.decode_content = True
    with open("{}.mp4".format(VID), 'wb') as f:
        shutil.copyfileobj(res.raw, f)


if __name__ == "__main__":
    main()
