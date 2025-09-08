import re
import os

interface_name = "ens160"

command_output = os.popen(f"ifconfig {interface_name}").read()

if not command_output.strip():
    print(f" 网卡 '{interface_name}' 不存在")
    exit(1)
    # raise ValueError(f" 网卡 '{interface_name}' 不存在或无输出")
    # 独立脚本推荐exit(1) 希望立即终止
    # 函数/模块 推荐 raise ValueError 希望调用者处理错误

pattern = re.compile(r"""
    [\S\s]+?inet\s+
    (?P<IP_address>(?:\d{1,3}\.){3}\d{1,3})
    \s+netmask\s+
    (?P<Netmask>(?:\d{1,3}\.){3}\d{1,3})
    \s+broadcast\s+
    (?P<Broadcast_IP>(?:\d{1,3}\.){3}\d{1,3})
    [\S\s]+?ether\s+
    (?P<Mac_address>(?:[0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2})
""", re.VERBOSE)

match = pattern.search(command_output.strip())

if not match:
    print(" 未能从 ifconfig 输出中解析出网络信息")
    exit(1)
    # raise ValueError("无法从 ifconfig 输出中提取网络信息")

result = match.groupdict()

fields = [
    ("ipv4_address",    "IP_address"),
    ("netmask",    "Netmask"),
    ("broadcast",    "Broadcast_IP"),
    ("MAC_address",     "Mac_address"),
]

for label, key in fields:
    print(f"{label:<15}: {result[key]}")

try:
    broadcast_to_gateway_offset = 253
    broadcast_parts = result["Broadcast_IP"].split(".")

    if len(broadcast_parts) != 4:
        raise ValueError("广播地址格式错误")

    last_octet = int(broadcast_parts[-1])

    gw_last_octet = last_octet - broadcast_to_gateway_offset
    
    if gw_last_octet < 1:
        print("计算出的网关IP最后一位小于1，可能不合理")
        exit(1)
        # raise ValueError(f"网关地址最后一位 {gw_last_octet} 不合理")
        
    broadcast_parts[-1] = str(gw_last_octet)
    gw_ipv4 = ".".join(broadcast_parts)
    
except (ValueError, IndexError) as e:
    print(f"解析广播地址时出错: {e}")
    exit(1)

print(f"\n我们假设网关IP为网段的第二位，计算得: {gw_ipv4}\n")

ping_command = f"ping {gw_ipv4} -c 1"

ping_output = os.popen(ping_command).read()

if re.search(r"(\d+) received, 0% packet loss", ping_output):
    print("网关可达 ")
else:
    print("网关不可达")

# 可选：显示 Ping 详细结果（调试用）
# print("\n📋 Ping 详细输出：")
# print(ping_output)