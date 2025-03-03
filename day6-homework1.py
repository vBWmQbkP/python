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

src_ip = "src_ip"
src_port = "src_port"
dst_ip = "dst_ip"
dst_port = "dst_port"
bytes = "bytes"
flags = "flags"

format_str1 = f'{"src_ip":^10}:{src_ip:^10}|{"src_port":^10}:{src_port:^10}|{"dst_ip":^10}:{dst_ip:^10}|{"dst_port":^10}:{dst_port:^10}'
format_str2 = f'{"bytes":^10}:{bytes:^10}|{"flags":^10}:{flags:^10}'

print("\n格式化打印输出\n")

for key, value in asa_dict.items():
    src_ip, src_port, dst_ip, dst_port = key
    bytes_count, flags = value
    print(format_str1)
    print(format_str2)
    max_length = max(len(format_str1), len(format_str2))
    print("=" * max_length)

#deepseek===========
