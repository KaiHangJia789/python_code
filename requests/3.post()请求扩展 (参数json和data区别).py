"""
案例:
    新增学院 ------用data 方式,不用json------
                  将字典转换为json字符串:
                  1.  导入json模块
                  2.  json.dumps(data)
参数:
    1.json: 传入json字符串
    2.headers: 传入请求信息头内容

响应:
    1.响应对象.json()


#json.dump()和 json.dumps()的区别:
    #json.dump()是将字典转换为json字符串,并写入文件
    #json.dumps()是将字典转换为json字符串,并返回字符串
"""
import requests
import json
#2.调用post

#定义url
url = 'http://127.0.0.1:8081/' #添加学院
#定义headers
headers = {"Content-Type":"application/json"} #告诉服务器，我发送的是json数据
#定义json
data = {
        "data":
                [{
                    "name":"信息工程学院",
                    "address":"北京",
                    "phone":"010-12345678"
                }]
       }
#使用json方式来新增学院-->成功
    #json=data: 传入json数据|| headers=headers: 传入请求头信息
#r = requests.post(url,json=data,headers=headers)

#使用data方式来新增学院-->失败
# r = requests.post(url,json=data,headers=headers)

#使用json.dumps()方法将字典转换为json字符串
r = requests.post(url,json=json.dumps(data),headers=headers)
#3.调获取响应对象
print(r.json())
#4.获取响应状态码
print(r.status_code)
