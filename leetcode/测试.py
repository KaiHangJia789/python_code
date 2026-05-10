import requests
import json

# 改用公共测试接口（能打印你的请求内容并返回）
url = 'https://httpbin.org/post'  # 这个接口会原样返回你发送的所有请求信息
headers = {"Content-Type":"application/json"}

data = {
    "data": [{
        "dep_id": "TT702",
        "dep_name": "Test学院",
        "master_name": "Test-Master",
        "slogan": "Here is Slogan"
    }]
}

# 不管你用 json=data 还是 data=json.dumps(data)，都能看到请求发出
# 写法1：json 参数
r = requests.post(url, json=data, headers=headers)

# 写法2：data 参数（如果你要测试这种方式，注释上面一行，取消下面注释）
# r = requests.post(url, data=json.dumps(data), headers=headers)

# 打印响应（能看到请求是否成功发出，以及接口接收到的内容）
print("==== 响应状态码（200=请求成功发出） ====")
print(r.status_code)
print("\n==== 接口接收到的你的请求内容 ====")
# 格式化输出，看得更清楚
print(json.dumps(r.json(), indent=2, ensure_ascii=False))