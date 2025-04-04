import requests
import warnings
from urllib3.exceptions import InsecureRequestWarning

# 禁用SSL警告（生产环境需配置证书）
warnings.filterwarnings("ignore", category=InsecureRequestWarning)

def get_si_networklist_id(fmc_ip, username, password, target_name):
    # ====== 认证流程 ======
    auth_url = f"https://{fmc_ip}/api/fmc_platform/v1/auth/generatetoken"
    try:
        auth_res = requests.post(auth_url, auth=(username, password), verify=False)
        auth_res.raise_for_status()
        access_token = auth_res.headers.get("X-auth-access-token")
        domain_uuid = auth_res.headers.get("DOMAIN_UUID")  # 网页6的DOMAIN_ID获取方式
    except Exception as e:
        print(f"认证失败: {str(e)}")
        return None

    # ====== 分页获取SI列表 ======
    headers = {"X-auth-access-token": access_token}
    si_url = f"https://{fmc_ip}/api/fmc_config/v1/domain/{domain_uuid}/object/customsiiplists"

    all_items = []
    params = {"limit": 100, "offset": 0}

    while True:
        try:
            response = requests.get(si_url, headers=headers, params=params, verify=False)
            response.raise_for_status()
            data = response.json()
            all_items.extend(data.get("items", []))

            if len(data.get("items", [])) < params["limit"]:
                break
            params["offset"] += params["limit"]
        except requests.exceptions.HTTPError as http_err:
            print(f"API请求错误: {http_err}")
            break
        except Exception as e:
            print(f"数据处理异常: {str(e)}")
            break

    # ====== 精确匹配目标列表 ======
    for item in all_items:
        if item.get("name") == target_name:
            return item.get("id")

    print(f"未找到名称为'{target_name}'的列表")
    return None

# ====== 使用示例 ======
if __name__ == "__main__":
    FMC_IP = "172.18.6.137"  # 网页6的示例IP
    USERNAME = "apiadmin"
    PASSWORD = "Cisc0123"
    TARGET_NAME = "test1_network_lists_and_feeds"

    list_id = get_si_networklist_id(FMC_IP, USERNAME, PASSWORD, TARGET_NAME)
    print(f"获取到的列表ID: {list_id}")