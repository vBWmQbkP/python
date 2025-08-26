#way1
# word = "Python"
# new_word = word[1:]+'-'+word[0]+'y'
# print(new_word)

# #way2-kimi
# print("Python"[1:] + '-' + "Python"[0] + 'y')
#
# #way3-deepseek
# print(f"{'Python'[1:]}-Py")

# word = input("Enter a word: ")
# new_word = word[1:]+'-'+word[0]+'y'
# print(new_word)

# way2-deepseek
# word = str(input("输入一个英文单词：").strip())
# new_word = word[1:]+'-'+word[0]+'y'
# print("新的单词是："+new_word)



# import re

# word = str(input("输入一个英文单词：").strip())

# if not word:
#     print("输入不能为空,请输入一个英文单词")
    
# if re.match(r'^[a-zA-Z]+$', word):
#     new_word = word[1:]+"-"+word[0]+"y"
#     print(new_word)
# else:
#     print("只能请输入一个英文单词")

import re

while True:
    word = input("输入一个英文单词：").strip()
    
    if not word:
        print("输入不能为空，请输入一个英文单词")
        continue
    
    if re.match(r'^[a-zA-Z]+$', word):
        new_word = f'{word[1:]}-{word[0]}y'
        print(new_word)
        break
    else:
        print("错误：只能输入一个英文单词（只允许包含字母a-z, A-Z）")


# import re

# # 当为真的时候执行循环
# while True:
#     word = input("输入一个英文单词：").strip()
    
#     # 检查是否为空
#     # if not word: 等价 if word == "":
#     if not word:
#         print("输入不能为空，请输入一个英文单词")
#         continue # 跳过下面的代码，直接回到 while 开始
    
#     # 检查是否只包含英文字母
#     if re.match(r'^[a-zA-Z]+$', word):
#         new_word = word[1:] + "-" + word[0] + "y"
#         print(new_word)
#         break # 退出循环
#     else:
#         print("错误：只能输入一个英文单词（只允许包含字母a-z, A-Z）")
