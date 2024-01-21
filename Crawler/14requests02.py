import requests

data = {
    "name": "germey",
    "age": 22
}
r = requests.get("http://httpbin.org/get", params=data)
print(r.text)
print("------------")
print(type(r))
print("------------")
print(r.json())


















