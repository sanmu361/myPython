import urllib.request

response = urllib.request.urlopen('http://www.netbian.com/desk/21421-1920x1080.htm')


print(response.read().decode('gbk'))

print("test1")

request = urllib.request.Request("http://www.baidu.com")
response = urllib.request.urlopen(request)

print(response.read().decode("utf-8"))