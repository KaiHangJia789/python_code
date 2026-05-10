"""
数据结构.4.生成器与正则表达式.4.多线程共享全局变量的问题 的 Docstring

累加次数不够

产生原因:
    线程一还没来得及执行完，线程二抢走了资源
解决方案:
    互斥锁

使用方法:
lock = threading.Lock() 创建锁
lock.acquire() 获取锁,使用锁
lock.release() 释放锁,开锁
"""

import threading

global_num = 0
lock = threading.Lock()
def work1():
    global global_num
    lock.acquire()
    for i in range(1000000):
       
        global_num += 1
    print(f"线程一执行了{global_num}次")
    lock.release()
        
def  work2():
    global global_num
    lock.acquire()
    for i in range(1000000):
        global_num += 1
    print(f"线程二执行了{global_num}次")
    lock.release()

if __name__ == "__main__":
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)
    t1.start()
    t2.start()
    
    

