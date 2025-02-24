from kamene.all import sr1, IP, ICMP

def ping_ip(ip_address, timeout=2, verbose=False):
    try:
        # 显式设置ICMP参数
        icmp = ICMP(id=1, seq=1)
        # 增加超时时间至2秒
        response = sr1(IP(dst=ip_address)/icmp, timeout=timeout, verbose=verbose)

        if response and response.haslayer(ICMP) and response.getlayer(ICMP).type == 0:
            print(f"成功收到来自 {ip_address} 的ICMP应答:")
            response.show()
            return True
        else:
            print(f"向 {ip_address} 发送ICMP请求超时或收到非应答包。")
            return False

    except Exception as e:
        print(f"发送ICMP请求时发生错误: {e}")
        return False

# 使用sudo运行此脚本
ping_ip('223.5.5.5', timeout=2, verbose=True)