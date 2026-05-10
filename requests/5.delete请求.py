"""
案例:
    删除数据

参数:
    1.json: 传入json字符串
    2.headers: 传入请求信息头内容

响应:
    1.响应对象.json()

    响应状态码:
        204

put方法:
    作用:
        修改数据
    应用:
        requests.put()
        
        例子:
        requests.put(url,json=data,headers=headers)
"""
import requests

#2.调用post

#定义url
url = 'http://127.0.0.1:8081/id/' #添加学院

r = requests.delete(url)
#4.获取响应状态码
print(r.status_code)