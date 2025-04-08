import requests

fmc_ip = "172.20.5.36"  # 替换为实际FMC IP
username = "test2"  # FMC管理员账号
password = "Cisc0123"  # FMC管理员密码

auth_url = f"https://{fmc_ip}/api/fmc_platform/v1/auth/generatetoken"
response = requests.post(auth_url, auth=(username, password), verify=False)
access_token = response.headers["X-auth-access-token"]

# 获取Domain UUID
domain_api = f"https://{fmc_ip}/api/fmc_platform/v1/info/domain"
headers = {"X-auth-access-token": access_token}
domain_response = requests.get(domain_api, headers=headers, verify=False)
domain_uuid = domain_response.json()["items"][0]["uuid"]

# 获取SI Network List
si_list_api = f"https://{fmc_ip}/api/fmc_config/v1/domain/{domain_uuid}/object/customsiiplists"
si_response = requests.get(si_list_api, headers=headers, verify=False)

if si_response.status_code == 200:
    for item in si_response.json().get("items", []):
        print(f"Name: {item['name']}, ID: {item['id']}")
else:
    print(f"请求失败，状态码：{si_response.status_code}")