# print("hello world")

# #for循环输出
# myjob = "hacker"
# for c in myjob:
#     print(c)

# str1 = "hello world"
# #切片
# #第0位
# print(str1[0])
# #最后一位
# print(str1[-1])

# #上边界包含，下边界不包含
# #第0位到第4位
# print(str1[0:5])
# #到最后第2位
# print(str1[:-1])
# #全部
# print(str1[:])
# print(str1)

# #修改字符串
# new_str1 = str1[:3] + "A" + str1[4:]
# print(new_str1)

# #首字母大写
# print(str1.capitalize())

# #字符串全小写
# print(str1.lower())
# #字符串全大写
# print(str1.upper())

# #将变量中的hello都替换成world
# new_str2 = str1.replace("hello", "world")
# print(new_str2)

# #分割字符串,以" "空格分割,也可以依据其他的分割
# print(str1.split())
# print(str1.split(" "))

# #查找字符串第一个匹配的字母的位置,从0开始计数，不会向后匹配
# print(str1.find("o"))

# str2 = "   hello world 4    "
# #删除两头的空格
# print(str2.strip())
# print(str2.strip()[-1])

# #删除左边空格
# print(str2.lstrip())
# #删除右边空格
# print(str2.rstrip())

# str3 = " \t \n \r  hello world \t \n \r  "
# print(str3)

# #计算字符串长度
# str5 = "     hello world     "
# print(str5.strip(), len(str5.strip()))
# print(str5.lstrip(), len(str5.lstrip()))
# print(str5.rstrip(), len(str5.rstrip()))

# #修改字符串方法2
# str7 = "hello world"
# list2 = list(str7)
# list2[4] = "A"
# print(list2)
# #这里由于原本的字符串被转换成了列表
# #因此需要用join重新连接成字符串
# print(''.join(list2))

# #拼接字符串,使用A连接字符串中的字符
# str6 = "hello world"
# print("A".join(str6))

# #拼接列表,连接列表中的字符串
# list1 = ["A", "B", "C"]
# print("".join(list1))

# #拼接列表,使用空格连接列表中的字符串
# list2 = ["CC","DD","EE"]
# print(" ".join(list2))

# #拼接列表,使用空格连接列表中的字符串
# list3 = ["CA","bD","3E"]
# print(".".join(list3))

# #chr()函数
# #一个整数（代表 Unicode 码点）转换为对应的单个字符
# print(chr(65))
# print("%c" % 65)

# print(chr(2500))
# print("%c" % 2500)

# print(chr(97))
# print(chr(8364))
# print(chr(128512))


# # % 字符串格式化
# #%s 字符串占位符
# print('That is 1 %s bird ' % 'dead')
# #%d 数字占位符
# print('That is %d dead bird ' % 1)
# print('That is %u dead bird ' % 1)

# print('That is %d %s bird' % (1, 'dead'))

# print("this is %d" %(-1))
# print("this is %u" %(-1))

# # 浮点数
# print("this is %.1f" %(-1))

# print("The percentage is %d%%" % 10)

# print('That is %r dead bird ' % 1)

# #左对齐
# print("%-10d" %(1000))

# #验证 repr()函数会显示字符串的官方表示 包括引号和空格
# result1 = "%-10d" %(1000)
# print(repr(result1))

# #或者可以考虑使用 len函数计算字符串长度
# print(len(result1))

# #默认是右对齐，宽度10
# print("%10d" %(1000))

# #右对齐，宽度10，补0
# print("%010d" %(1000))

# #左对齐，宽度10，补0 该方式无法实现,使用f-string可以
# print("%0-10d" %(1000))

# # .format 字符串格式化 way2
# tmp = "{A}, {0} and {cisco}"
# str10 = tmp.format("A",A=111,cisco=333)
# print(str10)

# # 定义字符串位置 , 宽度
# str11 = "{0:5},{1:5} and {2}".format("1","2","3")
# print(str11)

# #宽度10
# tmp1 = "{:10}，{:10} and {:10}"
# str12 = tmp1.format("1111", "AAAA", "3333")
# print(str12)

# #使用字典解包
# # **操作符的作用是讲字典解包 将其键值对 作为关键字参数传递给函数
# str_format = '{local1},{local2},{local3}'
# str17 = str_format.format(**{"local1":"qytang","local2":"test","local3":"cisco"})
# print(str17)

# #使用字典解包，宽度10,默认左对齐
# str_format1 = '{local1:10},{local2:10},{local3:10}'
# str13 = str_format1.format(**{"local1":"qytang","local2":"test","local3":"cisco"})
# print(str13)

# #使用字典解包，宽度10，居中对齐
# str_format1 = '{local1:^10},{local2:^10},{local3:^10}'
# str14 = str_format1.format(**{"local1":"qytang","local2":"test","local3":"cisco"})
# print(str14)

