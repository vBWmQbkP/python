import re

str1= "Port-channel1.189  192.168.189.254   YES   CONFIG  up"

# result = re.match(r"([A-Z]\S+\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+YES\s+CONFIG\s+(\w+)",str1).groups()
#
# print(f'{"接口":10}: {result[0]}')
# print(f'{"IP地址":10}: {result[1]}')
# print(f'{"状态":10}: {result[-1]}')

pattern = re.compile(
    r"(?P<interface>[A-Z]\S+\d)\s+"
    r"(?P<ip_address>(?:\d{1,3}\.){3}\d{1,3})\s+"
    r"YES\s+CONFIG\s+(?P<status>\w+)"
)

match = pattern.match(str1)

# if match:
#     result = match.groupdict()
#     print(result)
#     fields = [
#         ("Interface", "interface"),
#         ("IP_address", "ip_address"),
#         ("Status", "status"),
#     ]
#     print(fields)
#     for title, key in fields:
#         print(f"{title:10}: {result[key]}")

if match:
    interface = match.group('interface')
    ip_address = match.group('ip_address')
    status = match.group('status')
    print(f'{"接口":10}: {interface}\n{"IP地址":10}: {ip_address}\n{"状态":10}: {status}')
else:
    print("No match")