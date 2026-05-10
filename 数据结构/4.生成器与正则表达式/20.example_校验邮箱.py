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

#需求:  匹配163,126,qq等邮箱,       数字下划线字母[4-20]@域名.com
import re

yx = "abcff@163.com"

result = re.match(r'^[a-zA-Z_0-9]{4,20}@(163|162|qq)\.com$',yx)
if result:
    print(f"合法邮箱为:     {result.group()}")
    print(f"合法邮箱为:     {result.group(0)}")#获取第0组信息,即整个数据
    print(f"合法邮箱为:     {result.group(1)}")#获取第1组信息,即qq

else:
    print("非法邮箱")