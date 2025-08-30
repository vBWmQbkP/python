# # import re
# #
# # showconn = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

# # result = re.match(r'([A-Z]{1,3})\s+[a-z]+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5})\s+[a-z]+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}),\s+[a-z]+\s+(\d{1,2}):(\d{1,2}):(\d{1,2}),\s+[a-z]+\s+(\d+),\s+[a-z]+\s+(\w+)',showconn).groups()
# #
# # print(f'{"protocol":20}: {result[0]}')
# # print(f'{"server":20}: {result[1]}')
# # print(f'{"localserver":20}: {result[2]}')
# # print(f'{"idle":20}: {result[3]} 小时 {result[4]} 分钟 {result[5]} 秒')
# # print(f'{"bytes":20}: {result[6]}')
# # print(f'{"flags":20}: {result[7]}')

# import re

# showconn = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

# ip_port = r"((?:\d{1,3}.){3}\d{1,3}:\d{1,5})"
# time_component = r"((?:\d{1,2}:){2}\d{1,2})"

# pattern = re.compile(
#     r"(?P<protocol>[A-Z]{1,3})\s+server\s+"
#     rf"(?P<server>{ip_port})\s+localserver\s+"
#     rf"(?P<localserver>{ip_port}),\s+idle\s+"
#     rf"(?P<idle>{time_component}),\s+bytes\s+"
#     r"(?P<bytes>\d+),\s+flags\s+"
#     r"(?P<flags>\w+)"
# )

# match = pattern.search(showconn)

# # if match:
# #     result = match.groupdict()
# #
# #     hours, minutes, seconds = result['idle'].split(':')
# #
# #     filed = [
# #         ("protocol", result["protocol"]),
# #         ("server", result["server"]),
# #         ("localserver", result["localserver"]),
# #         ("idle", f"{hours} 小时 {minutes} 分钟 {seconds} 秒"),
# #         ("bytes", result["bytes"]),
# #         ("flags", result["flags"]),
# #     ]
# #
# #     for title , value in filed:
# #         print(f'{title:20}: {value}')
# # else:
# #     print("No match")

# if match:
#     protocol = match.group('protocol')
#     server = match.group('server')
#     localserver = match.group('localserver')
#     hours, minutes, seconds = match.group('idle').split(':')
#     bytes = match.group('bytes')
#     flags = match.group('flags')
#     print(f'{"protocol":20}: {protocol}')
#     print(f'{"server":20}: {server}')
#     print(f'{"localserver":20}: {localserver}')
#     print(f'{"idle":20}: {hours} 小时 {minutes} 分钟 {seconds}')
#     print(f'{"bytes":20}: {bytes}')
#     print(f'{"flags":20}: {flags}')
# else:
#     print("No match")
#===============================================================================================================
# #deepseek-1
# import re
#
# show_conn = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
#
# # 定义可复用的正则组件
# ip_port = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5})"
# time_component = r"\d{1,2}:\d{1,2}:\d{1,2}"
#
# pattern = re.compile(
#     r"(?P<protocol>[A-Z]{1,3})\s+server\s+"
#     rf"(?P<server>{ip_port})\s+localserver\s+"
#     rf"(?P<localserver>{ip_port}),\s+idle\s+"
#     rf"(?P<idle>{time_component}),\s+bytes\s+"
#     r"(?P<bytes>\d+),\s+flags\s+"
#     r"(?P<flags>\w+)"
# )
#
# match = pattern.match(show_conn)
# if match:
#     data = match.groupdict()
#     # 解析时间组件
#     hours, minutes, seconds = data['idle'].split(':')
#
#     # 统一输出格式
#     output_fields = [
#         ('protocol', data['protocol']),
#         ('server', data['server']),
#         ('localserver', data['localserver']),
#         ('idle', f"{hours} 小时 {minutes} 分钟 {seconds} 秒"),
#         ('bytes', data['bytes']),
#         ('flags', data['flags'])
#     ]
#
#     for title, value in output_fields:
#         print(f"{title:20}: {value}")
# else:
#     print("No match found")

