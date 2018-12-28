from urllib import request

url = 'https://www.douban.com/'

proxy = {'http':'121.232.148.196:9000'}

proxy_support = request.ProxyHandler(proxy)

opener = request.build_opener(proxy_support)

opener.addheaders = [('User-Agent', "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")]

request.install_opener(opener)

response = request.urlopen(url)

print(response.read().decode("utf-8"))

