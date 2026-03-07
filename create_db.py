import sys
import os

# 打印 Python 信息
print(f"Python 版本：{sys.version}")
print(f"Python 路径：{sys.executable}")
print(f"当前目录：{os.getcwd()}")

# 尝试导入 pymysql
try:
    import pymysql
    print("✓ pymysql 已安装")
    
    # 连接 MySQL 服务器
    try:
        connection = pymysql.connect(
            host='192.168.80.130',
            port=3306,
            user='fmrober',
            password='Lhx123!@#',
            charset='utf8mb4'
        )
        print("✓ MySQL 连接成功")
        
        cursor = connection.cursor()
        
        # 创建数据库
        cursor.execute("CREATE DATABASE IF NOT EXISTS procurement_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        print("✓ 数据库 procurement_db 创建成功！")
        
        # 验证数据库是否存在
        cursor.execute("SHOW DATABASES LIKE 'procurement_db'")
        result = cursor.fetchone()
        if result:
            print(f"✓ 数据库已确认存在：{result[0]}")
        else:
            print("⚠ 数据库可能已存在")
        
        cursor.close()
        connection.close()
        
    except pymysql.Error as e:
        print(f"✗ MySQL 连接或操作失败：{e}")
        sys.exit(1)
        
except ImportError as e:
    print(f"✗ pymysql 未安装：{e}")
    print("请手动安装：pip install pymysql")
    sys.exit(1)
