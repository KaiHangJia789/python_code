"""
^ 匹配字符串开头
$ 表示结尾

"""

import re
#要求必须是以数字为开头,无论match(),还是search()

result = re.match(r"\d+.*",'ab123abc')       #匹配失败
result = re.search(r"\d+.*",'ab123abc')      #匹配成功

result = re.match(r"^\d+.*",'abc123abc')     #匹配失败
result = re.search(r"^\d+.*",'abc123abc')    #匹配失败

#要求二:字符串必须以数字开头，任意三个字母结尾
result = re.match(r"^\d+[a-zA-Z]{3}$",'123abc')     #匹配成功
result = re.match(r"^\d+[a-zA-Z]{3}$",'123abcd')    #匹配失败
result = re.match(r"^\d+.*[a-zA-Z]{3}$",'123abcd')  #匹配成功







print(result.group() if result else '匹配失败')
