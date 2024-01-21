import re

import requests


def get_one_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"

    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def main(page):
    url = f"https://ssr1.scrape.center/page/{page}"
    html = get_one_page(url)
    pattern_name = re.compile("class=\"m-b-sm\">(.*?)</h2>")
    items_name = re.findall(pattern_name, html)
    for name in items_name:
        print(name)


for i in range(1, 11):
    main(i)
