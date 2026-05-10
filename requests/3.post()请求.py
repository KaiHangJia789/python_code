"""
案例:
    新增学院

参数:
    1.json: 传入json字符串
    2.headers: 传入请求信息头内容

响应:http://127.0.0.1:4523/m2/7786353-7532992-default/425794843
    1.响应对象.json()
"""
import requests

# 2.调用post
# 定义url
url = '/m2/7786353-7532992-default/425794843'  # 添加学院
# 定义headers
headers = {"Content-Type":"application/json"}  # 告诉服务器，我发送的是json数据
# 定义json
data = {
    {
    "data": [
        {
            "name":"信息工程学院",
            "address": "北京",
            "phone": "010-12345678"
        }
    ]
}
}
# 修正缩进：和上一行保持一致，避免IndentationError
r = requests.post(url, json=data, headers=headers)

# 3.获取响应对象
print(r.json())

# 4.可选：打印响应状态码，验证请求是否成功
print("响应状态码：", r.status_code)