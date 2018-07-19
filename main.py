import requests
from urllib.parse import parse_qs
import shutil
import subprocess
import os


# VID = "AQsAuvGIP9U"

REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")
PARENT = "1kzNSmD2lH880XbdsAOwV9oHwhDIMArkj"
YOUTUBE_API_KEY= os.getenv("YOUTUBE_API_KEY")


def parse(qs):
    d = parse_qs(qs)
    stream_list = d["url_encoded_fmt_stream_map"][0].split(',')
    d2 = parse_qs(stream_list[0])
    url = d2["url"]
    return url


def main():
    latest = ""
    record_file = "latest_id"
    with open(record_file, 'r') as f:
         latest = f.readline()
    if latest == "":
        print("can't get latest id, about exiting")
        return
    params = {
        "playlistId": "PLDYAvKPeZGgC1HGrJ-0oNftx5Ry9u0Nne",
        "part": "snippet,contentDetails",
        "key": YOUTUBE_API_KEY,
        "maxResults": "50",
    }
    resp = requests.get(
        "https://www.googleapis.com/youtube/v3/playlistItems", params=params)
    ids = []
    for item in resp.json()["items"]:
        id = item["contentDetails"]["videoId"]
        if id == latest.strip():
            break
        else:
            download_video(id)
            ids.append(id)
    for id in ids:
        upload_file("{}.mp4".format(id))

    with open(record_file, 'w') as f:
        f.write(ids[0])

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
        ["./gdrive-linux-x64", "upload", "--refresh-token", REFRESH_TOKEN, "-p", PARENT,  fname])


if __name__ == "__main__":
    main()
