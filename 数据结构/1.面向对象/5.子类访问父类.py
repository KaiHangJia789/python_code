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
    def __init__(self):
        self.kongfu = '[自创煎饼果子配方]'
    def make_moster_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

s = Student()
s.make_cake()
s.make_moster_cake()