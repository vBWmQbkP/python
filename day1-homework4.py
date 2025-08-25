import random

#way1
# section1=random.randint(1,255)
# section2=random.randint(1,255)
# section3=random.randint(1,255)
# section4=random.randint(1,255)

# random_ipv4=str(section1)+'.'+str(section2)+'.'+str(section3)+'.'+str(section4)

# print(random_ipv4)

#way2
random_ipv4 = ".".join(str(random.randint(1, 255)) for _ in range(4))
print(random_ipv4)

# a = ".".join(str(random.randint(1, 255)) for b in range(4))
# print(a)

# #way3
# ip_parts = []

# # 使用 for 循环生成 4 个随机数
# for _ in range(4):
#     # 生成一个 1 到 255 之间的随机整数，并将其转换为字符串
#     random_part = str(random.randint(1, 255))
#     # 将生成的随机数字符串添加到列表中
#     ip_parts.append(random_part)

# # 使用 "." 将列表中的字符串连接起来，形成一个完整的 IP 地址
# a = ".".join(ip_parts)

# # 打印生成的 IP 地址
# print(a)