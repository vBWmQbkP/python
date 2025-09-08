# ==========
# way2 通义千问
import re
import os

# === 1. 获取网卡信息 ===
interface_name = "ens160"
print(f"🔍 正在获取网卡 '{interface_name}' 的信息...")

# 执行 ifconfig 命令
command_output = os.popen(f"ifconfig {interface_name}").read()

# 检查输出是否为空
if not command_output.strip():
    print(f"❌ 网卡 '{interface_name}' 不存在或无输出")
    exit(1)  # 终止程序

# === 2. 定义正则表达式，提取 IPv4、子网掩码、广播地址、MAC 地址 ===
print("🧩 正在解析网络配置...")

# [\S\s]+?是非贪婪模式 尽可能少的匹配字符 匹配第一个inet就停下来
# [\S\s]+inet 在多网卡输出的时候 会跳过第一个 inet，匹配到最后一个inte，导致提取错误
# [0-9a-fA-F]{2}: MAC地址只能是十六进制数更规范
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

match = pattern.search(command_output.strip())  # 更安全

# 更健壮的错误处理
if not match:
    print("❌ 未能从 ifconfig 输出中解析出网络信息")
    # 终止程序，防止后续代码因 result 未定义而崩溃
    exit(1)

# 提取结果
result = match.groupdict()

# === 3. 打印提取的信息 ===
fields = [
    ("ipv4_address",    "IP_address"),
    ("netmask",    "Netmask"),
    ("broadcast",    "Broadcast_IP"),
    ("MAC_address",     "Mac_address"),
]

print("\n📋 解析结果：")
for label, key in fields:
    print(f"{label:<15}: {result[key]}")

# === 4. 计算网关 IP（广播地址最后一位 -253）===
print("\n⚙️  正在计算网关IP...")

# 异常处理
# try:
#     # 尝试执行的代码（可能出错）
#     pass
# except 错误类型: （根据错误类型的种类执行except的动作）
#     # 如果 try 中的代码出错了，就执行这里的代码
#     pass
try:
    broadcast_to_gateway_offset = 253
    broadcast_parts = result["Broadcast_IP"].split(".")
    # print(broadcast_parts)        # ['172', '18', '6', '255']
    
    # print(len(broadcast_parts))   # 4
    if len(broadcast_parts) != 4:
        # raise 引发异常主动制造异常
        # ValueError 表示值异常 格式不对/不符合逻辑 
        raise ValueError("广播地址格式错误")

    last_octet = int(broadcast_parts[-1])

    # 通常网关是广播地址 -1，例如 192.168.1.255 → 192.168.1.254
    gw_last_octet = last_octet - broadcast_to_gateway_offset
    
    if gw_last_octet < 1:
        print("⚠️  计算出的网关IP最后一位小于1，可能不合理")
        exit(1)
        # raise ValueError(f"网关地址最后一位 {gw_last_octet} 不合理")
        
    broadcast_parts[-1] = str(gw_last_octet)
    gw_ipv4 = ".".join(broadcast_parts)
    
except (ValueError, IndexError) as e:
    print(f"❌ 解析广播地址时出错: {e}")
    exit(1)

print(f"🌐 假设网关IP为广播地址-1，计算得: {gw_ipv4}")

# === 5. Ping 测试网关是否可达 ===
print(f"\n📡 正在 Ping 网关 {gw_ipv4} ...")

# ping 一次可能会存在误差,ping2次等待时间会增加1秒
# -c 2 发送2个数据包
# -W 1 每个包等待1秒
ping_command = f"ping {gw_ipv4} -c 2 -W 1"  # 发送2个包，超时1秒
# ping_command = f"ping {gw_ipv4} -c 1" 
ping_output = os.popen(ping_command).read()

# 判断是否收到回复（0% 丢包）
if re.search(r"(\d+) received, 0% packet loss", ping_output):
    print("✅ 网关可达 ✅")
else:
    print("❌ 网关不可达 ❌")

# 可选：显示 Ping 详细结果（调试用）
# print("\n📋 Ping 详细输出：")
# print(ping_output)