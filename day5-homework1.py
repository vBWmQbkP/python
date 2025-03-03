# import os
# import re
# route_n_result = os.popen("route -n").read()
#
# gateway_result = re.findall(r'((?:\d{1,3}.){3}\d{1,3})\s+0.0.0.0\s+UG', route_n_result)
#
# if gateway_result:
#     gateway = gateway_result[0]
#     print(f'网关为:{gateway}')
# else:
#     print("no gateway")

#===kimi=====================================================================================
# import subprocess
# import re
#
# def get_gateway():
#     try:
#         # 执行 route -n 命令并获取输出
#         route_n_result = subprocess.check_output(["route", "-n"]).decode('utf-8')
#
#         # 编译正则表达式
#         gateway_pattern = re.compile(r'((?:\d{1,3}\.){3}\d{1,3})\s+0\.0\.0\.0\s+UG')
#
#         # 查找所有匹配的网关
#         gateway_result = gateway_pattern.findall(route_n_result)
#
#         if gateway_result:
#             # 返回第一个匹配的网关
#             return gateway_result[0]
#         else:
#             return None
#     except subprocess.CalledProcessError as e:
#         print(f"命令执行失败: {e}")
#         return None
#     except Exception as e:
#         print(f"发生错误: {e}")
#         return None
#
# # 调用函数并打印结果
# gateway = get_gateway()
# if gateway:
#     print(f'网关为: {gateway}')
# else:
#     print("no gateway")

#===deepseek===============================================================================
import re
import subprocess

def get_gateway():
    try:
        # 执行route -n命令并捕获输出
        output = subprocess.check_output(['route', '-n'], text=True, stderr=subprocess.STDOUT)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None

    # 使用正则表达式匹配默认网关行
    gateway_pattern = re.compile(
        r'^0\.0\.0\.0\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+0\.0\.0\.0\s+.*[UG].*',
        re.MULTILINE
    )
    matches = gateway_pattern.findall(output)

    return matches[0] if matches else None

if __name__ == '__main__':
    gateway = get_gateway()
    print(f'网关为:{gateway}' if gateway else 'no gateway')