"""
数据结构.闭包和装饰器.11 的 Docstring

需求: 定义一个既能装饰减法又能装饰加法的装饰器

装饰器只能有一个参数
"""


def decorator(fn_name):
    def fn_inner(a,b):
        if fn_name.__name__ == 'add':
                print("正在进行加法...")
        elif fn_name.__name__ == 'sub':
                print("正在进行减法...")
        return fn_name(a,b)
    return fn_inner


@decorator
def add(a,b):
    return a + b

@decorator
def sub(a,b):
    return a-b

if __name__ == '__main__':
    print(add(1,2))
    print(sub(1,2))