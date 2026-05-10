"""
数据结构.4.生成器与正则表达式.10.property_装饰器用法 的 Docstring

概述/目的/作用
    把函数当作变量来用
实现方式:
    方式一:  装饰器
    方式二:  类属性


property的装饰器用法:
    @property                  # 获取值的函数名
    @获取值的函数名.setter      # 设置值的函数名
    之后就可以直接  上述的函数名  来当变量直接用
"""


#需求:  定义学生类,私有属性 age  来通过property实现简化调用
#1.定义学生类
class Student: 
    def __init__(self,):
        
        self._age = 18

    #提供共有的访问方式
    @property
    def get_age(self):
        return self._age
    
    @get_age.setter
    def set_age(self, age):
        #可以在这里对传入的age值做判断，但一般不做，重要字段才做判断
        #因为实际开发中数据是从前端来的
        self._age = age


if __name__ == '__main__':
    stu = Student()
    print(stu.get_age)  #18


    stu.set_age = 20    #看似是属性，其实是调用了setter方法，
                        #是函数，提高代码安全性
    print(stu.get_age)  #20