#===============================================================================================================
#deepseek+kimi
# import re
#
# # 原始输入字符串
# conn_str = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
#
# # 定义正则表达式组件（DRY原则）
# PROTOCOL = r"(?P<protocol>[A-Z]{1,3})"
# SERVER_IP_PORT = r"(?P<server_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(?P<server_port>\d{1,5})"
# LOCAL_IP_PORT = r"(?P<local_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(?P<local_port>\d{1,5})"
# IDLE_TIME = r"(?P<idle>\d+:\d{2}:\d{2})"
# BYTES = r"(?P<bytes>\d+)"
# FLAGS = r"(?P<flags>[A-Z]+)"
#
# # 构建完整正则模式（清晰的分段结构）
# pattern = re.compile(
#     rf"{PROTOCOL}\s+server\s+{SERVER_IP_PORT}\s+localserver\s+{LOCAL_IP_PORT},\s+"
#     rf"idle\s+{IDLE_TIME},\s+bytes\s+{BYTES},\s+flags\s+{FLAGS}"
# )
#
# # 执行匹配
# match = pattern.match(conn_str)
# if not match:
#     raise ValueError("Invalid connection string format")
#
# # 提取结构化数据
# data = match.groupdict()
# server = f"{data['server_ip']}:{data['server_port']}"  # 组合第一个IP:PORT
# local_server = f"{data['local_ip']}:{data['local_port']}"  # 组合第二个IP:PORT
# hours, mins, secs = data['idle'].split(':')
#
# # 定义输出模板（便于国际化修改）
# OUTPUT_TEMPLATE = """\
# {:<20}: {}
# {:<20}: {}
# {:<20}: {}
# {:<20}: {} 小时 {} 分钟 {} 秒
# {:<20}: {}
# {:<20}: {}"""
#
# # 生成格式化输出
# print(OUTPUT_TEMPLATE.format(
#     'protocol', data['protocol'],
#     'server', server,
#     'localserver', local_server,
#     'idle', hours, mins, secs,
#     'bytes', data['bytes'],
#     'flags', data['flags']
# ))



# import re

# str1 = "TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO"

# pattern = re.compile(r"""
#     (?P<Protocol>TCP|UDP)           
#     \s+server\s+
#     (?P<Server_IP_Port>
#         (?:\d{1,3}\.){3}\d{1,3}
#         :\d{1,5}
#     )
#     \s+localserver\s+
#     (?P<Local_Server_IP_Port>
#         (?:\d{1,3}\.){3}\d{1,3}
#         :\d{1,5}
#     )
#     ,\s+idle\s+
#     (?P<Idle_time>\d{1,2}:\d{2}:\d{2})
#     ,\s+bytes\s+
#     (?P<Bytes>\d+)
#     ,\s+flags\s+
#     (?P<Flags>[A-Z]+)
# """,re.VERBOSE)

# match = pattern.search(str1.strip())

# if match:
#     result = match.groupdict()
#     # print(result)

#     idle_time = result["Idle_time"]
#     # print(idle_time)

#     #Python支持给多个变量同时赋值，名为 序列解包 Sequence Unpacking
#     #idle_time.split(":") = ['0', '01', '09'] 包含三个元素的列表
#     h,m,s = idle_time.split(":")
#     # print(h)
#     # print(m)
#     # print(s)

#     formatted_idle = f"{int(h)}小时{m.zfill(2)}分{s.zfill(2)}秒"
#     result["Idle_time"] = formatted_idle

#     fields = [
#         ("protocol","Protocol"),
#         ("server","Server_IP_Port"),
#         ("localserver","Local_Server_IP_Port"),
#         ("idle","Idle_time"),
#         ("bytes","Bytes"),
#         ("flags","Flags"),
#     ]
#     for title,key in fields:
#         print(f"{title:20}: {result[key]}")
# else:
#     print("No match")


# import re
# #typing是Python内置模块，用于 类型提示 Type Hints
# #使代码更清晰,更安全, 便于团队协作
# from typing import Dict, Optional, Tuple

# # 定义函数 函数名称:parse_connection_info
# # 参数long_line 是一个str字符串类型的参数
# def parse_connection_info(log_line: str) -> Optional[Dict[str, str]]:
#     """
#     解析 TCP/UDP 连接日志行，提取关键信息。

#     Args:
#         log_line: 日志字符串

#     Returns:
#         匹配成功返回字段字典，否则返回 None
#     """
#     # 编译正则表达式（只编译一次，可提升性能）
#     pattern = re.compile(r"""
#         (?P<Protocol>TCP|UDP)                           # 协议
#         \s+server\s+                                    # 分隔词
#         (?P<Server_IP_Port>
#             (?:\d{1,3}\.){3}\d{1,3}                     # IP 地址
#             :\d{1,5}                                    # 端口
#         )
#         \s+localserver\s+                               # 分隔词
#         (?P<Local_Server_IP_Port>
#             (?:\d{1,3}\.){3}\d{1,3}
#             :\d{1,5}
#         )
#         ,\s+idle\s+
#         (?P<Idle_time>\d{1,2}:\d{2}:\d{2})              # 空闲时间
#         ,\s+bytes\s+
#         (?P<Bytes>\d+)                                  # 字节数
#         ,\s+flags\s+
#         (?P<Flags>[A-Z]+)                               # 标志位
#     """, re.VERBOSE | re.IGNORECASE)

