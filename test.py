print("hello world")

#for循环输出
myjob = "hacker"
for c in myjob:
    print(c)

str1 = "hello world"
#切片
#第0位
print(str1[0])
#最后一位
print(str1[-1])

#上边界包含，下边界不包含
#第0位到第4位
print(str1[0:5])
#到最后第2位
print(str1[:-1])
#全部
print(str1[:])
print(str1)

#修改字符串
new_str1 = str1[:3] + "A" + str1[4:]
print(new_str1)

#首字母大写
print(str1.capitalize())

#字符串全小写
print(str1.lower())
#字符串全大写
print(str1.upper())

#将变量中的hello都替换成world
new_str2 = str1.replace("hello", "world")
print(new_str2)

#分割字符串,以" "空格分割,也可以依据其他的分割
print(str1.split())
print(str1.split(" "))

#查找字符串第一个匹配的字母的位置,从0开始计数，不会向后匹配
print(str1.find("o"))

str2 = "   hello world 4    "
#删除两头的空格
print(str2.strip())
print(str2.strip()[-1])

#删除左边空格
print(str2.lstrip())
#删除右边空格
print(str2.rstrip())

str3 = " \t \n \r  hello world \t \n \r  "
print(str3)

#计算字符串长度
str5 = "     hello world     "
print(str5.strip(), len(str5.strip()))
print(str5.lstrip(), len(str5.lstrip()))
print(str5.rstrip(), len(str5.rstrip()))

#修改字符串方法2
str7 = "hello world"
list2 = list(str7)
list2[4] = "A"
print(list2)
#这里由于原本的字符串被转换成了列表
#因此需要用join重新连接成字符串
print(''.join(list2))

#拼接字符串,使用A连接字符串中的字符
str6 = "hello world"
print("A".join(str6))

#拼接列表,连接列表中的字符串
list1 = ["A", "B", "C"]
print("".join(list1))

#拼接列表,使用空格连接列表中的字符串
list2 = ["CC","DD","EE"]
print(" ".join(list2))

#拼接列表,使用空格连接列表中的字符串
list3 = ["CA","bD","3E"]
print(".".join(list3))

#
str9 = 65
print(chr(str9))
print("%c" % str9)
		
str10 = 2500
print(chr(str10))
print("%c" % str10)







import random

#定义个列表
ip_parts = []
#for循环执行4次 , 其中 _ 只是一个临时变量的名字,可以换成任意其他名字
for _ in range(4):
    #产生随机数
    random_part = str(random.randint(1, 255))
    #产生的随机数添加到列表末尾
    ip_parts.append(random_part)
    print(ip_parts)
#这里可以看到ip_parts是列表的形式,总共4个字符串
#使用join函数将列表的值连成字符串 使用“.”连接
a = ".".join(ip_parts)
print(a)