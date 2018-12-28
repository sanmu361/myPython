import urllib.request as url_re

header={'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

url='https://www.douban.com/'

request = url_re.Request(url,headers= header)

response=url_re.urlopen(request)

print(response.read().decode('utf-8'))