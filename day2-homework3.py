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
word = str(input("输入一个英文单词：").strip())
new_word = word[1:]+'-'+word[0]+'y'
print("新的单词是："+new_word)