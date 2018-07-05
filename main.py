import requests
from urllib.parse import parse_qs
import shutil


VID = "tk2AXB3wf9s"


def parse(qs):
    d = parse_qs(qs)
    stream_list = d["url_encoded_fmt_stream_map"][0].split(',')
    d2 = parse_qs(stream_list[0])
    url = d2["url"]
    return url


def main():
    resp = requests.get("https://www.youtube.com/get_video_info?video_id={}".format(VID))
    url = parse(resp.text)[0]
    res = requests.get(url)  # video url
    with open("{}.mp4".format(VID), 'wb') as file:
        # res.raw.decode_content = True
        shutil.copyfileobj(res.raw, file)


if __name__ == "__main__":
    main()
