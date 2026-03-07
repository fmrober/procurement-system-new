import sys
print(f"Python 版本：{sys.version}")
print(f"Python 路径：{sys.executable}")

try:
    import pymysql
    print("✓ pymysql 已安装")
except ImportError:
    print("✗ pymysql 未安装，尝试安装...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pymysql"])
    import pymysql
    print("✓ pymysql 安装成功")
