import paramiko
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def transfer_file(local_file, remote_host, remote_user, remote_pwd, remote_path):
    # 预初始化所有连接对象
    client_a, sftp_a = None, None
    client_b, sftp_b = None, None

    # 读取本地文件（服务器A）
    try:
        with open(local_file, 'r') as f:
            content = f.read()
        logger.info(f"成功读取本地文件: {local_file}，长度: {len(content)}字节")
    except IOError as e:
        logger.error(f"本地文件读取失败: {str(e)}")
        raise

    # 写入远程文件（服务器B）
    try:
        client_b = paramiko.SSHClient()
        client_b.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client_b.connect(remote_host, username=remote_user, password=remote_pwd, timeout=10)
        sftp_b = client_b.open_sftp()

        # 覆盖写入模式
        with sftp_b.open(remote_path, 'w') as remote_file:
            remote_file.write(content)
        logger.info(f"成功写入远程文件: {remote_path}")

    except paramiko.SSHException as e:
        logger.error(f"SSH连接失败: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"写入操作失败: {str(e)}")
        raise
    finally:
        # 安全关闭服务器B连接
        if sftp_b:
            sftp_b.close()
        if client_b:
            client_b.close()


if __name__ == "__main__":
    transfer_file(
        local_file="/tmp/network_list.txt",
        remote_host="172.18.6.137",
        remote_user="echouser",
        remote_pwd="Cisc0132",
        remote_path="/var/sf/iprep_download/1628c08c-115d-11f0-abb4-91b175edea33"
    )