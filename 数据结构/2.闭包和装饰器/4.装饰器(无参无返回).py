"""
数据结构.闭包和装饰器.4.装饰器(无参无返回) 的 Docstring

细节:
    装饰器的内部函数格式,要和被装饰的原函数 保持一致
    即: 参数列表,返回值类型,函数体 都要一致
"""

#定义装饰器
def my_decorator(fn_name):
    def fn_inner():
        print("正在努力计算中")
        fn_name()
    return fn_inner
#定义原函数
@my_decorator
def get_sum():
    a=10
    b=20
    sum = a+b
    print(f"sum={sum}")


if __name__ == '__main__':
    get_sum()