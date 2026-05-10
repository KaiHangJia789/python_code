"""
数据结构.3.网编和多线程.10.获取进程的编号 的 Docstring

获取进程的编号: os.getpid()   multiprocessing.current_process().pid
获取父进程的编号: os.getppid()
"""

import multiprocessing ,time,os

def coding(name,num):
    for i in range(1,num+1):
        time.sleep(0.2)
        print(f"{name}正在写第{i}行代码!")
    print(f"p1 的进程编号: {os.getpid()},{multiprocessing.current_process().pid},父进程: {os.getppid()}")

def music(name,count):
    for i in range(1,count+1):
        time.sleep(0.2)
        print(f"{name}正在听第{i}首歌....")
    print(f"p2 的进程编号: {os.getpid()},{multiprocessing.current_process().pid},父进程: {os.getppid()}")


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=coding,args=("小王",10))
    p2 = multiprocessing.Process(target=music,kwargs={'count':20,'name':'小李'})
    p1.start()
    p2.start()
    print(f"main 的进程编号: {os.getpid()},{multiprocessing.current_process().pid},父进程: {os.getppid()}")