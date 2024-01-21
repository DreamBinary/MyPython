import requests
from pyquery import PyQuery as pq

url = "https://www.zhihu.com/explore"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
html = requests.get(url, headers=headers).text
doc = pq(html)
print(doc)
items1 = doc(".css-1nd7dqm").items()

for item in list(items1):
    print("ok")
    topic = item.text()
    file = open("explore.txt", "a", encoding="utf8")
    file.write(topic + "\n")
    file.write("\n" + "=" * 50 + "\n")
    file.close()

print("ooo")
