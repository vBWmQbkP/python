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

# way2-deepseek
#结构化部门数据，便于扩展和维护
departments = [
    {"num": 1, "name": "Security", "manager": "cq_bomb", "fee": 456789.12456},
    {"num": 2, "name": "Python",   "manager": "qinke",   "fee": 1234.3456}
]

# 统一格式模板
FORMAT_TEMPLATE = "Department{num} name:{name:<10} Manager:{manager:<10} COURSE FEES:{fee:<10.2f} The End!"

# print(FORMAT_TEMPLATE)

# 生成所有行并计算最大长度
# lines = [FORMAT_TEMPLATE.format(**dept) for dept in departments]

lines = []
for dept in departments:
    line_part = FORMAT_TEMPLATE.format(**dept)
    lines.append(line_part)

# max_length = max(len(line) for line in lines)

# line_length = []
#
# for line in lines:
#     line_length_part = len(line)
#     line_length.append(line_length_part)
#
# max_length = max(line_length)

# 初始化 max_length 为 0
max_length = 0
# 使用普通的 for 循环遍历 lines 列表
for line in lines:
    # 获取当前行的长度
    current_length = len(line)
    # 如果当前行的长度大于 max_length，则更新 max_length
    if current_length > max_length:
        max_length = current_length

# 输出结果
print("=" * max_length)
print('\n'.join(lines))
print("=" * max_length)

