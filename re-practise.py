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

str5 = re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+1.1.1","192.168.1.1 1.1.1").group(0)
print(str5)

# if str5:
# 	match = str5.group()
# 	print(match)
# else:
#     print("没有找到匹配项")