"""
|       匹配左右任意一个表达式
(ab)    将括号中的字符作为一个分组
\num    引用分组num匹配到的字符串


|        表示或者的意思
()       表示 分组 从左往右数 第几个左括号(,就表示第几组
\num      引用分组num匹配到的字符串

扩展:
    (?P<分组名>...)   命名分组
    (?P=分组名)       引用命名分组
    """

import re

html_s = "<html><h1>我是html页面</h1></html>"

result = re.match(r'<[a-zA-Z]{1,4}><h[1-6]>.*</h[1-6]></[a-zA-Z]{1,4}>',html_s)

#引入分组概念
result = re.match(r'<([a-zA-Z]{1,4})><(h[1-6])>.*</\2></\1>',html_s)
#给分组起名
result = re.match(r'<(?P<A>[a-zA-Z]{1,4})><(?P<B>h[1-6])>.*</(?P=B)></(?P=A)>',html_s)

if result:
    print(result.group())
else:
    print("匹配失败")