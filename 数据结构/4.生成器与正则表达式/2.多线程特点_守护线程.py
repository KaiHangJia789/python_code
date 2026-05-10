"""
数据结构.4.生成器与正则表达式.2.多线程特点_守护线程 的 Docstring
"""
import threading
import time

def work():
    for i in range(10):
        time.sleep(0.2)
        print(f"正在执行任务{i}...")

if __name__ == "__main__":
    t = threading.Thread(target=work,daemon=True)
    
    t.start()
    time.sleep(1)
    print("主线程结束")