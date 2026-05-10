"""
数据结构.面向对象.7.封装_私有属性 的 Docstring

class Student:
    def :__init__(self)
    self._b = 2
"""

class Master:
    def __init__(self):
        self.kongfu = '[传统煎饼果子配方]'
        self.__money = 1000
    def make_cake(self):
        print(f"使用{self.kongfu}制作煎饼果子")

    def get_money(self):
       return self.__money
    
    def set_money(self,money):
        self.__money = money

class Student:
    pass

if __name__ == '__main__':
    