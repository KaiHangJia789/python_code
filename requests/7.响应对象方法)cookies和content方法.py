"""         
    1.  cookies
        获取响应cookies信息
    2.  context
        以字节码形式获取响应信息(图片，视频)

案例:
    cookies:    http://www.baidu.com
    context:    https://image.baidu.com/search/detail?adpicid=0&b_applid=11877003518930197583&bdtype=0&commodity=&copyright=&cs=1479272385%2C1167922678&di=7607122379617075201&fr=click-pic&fromurl=http%253A%252F%252Fm.dianping.com%252Fugcdetail%252F273784980%253FsceneType%253D0%2526bizType%253D29%2526msource%253Dbaiduappugc&gsm=1e&hd=&height=0&hot=&ic=&ie=utf-8&imgformat=&imgratio=&imgspn=0&is=3286067455%2C2660678006&isImgSet=&latest=&lid=&lm=&objurl=https%253A%252F%252Fqcloud.dpfile.com%252Fpc%252F9f00zcH9AT1TekEAAduD2cHyla3jCrccg3zgHHI_eF6aKF3WiTGKFQQjvS4o_t_2.jpg&os=3286067455%2C2660678006&pd=image_content&pi=0&pn=0&rn=1&simid=3514996123%2C333181956&tn=baiduimagedetail&width=0&word=%E9%9D%92%E5%B2%9B&z=

"""

import requests

url = "http://www.baidu.com"
#r = requests.get(url)

url_2 = "https://image.baidu.com/search/detail?adpicid=0&b_applid=11877003518930197583&bdtype=0&commodity=&copyright=&cs=1479272385%2C1167922678&di=7607122379617075201&fr=click-pic&fromurl=http%253A%252F%252Fm.dianping.com%252Fugcdetail%252F273784980%253FsceneType%253D0%2526bizType%253D29%2526msource%253Dbaiduappugc&gsm=1e&hd=&height=0&hot=&ic=&ie=utf-8&imgformat=&imgratio=&imgspn=0&is=3286067455%2C2660678006&isImgSet=&latest=&lid=&lm=&objurl=https%253A%252F%252Fqcloud.dpfile.com%252Fpc%252F9f00zcH9AT1TekEAAduD2cHyla3jCrccg3zgHHI_eF6aKF3WiTGKFQQjvS4o_t_2.jpg&os=3286067455%2C2660678006&pd=image_content&pi=0&pn=0&rn=1&simid=3514996123%2C333181956&tn=baiduimagedetail&width=0&word=%E9%9D%92%E5%B2%9B&z="
r2 = requests.get(url_2)

# #获取响应cookies    返回字典对象
# print("cookies信息为:",r.cookies)
# #通过键名获取响应 cookies值
# print("cookies信息为:",r.cookies['BAIDUID'])

#以text文本形式解析图片
#print(r2.text)

#已字节形式解析图片
#print(r2.content)

with open ("./data.png",'wb') as f:
    f.write(r2.content)