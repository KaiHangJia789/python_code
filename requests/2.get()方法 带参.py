"""
获取百度首页
     https://www.baidu.com?id=1001
     https://www.baidu.com?id=1001,1002
     https://www.baidu.com?id=1001&kw=北京
请求:
    get()方法

参数:
    params: 字典或字符串 (推荐使用字典)

响应：
    2. 响应对象.url  # 获取响应的URL
    3. 响应对象.status_code  # 获取响应的状态码
    4. 响应对象.encoding  # 获取响应的编码方式
    5. 响应对象.text  # 获取响应的文本内容

"""

import requests

url = "https://www.baidu.com"

#案例1:  定义字典
#params = {"id":1001}

#案例2:  定义多参
#params = {"id":"1001,1002"} #   ,   转义是  %2c

#案例3:  定义不同参数
params = {"id":"1001","kw":"北京"}  #   &   转义是  %26

#请求的是带参params
r = requests.get(url,params=params)  #r:响应对象

#3.获取请求url地址
print("url--->",r.url)
# #4.获取响应的状态码
# print("status_code--->",r.status_code)

# #5.获取响应的编码方式
# print("encoding--->",r.encoding)

# #6.获取响应的文本内容
# print("text--->",r.text)


