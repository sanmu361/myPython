import urllib.request as url_re
import urllib.parse as url_pa

post_data={'username':'admin','password':'123456'}
url = "http://www.baidu.com"

data = url_pa.urlencode(post_data)

request=url_re.Request(url)

response = url_re.urlopen(request,data.encode('utf-8'))

print(response.read().decode('utf-8'))