# #使用字典解包，宽度10,右对齐
# str_format1 = '{local1:>10},{local2:>10},{local3:>10}'
# str15 = str_format1.format(**{"local1":"qytang","local2":"test","local3":"cisco"})
# print(str15)

# str_format2 = '{local1:>10},{local2:^10},{local3:<10}'
# str19 = str_format2.format(**{"local1":"qytang","local2":"test","local3":"cisco"})
# print(str19)

# 
# import sys

# str20 = "{0.platform:>10}={1[kind]:<10}".format(sys, dict(kind="laptop"))
# print(str20)

# # 创建一个字典 dict(kind="laptop") 等价于 {"kind": "laptop"}
# print(sys, dict(kind="laptop"))
# print(sys, {"kind": "laptop"})
# print(sys)
# print(sys.platform)

# # 0和1表示位置参数索引 表示元组中的第0 和第1位
# # [kind] 是一个键查找/索引操作
# str_format3 = "{0.platform:>10}={1[kind]:<10}"
# str21 = str_format3.format(sys, dict(kind="laptop"))
# print(str21)

# #浮点数
# #居中对齐,小数点2位,宽度10,填充空格
# #小数点3位,宽度10,填充0
# # 这里设计了对齐的隐含规则 指定非空格填充字符如:0 对齐方式会自动变为右对齐
# #右对齐,小数点4位,宽度10,
# str_format4 = "{0:f}, {1:^10.2f}, {2:010.3f}, {3:>10.4f}"
# str22 = str_format4.format(1.111, 2.222, 3.333, 4.444)
# print(str22)


# # f-string 字符串格式化 python3.6引入
# value= 10
# str31 = (f"The percentage is {value}%")
# print(str31)

# value = 1000
# result = "{0:<010d}".format(value)
# print(f"'{result}'")  # 输出: '1000000000'

# str32 = 333.3
# str33 = 123.3
# str34 = 666

# #str32:1<10.2f
# # 1 填充1
# # < 左对齐，^ 居中 > 右对齐
# # 10 宽度10
# # .2f 浮点数,小数2位
# str35 = f"{str32:1<10.2f} {str33:^10.2f} {str34:>10}"
# print(str35)

# str36 = "test1"
# str37 = "test22"
# str38 = "test3"

# str39 = f"{str36:<010} {str37:^010} {str38:>010}"
# print(str39)

# #正则
# import re

# #re.match() 从头往后开始匹配 匹配成功返回一个match对象 匹配失败返回none
# # r""表示原始字符串 字符串内的反斜杠不进行转义，正则表达式收到的时候会进行转义\.变为. 
# # 正则表达式中使用.将会匹配除\n以外的任意单个字符
# # 这里使用\.的目的是严格匹配. 没有\.的话就是模糊匹配
# str1 = re.match(r"cmd\.exe","cmd.exe")
# print(str1)
# print(str1.group())

# str2 = re.match(r"cmd.exe","cmd1exe")
# print(str2)
# print(str2.group())

# import re
# str2 = re.match(r"qwe","qweqwe1231asdfqse").group()
# print(str2)

# re.match(pattern, string, flags=0)
# re.match 只从头开始匹配pattern 不会在整个字符串中搜索
# re.search(pattern, string, flags=0)
# re.search扫描整个string 找到第一个与pattern匹配的子字符串
# import re
# str3 = re.search(r"(qse)$","qweqwe1231asdfqse")

# if str3:
#     str4 = str3.groups()
#     print(str4)
# else:
#     print("none")


# # group()返回匹配到的整个字符串
# import re

# text = "The price is $123.45."
# # 匹配美元符号后跟数字和小数点
# pattern = r"\$\d+\.\d{2}"

# match = re.search(pattern, text)
# if match:
#     full_match = match.group() # 或 match.group(0)
#     print(f"Full match found: {full_match}") # 输出: Full match found: $123.45
# else:
#     print("No price found.")

# 这里 r"(\d{4})-(\d{2})-(\d{2})" 使用()可以获取到年月日三个独立部分
# 加了括号之后可以通过match.group(1)-(3)来分别获取所需的内容

# import re

# # 从日期字符串中提取年、月、日
# date_text = "Today is 2024-06-18."
# # (\d{4}) - 组 1: 匹配四位年份
# # -       - 匹配字面量连字符
# # (\d{2}) - 组 2: 匹配两位月份
# # -       - 匹配字面量连字符
# # (\d{2}) - 组 3: 匹配两位日期
# date_pattern = r"(\d{4})-(\d{2})-(\d{2})"

