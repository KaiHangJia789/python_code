import threading
import time

def coding(name,num):
    for i in range(1,num):
        time.sleep(0.2)
        print(f"{name}正在写第{i}行代码!")

def reading(name,count):
    for i in range(1,count):
        time.sleep(0.2)
        print(f"{name}正在读第{i}行书.....")

if __name__ == '__main__':
    p1 = threading.Thread(target=coding,args=('李湘',10))
    p2 = threading.Thread(target=reading,kwargs={'name':'张三','count':10})
    p1.start()
    p2.start()