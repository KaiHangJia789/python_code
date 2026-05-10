"""
    目标:响应对象常用方法
        1. encoding
            1). 获取请求编码
            2). 设置响应编码
        2. headers
            1). 获取响应信息头信息
    案例:
        http://www.baidu.com

"""

import requests

url = "http://www.baidu.com"

r = requests.get(url)

#1.查看默认请求编码
print(r.encoding)

#1-2. 设置响应编码
r.encoding='utf-8'

#2.查看响应内容 text形式
print(r.text)

#3. 查看响应信息头     一般服务器返回的token/session相关信息都在headers中
print(r.headers)