# match = re.search(date_pattern, date_text)
# if match:
#     print(match.group())
#     year = match.group(1)
#     month = match.group(2)
#     day = match.group(3)
#     print(f"Year: {year}, Month: {month}, Day: {day}") # 输出: Year: 2024, Month: 06, Day: 18
# else:
#     print("Date not found in the expected format.")


# 也可以使用match.groups()获取所有捕获组内容,作为一个元组
# # match仅匹配字符串开头/从开头开始匹配字符串
# import re

# date_text2 = "Today is 2025-07-19."
# date_pattern2 = r"\w+\s\w+\s(\d{4})-(\d{2})-(\d{2})"
# match = re.match(date_pattern2, date_text2)

# if match:
#     str1 = match.groups()
#     print(str1)
# else:
#     print(0)

# # search匹配字符串中任意位置的第一个匹配项
# import re

# date_text2 = "Today is 2025-07-19."
# date_pattern2 = r"(\d{4})-(\d{2})-(\d{2})"
# match = re.search(date_pattern2, date_text2)

# if match:
#     str1 = match.groups()
#     print(str1)
# else:
#     print(0)


# # groups()返回一个元组 包含所有捕获组匹配到的字符串 不包含group(0)即整个匹配
# # groups()只会返回被括号包围的部分, 由于空格部分 \s+ 没有匹配则不会返回结果
# import re
# match = re.match(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(1.1.1)","192.168.1.1 1.1.1")
# if match:
#     str5 = match.groups()
#     print(str5)
# else:
#     print("没有找到匹配项")

# import re
# match = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(1.1.1)","192.168.1.1 1.1.1")
# if match:
#     str5 = match.groups()
#     print(str5)
# else:
#     print("没有找到匹配项")


# # findall会找到所有不重叠的匹配项,从整个字符串中
# # re.findall(pattern, string, flags=0)
# import re

# pattern1 = r'fox'
# result1 = re.findall(pattern1, "foxefoxs")
# print(result1)
	
# pattern2 = r'\bfox'
# result2 = re.findall(pattern2, "foxbbbbbbbbbb")
# print(result2)
	
# pattern3 = r'fox\b'
# result3 = re.findall(pattern3, "aafoxaaaaafox")
# print(result3)
	
# pattern4 = r'fox\b'
# result4 = re.findall(pattern4, "fox")
# print(result4)

# # 正则表达式 | 或
# import re

# str1 = re.match(r"root|Root","root")
# if str1:
#     print(str1.group())
# else:
#     print(none)

# import re

# str2 = re.match(r"([r|R]oot)","root")
# if str2:
#     str3_tuple = str2.groups()
#     print(str3_tuple)

#     str3 = str3_tuple[0]
#     print(str3)
#     print(str3_tuple[0])
# else:
#     print(0)

# # 测试匹配IP地址
# # 匹配开头的IP地址
# import re

# str1 = "224.0.0.1 192.178.0.1 192.162.132.3"

# match_template = r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'

# str2 = re.match(match_template,str1)

# if str2:
#     str3 = str2.group()
#     print(str3)
# else:
#     print(0)

# # 匹配第一个IP地址
# import re

# str1 = "224.0.0.1 192.178.0.1 192.162.132.3"

# match_template = r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'

# str2 = re.search(match_template,str1)

# if str2:
#     # 输出整个正则表达式匹配到的内容
#     print(str2.group(0))
#     # 返回第1个捕获组匹配的内容， ((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.)
#     # 整体匹配了224. 0. 0. 三个部分
#     # 由于{3}进行迭代匹配,只会保留最后一次匹配的结果 0.
#     print(str2.group(1))
#     # 第2个捕获组的内容 (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)
#     # 整体匹配了224 0 0 三个部分
#     # 由于{3}进行迭代匹配,只会保留最后一次匹配的结果 0
#     print(str2.group(2))
#     # 第3个捕获组的内容 (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)
#     # 整体匹配 1
#     print(str2.group(3))


# import re

# str1 = "224.0.0.1 192.178.0.1 192.162.132.3"

# match_template = r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?\d{1,2})\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?\d{1,2})'

# str2 = re.search(match_template,str1)

# if str2:
#     # 输出整个正则表达式匹配到的内容
#     print(str2.group(0))
#     print(str2.group())
#     str3 = str2.group()
#     print(str3)
# else:
#     print(0)


# # group()使用括号进行匹配,返回的结果总是一个字符串

# # 使用groups() 
# # groups()需要使用括号在模板中进行匹配，返回的结果是元组
# # 针对不想匹配的项如果使用了()需要使用(?：)进行不匹配
# import re

# str1 = "224.0.0.1 192.178.0.1 192.162.132.3"

# match_template = r'((?:(?:25[0-5]|2[0-4][0-9]|[01]?\d{1,2})\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?\d{1,2}))'

