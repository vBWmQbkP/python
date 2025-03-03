# a = 'test1'
# b = "test2"
# c = '''span's
# test3'''
# print(a)
# print(b)
# print(c)

# d = a+b+c
# e = "a" 'b' "c"
# f = a*3
# g = len(c)
# print(d)
# print(e)
# print(f)
# print(g)

# print(r"C:\new\test\bin")

# myjob = "hacker"
# for c in myjob:
#     print(c,end=" ")
#
# str = "hello world"
# print(str[0])
# print(str[-1])

# print(str[0:5])
# print(str[:-1])
# new_str = str[:3] + "A" + str[4:]
# print(new_str)
#
# print(str.upper())
#
# print(dir(str))

# str0 = "hello world"
# print(str0.upper())
#
# str1 = "hello world"
# new_str1 = str1.replace("hello", "world")
# print(new_str1)
# print(str1)

# str2 = "hello world"
# print(str2.capitalize())

# str3 = "hello world"
# print(str3.find("world"))

# str4 = "hello world"
# print(str4.split( ))
#
# str5 = " \t \n \r  hello world \t \n \r  "
# print(str5.strip(), len(str5.strip()))
# print(str5.lstrip(), len(str5.lstrip()))
# print(str5.rstrip(), len(str5.rstrip()))

# str6 = "hello world"
# print("A".join(str6))

# list1 = ["A", "B", "C"]
# print("".join(list1))

# str7 = "hello world"
# list2 = list(str7)
# list2[4] = "A"
# print(''.join(list2))

# print('That is %d %s bird' % (1, 'dead'))
# print('That is %d dead bird ' % 1)
# print('That is 1 %s bird ' % 'dead')

# str8 = 12311111111111112
# print("%o" % str8)

# str9 = 65
# print(chr(str9))
# print("%c" % str9)
#
# str10 = 2500
# print(chr(str10))
# print("%c" % str10)

# str11 = 65
# print("hello",repr(str11))
# print("%r" % str11)

# str12 = 123.123
# print("%i" % str12)
# print(int(str12))

# str13 = 11111111111111111123.123
# print("%G" % str13)
# print("The percentage is %d%%" % 10)

# tmp = "{qytang}，{0} and {cisco}"                   #定义格式
# str14 = tmp.format("A", qytang=1, cisco=3)     #字符串格式化
# print(str14)

# str15 = '{0:5}, {1:5} and {2:5}'.format("1", "A", "3")
# print(str15)

# tmp1 = "{}，{} and {}"                   #定义格式
# str16 = tmp1.format("1", "A", "3")     #字符串格式化
# print(str16)

# str_format = '{local1},{local2},{local3}'
# str17 = str_format.format(**{"local1":"qytang","local2":"test","local3":"cisco"})
# print(str17)
#
# str_format1 = '{local1:10},{local2:10},{local3:10}'
# str18 = str_format1.format(**{"local1":"qytang","local2":"test","local3":"cisco"})
# print(str18)

# str_format2 = '{local1:>10},{local2:^10},{local3:<10}'
# str19 = str_format2.format(**{"local1":"qytang","local2":"test","local3":"cisco"})
# print(str19)
#
# import sys
# str22 = sys.platform
# print(str22)
# mydict= dict([("kind", "laptop")])
# str20 = "{0.platform:>10}={1[kind]:<10}".format(sys, mydict)
# print(str20)
#
# kind = "kind"
# my_dict = {"kind":"laptop"}
# print(my_dict["kind"])

# format3 = "{0:f},{1:^10.2f},{2:010.3f},{3:>10.4f}"
# str21 = format3.format(1.111,2.222,3.333,4.44)
# print(str21)

# local1 = "qyt"
# local2 = "123"
# local3 = "cisco"
# str22 = f'{local1} {local2} {local3}'
# print(str22)
