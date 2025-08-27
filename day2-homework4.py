# department1 = "Security"
# department2 = "Python"
# depart1_m = "cq_bomb"
# depart2_m = "qinke"
# COURSE_FEES_SEC = 456789.12456
# COURSE_FEES_Python = 1234.3456
#
# line1 = "Department1 name:%-10s Manager:%-10s COURSE FEES:%-10.2f The End!" % (department1,depart1_m,COURSE_FEES_SEC)
# line2 = f"Department2 name:{department2:<10} Manager:{depart2_m:<10} COURSE FEES:{COURSE_FEES_Python:<10.2f} The End!"
#
# length = len(line1)
# print("="*length)
# print(line1)
# print(line2)
# print("="*length)

# line2 = "Department2 name:%-10s Manager:%-10s COURSE FEES:%-10.2f The End!" % (department2,depart2_m,COURSE_FEES_Python)
# line3 = "{0}{1:10}{2}{3:10}{4}{5:<10.2f}{6}".format("Department1 name:",department1," Manager:",depart1_m," COURSE_FEES:",COURSE_FEES_SEC," The End!")
# print(line3)


# # way2-deepseek
# #结构化部门数据，便于扩展和维护
# departments = [
#     {"num": 1, "name": "Security", "manager": "cq_bomb", "fee": 456789.12456},
#     {"num": 2, "name": "Python",   "manager": "qinke",   "fee": 1234.3456}
# ]

# # 统一格式模板
# FORMAT_TEMPLATE = "Department{num} name:{name:<10} Manager:{manager:<10} COURSE FEES:{fee:<10.2f} The End!"

# # print(FORMAT_TEMPLATE)

# # 生成所有行并计算最大长度
# # lines = [FORMAT_TEMPLATE.format(**dept) for dept in departments]

# lines = []
# for dept in departments:
#     # **dept将字典解包传给.format()
#     # 相当于FORMAT_TEMPLATE.format(num=1, name="Security", manager="cq_bomb", fee=456789.12456)
#     line_part = FORMAT_TEMPLATE.format(**dept)
#     # print(line_part)
    
#     #每次循环生成的一行格式化后的字符串添加到lines列表中
#     lines.append(line_part)
#     # print(lines)

# # 计算最长行的长度 way1 推荐
# # for line in lines 遍历lines 进行循环
# # (len(line) for line in lines)是一个生成器表达式 计算每行字符串长度 生成一个长度序列
# # 生成器表达式是pyhton语言内置的语法特性
# # (表达式 for 变量 in 可迭代对象 if 条件)
# # (expression for variable in iterable)
# # max()函数计算其中的最大值
# max_length = max(len(line) for line in lines)

# # 列表推导式 和 生成器表达式 很相似 只是把[]换成了()
# # 圆括号，表示这是一个生成器表达式
# # 表达式expression表示对每个元素进行的操作
# # 变量variable 临时变量名
# # 可迭代对象 iterable 如 list,range,str,tuple等能被for循环遍历的对象
# # if 条件 可选 只有满足条件的元素才会被处理

# # 1. 列表推导式：立即生成完整列表
# squares_list = [x**2 for x in range(4)]
# print(squares_list)  # 输出: [0, 1, 4, 9]
# print(type(squares_list))  # <class 'list'>

# # 2. 生成器表达式：返回一个生成器对象
# squares_gen = (x**2 for x in range(4))
# print(squares_gen)   # <generator object <genexpr> at 0x...>
# print(type(squares_gen))  # <class 'generator'>
# # 将可迭代对象转换成列表,会不变的调用next()函数
# # next()函数 作用是：从一个迭代器（iterator）中获取下一个值。
# print(list(squares_gen))

# # 生成器优势 节省内存 ；使用列表推导式可能会爆内存
# # 适合用完即弃的场景 不适合需要反复访问的数据
# # 本质上是一个迭代器iterator
# # 不包含所有数据,而是一个能计算出数据的机器
# # 懒惰, 不取值,就不会进行计算； 且只能遍历一次


# # way2
# # 定义列表
# line_length = []
# # 将每行的长度分别计算, 添加到line_length列表中
# for line in lines:
#     # 计算单行的长度
#     line_length_part = len(line)
#     # 将计算的长度值添加到 line_length列表
#     line_length.append(line_length_part)
# # 再通过max函数计算出最大值
# max_length = max(line_length)

# # way 3
# # 初始化 max_length 为 0
# max_length = 0
# # 使用普通的 for 循环遍历 lines 列表
# for line in lines:
#     # 获取当前行的长度
#     current_length = len(line)
#     # 如果当前行的长度大于 max_length，则更新 max_length
#     if current_length > max_length:
#         max_length = current_length

# # 输出结果
# print("=" * max_length)
# print('\n'.join(lines))
# print("=" * max_length)



# department1 = "Security"
# department2 = "Python"
# depart1_m = "cq_bomb"
# depart2_m = "qinke"
# COURSE_FEES_SEC = 456789.12456
# COURSE_FEES_Python = 1234.3456

# # line1 = "Department1 name:%-10s Manager:%-10s COURSE FEES:%-10.2f The End!" %(department1,depart1_m,COURSE_FEES_SEC)
# # line2 = "Department2 name:%-10s Manager:%-10s COURSE FEES:%-10.2f The End!" %(department2,depart2_m,COURSE_FEES_Python)

# line1 = f'Department1 name:{department1:<10} Manager:{depart1_m:<10} COURSE FEES:{COURSE_FEES_SEC:<10.2f} The End!'
# line2 = f'Department1 name:{department2:<10} Manager:{depart2_m:<10} COURSE FEES:{COURSE_FEES_Python:<10.2f} The End!'

# length = len(line1)
# print("="*length)
# print(line1)
# print(line2)
# print("="*length)