class text(object):#object是python3中所有类的父类
    def __init__(self,name):
        self.name = name
    def __or__(self, other):
        return MySequence(self,other)    

    def __str__(self):
        return self.name
    
class MySequence(object):
    def __init__(self,*args):
        self.sequence = []
        for i in args:
            self.sequence.append(i)

    def __or__(self, other):
        self.sequence.append(other)
        return self

    def run(self):#运行这个序列
        for i in self.sequence:
            print(i)

    
if __name__ == "__main__":
    a = text("a")
    b = text("b")
    c = text("c")
    d = text("d")
    e = text("e")
    result = a | b | c | d | e
    result.run()