#     match = pattern.search(log_line.strip())

#     # Python 条件表达式/三元运算符
#     # return A if condition else B
#     # 等价于下面这种写法
#     # if match:
#     #     return match.groupdict()
#     # else:
#     #     return None
#     return match.groupdict() if match else None

# # 定义函数 display_results()
# # 参数类型 字符串,字符串的字典
# def display_results(data: Dict[str, str]) -> None:
#     """
#     格式化输出解析结果。

#     Args:
#         data: 解析出的字段字典
#     """
#     # 字段映射：显示名 -> 字典键
#     # : Tuple[Tuple[str, str], ...]部分属于 类型标注，没有实际用途
#     # field_mapping变量名 是一个元组
#     # 内部包含了 0/1/多个 (str,str)的元组
#     # list列表后期允许修改 元组防止他人误改
#     # 中间空格只是为了代码美观和对齐
#     field_mapping: Tuple[Tuple[str, str], ...] = (
#         ("Protocol",   "Protocol"),
#         ("Server",     "Server_IP_Port"),
#         ("Local",      "Local_Server_IP_Port"),
#         ("Idle",       "Idle_time"),
#         ("Bytes",      "Bytes"),
#         ("Flags",      "Flags"),
#     )

#     # print("Connection Details:")
#     # print("-" * 40)
    # for display_name, key in field_mapping:
    #     # data是一个字典
    #     # .get是字典的安全访问方式
    #     # key存在于data返回对应的值 否则返回N/A 防止程序崩溃
    #     value = data.get(key, "N/A")
    #     # 格式化输出 向左对其 宽度12
    #     print(f"{display_name:<12} : {value}")


# # ==================== 使用示例 ====================
# if __name__ == "__main__":
#     str1 = "TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO"

#     # parse_connection_info()函数执行完后 return结果送回到这一行 赋值给变量result
#     result = parse_connection_info(str1)
#     # print(result)

#     if result:
#         display_results(result)
#     else:
#         print("❌ No match found. Input format may be invalid.")


import re

def parse_connection_info(log_line):
    pattern = re.compile(r"""
        (?P<Protocol>TCP|UDP)                           # 协议
        \s+server\s+                                    # 分隔词
        (?P<Server_IP_Port>
            (?:\d{1,3}\.){3}\d{1,3}                     # IP 地址
            :\d{1,5}                                    # 端口
        )
        \s+localserver\s+                               # 分隔词
        (?P<Local_Server_IP_Port>
            (?:\d{1,3}\.){3}\d{1,3}
            :\d{1,5}
        )
        ,\s+idle\s+
        (?P<Idle_time>\d{1,2}:\d{2}:\d{2})              # 空闲时间
        ,\s+bytes\s+
        (?P<Bytes>\d+)                                  # 字节数
        ,\s+flags\s+
        (?P<Flags>[A-Z]+)                               # 标志位
    """, re.VERBOSE | re.IGNORECASE)

    match = pattern.search(log_line.strip())

    return match.groupdict() if match else None

def display_results(data):
    # field_mapping = (
    #     ("Protocol",   "Protocol"),
    #     ("Server",     "Server_IP_Port"),
    #     ("Local",      "Local_Server_IP_Port"),
    #     ("Idle",       "Idle_time"),
    #     ("Bytes",      "Bytes"),
    #     ("Flags",      "Flags"),
    # )
    field_mapping = [
        ("protocol","Protocol"),
        ("server","Server_IP_Port"),
        ("localserver","Local_Server_IP_Port"),
        ("idle","Idle_time"),
        ("bytes","Bytes"),
        ("flags","Flags"),
    ]
    for display_name, key in field_mapping:
        value = data.get(key, "N/A")
        print(f"{display_name:<12} : {value}")

# ==================== 使用示例 ====================
if __name__ == "__main__":
    str1 = "TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO"

    result = parse_connection_info(str1)

    if result:
        display_results(result)
    else:
        print("❌ No match found. Input format may be invalid.")