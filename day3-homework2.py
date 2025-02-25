import re

show_conn = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

result = re.match(r'([A-Z]{1,3})\s+[a-z]+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{1,5})\s+[a-z]+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{1,5})\,\s+[a-z]+\s+(\d{1,2})\:(\d{1,2})\:(\d{1,2})\,\s+[a-z]+\s+(\d+)\,\s+[a-z]+\s+(\w+)',show_conn).groups()

print(f'{"protocol":20}: {result[0]}')
print(f'{"server":20}: {result[1]}')
print(f'{"localserver":20}: {result[2]}')
print(f'{"idle":20}: {result[3]} 小时 {result[4]} 分钟 {result[5]} 秒')
print(f'{"bytes":20}: {result[6]}')
print(f'{"flags":20}: {result[7]}')