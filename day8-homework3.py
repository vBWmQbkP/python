# import logging
# logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
# from kamene.all import *
#
# def ping_ip(ip_address):
#     icmp = ICMP(id=1, seq=1)
#     ping_result = sr1(IP(dst=ip_address)/icmp, timeout=2, verbose=False)
#
#     if ping_result:
#         print(f"{ip_address} 通！")
#         return True
#     else:
#         print(f"{ip_address} 不通！")
#         return False
#
# if __name__ == '__main__':
#     ping_ip("223.5.5.5")

import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *

def ping_ip(ip_address):
    icmp = ICMP(id=1, seq=1)
    ping_result = sr1(IP(dst=ip_address)/icmp, timeout=2, verbose=False)
    return ping_result is not None

if __name__ == '__main__':
    ip_address = "223.5.5.5"
    result = ping_ip(ip_address)
    if result:
        print(f"{ip_address} 通！")
    else:
        print(f"{ip_address} 不通！")