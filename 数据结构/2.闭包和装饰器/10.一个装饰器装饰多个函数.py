"""
数据结构.闭包和装饰器.10 的 Docstring

需求: 定义一个既能装饰减法又能装饰加法的装饰器

装饰器只能有一个参数
"""

def logging(flag):
    def decorator(fn_name):
        def fn_inner(a,b):
            if flag == '+':
                print("正在进行加法...")
            elif flag == '-':
                print("正在进行减法...")
            return fn_name(a,b)
        return fn_inner
    return decorator

@logging('+')
def add(a,b):
    return a + b

@logging('-')
def sub(a,b):
    return a-b

if __name__ == '__main__':
    print(add(1,2))
    print(sub(1,2))