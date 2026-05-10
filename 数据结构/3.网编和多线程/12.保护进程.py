"""

默认情况下,主进程会等待子进程执行结束在结束
如果要设置主进程结束时,子进程同步已结束
思路一:
    设置主进程为守护进程,当主进程结束的时候,守护进程会结束
    p1.daemon = True
思路二:
    强制关闭子进程
    p1.terminate()  (不推荐)
"""

import multiprocessing
import time

def coding():
    for i in range(1,11):
        time.sleep(0.2)
        print(f"正在写第{i}行代码!")

def reading():
    for i in range(1,11):
        time.sleep(0.2)
        print(f"正在读第{i}行书.....")

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=coding)
    
    p1.daemon = True
    p1.start()
    time.sleep(1)
    print("主进程结束")
    