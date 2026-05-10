#1.定义师傅类
class Master:
    def __init__(self):
        self.kongfu = '[传统煎饼果子配方]'

    def make_cake(self):
        print(f"使用{self.kongfu}制作煎饼果子")

#2.定义学校类
class School:
    def init__(self):
        self.kongfu = '[学校煎饼果子配方]'

    def make_cake(self):
        print(f"使用{self.kongfu}制作煎饼果子")

#3.定义徒弟类
class Student(Master,School):
    pass

s = Student()
s.make_cake()
print('-'*50)

#mro 方法:method resolution order   方法解析顺序
print(Student.mro())
print(Student.__mro__)