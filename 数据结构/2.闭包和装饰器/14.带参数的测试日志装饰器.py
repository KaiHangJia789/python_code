
def text_log(level):
    def outer(fun_c):
        def inter(*args,**kwargs):
            print(f"{level}测试用例{fun_c.__name__}:开始执行")
            if level=="info":
                