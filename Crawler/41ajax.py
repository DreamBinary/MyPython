from urllib.parse import urlencode
from pyquery import PyQuery as pq

import requests

base_url = "https://m.weibo.cn/api/container/getIndex?"

header = {
    "Host": "m.weibo.cn",
    "Referer": "https://m.weibo.cn/u/2830678474",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56",
    "X-Requested-With": "XMLHttpRequest"
}


def get_page(page):
    params = {
        "type": "uid",
        "value": "1076032830678474",
        "page": page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=header)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print("error", e.args)


def parse_page(json):
    if json:
        items = json.get("data").get("cards")
        for item in items:
            item = item.get("mblog")
            weibo = {}
            weibo["id"] = item.get("id")
            weibo["text"] = pq(item.get("text")).text()
            weibo["attitudes"] = item.get("attitudes_count")
            weibo["comments"] = item.get("comments_count")
            weibo["reports"] = item.get("reposts_count")
            yield weibo


def main():
    for page in range(1, 11):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)


main()