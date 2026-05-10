"""
数据结构.3.网编和多线程.1.创建socket对象 的 Docstring

网络编程介绍:
    网络编程也叫网络通信,Socket通信,即:通信双方都有自己的socket对象
    数据在socket之间通过,数据报包(UPC协议) 或者 字节流(TPC协议)的形式进行传输
"""


import socket

# 创建socket对象
#参1: Address Family, AF_INET: ipv4, AF_INET6: ipv6
#参2: Socket Type, Socket类型,即:TCP或UDP,
#    默认值:SOCK_STREAM: TCP, SOCK_DGRAM: UDP
socket_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(socket_obj)