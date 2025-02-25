# import re
#
# show_conn = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
#
# result = re.match(r'([A-Z]{1,3})\s+[a-z]+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{1,5})\s+[a-z]+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{1,5})\,\s+[a-z]+\s+(\d{1,2})\:(\d{1,2})\:(\d{1,2})\,\s+[a-z]+\s+(\d+)\,\s+[a-z]+\s+(\w+)',show_conn).groups()
#
# print(f'{"protocol":20}: {result[0]}')
# print(f'{"server":20}: {result[1]}')
# print(f'{"localserver":20}: {result[2]}')
# print(f'{"idle":20}: {result[3]} 小时 {result[4]} 分钟 {result[5]} 秒')
# print(f'{"bytes":20}: {result[6]}')
# print(f'{"flags":20}: {result[7]}')
#
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

#kimi-2-1
import re

# 原始输入字符串
conn_str = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

# 定义正则表达式组件（DRY原则）
PROTOCOL = r"(?P<protocol>[A-Z]{1,3})"
SERVER_IP_PORT = r"(?P<server_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(?P<server_port>\d{1,5})"
LOCAL_IP_PORT = r"(?P<local_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(?P<local_port>\d{1,5})"
IDLE_TIME = r"(?P<idle>\d+:\d{2}:\d{2})"
BYTES = r"(?P<bytes>\d+)"
FLAGS = r"(?P<flags>[A-Z]+)"

# 构建完整正则模式（清晰的分段结构）
pattern = re.compile(
    rf"{PROTOCOL}\s+server\s+{SERVER_IP_PORT}\s+localserver\s+{LOCAL_IP_PORT},\s+"
    rf"idle\s+{IDLE_TIME},\s+bytes\s+{BYTES},\s+flags\s+{FLAGS}"
)

# 执行匹配
match = pattern.match(conn_str)
if not match:
    raise ValueError("Invalid connection string format")

# 提取结构化数据
data = match.groupdict()
server = f"{data['server_ip']}:{data['server_port']}"  # 组合第一个IP:PORT
local_server = f"{data['local_ip']}:{data['local_port']}"  # 组合第二个IP:PORT
hours, mins, secs = data['idle'].split(':')

# 定义输出模板（便于国际化修改）
OUTPUT_TEMPLATE = """\
{:<20}: {}
{:<20}: {}
{:<20}: {}
{:<20}: {} 小时 {} 分钟 {} 秒
{:<20}: {}
{:<20}: {}"""

# 生成格式化输出
print(OUTPUT_TEMPLATE.format(
    'protocol', data['protocol'],
    'server', server,
    'localserver', local_server,
    'idle', hours, mins, secs,
    'bytes', data['bytes'],
    'flags', data['flags']
))

# #deepseek-2-bad
# import re
#
# # 原始输入字符串
# conn_str = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
#
# # 定义正则表达式组件（DRY原则）
# PROTOCOL = r"(?P<protocol>[A-Z]{1,3})"
# IP_PORT = r"(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(?P<port>\d{1,5})"
# IDLE_TIME = r"(?P<idle>\d+:\d{2}:\d{2})"
# BYTES = r"(?P<bytes>\d+)"
# FLAGS = r"(?P<flags>[A-Z]+)"
#
# # 构建完整正则模式（清晰的分段结构）
# pattern = re.compile(
#     rf"{PROTOCOL}\s+server\s+{IP_PORT}\s+localserver\s+{IP_PORT},\s+"
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
# server = f"{data['ip']}:{data['port']}"  # 组合第一个IP:PORT
# local_server = f"{data['ip']}:{data['port']}"  # 组合第二个IP:PORT
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

