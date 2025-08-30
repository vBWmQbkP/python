# import re
#
# input_str = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
#
# result = re.match(r"(\d{1,4})\s+(\w{1,4}\.\w{1,4}\.\w{1,4})\s+([A-Za-z]+)\s+([A-Z][a-z]\d{1,2}\/\d{1,2}\/\d{1,2})",input_str).groups()
#
# print(f'{"VLAN ID":10}: {result[0]}')
# print(f'{"MAC":10}: {result[1]}')
# print(f'{"Type":10}: {result[2]}')
# print(f'{"Interface":10}: {result[3]}')

# #way2-test
# import re
# input_str = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'

# pattern = re.compile(
#     r"(?P<vlanid>\d{1,4})\s+"
#     r"(?P<mac>(?:\w{4}\.){2}\w{4})\s+"
#     r"(?P<type>[A-Za-z]+)\s+"
#     r"(?P<interface>[A-Z][a-z](?:\d{1,2}/){2}\d{1,2})"
# )

# match = pattern.match(input_str)

# if match:
#     result = match.groupdict()
#
#     fileds = [
#         ("vlanid","vlanid"),
#         ("mac","mac"),
#         ("type","type"),
#         ("interface","interface")
#     ]
#
#     for title , key in fileds:
#         print(f"{title:10}:{result[key]}")
# else:
#     print("No match")

# if match:
#     vlanid = match.group('vlanid')
#     mac = match.group('mac')
#     type = match.group('type')
#     interface = match.group('interface')
#     print(f'{"VLAN ID":10}: {vlanid}\n{"MAC":10}: {mac}\n{"Type":10}: {type}\n{"Interface":10}: {interface}')
# else:
#     print('No match')

# #deepseek
# import re
#
# input_str = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
#
# # 使用命名分组并优化正则表达式
# pattern = re.compile(
#     r"(?P<vlan_id>\d{1,4})\s+"
#     r"(?P<mac>\w{4}\.\w{4}\.\w{4})\s+"
#     r"(?P<type>[A-Za-z]+)\s+"
#     r"(?P<interface>[A-Z][a-z]\d{1,2}/\d{1,2}/\d{1,2})"
# )
#
# match = pattern.match(input_str)
# print(match)
# if match:
#     result = match.groupdict()
#     # print(result)
#     # 使用字段列表统一输出格式
#     fields = [
#         ('VLAN ID', 'vlan_id'),
#         ('MAC', 'mac'),
#         ('Type', 'type'),
#         ('Interface', 'interface')
#     ]
#
#     for title, key in fields:
#         print(f'{title:10}: {result[key]}')

import re

str1 = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'

pattern = re.compile(r"""
    (?P<vlan_id>\d{1,4})                               # VLAN ID
    \s+
    (?P<mac_address>(?:[0-9a-fA-F]{4}\.){2}[0-9a-fA-F]{4})  # MAC 地址
    \s+
    (?P<type>DYNAMIC)                                  # 类型
    \s+
    (?P<interface>\w+(?:\d{1,2}\/){2}\d{1,2})                        # 接口
""", re.VERBOSE)

match = pattern.search(str1.strip())

if match:
    result = match.groupdict()
    # print(f'{"VLAN ID":10}: {result["vlan_id"]}')
    # print(f'{"MAC":10}: {result["mac_address"]}')
    # print(f'{"Type":10}: {result["type"]}')
    # print(f'{"Interface":10}: {result["interface"]}')
    fields = [
        ("VLAN_ID", "vlan_id"),
        ("MAC", "mac_address"),
        ("Type", "type"),
        ("Interface", "interface"),
    ]
    for title, key in fields:
        print(f"{title:10}: {result[key]}")
else:
    print("No match")