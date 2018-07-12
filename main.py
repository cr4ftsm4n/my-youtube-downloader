import requests
from urllib.parse import parse_qs
import shutil
import subprocess


# VID = "AQsAuvGIP9U"


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
    ids = []
    for item in resp.json()["items"]:
        id = item["contentDetails"]["videoId"]
        download_video(id)
        ids.append(id)
    for id in ids:
        upload_file("{}.mp4".format(id))

    with open("latest_id", 'w') as f:
        f.write(ids[0])
        upload_file("latest_id")


def download_video(id):
    resp = requests.get(
        "https://www.youtube.com/get_video_info?video_id={}".format(id))
    url = parse(resp.text)[0]
    res = requests.get(url, stream=True)  # video url
    res.raw.decode_content = True
    with open("{}.mp4".format(id), 'wb') as f:
        shutil.copyfileobj(res.raw, f)


def upload_file(fname):
    subprocess.run(
        ["gdrive", "--refresh-token", "1/_9dhEcE1SNwkdrIEQYrDpqtGsQXIelOuslJK7kNfCPM", "-p", "15mM7T3xvvhqfymg9OgWNJLgnwg3shzWn", "upload", fname])


if __name__ == "__main__":
    main()
