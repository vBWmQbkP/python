#way1
word = "scallywag"
sub_word = word[2:6]
print(sub_word)

#way2-kimi
word = "scallywag"
# 提取索引从2到5的子字符串
start_index = 2
end_index = 6
sub_word = word[start_index:end_index]
print(f"{sub_word}")

#way3-deepseek
word = "scallywag"; sub_word = word[2:6]; print(sub_word)

#way4-deepseek
(word := "scallywag", sub_word := word[2:6], print(sub_word))[-1]

#way5
word = "scallywag"
print(sub_word:=word[2:6])