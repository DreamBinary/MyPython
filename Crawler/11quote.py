import urllib.request
from urllib.parse import quote

keyword = "哈哈"
url = "http://www.baidu.com/s?wd=" + quote(keyword)
print(url)

response = urllib.request.urlopen(url)
print(response.read().decode("utf-8"))


















