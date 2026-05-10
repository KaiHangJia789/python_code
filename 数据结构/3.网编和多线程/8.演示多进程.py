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
    p2 = multiprocessing.Process(target=reading)
    p1.start()
    p2.start()