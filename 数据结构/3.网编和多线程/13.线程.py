"""
数据结构.3.网编和多线程.13.线程 的 Docstring

python想要实现多任务处理 除了使用进程 还可以使用线程
进程:
    分配资源的基本单位 一旦创建一个进程就会分配一定的资源
线程:
    CPU调度资源的基本单位,每个进程至少有一个线程 
"""

import threading
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
    p1 = threading.Thread(target=coding)
    p2 = threading.Thread(target=reading)
    p1.start()
    p2.start()