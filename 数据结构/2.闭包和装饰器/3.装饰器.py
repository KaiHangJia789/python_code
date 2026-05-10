"""
数据结构.闭包和装饰器.3.装饰器 的 Docstring

装饰器的作用:
    在不改变原有函数的基础上,给原有函数增加额外功能
    装饰其本身就是一个闭包函数
装饰器的构成条件:
    1.有嵌套
    2.有引用
    3.有返回
    4.有额外功能
装饰器的用法:
    1: 传统写法:
        装饰后的函数名 = 装饰器名(被装饰的原函数名)
        装饰后的函数名()
    
    2:语法糖:
        在要被装饰的原函数上,直接写@装饰器名,之后直接调用原函数即可
"""

#在评论前线检验登录

def check_login(fn_name):
    def fn_inner():
        print("登录中.. ")
        fn_name()
    return fn_inner


def comment():
    print("发表评论")

@check_login
def payment():
    print("充值中..")

#测试
#1.传统方式
fn = check_login(comment)
fn()
print('*'*50)
#2.语法糖
payment()