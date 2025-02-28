import re

str = """ens160: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500
              inet 172.16.66.166 netmask 255.255.255.0 broadcast 172.16.66.255
              inet6 fe80::250:56ff:feab:59bd prefixlen 64 scopeid 0x20<link>
              ether 00:50:56:ab:59:bd txqueuelen 1000 (Ethernet)
              RX packets 174598769 bytes 1795658527217 (1.6 TiB)
              RX errors 1 dropped 24662 overruns 0 frame 0
              TX packets 51706604 bytes 41788673420 (38.9 GiB)
              TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0"""

result = re.match(r"[\S\s]+inet\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+netmask\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+broadcast\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})[\S\s]+ether\s+(\w{1,2}.\w{1,2}.\w{1,2}.\w{1,2}.\w{1,2}.\w{1,2})", str).groups()

print(result)

print(f'{"ipv4_add":10}:{result[0]}')
print(f'{"netmask":10}:{result[1]}')
print(f'{"broadcast":10}:{result[2]}')
print(f'{"mac_addr":10}:{result[3]}')
print("我们假设网络IP地址为")