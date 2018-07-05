import requests
from urllib.parse import parse_qs

VID = "tk2AXB3wf9s"


def parse(qs):
    d = parse_qs(qs)
    stream_list = d["url_encoded_fmt_stream_map"][0].split(',')
    d2 = parse_qs(stream_list[0])
    url = d2["url"]
    print(url[0])


def main():
    resp = requests.get("https://www.youtube.com/get_video_info?video_id={}".format(VID))
    parse(resp.text)


if __name__ == "__main__":
    main()
