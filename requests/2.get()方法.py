"""
获取百度首页
    "https://www.baidu.com"
请求:
    get()方法

响应：
    2. 响应对象.url  # 获取响应的URL
    3. 响应对象.status_code  # 获取响应的状态码
    4. 响应对象.encoding  # 获取响应的编码方式
    5. 响应对象.text  # 获取响应的文本内容

"""

import requests

url = "https://www.baidu.com"
r = requests.get(url)  #r:响应对象

#3.获取请求url地址
print("url--->",r.url)
#4.获取响应的状态码
print("status_code--->",r.status_code)

#5.获取响应的编码方式
print("encoding--->",r.encoding)

#6.获取响应的文本内容
print("text--->",r.text)


