"""
re.match('正则表达式', '要匹配的字符串')# 匹配字符串的开始
re.search('正则表达式','要匹配的字符')# 匹配字符串的任意位置
re.compile('正则表达式').sub('替换后的内容','要被替换的字符串')# 编译正则表达式,并返回

result.group()  # 获取匹配成功的内容
"""


import re

s = '开心就大声笑,哈哈,嘿嘿,呵呵,桀桀桀,啦啦啦'

result = re.compile('哈|嘿|呵|桀').sub('❤️',s)

print(result)
print('-'*50)

#新的API的写法
#参一: 正则表达式, 参二:新的内容,  参三: 要被替换的字符串
result = re.sub('哈|嘿|呵|桀','❤️',s)
print(result)