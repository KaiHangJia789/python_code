"""
数据结构.4.生成器与正则表达式.11.property_类属性用法 的 Docstring

property类属性用法:
    类属性名 = property(获取值的函数名,设置值的函数名)

    之后就可以直接， 上述函数名， 来当做变量直接用

"""


class Student:
    def __init__(self):
        self.__age = 18

    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        self.__age = age

    #类属性名 = property(获取值的函数名,设置值的函数名)
    age = property(get_age,set_age)

if __name__ == '__main__':
    s = Student()
    print(s.age)
    s.age = 19
    print(s.age)
