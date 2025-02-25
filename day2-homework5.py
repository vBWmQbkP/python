import re

str1= "Port-channel1.189  192.168.189.254   YES   CONFIG  up"

result = re.match(r"([A-Z]\S+\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+YES\s+CONFIG\s+(\w+)",str1).groups()

print(f'{"接口":10}: {result[0]}')
print(f'{"IP地址":10}: {result[1]}')
print(f'{"状态":10}: {result[-1]}')