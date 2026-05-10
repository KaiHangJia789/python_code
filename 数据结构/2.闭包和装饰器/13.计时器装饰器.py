import time

#实现计时器装饰器
def calc_time(fun_c):
    def fuction(*args,**kwargs):
        start_time = time.time()#开始计时
        result = fun_c(*args,**kwargs)  #执行原函数,将执行结果（返回值）存到result
        end_time = time.time()  #计时结束
        cha_time= round(end_time-start_time,2)#记录执行所用时间,round(x,2):x保留两位小数
        print(f"函数{fun_c.__name__}执行完成用时{cha_time}")
        return result   #是调用者能拿到和原函数一样的返回值
    return fuction

#无参测试
@calc_time
def text1():
    time.sleep(0.1)#休眠0.1秒，模拟任务执行
    print("登录任务执行完成.")

@calc_time
def text2(user_id,order_type,page=1):
    time.sleep(0.2)
    print(f"查询用户:{user_id},订单:{order_type},第{page}页")

if "__main__"==__name__:
    text1()
    text2("suming","pay",3)

