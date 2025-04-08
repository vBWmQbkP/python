import requests

fmc_ip = "172.20.5.36"  # 替换为实际FMC IP
username = "test2"  # FMC管理员账号
password = "Cisc0123"  # FMC管理员密码

auth_url = f"https://{fmc_ip}/api/fmc_platform/v1/auth/generatetoken"
response = requests.post(auth_url, auth=(username, password), verify=False)

access_token = response.headers.get("X-auth-access-token")

domain_api = f"https://{fmc_ip}/api/fmc_platform/v1/info/domain"
headers = {
    "X-auth-access-token": access_token,
    "Content-Type": "application/json"
}

response = requests.get(domain_api, headers=headers, verify=False)
if response.status_code == 200:
    domains = response.json().get("items")
    for domain in domains:
        print(f"Domain Name: {domain['name']}, UUID: {domain['uuid']}")
else:
    print(f"请求失败，状态码：{response.status_code}")