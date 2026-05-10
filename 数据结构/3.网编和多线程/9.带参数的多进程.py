"""
数据结构.3.网编和多线程.9.带参数的多进程 的 Docstring

方式一:   args方式: 接受所有位置参数
方式二:  kwargs方式: 接受所有关键字参数
"""

import multiprocessing ,time

def coding(name,num):
    for i in range(1,num+1):
        time.sleep(0.2)
        print(f"{name}正在写第{i}行代码!")

def music(name,count):
    for i in range(1,count+1):
        time.sleep(0.2)
        print(f"{name}正在听第{i}首歌....")


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=coding,args=("小王",10))
    p2 = multiprocessing.Process(target=music,kwargs={'count':20,'name':'小李'})
    p1.start()
    p2.start()