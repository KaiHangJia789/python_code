"""
数据结构.3.网编和多线程.4.一句话_客户端 的 Docstring

客户端开发流程:
1.创建客户端Socket对象,   ipv4,字节流(TCP)
2.连接服务器
3.关联数据源文件,读取数据,写给服务器
5.关闭Socket
"""


import socket

kehu_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

kehu_socket.connect(('127.0.0.1',8081))

with open(r"C:\Users\苏铭\Pictures\辉夜姬.png",'rb')as f:
    while True:
        data = f.read(8192)
        kehu_socket.send(data)
        if data== b'':
            break
    kehu_socket.shutdown(socket.SHUT_WR)
rev = kehu_socket.recv(1024).decode('utf-8')
print(f"服务器:{rev}")
kehu_socket.close()
