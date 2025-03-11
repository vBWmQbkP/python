# import socket
# import time
#
# def check_port(host, port):
#     """
#     检查指定的TCP端口是否被打开
#     :param host: 主机地址
#     :param port: 端口号
#     :return: 如果端口打开返回True，否则返回False
#     """
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         try:
#             s.settimeout(1)  # 设置超时时间为1秒
#             s.connect((host, port))
#             return True
#         except (socket.timeout, ConnectionRefusedError):
#             return False
#
# def main():
#     host = '127.0.0.1'  # 替换为目标主机地址
#     port = 80  # 目标端口号
#     print(f"开始监控 {host}:{port} 的TCP端口状态...")
#
#     while True:
#         if check_port(host, port):
#             print(f"告警：TCP端口{port}已被打开！")
#             break
#         else:
#             print(f"TCP端口{port}未打开，等待一秒重新开始监控...")
#             time.sleep(1)
#
# if __name__ == "__main__":
#     main()

#===========
import socket
import time

def check_port(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.settimeout(1)
            s.connect((host, port))
            return True
        except (socket.timeout, ConnectionRefusedError):
            return False

def main():
    host = '127.0.0.1'
    port = 80
    print(f"开始监控 {host}:{port} 的TCP端口状态...")
    while True:
        if check_port(host, port):
            print(f"告警：TCP端口{port}已被打开！")
            break
        else:
            print(f"TCP端口{port}未打开，等待一秒重新开始监控...")
            time.sleep(1)

if __name__ == "__main__":
    main()