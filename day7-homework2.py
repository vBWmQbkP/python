# import os
#
# # 获取当前工作目录
# current_directory = os.getcwd()
# print(current_directory)
# # 定义要查找的关键字
# keyword = "qytang"
#
# # 遍历当前目录下的所有文件
# for file_name in os.listdir(current_directory):
#     # 检查是否是文件（排除文件夹）
#     if os.path.isfile(file_name):
#         # 打开文件并读取内容
#         with open(file_name, 'r', encoding='utf-8') as file:
#             try:
#                 content = file.read()
#                 # 检查文件内容是否包含关键字
#                 if keyword in content:
#                     print(f"文件 '{file_name}' 包含关键字 '{keyword}'")
#             except UnicodeDecodeError:
#                 # 如果文件不是文本文件，跳过
#                 print(f"文件 '{file_name}' 无法读取或不是文本文件，已跳过")
#==========================================================================
# import os
#
# # 自定义工作目录
# # custom_directory = input("请输入要搜索的目录路径：")  # 用户输入自定义目录
# custom_directory = "/python_basic/test"
# # 验证目录是否存在
# if not os.path.exists(custom_directory):
#     print(f"目录 '{custom_directory}' 不存在，请检查路径是否正确！")
#     exit()
#
# # 切换到自定义工作目录
# os.chdir(custom_directory)
#
# # 定义要查找的关键字
# keyword = "qytang"
#
# # 遍历当前目录下的所有文件
# for file_name in os.listdir(os.getcwd()):
#     # 检查是否是文件（排除文件夹）
#     if os.path.isfile(file_name):
#         # 打开文件并读取内容
#         with open(file_name, 'r', encoding='utf-8') as file:
#             try:
#                 content = file.read()
#                 # 检查文件内容是否包含关键字
#                 if keyword in content:
#                     print(f"文件 '{file_name}' 包含关键字 '{keyword}'")
#             except UnicodeDecodeError:
#                 # 如果文件不是文本文件，跳过
#                 print(f"文件 '{file_name}' 无法读取或不是文本文件，已跳过")
#==========================================================================
# import os
#
# # # 自定义工作目录
# # custom_directory = input("请输入要搜索的目录路径：")  # 用户输入自定义目录
# #
# # # 验证目录是否存在
# # if not os.path.exists(custom_directory):
# #     print(f"目录 '{custom_directory}' 不存在，请检查路径是否正确！")
# #     exit()
#
# custom_directory = "/python_basic/test"
# # 切换到自定义工作目录
# os.chdir(custom_directory)
#
# # 定义要查找的关键字
# keyword = "qytang"
#
# # 用于存储包含关键字的文件名
# matching_files = []
#
# # 遍历当前目录下的所有文件
# for file_name in os.listdir(os.getcwd()):
#     # 检查是否是文件（排除文件夹）
#     if os.path.isfile(file_name):
#         # 打开文件并读取内容
#         with open(file_name, 'r', encoding='utf-8') as file:
#             try:
#                 content = file.read()
#                 # 检查文件内容是否包含关键字
#                 if keyword in content:
#                     matching_files.append(file_name)
#             except UnicodeDecodeError:
#                 # 如果文件不是文本文件，跳过
#                 continue
#
# # 输出结果
# print("文件中包含 'qytang' 关键字的文件为：")
# for file_name in matching_files:
#     print(f"{file_name:>10}")
#================
#交
import os

custom_directory = "/python_basic/test"
os.chdir(custom_directory)

keyword = "qytang"

matching_files = []

for file_name in os.listdir(os.getcwd()):
    if os.path.isfile(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            try:
                content = file.read()
                if keyword in content:
                    matching_files.append(file_name)
            except UnicodeDecodeError:
                continue

print("文件中包含 'qytang' 关键字的文件为：")
for file_name in matching_files:
    print(f"{file_name:>10}")

os.chdir('..')
for root , dirs, files in os.walk("test", topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))
os.removedirs("test")