# str2 = re.search(match_template,str1)

# if str2:
#     print(str2.groups())
#     str3_tuple = str2.groups()
#     str3 = str3_tuple[0]
#     print(str3)
# else:
#     print(0)



# # 使用findall产生的结果是列表
# import re

# str1 = "224.0.0.1 192.178.0.1 192.162.132.3"

# match_template = r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'

# str2 = re.findall(match_template,str1)

# if str2:
#     print(str2)
# else:
#     print(0)

# #way2
# import re

# str1 = "224.0.0.1 192.178.0.1 192.162.132.3"

# # 可以使用原始模式，因为 finditer 返回匹配对象
# match_template = r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'

# # re.finditer 返回一个匹配对象的迭代器
# matches = re.finditer(match_template, str1)

# found = False
# for match in matches: # 遍历每个匹配对象
#     found = True
#     str3 = match.group() # 对匹配对象调用 .group()
#     print(str3)

# if not found:
#     print(0)








# import random

# #定义个列表
# ip_parts = []
# #for循环执行4次 , 其中 _ 只是一个临时变量的名字,可以换成任意其他名字
# for _ in range(4):
#     #产生随机数
#     random_part = str(random.randint(1, 255))
#     #产生的随机数添加到列表末尾
#     ip_parts.append(random_part)
#     print(ip_parts)
# #这里可以看到ip_parts是列表的形式,总共4个字符串
# #使用join函数将列表的值连成字符串 使用“.”连接
# a = ".".join(ip_parts)
# print(a)

# # 序列解包案例一
# _, minute, second = "0:01:09".split(":")
# print(minute)  # 01
# # 使用下划线_ Python中约定为 临时变量/被忽略的值
# # 在交互模式中, _ 有特殊用途 会自动保存上一次的计算结果, 因此交互模式下不建议用来丢弃变量
# # 在脚本中, 常用于忽略值

# # 序列解包 多个值忽略
# first, *_, last = [1, 2, 3, 4, 5]
# print(first)  # 1
# print(last)   # 5
# # 中间的 2,3,4 被忽略

# # 序列解包 只提取指定位置的值
# *_, third = ["a","b","c"]
# print(third)

# # 掐头去尾巴
# _, *middle, _ = [10, 20, 30, 40, 50]
# print(middle)  # [20, 30, 40]

# # *_用于 收集多余的元素 其实*任何变量名都可以 最后会放到变量列表中

# first, *rest = [1, 2, 3, 4]
# print(first)  # 1
# print(rest)   # [2, 3, 4]  ← 是一个列表

# # 实际案例 解析路径
# path = "/home/user/documents/report.txt"
# *_, filename = path.split("/")
# print(filename)

# x = "hello"
# print(x[::-1])

# # sequence[start:stop:step]
# # start 起始索引
# # 第一个冒号前面没有内容 当start部分被省略
# # 若step是正数 默认从序列的开头（索引0）开始
# # 若step是负数 默认从序列的末尾（索引-1）开始

# # stop 结束索引
# # 第二个冒号前面没有内容 当stop部分被省略
# # 若step是正数 默认从序列的末尾（索引-1）结束
# # 若step是负数 默认从序列的开头（索引0）结束

# # step 步长
# # step = 1 从start开始, 以步长1向后（正向）遍历 直到stop
# # step = 2 从start开始, 以步长2向后（正向）遍历 跳过中间元素 直到stop
# # step = -1 从start开始, 以步长1向前（反向）遍历 直到stop
# # step = -2 从start开始, 以步长2向前（反向）遍历 跳过中间元素 直到stop

# ==============
# from ipaddress import ip_network

# # 已知网络地址和子网掩码
# net = ip_network("192.168.1.128/25")
# gateway = list(net.hosts())[0]  # 通常是 .1
# print(gateway)  # 192.168.1.1

# try:
#     number = int("abc")  # 这里会出错
# except ValueError as e:
#     print(f"出错了：{e}") # e 是 Python 自动生成的 ValueError 异常对象，它包含错误信息

# 标准库
from ipaddress import ip_interface

# 输入一个 IP 地址 + 子网掩码
ip_with_mask = "192.168.1.100/24"  # 或 "192.168.1.100/255.255.255.0"
ip = ip_interface(ip_with_mask)

print(ip)
print(f"IP 地址: {ip.ip}")
print(f"子网掩码: {ip.netmask}")
print(f"网络地址: {ip.network.network_address}")
print(f"广播地址: {ip.network.broadcast_address}")
print(f"可用主机范围: {list(ip.network.hosts())[0]} ~ {list(ip.network.hosts())[-1]}")
print(f"总主机数: {ip.network.num_addresses - 2} (除去网络地址和广播地址)")