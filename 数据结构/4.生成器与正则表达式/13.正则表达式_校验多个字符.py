import re

result = re.match('\.it','.it')#匹配成功

result = re.match('[ahg]it','ait')#匹配成功
result = re.match('[ahg]it','a it')#匹配失败

result = re.match('[^ahg]it','ait')#匹配失败
result = re.match('[^ahg]it','a it')#匹配失败
result = re.match('[^ahg]it','bit')#匹配成功
result = re.match('[^ahg]it','acbit')#匹配失败

result = re.match('[1-7]it','3it')#匹配成功
result = re.match('[1-7]it','-it')#匹配失败



if result:
    print(f"匹配成功:   result.group()")
else:
    print('匹配失败')