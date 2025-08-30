# import re

# str1= "Port-channel1.189  192.168.189.254   YES   CONFIG  up"

# # 匹配方式1
# result = re.match(r"([A-Z]\S+\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+YES\s+CONFIG\s+(\w+)",str1).groups()

# # 输出方式1
# print(f'{"接口":10}: {result[0]}')
# print(f'{"IP地址":10}: {result[1]}')
# print(f'{"状态":10}: {result[-1]}')

# # 匹配方式2 可读性PLUS
# # re,compile()只编译一次可重复使用 避免了重复编译的开销
# pattern = re.compile(
#     # 可以在编译时设置flags后续调用 match/search方法无需重新制定
#     r"(?P<interface>[A-Z]\S+\d)\s+"
#     # 换行书写 可读性更强 易于维护
#     r"(?P<ip_address>(?:\d{1,3}\.){3}\d{1,3})\s+"
#     r"YES\s+CONFIG\s+(?P<status>\w+)"
# )

# # 匹配方式3  可读性MAX
# # 使用 VERBOSE 模式 + 注释
# # 使用三引号可以跨越多行书写
# # 若使用单引号/双引号 则需要每行书写
# # VERBOSE支持在正则内使用#注释,并且会自动忽略空格和换行
# # (?p<NAME>...) 是一个命名捕获组, 不命名将只能通过数字索引获取
# pattern = re.compile(r"""
#     (?P<interface>[A-Z]\S+\d)              # 接口名，如 Port-channel1.189
#     \s+
#     (?P<ip_address>(?:\d{1,3}\.){3}\d{1,3}) # IP 地址（简化版，够用）
#     \s+
#     YES\s+CONFIG\s+
#     (?P<status>\w+)                        # 状态：up/down
# """, re.VERBOSE)

# # way1
# str2 = pattern.match(str1)

# # way 2 使用 search + strip 更健壮
# # .match必须从字符串头开始匹配
# # .search在整个字符串任意位置查找 第一个匹配项
# # str1.strip()去除字符串尾的空白字符 不会修改原字符串 而是返回一个新的字符串
# # 标准写法
# match = pattern.search(str1.strip())
# # print(match)
# # # <re.Match object; span=(0, 53), match='Port-channel1.189  192.168.189.254   YES   CONFIG>
# # print(match.group())
# # # {'interface': 'Port-channel1.189', 'ip_address': '192.168.189.254', 'status': 'up'}

# # way 1 groupdict()+fields列表
# # 适合复杂+可扩展场景 
# if match:
#     # 提取为字典,便于后续使用
#     # 字典都是 键（key） - 值（value） 对组成
#     result = match.groupdict()
#     print(result)
#     # {'interface': 'Port-channel1.189', 'ip_address': '192.168.189.254', 'status': 'up'}
#     fields = [
#         ("接口", "interface"),
#         ("IP地址", "ip_address"),
#         ("状态", "status"),
#     ]
#     # print(fields)
#     # for 循环 提取 fields list列表中的值
#     for title, key in fields:
#         # result[key] result[interface]是Port-channel1.189
#         print(f"{title:10}: {result[key]}")
# else:
#     print("No match")

# # way2 直接使用group()提取变量
# if match:
#     interface = match.group('interface')
#     ip_address = match.group('ip_address')
#     status = match.group('status')
#     print(f'{"接口":10}: {interface}\n{"IP地址":10}: {ip_address}\n{"状态":10}: {status}')
# else:
#     print("No match")

# # way3 简介输出 日常使用
# if match:
#     result = match.groupdict()
#     print(f'{"接口":10}: {result["interface"]}')
#     print(f'{"IP地址":10}: {result["ip_address"]}')
#     print(f'{"状态":10}: {result["status"]}')
# else:
#     print("No match")



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


import re

str1 = "Port-channel1.189  192.168.189.254   YES   CONFIG  up"

pattern = re.compile(r"""
    (?P<interface>[A-Z]\S+\d)              # 接口名
    \s+
    (?P<ip_address>(?:\d{1,3}\.){3}\d{1,3}) # IP 地址
    \s+
    YES\s+CONFIG\s+
    (?P<status>\w+)                        # 状态
""", re.VERBOSE)

match = pattern.search(str1.strip())
print("-"*100)
if match:
    result = match.groupdict()
    print(f'{"接口":10}: {result["interface"]}')
    print(f'{"IP地址":10}: {result["ip_address"]}')
    print(f'{"状态":10}: {result["status"]}')
    # fields = [
    #     ("接口", "interface"),
    #     ("IP地址", "ip_address"),
    #     ("状态", "status"),
    # ]
    # for title, key in fields:
    #     print(f"{title:10}: {result[key]}")
else:
    print("No match")


