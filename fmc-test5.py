import requests
import os
from requests_toolbelt.multipart.encoder import MultipartEncoder
from urllib3.exceptions import InsecureRequestWarning

# 禁用SSL警告（生产环境应配置证书）
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


class CiscoFMCFileUploader:
    def __init__(self, fmc_ip, username, password):
        self.base_url = f"https://{fmc_ip}/api/fmc_config/v1/domain"
        self.auth_token, self.domain_uuid = self._authenticate(fmc_ip, username, password)

    def _authenticate(self, fmc_ip, username, password):
        """认证流程优化（基于网页6的认证规范）"""
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
        except Exception as e:
            raise ConnectionError(f"认证失败: {str(e)}")

    def upload_file(self, object_id, file_path, validate_only=False):
        """文件上传实现（符合网页7和网页10的multipart规范）"""
        url = f"{self.base_url}/{self.domain_uuid}/object/customsiiplists/{object_id}"

        # 构建多部分编码器（参考网页10的最佳实践）
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
            boundary='----WebKitFormBoundary7MA4YWxkTrZu0gW'  # 显式声明boundary
        )

        headers = {
            "X-auth-access-token": self.auth_token,
            "Content-Type": encoder.content_type  # 自动包含boundary
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
        """错误解析优化（基于网页9的错误处理建议）"""
        try:
            error_data = response.json()
            return error_data.get("error", {}).get("message", "未知错误")
        except ValueError:
            return f"非JSON响应: {response.text}"


# ====== 使用示例 ======
if __name__ == "__main__":
    # 配置参数
    FMC_IP = "172.18.6.137"
    USERNAME = "apiadmin"
    PASSWORD = "Cisc0123"
    TARGET_NAME = "test1_network_lists_and_feeds"
    FILE_PATH = "/tmp/1.txt"

    try:
        # 初始化上传器
        uploader = CiscoFMCFileUploader(FMC_IP, USERNAME, PASSWORD)

        # 获取列表ID（原有逻辑）
        # list_id = ... 此处保留原有获取逻辑

        # 假设已获取到list_id
        list_id = "32fd6c48-0b0f-11f0-994b-891bbfce0d61"

        # 两阶段提交流程
        print("开始验证性上传...")
        validate_result = uploader.upload_file(list_id, FILE_PATH, validate_only=True)

        if validate_result and validate_result.get('metadata', {}).get('invalidEntryCount', 1) == 0:
            print("验证通过，开始正式提交...")
            final_result = uploader.upload_file(list_id, FILE_PATH)
            if final_result:
                print(f"更新成功！版本号: {final_result.get('version')}")
                print(f"有效条目数: {final_result.get('metadata', {}).get('entryCount')}")
        else:
            print("文件校验失败，请检查以下无效条目：")
            print(validate_result.get('metadata', {}).get('invalidLines', []))

    except Exception as e:
        print(f"流程执行失败: {str(e)}")