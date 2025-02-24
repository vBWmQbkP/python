import re

str1= "Port-channel1.189  100.11.1.254   YES   CONFIG up"

result = re.match(r"([A-Z]\S+\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+YES\s+CONFIG\s+(\w+)",str1).groups()

print(result)

print(f'{"接口":10}: {result[0]}')
print(f'{"IP地址":10}: {result[1]}')
print(f'{"状态":10}: {result[-1]}')