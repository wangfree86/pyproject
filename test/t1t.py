import sqlite3
import os

dbPath = 'data.sqlite'
# 只有data.sqlite文件不存在时才创建该文件
if not os.path.exists(dbPath):
    conn = sqlite3.connect(dbPath)
    # 获取sqlite3.Cursor对象
    c = conn.cursor()
    # 创建persons表
    c.execute('''CREATE TABLE persons
       (id INT PRIMARY KEY     NOT NULL,
       name           TEXT    NOT NULL,
       age            INT     NOT NULL,
       address        CHAR(50),
       salary         REAL);''')

    # 修改数据库后必须调用commit方法提交才能生效
    conn.commit()
    # 关闭数据库连接
    conn.close()
    print('创建数据库成功')
