"""
案例:
    新增学院

参数:
    1.json: 传入json字符串
    2.headers: 传入请求信息头内容

响应:
    1.响应对象.json()

json()与text()
json()方法: 获取响应数据json形式 类型:dict 可以通过键名来获取数据
text()方法: 获取响应数据text形式 类型:str  可以通过索引来获取数据
"""
import requests

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
    #json=data: 传入json数据|| headers=headers: 传入请求头信息
r = requests.post(url,json=data,headers=headers)
#3.调获取响应对象

#获取响应数据json形式
print("r.json()--->")
print(r.json())     #类型:dict

#获取响应数据text形式
print("r.text--->")
print(r.text)       #类型:str
#4.获取响应状态码
print(r.status_code)