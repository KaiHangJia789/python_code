"""
数据结构.3.网编和多线程.5.文件上传_服务端 的 Docstring

1.创建服务端Socket对象
    2.绑定IP+端口
    3.设置最大监听数
    4.等待客户端连接
    5.给客户端发送消息
    6.读取客户上传的文件数据,写到目的地文件中
    7.释放资源
"""
import socket
# 1.创建服务端Socket对象,   ipv4,字节流(TCP)
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     2.绑定IP+端口
server_socket.bind(('127.0.0.1',8081))
#     3.设置最大监听数
server_socket.listen(5)
#     4.等待客户端连接
accept_socket,client_info = server_socket.accept()
count = 1
with open('./data/picture_'+'str(count)'+'.png','wb')as f:
    while True:
        
        bys = accept_socket.recv(8192)
        if bys ==b'':
            break
             
        f.write(bys)
accept_socket.send('文件上传成功'.encode('utf-8'))
#server_socket.close()#服务器端一般不关闭
#     7.释放资源
accept_socket.close()
#扩展:设置端口号重用,目的shi:快速重启服务器(服务器关闭后,立即释放端口)
#参一:当前的套接字对象,     参二:选项名,    参三:该选项的值
# server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)