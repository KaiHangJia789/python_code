"""
数据结构.闭包和装饰器.12.浅拷贝操作可变类型 的 Docstring

浅拷贝:
    copy.copy() #   import copy

深拷贝:
    copy.deepcopy()

深浅拷贝主要针对可变类型来讲:
    深拷贝拷贝所有层(可变)
    浅拷贝只拷贝第一层(可变)

可变类型:
    列表
    字典
    集合
不可变类型:
    数字
    字符串
    布尔值
    元组
"""

import copy

def dm01_普通赋值():
    #python中的赋值，属于引用赋值(把a的地址复制给b)
    #b是a的别名，b和a指向相同的地址
    a=10
    b=a
    print('id(a)-->',id(a))# id(a)--> 0x01
    print('id(b)-->',id(b))# id(b)--> 0x01

    #列表的赋值，属于引用赋值
    a = [1,2,3]
    b = [11,22,33]
    c = [a,b]
    d = c
    print('id(c)-->',id(c))# id(c)--> 0x02
    print('id(d)-->',id(d))# id(d)--> 0x02


def dm02_浅拷贝可变类型():
    #列表的浅拷贝，只拷贝第一层
    a = [1,2,3]
    b = [11,22,33]
    c = [6,7,a,b]
    d = copy.copy(c)
    print('id(c)-->',id(c))# id(c)--> 0x02
    print('id(d)-->',id(d))# id(d)--> 0x03
    print("id(c)和id(d)的值不一样,说明浅拷贝第一层")

    #测试二
    print('id(c[2])--->',id(c[2]))# id(c[2])---> 0x04
    print('id(a)-->',id(a))       # id(a)--> 0x04
    print("id(c[2])和id(a)的值一样,说明浅拷贝第二层的数据")

    #修改a[2]=22
    a[2]=22
    print('id(c)-->',c) # id(c)--> [6, 7, 22, [11, 22, 33]]
    print('id(d)-->',d) # id(d)--> [6, 7, 22, [11, 22, 33]]

def dom03_浅拷贝不可变类型():
    """
    深浅拷贝对于不可变类型的用法和普通赋值一样

    """
    a = (1,2,3)#0x01
    b = (11,22,33)#0x02
    c = (6,7,a,b)#0x03
    d = copy.copy(c)

    print('id(c)-->',id(c))## id(c)--> 0x03
    print('id(d)-->',id(d))# id(d)--> 0x03


def dm04_深拷贝_可变类型():
    """
    深拷贝拷贝所有层(可变)
    """
    a = [1,2,3]#0x01
    b = [11,22,33]#0x02
    c = [6,7,a,b]#0x03
    d = copy.deepcopy(c)

    print('id(c)-->',id(c))# id(c)--> 0x03
    print('id(d)-->',id(d))# id(d)--> 0x04

    a[1] = 100
    b[1] = 200
    print(f"c:{c}")# c:[6, 7, [1, 100, 3], [11, 200, 33]]
    print(f"d:{d}")# d:[6, 7, [1, 2, 3], [11, 22, 33]]

def dm05_深拷贝_不可变类型():
    """
    深拷贝对于不可变类型的用法和普通赋值一样
    """
    a = (1,2,3)#0x01
    b = (11,22,33)#0x02
    c = (6,7,a,b)#0x03
    d = copy.deepcopy(c)

    print('id(c)-->',id(c))# 0x03
    print('id(d)-->',id(d))# 0x03
if __name__ == '__main__':
    dm01_普通赋值()
    print('-'*30)
    dm02_浅拷贝可变类型()
    print('-'*30)
    dom03_浅拷贝不可变类型()
    print('-'*30)
    dm04_深拷贝_可变类型()
    print('-'*30)
    dm05_深拷贝_不可变类型()