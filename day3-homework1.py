# import re
#
# str = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
#
# result = re.match(r"(\d{1,4})\s+(\w{1,4}\.\w{1,4}\.\w{1,4})\s+([A-Za-z]+)\s+([A-Z][a-z]\d{1,2}\/\d{1,2}\/\d{1,2})",str).groups()
#
# print(f'{"VLAN ID":10}: {result[0]}')
# print(f'{"MAC":10}: {result[1]}')
# print(f'{"Type":10}: {result[2]}')
# print(f'{"Interface":10}: {result[3]}')

#deepseek
import re

input_str = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'

# 使用命名分组并优化正则表达式
pattern = re.compile(
    r"(?P<vlan_id>\d{1,4})\s+"
    r"(?P<mac>\w{4}\.\w{4}\.\w{4})\s+"
    r"(?P<type>[A-Za-z]+)\s+"
    r"(?P<interface>[A-Z][a-z]\d{1,2}/\d{1,2}/\d{1,2})"
)

match = pattern.match(input_str)
print(match)
if match:
    result = match.groupdict()
    # print(result)
    # 使用字段列表统一输出格式
    fields = [
        ('VLAN ID', 'vlan_id'),
        ('MAC', 'mac'),
        ('Type', 'type'),
        ('Interface', 'interface')
    ]

    for title, key in fields:
        print(f'{title:10}: {result[key]}')