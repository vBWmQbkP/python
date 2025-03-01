import re
import os

ifconfig_result = os.popen("ifconfig " + "ens160").read()

pattern = re.compile(
    r"[\S\s]+inet\s+(?P<ipv4_add>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+"
    r"netmask\s+(?P<netmask>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+"
    r"broadcast\s+(?P<broadcast>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})[\S\s]+"
    r"ether\s+(?P<mac_addr>\w{1,2}:\w{1,2}:\w{1,2}:\w{1,2}:\w{1,2}:\w{1,2})"
)

match = pattern.match(ifconfig_result)

if match:
    broadcast_ip = (match.group("broadcast"))

    result = match.groupdict()

    fields = [
        ("ipv4_add", "ipv4_add"),
        ("netmask", "netmask"),
        ("broadcast", "broadcast"),
        ("mac_addr", "mac_addr"),
    ]

    for title, key in fields:
        print(f"{title:10}: {result[key]}")

parts = broadcast_ip.split(".")
last_part = int(parts[-1])-2
parts[-1] = str(last_part)
ipv4_gw = ".".join(parts)

print("\n我们假设网关IP地址为最后第二位 "+ str(last_part) + "，因此网关IP地址为：" + ipv4_gw + "\n")

ping_result = os.popen("ping " + ipv4_gw + " -c 4").read()

re_ping_result = re.search(r"4 received, 0% packet loss", ping_result)

if re_ping_result:
    print("网关可达！")
else:
    print("网关不可达！")