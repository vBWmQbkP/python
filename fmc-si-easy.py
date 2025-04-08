import requests
import warnings
import logging
import uuid
from requests_toolbelt.multipart.encoder import MultipartEncoder
from urllib3.exceptions import InsecureRequestWarning
from io import BytesIO
from requests.adapters import HTTPAdapter

# 配置调试日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
warnings.filterwarnings("ignore", category=InsecureRequestWarning)


class CiscoFMCFileUploader:
    def __init__(self, fmc_ip, username, password):
        self.session = requests.Session()
        self.session.mount('https://', HTTPAdapter(max_retries=3))
        try:
            self.auth_token = self._authenticate(fmc_ip, username, password)
            self.headers = {
                "X-auth-access-token": self.auth_token,
                "User-Agent": "FMC-Uploader/1.0",
                "Accept": "application/json"
            }
            logging.info(f"认证成功 | Token:{self.auth_token[:8]}...")
        except Exception as e:
            logging.error("初始化失败: %s", str(e))
            raise

    def _authenticate(self, fmc_ip, username, password):
        """简化认证流程，仅获取Token"""
        auth_url = f"https://{fmc_ip}/api/fmc_platform/v1/auth/generatetoken"
        try:
            response = self.session.post(
                auth_url,
                auth=(username, password),
                verify=False,
                timeout=15
            )
            response.raise_for_status()

            if not (token := response.headers.get("X-auth-access-token")):
                raise ValueError("未获取到认证令牌")
            return token
        except requests.exceptions.RequestException as e:
            logging.error("认证请求失败: %s", str(e))
            raise

    def upload_file(self, file_url, validate_only=False):
        """使用固定URL进行文件上传"""
        FIXED_UPLOAD_URL = "https://172.20.5.36/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/customsiiplists/97e0626c-1476-11f0-ac75-a7c9ac948425"

        try:
            # 下载文件内容
            file_content, filename = self._fetch_remote_file(file_url)

            # 构建请求体
            boundary = f"----FMCBoundary_{uuid.uuid4().hex}"
            encoder = MultipartEncoder(
                fields={
                    'name': 'test1_network_lists_and_feeds',
                    'id': '97e0626c-1476-11f0-ac75-a7c9ac948425',  # 固定列表ID
                    'validateOnly': str(validate_only).lower(),
                    'payloadFile': (
                        filename,
                        file_content,
                        'application/octet-stream'
                    )
                },
                boundary=boundary
            )

            headers = {
            **self.headers,
            "Content-Type": encoder.content_type,
            "Connection": "keep-alive"
            }

            # 发送上传请求
            response = self.session.put(
                FIXED_UPLOAD_URL,
                headers=headers,
                data=encoder,
                verify=False,
                timeout=(30, 120)
            )
            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException as e:
            error_msg = self._parse_error(e.response) if e.response else str(e)
            logging.error("上传失败: %s", error_msg)
            return {"status": "error", "message": error_msg}
        except Exception as e:
            logging.error("处理异常: %s", str(e))
            return {"status": "error", "message": str(e)}

    def _fetch_remote_file(self, file_url):
        """带重试的文件下载（保持不变）"""
        for attempt in range(3):
            try:
                response = self.session.get(
                    file_url,
                    verify=False,
                    timeout=15,
                    headers={"Cache-Control": "no-cache"}
                )
                response.raise_for_status()
                return BytesIO(response.content), self._extract_filename(file_url)
            except requests.exceptions.RequestException as e:
                if attempt == 2:
                    raise
                logging.warning("下载重试中(%d/3)...", attempt + 1)

    def _parse_error(self, response):
        """错误解析（保持不变）"""
        try:
            return response.json().get('error', {}).get('message', '未知错误')
        except ValueError:
            return f"响应内容: {response.text[:200]}"

    def _extract_filename(self, url):
        """文件名提取（保持不变）"""
        filename = url.split('/')[-1].split('?')[0]
        return filename or f"network_list_{uuid.uuid4().hex[:8]}.txt"


# ====== 配置和执行 ======
if __name__ == "__main__":
    CONFIG = {
        "fmc_ip": "172.20.5.36",
        "username": "test2",
        "password": "Cisc0123",
        "file_url": "http://172.18.6.135/network_list.txt",
    }

    try:
        print("=" * 40 + "\n初始化认证...")
        uploader = CiscoFMCFileUploader(
            CONFIG["fmc_ip"],
            CONFIG["username"],
            CONFIG["password"]
        )

        print("\n" + "=" * 40 + "\n验证性上传:")
        result = uploader.upload_file(CONFIG["file_url"], validate_only=True)
        if result.get('status') == 'error':
            print(f"!! 预检失败: {result.get('message')}")
            exit(1)

        if result.get('metadata', {}).get('invalidEntryCount', 1) == 0:
            print("\n" + "=" * 40 + "\n正式提交:")
            final_result = uploader.upload_file(CONFIG["file_url"])
            if final_result.get('status') != 'error':
                print(f"成功更新 | 版本: {final_result.get('version', '未知')}")
            else:
                print(f"!! 提交失败: {final_result.get('message')}")
        else:
            print("!! 无效条目检测:")
            print(result.get('metadata', {}).get('invalidLines', []))

    except Exception as e:
        print(f"\n!! 流程异常: {str(e)}")
        exit(1)