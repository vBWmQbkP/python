import re
import os

ifconfig_result = os.popen("ifconfig " + "ens160").read()
# print(ifconfig_result)

# ifconfig_result = """ens160: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500
#               inet 172.16.66.166 netmask 255.255.255.0 broadcast 172.16.66.255
#               inet6 fe80::250:56ff:feab:59bd prefixlen 64 scopeid 0x20<link>
#               ether 00:50:56:ab:59:bd txqueuelen 1000 (Ethernet)
#               RX packets 174598769 bytes 1795658527217 (1.6 TiB)
#               RX errors 1 dropped 24662 overruns 0 frame 0
#               TX packets 51706604 bytes 41788673420 (38.9 GiB)
#               TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0"""

# result = re.match(r"[\S\s]+inet\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+netmask\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+broadcast\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})[\S\s]+ether\s+(\w{1,2}.\w{1,2}.\w{1,2}.\w{1,2}.\w{1,2}.\w{1,2})", str).groups()
#
# print(result)
#
# print(f'{"ipv4_add":10}:{result[0]}')
# print(f'{"netmask":10}:{result[1]}')
# print(f'{"broadcast":10}:{result[2]}')
# print(f'{"mac_addr":10}:{result[3]}')
# print("我们假设网络IP地址为")

pattern = re.compile(
    r"[\S\s]+inet\s+(?P<ipv4_add>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+"
    r"netmask\s+(?P<netmask>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+"
    r"broadcast\s+(?P<broadcast>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})[\S\s]+"
    r"ether\s+(?P<mac_addr>\w{1,2}.\w{1,2}.\w{1,2}.\w{1,2}.\w{1,2}.\w{1,2})"
)

match = pattern.match(ifconfig_result)

if match:
    # print(match.group("ipv4_add"))
    # print(match.group("netmask"))
    broadcast_ip = (match.group("broadcast"))
    # print(match.group("mac_addr"))
    result = match.groupdict()
    # print(result)
    fields = [
        ("ipv4_add", "ipv4_add"),
        ("netmask", "netmask"),
        ("broadcast", "broadcast"),
        ("mac_addr", "mac_addr"),
    ]
    # print(fields)
    for title, key in fields:
        print(f"{title:10}: {result[key]}")

#打印网关IP地址
parts = broadcast_ip.split(".")
last_part = int(parts[-1])-2
parts[-1] = str(last_part)
ipv4_gw = ".".join(parts)

print("\n我们假设网关IP地址为最后第二位"+ str(last_part) + "，因此网关IP地址为：" + ipv4_gw + "\n")

ping_result = os.popen("ping " + ipv4_gw + " -c 1").read()

re_ping_result = re.search(r"1 received, 0% packet loss", ping_result)
# print(re_ping_result)
if re_ping_result:
    print("网关可达！")
else:
    print("网关不可达！")