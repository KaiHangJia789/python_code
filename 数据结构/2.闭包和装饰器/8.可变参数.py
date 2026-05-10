#定义一个可以计算多个数据和字典value值和的函数,并给其友好提示


#1.定义装饰器
def my_decorator(fn_name):
    def fn_inner(*args,**kwargs):
        print("正在努力计算中")
        return fn_name(*args,**kwargs)
    return fn_inner
#2.定义原函数
@my_decorator
def get_sum(*args,**kwargs):
    """
    get_sum 的 Docstring
    
    :param args:  数字元组 *args->接收所有的位置参数，并封装到 元组
    :param kwargs: 字典 **kwargs->接收所有的关键字参数，并封装到 字典
    return:结束之和
    """
    # sum = 0
    # for i in args:  # 遍历元组
    #     sum += i
    #     print(f"正在计算{i}")             #kwarg.key 获取字典所有key
    # for i in kwargs.values():  # 遍历字典 #kwargs.values() 获取字典所有value值
    #     sum += i                         #kwargs.items() 获取字典所有key-value值
    # return sum
    #优化
    return sum(args) + sum(kwargs.values())


if __name__ == '__main__':
   
    # sum = get_sum(1,2,3,a=4,b=5,c=6)
    # print(sum)
    result = get_sum(1,2,3,a=4,b=5,c=6)
    print(f"result={result}")


                                  