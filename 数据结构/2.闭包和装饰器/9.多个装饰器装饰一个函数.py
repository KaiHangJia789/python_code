"""
数据结构.闭包和装饰器.9.多个装饰器装饰一个函数 的 Docstring

记忆:
    多个装饰器装饰一个函数,是按照由内到外的顺序来装饰的
    但如果用 装饰器的写法，看到的效果是:从上往下执行的
"""

#需求: 发表评论前,要先登录,在验证验证码,

def check_login(fn_name):
    def fn_inner():
        print("登录中.. ")
        fn_name()
    return fn_inner

def check_code(fn_name):
    def fn_inner():
        print("验证码验证中.. ")
        fn_name()
    return fn_inner

@check_login
@check_code
def comment():
    print("发表评论")

if __name__ == '__main__':
    comment()