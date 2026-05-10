"""
数据结构.3.网编和多线程.4.一句话_客户端 的 Docstring

客户端开发流程:
1.创建客户端Socket对象,   ipv4,字节流(TCP)
2.连接服务器
3.接收服务器的消息并打印
4.发送消息
5.关闭Socket
"""


import socket

kehu_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

kehu_socket.connect(('127.0.0.1',8081))

ser_data = kehu_socket.recv(1024).decode('utf-8')
print(f"服务器:{ser_data}")

kehu_socket.send('你好'.encode('utf-8'))
print(f"客户端:你好")
kehu_socket.close()
