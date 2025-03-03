import re

# str1 = re.match(r"cmd\.exe","cmd.exe")
# print(str1)
# print(str1.group())


# str2 = re.match(r"^qwe","qweqwe1231asdfqse").group()
# print(str2)

# str3 = re.match(r"qwe$","qweqwe1231asdfqse").group()
# print(str3)

# match = re.search(r"qse$", "qweqwe1231asdfqse")
# if match:
#     str3 = match.group()
#     print(str3)
# else:
#     print("没有找到匹配项")

# pattern1 = r'fox'
# result1 = re.findall(pattern1, "foxes")
# print(result1)
#
# pattern2 = r'\bfox'
# result2 = re.findall(pattern2, "foxbbbbbbbbbb")
# print(result2)
#
# pattern3 = r'fox\b'
# result3 = re.findall(pattern3, "aaaaaaafox")
# print(result3)
#
# pattern4 = r'fox\b'
# result4 = re.findall(pattern4, "fox")
# print(result4)

# str5 = re.match(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(1.1.1)","192.168.1.1 1.1.1")
# # print(str5)
#
# if str5:
# 	match = str5.groups()
# 	print(match)
# else:
#     print("没有找到匹配项")

ip = "10.10.10.1/24"

ipv4_addr_pro = r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?\d{1,2})\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?\d{1,2})'

pre_exec_str = re.compile(
	rf"(?P<ip_address>unassigned|{ipv4_addr_pro})"
)

match = pre_exec_str.match(ip)

if match:
	ip_address = match.groups()
	print(ip_address[0])
else:
	print("no match")

#====================================================================================

# ip = "10.10.10.1/24"
#
# # IPv4 正则（已使用非捕获组）
# ipv4_addr_pro = r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?\d{1,2})\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?\d{1,2})'
#
# # 组合正则时，IPv4 部分不再额外包裹捕获组
# pre_exec_str = re.compile(
#     rf"(?P<ip_address>unassigned|{ipv4_addr_pro})"
# )
#
# match = pre_exec_str.match(ip)
#
# if match:
#     # 直接通过命名分组获取结果
#     ip_address = match.group("ip_address")
#     print(ip_address)  # 输出：10.10.10.1/24
# else:
#     print("no match")