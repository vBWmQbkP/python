import paramiko
import requests
import logging
import os
import shlex
from io import BytesIO

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def ssh_write_http_content(http_url, remote_host, remote_user, remote_pwd, remote_path):
    """
    通过HTTP获取内容并SSH写入远程文件
    :param http_url: HTTP文件链接
    :param remote_host: SSH主机地址
    :param remote_user: SSH用户名
    :param remote_pwd: SSH密码
    :param remote_path: 远程文件绝对路径
    """
    client = None
    try:
        # 1. 从HTTP获取文件内容
        response = requests.get(http_url, timeout=15)
        response.raise_for_status()

        # 内容验证
        if not response.content:
            raise ValueError("HTTP响应内容为空")
        if b"<html>" in response.content[:100].lower():
            raise ValueError("获取到HTML页面而非数据文件")

        content = response.text
        logger.info(f"成功获取HTTP内容，长度: {len(content)}字符")

        # 2. 转义特殊字符
        escaped_content = content.replace("'", "'\"'\"'")  # 处理单引号
        escaped_content = escaped_content.replace("\n", "\\n")  # 保留换行符

        # 3. 构建安全写入命令
        dir_path = shlex.quote(os.path.dirname(remote_path))
        cmd = f"mkdir -p {dir_path} && "
        cmd += f"echo -e '{escaped_content}' > {shlex.quote(remote_path)}"

        # 4. 执行SSH操作
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(remote_host,
                       username=remote_user,
                       password=remote_pwd,
                       timeout=20,
                       banner_timeout=30)

        # 执行命令
        logger.debug(f"执行命令: {cmd}")
        stdin, stdout, stderr = client.exec_command(cmd)
        exit_status = stdout.channel.recv_exit_status()

        if exit_status != 0:
            error_msg = stderr.read().decode('utf-8', errors='ignore')
            raise RuntimeError(f"命令执行失败 [Code:{exit_status}]: {error_msg}")

        logger.info(f"文件成功写入远程路径: {remote_path}")
        return True

    except requests.exceptions.RequestException as e:
        logger.error(f"HTTP请求失败: {str(e)}")
        return False
    except paramiko.AuthenticationException:
        logger.error("SSH认证失败，请检查用户名/密码")
        return False
    except Exception as e:
        logger.error(f"操作失败: {str(e)}")
        return False
    finally:
        if client:
            client.close()


if __name__ == "__main__":
    # 配置参数
    config = {
        "http_url": "http://172.18.6.135/network_list.txt",
        "remote_host": "172.18.6.137",
        "remote_user": "echouser",
        "remote_pwd": "Cisc0132",
        "remote_path": "/var/sf/iprep_download/1628c08c-115d-11f0-abb4-91b175edea33"
    }

    # 执行写入操作
    success = ssh_write_http_content( **config)

    if success:
        print("操作成功完成")
    else:
        print("操作执行失败，请检查日志")
        exit(1)