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
        self.base_url = f"https://{fmc_ip}/api/fmc_config/v1/domain"
        self.session = requests.Session()  # 使用持久会话
        # 配置重试策略（总尝试3次，间隔1秒）
        self.session.mount('https://', HTTPAdapter(max_retries=3))
        try:
            self.auth_token, self.domain_uuid = self._authenticate(fmc_ip, username, password)
            self.headers = {
                "X-auth-access-token": self.auth_token,
                "User-Agent": "FMC-Uploader/1.0",
                "Accept": "application/json"
            }
            logging.info(f"认证成功 | Token:{self.auth_token[:8]}... Domain:{self.domain_uuid}")
        except Exception as e:
            logging.error("初始化失败: %s", str(e))
            raise

    def _authenticate(self, fmc_ip, username, password):
        """增强认证流程"""
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
            if not (domain := response.headers.get("DOMAIN_UUID")):
                raise ValueError("未获取到域UUID")

            return token, domain
        except requests.exceptions.RequestException as e:
            logging.error("认证请求失败: %s", str(e))
            raise

    def get_si_list_id(self, target_name):
        """增强列表查询"""
        si_url = f"{self.base_url}/{self.domain_uuid}/object/customsiiplists"
        all_items = []
        params = {"limit": 100, "offset": 0}

        try:
            while True:
                response = self.session.get(
                    si_url,
                    headers=self.headers,
                    params=params,
                    verify=False,
                    timeout=20
                )
                response.raise_for_status()

                data = response.json()
                logging.debug("分页响应: %s", data.get('paging', {}))

                if items := data.get("items"):
                    all_items.extend(items)
                    # 提前终止条件
                    if len(items) < params["limit"] or params["offset"] >= 1000:
                        break
                    params["offset"] += params["limit"]
                else:
                    logging.warning("未获取到列表条目")
                    break

            # 精确匹配
            for item in all_items:
                if item.get("name") == target_name:
                    logging.info("匹配到列表项: %s", item['id'])
                    return item['id']
            raise ValueError(f"'{target_name}' 不存在，共找到 {len(all_items)} 个列表项")

        except requests.exceptions.RequestException as e:
            logging.error("列表查询失败: %s", str(e))
            raise

    def upload_file(self, object_id, file_url, validate_only=False):
        """增强文件上传"""
        url = f"{self.base_url}/{self.domain_uuid}/object/customsiiplists/{object_id}"

        try:
            # 下载文件（带重试）
            file_content, filename = self._fetch_remote_file(file_url)

            # 构建动态boundary
            boundary = f"----FMCBoundary_{uuid.uuid4().hex}"
            encoder = MultipartEncoder(
                fields={
                    'name': 'test1_network_lists_and_feeds',
                    'id': object_id,
                    'validateOnly': str(validate_only).lower(),
                    'payloadFile': (
                        filename,
                        file_content,
                        'application/octet-stream'  # 更普适的MIME类型
                    )
                },
                boundary=boundary
            )

            headers = {
            **self.headers,
            "Content-Type": encoder.content_type,
            "Connection": "keep-alive"
            }

            # 发送请求（延长超时到120秒）
            response = self.session.put(
                url,
                headers=headers,
                data=encoder,
                verify=False,
                timeout=(30, 120)  # 连接30s，读取120s
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
        """带重试的文件下载"""
        for attempt in range(3):
            try:
                response = self.session.get(
                    file_url,
                    verify=False,
                    timeout=15,
                    headers={"Cache-Control": "no-cache"}
                )
                response.raise_for_status()

                # 内容验证
                if not (content := response.content):
                    raise ValueError("文件内容为空")
                if len(content) < 10:
                    raise ValueError("文件内容过短（至少10字节）")
                if b"<html>" in content[:100].lower():
                    raise ValueError("下载到HTML页面而非数据文件")

                return BytesIO(content), self._extract_filename(file_url)

            except requests.exceptions.RequestException as e:
                if attempt == 2:
                    raise
                logging.warning("下载重试中(%d/3)...", attempt + 1)
                continue

    def _extract_filename(self, url):
        """从URL提取安全文件名"""
        filename = url.split('/')[-1].split('?')[0]
        if not filename or '.' not in filename:
            return f"network_list_{uuid.uuid4().hex[:8]}.txt"
        return filename

    def _parse_error(self, response):
        """增强错误解析"""
        try:
            return response.json().get('error', {}).get('message', '未知错误')
        except ValueError:
            return f"响应内容: {response.text[:200]}"


# ====== 配置和执行 ======
if __name__ == "__main__":
    CONFIG = {
        "fmc_ip": "172.18.6.137",
        "username": "test2",
        "password": "Cisc0123",
        "target_name": "test1_network_lists_and_feeds",
        "file_url": "http://172.18.6.135/network_list.txt",
        # "proxies": {"http": "http://proxy:port", "https": "http://proxy:port"}  # 按需启用
    }

    try:
        print("=" * 40 + "\n初始化认证...")
        uploader = CiscoFMCFileUploader(
            CONFIG["fmc_ip"],
            CONFIG["username"],
            CONFIG["password"]
        )

        print("\n" + "=" * 40 + "\n获取列表ID:")
        list_id = uploader.get_si_list_id(CONFIG["target_name"])
        print(f"--> 列表ID: {list_id}")

        print("\n" + "=" * 40 + "\n验证性上传:")
        result = uploader.upload_file(list_id, CONFIG["file_url"], validate_only=True)
        if result.get('status') == 'error':
            print(f"!! 预检失败: {result.get('message')}")
            exit(1)

        if result.get('metadata', {}).get('invalidEntryCount', 1) == 0:
            print("\n" + "=" * 40 + "\n正式提交:")
            final_result = uploader.upload_file(list_id, CONFIG["file_url"])
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