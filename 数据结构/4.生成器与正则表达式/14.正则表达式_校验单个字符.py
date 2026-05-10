""" 
re.match()# 匹配字符串的开始
re.search()# 匹配字符串的任意位置
re.compile()# 编译正则表达式,并返回

\d表示[0-9]         .*表示任意字符(可0个,可多个)
"""

import re
result = re.search("\d.*","city:sfjsfisj2.shenzhen")

if result:
    print(f"匹配成功:   result.group()")

else:
    print('匹配失败')