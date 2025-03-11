# list1 = ['aaa', 111, (4, 5), 2.01]
# list2 = ['bbb', 333, 111, 3.14, (4, 5)]
#
# # 找出只在 list1 中的元素
# only_in_list1 = [item for item in list1 if item not in list2]
#
# # 找出只在 list2 中的元素
# only_in_list2 = [item for item in list2 if item not in list1]
#
# # 找出在两个列表中都存在的元素
# in_both_lists = [item for item in list1 if item in list2]
#
# # 打印结果
# for item in only_in_list1:
#     print(f"{item} only in List1")
#
# for item in only_in_list2:
#     print(f"{item} only in List2")
#
# for item in in_both_lists:
#     print(f"{item} in List1 and List2")

list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]

only_in_list1 = [item for item in list1 if item not in list2]

only_in_list2 = [item for item in list2 if item not in list1]

in_both_lists = [item for item in list1 if item in list2]

for item in only_in_list1:
    print(f"{item} only in List1")

for item in only_in_list2:
    print(f"{item} only in List2")

for item in in_both_lists:
    print(f"{item} in List1 and List2")