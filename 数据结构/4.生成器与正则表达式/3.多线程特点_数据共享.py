import threading,time

my_list = []

def write():
    for i in range(10):
        my_list.append(i)
        print(f"正在写入数据{i}")
    print(f"write中的数据{my_list}")

def read():
    time.sleep(2)
    print(f"read中的数据{my_list}")

if __name__ == '__main__':
    t1 = threading.Thread(target=write)
    t2 = threading.Thread(target=read)
    t1.start()
    t2.start()