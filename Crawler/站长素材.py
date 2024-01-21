import time
from urllib import request

import requests
from lxml import etree


def get_page(url):
    html = request.urlopen(url)
    tree = etree.HTML(html.read().decode("utf-8"))
    src = tree.xpath('//div/a[@target="_blank"]/img/@src')
    alt = tree.xpath('//div/a[@target="_blank"]/img/@alt')
    for i in range(0, len(src)):
        print(alt[i])
        content = requests.get("https:" + src[i]).content
        with open("D:/MyPython/MyProject_1/img/" + alt[i] + ".jpg", "wb") as file:
            file.write(content)
        file.close()


for i in range(1, 200):
    if i == 1:
        get_page("https://sc.chinaz.com/tupian/meishitupian.html")
    else:
        get_page(f"https://sc.chinaz.com/tupian/meishitupian_{i}.html")
