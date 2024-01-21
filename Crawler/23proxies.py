import requests

proxies = {
    "http": "http://user:password@10.10.1.10:3128/"

}
response = requests.get("https://www.taobao.com", proxies=proxies)
print(response.text)


















