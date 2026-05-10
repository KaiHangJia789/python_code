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

#需求:在列表fruits = ['apple', 'orange', 'banana', 'watermelon'] 匹配 apple banana

fruits = ['apple', 'orange', 'banana', 'watermelon']

for fruit in fruits:
    if re.match('(apple|banana)',fruit):
        print(f"喜欢吃:     {fruit}")

    else:
        print(f"不喜欢吃:   {fruit}")
