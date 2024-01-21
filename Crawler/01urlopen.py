import urllib.request

response = urllib.request.urlopen('https://www.python.org')
# print(type(response))
# print("-------------")
# print(response.read().decode('utf-8'))
# print("-------------")
print(response.status)
print("-------------")
print(response.getheaders())
print("-------------")
print(response.getheader('Server'))


















