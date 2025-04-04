import requests
import os
import warnings
from requests_toolbelt.multipart.encoder import MultipartEncoder
from urllib3.exceptions import InsecureRequestWarning

# 禁用SSL警告（生产环境需配置证书）
warnings.filterwarnings("ignore", category=InsecureRequestWarning)


class CiscoFMCFileUploader:
    def __init__(self, fmc_ip, username, password):
        self.base_url = f"https://{fmc_ip}/api/fmc_config/v1/domain"
        self.auth_token, self.domain_uuid = self._authenticate(fmc_ip, username, password)
        self.headers = {"X-auth-access-token": self.auth_token}  # 网页8的会话保持建议

    def _authenticate(self, fmc_ip, username, password):
        """统一认证模块（符合网页6的规范）"""
        auth_url = f"https://{fmc_ip}/api/fmc_platform/v1/auth/generatetoken"
        try:
            response = requests.post(
                auth_url,
                auth=(username, password),
                verify=False,
                timeout=10
            )
            response.raise_for_status()
            return (
                response.headers.get("X-auth-access-token"),
                response.headers.get("DOMAIN_UUID")
            )
        except requests.exceptions.HTTPError as e:
            raise ConnectionError(f"认证失败[{e.response.status_code}]: {e.response.text}")
        except Exception as e:
            raise ConnectionError(f"认证异常: {str(e)}")

    def get_si_list_id(self, target_name):
        """动态获取列表ID（基于网页7的分页策略）"""
        si_url = f"{self.base_url}/{self.domain_uuid}/object/customsiiplists"

        all_items = []
        params = {"limit": 100, "offset": 0}  # 网页7推荐的分页参数

        while True:
            try:
                response = requests.get(si_url, headers=self.headers, params=params, verify=False)
                response.raise_for_status()
                data = response.json()

                # 网页3建议的列表遍历方式
                if current_items := data.get("items"):
                    all_items.extend(current_items)
                    if len(current_items) < params["limit"]:
                        break
                    params["offset"] += params["limit"]
                else:
                    break
            except requests.exceptions.HTTPError as http_err:
                print(f"API请求错误: {http_err}")
                break
            except Exception as e:
                print(f"数据处理异常: {str(e)}")
                break

        # 精确匹配目标列表（网页9建议的精确查询方式）
        for item in all_items:
            if item.get("name") == target_name:
                return item.get("id")

        raise ValueError(f"未找到名称为'{target_name}'的列表")

    def upload_file(self, object_id, file_path, validate_only=False):
        """文件上传实现（符合网页10的multipart规范）"""
        url = f"{self.base_url}/{self.domain_uuid}/object/customsiiplists/{object_id}"

        # 网页5建议的文件操作方式
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"文件不存在: {file_path}")

        # 构建多部分编码器（网页10最佳实践）
        encoder = MultipartEncoder(
            fields={
                'name': 'test1_network_lists_and_feeds',
                'id': object_id,
                'validateOnly': str(validate_only).lower(),
                'payloadFile': (
                    os.path.basename(file_path),
                    open(file_path, 'rb'),
                    'text/plain'
                )
            },
            boundary='----WebKitFormBoundary7MA4YWxkTrZu0gW'
        )

        headers = {
        **self.headers,
        "Content-Type": encoder.content_type
        }

        try:
            response = requests.put(
                url,
                headers=headers,
                data=encoder,
                verify=False,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as e:
            error_msg = self._parse_error(e.response)
            print(f"更新失败 [{e.response.status_code}]: {error_msg}")
            return None
        except Exception as e:
            print(f"请求异常: {str(e)}")
            return None

    def _parse_error(self, response):
        """错误解析优化（基于网页9的规范）"""
        try:
            error_data = response.json()
            return error_data.get("error", {}).get("message", "未知错误")
        except ValueError:
            return f"非JSON响应: {response.text[:200]}"  # 网页9建议截断长文本


# ====== 使用示例 ======
if __name__ == "__main__":
    # 配置参数（网页3建议的配置管理方式）
    CONFIG = {
        "fmc_ip": "172.18.6.137",
        "username": "apiadmin",
        "password": "Cisc0123",
        "target_name": "test1_network_lists_and_feeds",
        "file_path": "/tmp/network_list.txt"
    }

    try:
        # 初始化上传器（网页8推荐的会话保持方式）
        uploader = CiscoFMCFileUploader(
            CONFIG["fmc_ip"],
            CONFIG["username"],
            CONFIG["password"]
        )

        # 动态获取列表ID（网页7的分页策略）
        print("正在获取列表ID...")
        list_id = uploader.get_si_list_id(CONFIG["target_name"])
        print(f"成功获取列表ID: {list_id}")

        # 两阶段提交流程（网页10推荐的验证机制）
        print("开始验证性上传...")
        validate_result = uploader.upload_file(list_id, CONFIG["file_path"], validate_only=True)

        if validate_result and validate_result.get('metadata', {}).get('invalidEntryCount', 1) == 0:
            print("验证通过，开始正式提交...")
            final_result = uploader.upload_file(list_id, CONFIG["file_path"])
            if final_result:
                print(f"更新成功！版本号: {final_result.get('version')}")
                print(f"有效条目数: {final_result.get('metadata', {}).get('entryCount')}")
        else:
            print("文件校验失败，无效条目：")
            print(validate_result.get('metadata', {}).get('invalidLines', []))

    except Exception as e:
        print(f"流程执行失败: {str(e)}")
        exit(1)