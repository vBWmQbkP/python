import logging
from typing import Optional, Tuple
import socket
from kamene.all import ICMP, IP, sr1
from kamene.error import Kamene_Exception

# 配置日志
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)


class PingResult:
    """Ping操作结果对象"""

    def __init__(self,
                 success: bool,
                 ip: str,
                 latency: Optional[float] = None,
                 error: Optional[str] = None):
        self.success = success
        self.ip = ip
        self.latency = latency  # 单位：毫秒
        self.error = error

    def __str__(self) -> str:
        if self.success:
            return f"{self.ip} 通！延迟 {self.latency:.2f}ms"
        if self.error:
            return f"{self.ip} 错误：{self.error}"
        return f"{self.ip} 不通！"


def validate_ip(ip: str) -> bool:
    """验证IP地址格式是否合法"""
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False


def send_icmp_request(
        ip_address: str,
        timeout: int = 2,
        retry: int = 1,
        packet_size: int = 64,
        verbose: bool = False
) -> PingResult:
    """
    发送ICMP请求并返回结果
    :param ip_address: 目标IP地址
    :param timeout: 单次请求超时时间（秒）
    :param retry: 重试次数
    :param packet_size: ICMP数据包大小（字节）
    :param verbose: 是否显示详细信息
    :return: PingResult对象
    """
    if not validate_ip(ip_address):
        return PingResult(False, ip_address, error="无效的IP地址格式")

    icmp_id = 0x1234  # 固定ID用于跟踪会话
    base_seq = 1

    # 构造ICMP载荷
    payload = b'x' * (packet_size - 8)  # 8字节ICMP头

    for attempt in range(1, retry + 1):
        try:
            icmp_seq = base_seq + attempt
            icmp_pkt = ICMP(id=icmp_id, seq=icmp_seq)
            ip_pkt = IP(dst=ip_address) / icmp_pkt / payload

            # 记录发送时间
            start_time = time.time()
            response = sr1(ip_pkt, timeout=timeout, verbose=verbose)
            latency = (time.time() - start_time) * 1000  # 转毫秒

            if response:
                if response.haslayer(ICMP):
                    icmp_type = response.getlayer(ICMP).type
                    if icmp_type == 0:  # Echo Reply
                        return PingResult(True, ip_address, latency)
                    elif icmp_type == 3:  # Destination Unreachable
                        return PingResult(False, ip_address, error="目标不可达")
            return PingResult(False, ip_address)

        except Kamene_Exception as e:
            error_msg = f"网络错误: {str(e)}"
            if attempt == retry:
                return PingResult(False, ip_address, error=error_msg)
        except PermissionError:
            return PingResult(False, ip_address, error="需要管理员权限执行ICMP操作")
        except Exception as e:
            error_msg = f"未知错误: {str(e)}"
            if attempt == retry:
                return PingResult(False, ip_address, error=error_msg)

    return PingResult(False, ip_address)


if __name__ == '__main__':
    # 示例使用
    results = [
        send_icmp_request("223.5.5.5", timeout=3, retry=3),
        send_icmp_request("8.8.8.8"),
        send_icmp_request("invalid_ip")
    ]

    for result in results:
        print(result)