#way1
# word = "scallywag"
# sub_word = word[2:6]
# print(sub_word)

# #way2-kimi
# word = "scallywag"
# # 提取索引从2到5的子字符串
# start_index = 2
# end_index = 6
# sub_word = word[start_index:end_index]
# print(f"{sub_word}")
#
# #way3-deepseek
# word = "scallywag"; sub_word = word[2:6]; print(sub_word)
#
# #way4-deepseek
# (word1 := "scallywag", sub_word1 := word1[2:6], print(sub_word1))[-1]
str1 = (word3 := "scallywag", sub_word3 := word3[2:6], print(sub_word3))[1]
print(str1)
#
# #way5
# word2 = "scallywag"
# print(sub_word2:=word2[2:6])