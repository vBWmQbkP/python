import requests
import base64

# 配置参数
fmc_ip = "172.18.6.137"  # 替换为实际FMC IP
username = "apiadmin"  # FMC管理员账号
password = "Cisc0123"  # FMC管理员密码

# 生成Base64编码的认证凭证
credentials = f"{username}:{password}".encode("utf-8")
base64_credentials = base64.b64encode(credentials).decode("utf-8")

# 构建请求
url = f"https://{fmc_ip}/api/fmc_platform/v1/auth/generatetoken"
headers = {
    "Authorization": f"Basic {base64_credentials}",
    "Content-Type": "application/json"
}

try:
    # 发送POST请求
    response = requests.post(url, headers=headers, verify=False)  # verify=False仅用于测试环境

    if response.status_code == 204:
        # 从响应头提取token
        access_token = response.headers.get("X-auth-access-token")
        refresh_token = response.headers.get("X-auth-refresh-token")

        print(f"Access Token: {access_token}")
        print(f"Refresh Token: {refresh_token}")
    else:
        print(f"认证失败，状态码: {response.status_code}")
        print(f"响应内容: {response.text}")

except requests.exceptions.RequestException as e:
    print(f"请求异常: {str(e)}")
except Exception as e:
    print(f"系统异常: {str(e)}")