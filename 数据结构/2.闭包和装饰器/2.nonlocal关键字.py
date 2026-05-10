"""
数据结构.闭包和装饰器.2.nonlocal关键字 的 Docstring

nonlocal 关键字:
    nonlocal 关键字用于实现 在内部函数中 修改外部函数的变量

global  关键字: 
    global 关键字用于实现 在内部函数中 修改全局变量
"""

def fn_outer():
    a = 100
    def fn_inner():
        nonlocal a
        a +=1
        print(a)
    return fn_inner
    

if __name__ == '__main__':
    fn_inner = fn_outer()
    fn_inner()#101
    fn_inner()#102
    fn_inner()#103
    

