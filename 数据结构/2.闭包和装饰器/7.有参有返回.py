"""
数据结构.闭包和装饰器.4.装饰器(有参有返回) 的 Docstring

细节:
    装饰器的内部函数格式,要和被装饰的原函数 保持一致
    即: 参数列表,返回值类型,函数体 都要一致
"""

#定义装饰器
def my_decorator(fn_name):
    def fn_inner(x,y):
        print("正在努力计算中")
        return fn_name(x,y)
    return fn_inner
#定义原函数
@my_decorator
def get_sum(a,b):
    sum = a+b
    return sum


if __name__ == '__main__':
    result = get_sum(10,20)
    print(f"result={result}")