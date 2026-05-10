"""
数据结构.面向对象.9.类方法与静态方法 的 Docstring

类方法：
类方法与静态方法区别：
1.类方法有@classmethod 装饰器
2.类方法有cls参数
3.类方法有类属性
4.类方法有类方法
5.类方法有静态方法    第一个参数必须是类对象

静态方法与类方法区别：
1.静态方法有@staticmethod 装饰器
2.静态方法没有cls参数
3.静态方法没有类属性
4.静态方法没有类方法
5.静态方法有静态方法

"""

#定义学生类
class Student:
    #类属性
    name = '小王'
    #类方法
    @classmethod
    def show1(cls):
        print(cls.name)
        print("我是类方法")

    #静态方法
    @staticmethod
    def show2():
        print(Student.name)
        print("我是静态方法")


if __name__ == '__main__':
    #创建对象
    s = Student()
    #调用类方法
    s.show1()
    #调用静态方法
    s.show2()
