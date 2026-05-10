"""
数据结构.4.生成器与正则表达式.1.多线程特点_随机性 的 Docstring

多线程特点:
    1.线程执行具有随机性,原因是因为CPU在做高效的切换
    2.默认情况下,主线程会等待子线程结束在结束
    3.线程之间数据共享
    4.多线程操作共享数据,可能会出现安全问题,可以用 互斥锁解决

CPU调度资源的策略:
    1.均分时间片
    2.抢占式调度
"""

import threading
import time

def print_info():
    time.sleep(0.2)
    threading_1 = threading.current_thread()
    print(threading_1.name)

if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=print_info)
        t.start()