import requests

r = requests.get('http://www.baidu.com')


# requests.post()
# requests.put()
# requests.delete()
# requests.head()
# requests.options()

# 参数：
# 	 Headers：字典形式的头文件信息数据包
# 	 Cookies：字典或者CookieJar对象形式数据包
# 	 Files：字典形式多部分编码上传，类似于“name“：文件类似于对象”或者{“name”:文件元祖}
# 	 auth：身份验证元组,允许基本/精华/自定义HTTP身份验证
# 	 timeout：设置等待服务发送数据的时间
# 	 allow_redirects：布尔形式。允许/拒绝 GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD 重定向。默认为“TRUE”
# 	 proxies：字典形式的URL代理映射协议。
# 	 verify：SSL证书是否需要验证。CA_BUNDLE路径也可以提供。默认为“TRUE”。
# 	 stream：如果为False，就立即下载响应内容。
# 	 cert：如果为字符串，则传入SSL客户机证书文件路径（.pem）。如果为元祖，则使用（“证书”，“关键词”）方式


print(type(r))

print(r.status_code)

print(r.encoding)

print(r.cookies)