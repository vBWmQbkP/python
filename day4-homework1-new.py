import re
import os

ifconfig_str = os.popen("ifconfig "+"ens160").read()
# str1 = """
# ens160: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500
#               inet 172.16.66.166 netmask 255.255.255.0 broadcast 172.16.66.255
#               inet6 fe80::250:56ff:feab:59bd prefixlen 64 scopeid 0x20<link>
#               ether 00:50:56:ab:59:bd txqueuelen 1000 (Ethernet)
#               RX packets 174598769 bytes 1795658527217 (1.6 TiB)
#               RX errors 1 dropped 24662 overruns 0 frame 0
#               TX packets 51706604 bytes 41788673420 (38.9 GiB)
#               TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0
# """
# print(str1)

# #编译一个正则对象,方便重复使用
# re.compile本身不具备匹配功能只是准备工具
pattern = re.compile(r"""
    [\S\s]+inet\s+
    (?P<IP_address>(?:\d{1,3}\.){3}\d{1,3})
    \s+netmask\s+
    (?P<Netmask>(?:\d{1,3}\.){3}\d{1,3})
    \s+broadcast\s+
    (?P<Broadcast_IP>(?:\d{1,3}\.){3}\d{1,3})
    [\S\s]+ether\s+
    (?P<Mac_address>(?:\w{2}:){5}\w{2})
""",re.VERBOSE)

#str1.strip()去除字符串收尾的空白字符
#pattern.search() 清理后的字符串第一个匹配
match = pattern.search(ifconfig_str.strip())

if match:
    result = match.groupdict()
    # print(result)

    fields = [
        ("ipv4_add","IP_address"),
        ("netmask","Netmask"),
        ("broadcast","Broadcast_IP"),
        ("mac_add","Mac_address"),
    ]

    for key,value in fields:
        print(f'{key:<10}: {result[value]}')

else:
    print("No match")

# print(result["Broadcast_IP"])
broadcast_parts = result["Broadcast_IP"].split(".")
# print(broadcast_parts)
gw_last_parts = int(broadcast_parts[-1])-253
# print(gw_last_parts)
#这里由于之前已经改为了整型,需要修改会字符串类型,否则后面 .join连接起来会报错
broadcast_parts[-1] = str(gw_last_parts)
# print(broadcast_parts)
gw_ipv4 = ".".join(broadcast_parts)
# print(gw_ipv4)

print("\n假设网关IP地址为第二位为2,因此网关IP地址为"+gw_ipv4+"\n")

ping_result = os.popen("ping "+gw_ipv4+" -c 1").read()
# print(ping_result)

re_ping_result =  re.search(r"1 received, 0% packet loss", ping_result)

if re_ping_result:
    print("网关可达")
else:
    print("网关不可达")



# #============
# #函数版本
# import re
# import os

# def get_interface_info(interface_name):
#     """执行 ifconfig 命令并返回输出"""
#     try:
#         result = os.popen(f"ifconfig {interface_name}").read()
#         if not result.strip():
#             print(f"❌ 网卡 '{interface_name}' 不存在或无输出")
#             return None
#         return result
#     except Exception as e:
#         print(f"❌ 执行 ifconfig 时出错: {e}")
#         return None

# def parse_interface_data(data):
#     """使用正则解析 IP、子网掩码、广播地址、MAC 地址"""
#     pattern = re.compile(r"""
#         [\S\s]+?inet\s+
#         (?P<IP_address>(?:\d{1,3}\.){3}\d{1,3})
#         \s+netmask\s+
#         (?P<Netmask>(?:\d{1,3}\.){3}\d{1,3})
#         \s+broadcast\s+
#         (?P<Broadcast_IP>(?:\d{1,3}\.){3}\d{1,3})
#         [\S\s]+?ether\s+
#         (?P<Mac_address>(?:[0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2})
#     """, re.VERBOSE)

#     match = pattern.search(data)
#     return match.groupdict() if match else None

# def calculate_gateway(broadcast_ip, offset=1):
#     """
#     根据广播地址计算网关IP（默认为广播-1）
#     例如：172.16.66.255 -> 172.16.66.254
#     """
#     try:
#         parts = broadcast_ip.split(".")
#         last_octet = int(parts[-1])
#         if last_octet - offset < 1:
#             print("⚠️  计算出的网关IP最后一位小于1，可能不合理")
#             return None
#         parts[-1] = str(last_octet - offset)
#         return ".".join(parts)
#     except (ValueError, IndexError):
#         print("❌ 广播地址格式错误，无法计算网关")
#         return None

# def ping_host(host, count=1):
#     """Ping 一个主机，返回是否可达"""
#     try:
#         result = os.popen(f"ping {host} -c {count}").read()
#         # 匹配成功接收的包：如 "1 packets transmitted, 1 received"
#         if re.search(r"\d+ received, 0% packet loss", result):
#             return True
#         return False
#     except Exception as e:
#         print(f"❌ Ping 命令执行失败: {e}")
#         return False

# def main():
#     interface_name = "ens160"

#     # 1. 获取网卡信息
#     print(f"🔍 正在获取网卡 '{interface_name}' 的信息...")
#     ifconfig_output = get_interface_info(interface_name)
#     if not ifconfig_output:
#         return

#     # 2. 解析关键字段
#     print("🧩 正在解析网络配置...")
#     result = parse_interface_data(ifconfig_output)
#     if not result:
#         print("❌ 未能从输出中解析出有效信息")
#         return

#     # 3. 输出解析结果
#     fields = [
#         ("IPv4地址", "IP_address"),
#         ("子网掩码", "Netmask"),
#         ("广播地址", "Broadcast_IP"),
#         ("MAC地址", "Mac_address"),
#     ]
#     print("\n📋 解析结果：")
#     for label, key in fields:
#         print(f"{label:<8}: {result[key]}")

#     # 4. 计算网关（广播地址最后一位 -1）
#     print("\n⚙️  正在计算网关IP...")
#     gw_ipv4 = calculate_gateway(result["Broadcast_IP"], offset=1)  # 更合理：-1 而不是 -253
#     if not gw_ipv4:
#         return

#     print(f"🌐 假设网关IP为广播地址-1，计算得: {gw_ipv4}")

#     # 5. Ping 测试网关
#     print(f"\n📡 正在 Ping 网关 {gw_ipv4} ...")
#     if ping_host(gw_ipv4, count=2):
#         print("✅ 网关可达 ✅")
#     else:
#         print("❌ 网关不可达 ❌")

# if __name__ == "__main__":
#     main()