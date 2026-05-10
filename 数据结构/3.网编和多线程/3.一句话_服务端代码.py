"""
┌─────────────────────────────────────────────────────────────┐
│ 服务器端（被动等待）                          客户端（主动发起） │
├─────────────────────────┐                   ┌─────────────────┤
│ 1. socket() 创建监听套接字 │                   │ 1. socket() 创建客户端套接字 │
│ 2. bind() 绑定IP+端口     │                   │ 2. connect() 发起连接      │
│ 3. listen() 开始监听       │◄──────────────────┤ （触发TCP三次握手）        │
│ 4. accept() 阻塞等待连接  │───────────────────►│ 3. 连接建立                │
│ 5. 生成“专属交互套接字”   │                   │                           │
│ 6. recv() 接收客户端数据  │◄──────────────────┤ 4. send() 发送请求数据     │
│ 7. send() 发送应答数据    │──────────────────►│ 5. recv() 接收应答数据     │
│ ...（循环交互）...        │                   │ ...（循环交互）...         │
│ 8. close() 关闭套接字      │◄──────────────────┤ 6. close() 关闭套接字      │
└───────────────────────────┘                   └─────────────────┘

服务器端给客户端发送消息,客户端给出回执信息
服务器开发流程:
    1.创建服务端Socket对象
    2.绑定IP+端口
    3.设置最大监听数
    4.等待客户端连接
    5.给客户端发送消息
    6.接收客户端的信息并打印
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
while True:
    accept_socket,client_info = server_socket.accept()
    #     5.给客户端发送消息
    accept_socket.send(b'hello world')  #b的意思:转成二进制
    print("客户端:hello world")
    #     6.接收客户端的信息并打印  编码:encode,解码:decode
    data = accept_socket.recv(1024).decode('utf-8')
    print(f"服务端收到 来自{client_info}的信息: {data}")
    #     7.释放资源
    accept_socket.close()
    #server_socket.close()#服务器端一般不关闭

#扩展:设置端口号重用,目的shi:快速重启服务器(服务器关闭后,立即释放端口)
#参一:当前的套接字对象,     参二:选项名,    参三:该选项的值
# server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)