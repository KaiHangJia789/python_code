"""
*        正则校验多个字符
?          匹配前面的字符零次或一次
+          匹配前面的字符一次或多次
{n}         恰好匹配前面的字符n次
{n,}        至少匹配前面的字符n次
{n,m}       匹配前面的字符至少n次,至多m次
|          匹配前面的一个或多个模式，或者匹配后面的一个或多个模式
"""


import re

result = re.match(r'.*hm.*','abchm123')  #匹配成功
result = re.match(r'.*hm.*','hm1234')    #匹配成功
result = re.match(r'.*hm.*','abchm')     #匹配成功

result = re.match(r'.+hm.*','abchm')     #匹配成功
result = re.match(r'.+hm.*','hm123')     #匹配失败

result = re.match(r'.?hm.*','ahm123')    #匹配成功
result = re.match(r'.?hm.*','hm123')     #匹配成功
result = re.match(r'.?hm.*','abchm1234') #匹配失败

result = re.match(r'\d{3}hm\w{2,5}','123hm1234') #匹配成功
result = re.match(r'\d{3}hm\w{2,5}','1234hm1234')#匹配失败
result = re.match(r'\d{3}hm\w{2,5}','12hm1234')  #匹配失败
result = re.match(r'\d{3}hm\w{2, 5}','12hm1234') #匹配失败,注意空格

print(f"匹配成功:{result.group()}" if result else '匹配失败') 