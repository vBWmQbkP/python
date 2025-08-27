import re

str1= "Port-channel1.189  192.168.189.254   YES   CONFIG  up"

# result = re.match(r"([A-Z]\S+\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+YES\s+CONFIG\s+(\w+)",str1).groups()

# print(f'{"接口":10}: {result[0]}')
# print(f'{"IP地址":10}: {result[1]}')
# print(f'{"状态":10}: {result[-1]}')

pattern = re.compile(
    r"(?P<interface>[A-Z]\S+\d)\s+"
    r"(?P<ip_address>(?:\d{1,3}\.){3}\d{1,3})\s+"
    r"YES\s+CONFIG\s+(?P<status>\w+)"
)

str2 = pattern.match(str1)

# if str2:
#     result = str2.groupdict()
#     print(result)
#     fields = [
#         ("Interface", "interface"),
#         ("IP_address", "ip_address"),
#         ("Status", "status"),
#     ]
#     # print(fields)
#     # for title, key in fields:
#     #     print(f"{title:10}: {result[key]}")

# if str2:
#     interface = str2.group('interface')
#     ip_address = str2.group('ip_address')
#     status = str2.group('status')
#     print(f'{"接口":10}: {interface}\n{"IP地址":10}: {ip_address}\n{"状态":10}: {status}')
# else:
#     print("No match")

if str2:
    result = str2.groupdict()
    print(f'{"接口":10}: {result["interface"]}')
    print(f'{"IP地址":10}: {result["ip_address"]}')
    print(f'{"状态":10}: {result["status"]}')
else:
    print("No match")


import re

str1 = "Port-channel1.189  192.168.189.254   YES   CONFIG  up"

# 使用 VERBOSE 模式 + 注释
pattern = re.compile(r"""
    (?P<interface>[A-Z]\S+\d)              # 接口名，如 Port-channel1.189
    \s+
    (?P<ip_address>(?:\d{1,3}\.){3}\d{1,3}) # IP 地址（简化版，够用）
    \s+
    YES\s+CONFIG\s+
    (?P<status>\w+)                        # 状态：up/down
""", re.VERBOSE)

# 使用 search + strip 更健壮
match = pattern.search(str1.strip())

if match:
    result = match.groupdict()
    print(f'{"接口":10}: {result["interface"]}')
    print(f'{"IP地址":10}: {result["ip_address"]}')
    print(f'{"状态":10}: {result["status"]}')
else:
    print("No match")











# import re

# str1 = 'Portal-channel1.189       192.168.189.254     YES   CONFIG  up'

# match_template = r'(\w+-\w+\d+\.\d+)\s+((?:(?:25[0-5]|2[0-4][0-9]|[01]?\d{1,2})\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?\d{1,2}))\s+(\w+)\s+(\w+)\s+(\w+)'

# match = re.match(match_template, str1)
# if match:
#     str_interface = match.groups()
#     print(str_interface[0])
#     print(str_interface[1])
#     print(str_interface[4])
# else:
#     print("No match found!")





