import re

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n \
TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"

asa_dict = {}

pattern = re.compile(
    r'\S+\s+\S+\s+(?P<src_ip>(?:\d{1,3}\.){3}\d{1,3}):'
    r'(?P<src_port>\d{1,5})\s+'
    r'\S+\s+(?P<dst_ip>(?:\d{1,3}\.){3}\d{1,3}):'
    r'(?P<dst_port>\d{1,5}),'
    r'[\S\s]+bytes\s+(?P<bytes>\d+),'
    r'\s+flags\s+(?P<flags>\w+)'
)

for conn in asa_conn.split('\n'):
    re_result = pattern.search(conn)
    if re_result:
        key = (re_result.group('src_ip'), re_result.group('src_port'), re_result.group('dst_ip'), re_result.group('dst_port'))
        value = (re_result.group('bytes'), re_result.group('flags'))
        asa_dict[key] = value
    else:
        print("no match")

print("打印分析后的字典！\n")
print(asa_dict)
print("\n格式化打印输出\n")

for key, value in asa_dict.items():

    src_ip, src_port, dst_ip, dst_port = key
    bytes, flags = value

    format_str1 = f'{"src":^10}:{src_ip:^20}|{"src_port":^10}:{src_port:^20}|{"dst":^10}:{dst_ip:^20}|{"dst_port":^10}:{dst_port:^20}'
    format_str2 = f'{"bytes":^10}:{bytes:^20}|{"flags":^10}:{flags:^20}'

    print(format_str1)
    print(format_str2)

    max_length = max(len(format_str1), len(format_str2))
    print("=" * max_length)

#deepseek===========
# import re
#
# asa_conn = """TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO
# TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"""
#
# asa_dict = {}
#
# pattern = re.compile(
#     r'TCP Student (?P<src_ip>\d+\.\d+\.\d+\.\d+):(?P<src_port>\d+) '
#     r'Teacher (?P<dst_ip>\d+\.\d+\.\d+\.\d+):(?P<dst_port>\d+), '
#     r'.*?bytes (?P<bytes>\d+), flags (?P<flags>\w+)'
# )
#
# for conn in asa_conn.split('\n'):
#     if match := pattern.search(conn.strip()):
#         key = (match['src_ip'], match['src_port'],
#                match['dst_ip'], match['dst_port'])
#         asa_dict[key] = (match['bytes'], match['flags'])
#
# print("打印分析后的字典：\n", asa_dict)
#
# print("\n格式化打印输出：")
#
# # 定义固定宽度的列格式
# col_width = 20
# sep_line = '|'.join(['-' * col_width] * 4)
#
# for key, value in asa_dict.items():
#     src_ip, src_port, dst_ip, dst_port = key
#     bytes_cnt, flags = value
#
#     # 第一部分输出（连接信息）
#     print(f"{'src_ip':<{col_width}}|{'src_port':<{col_width}}|{'dst_ip':<{col_width}}|{'dst_port':<{col_width}}")
#     print(f"{src_ip:<{col_width}}|{src_port:^{col_width}}|{dst_ip:<{col_width}}|{dst_port:^{col_width}}")
#     print(sep_line)
#
#     # 第二部分输出（传输信息）
#     print(f"{'bytes':<{col_width}}|{'flags':<{col_width}}")
#     print(f"{bytes_cnt:^{col_width}}|{flags:^{col_width}}")
#     print('=' * (col_width * 4 + 3))  # 计算总长度：4列+3个分隔符
#===========
# import re
#
# # 原始数据
# asa_conn = """TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO
# TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"""
#
# # 初始化字典
# asa_dict = {}
#
# # 定义正则表达式模式
# pattern = re.compile(
#     r'\S+\s+\S+\s+(?P<src_ip>(?:\d{1,3}\.){3}\d{1,3}):'
#     r'(?P<src_port>\d{1,5})\s+'
#     r'\S+\s+(?P<dst_ip>(?:\d{1,3}\.){3}\d{1,3}):'
#     r'(?P<dst_port>\d{1,5}),'
#     r'[\S\s]+bytes\s+(?P<bytes>\d+),'
#     r'\s+flags\s+(?P<flags>\w+)'
# )
#
# # 遍历每一行数据并填充字典
# for conn in asa_conn.split('\n'):
#     re_result = pattern.search(conn)
#     if re_result:
#         key = (
#             re_result.group('src_ip'),
#             re_result.group('src_port'),
#             re_result.group('dst_ip'),
#             re_result.group('dst_port')
#         )
#         value = (
#             re_result.group('bytes'),
#             re_result.group('flags')
#         )
#         asa_dict[key] = value
#     else:
#         print("no match")
#
# # 打印分析后的字典
# print("打印分析后的字典！\n")
# print(asa_dict)
#
# # 格式化打印输出
# print("\n格式化打印输出\n")
# for key, value in asa_dict.items():
#     src_ip, src_port, dst_ip, dst_port = key
#     bytes_count, flags = value
#
#     # 格式化字符串
#     format_str1 = f'{"src_ip":<10}:{src_ip:<15}|{"src_port":<10}:{src_port:<10}|{"dst_ip":<10}:{dst_ip:<15}|{"dst_port":<10}:{dst_port:<10}'
#     format_str2 = f'{"bytes":<10}:{bytes_count:<15}|{"flags":<10}:{flags:<10}'
#
#     # 打印格式化字符串
#     print(format_str1)
#     print(format_str2)
#
#     # 计算等号分隔线的长度
#     max_length = max(len(format_str1), len(format_str2))
#     print("=" * max_length)