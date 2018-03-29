#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import pymysql
from pymysql.cursors import DictCursor
from DBUtils.PooledDB import PooledDB

sql_settings = {'mysql': {'host': '127.0.0.1', 'port': 3306, 'user': 'root', 'password': 'root', 'database': 'python', }}


class ConnUtil(object):

    __pool = {}

    def __init__(self, conf_name='mysql'):
        self._conn = ConnUtil._get_conn(conf_name)
        self._cursor = self._conn.cursor()

        # Enforce UTF-8 for the connection.
        self._cursor.execute('SET NAMES utf8mb4')
        self._cursor.execute("SET CHARACTER SET utf8mb4")
        self._cursor.execute("SET character_set_connection=utf8mb4")

    @classmethod
    def _get_conn(cls, conf_name):
        if conf_name not in ConnUtil.__pool:
            print('create pool for %s' % conf_name)
            ConnUtil.__pool[conf_name] = PooledDB(
                creator=pymysql,
                mincached=1,
                maxcached=20,
                use_unicode=True,
                charset='utf8',
                cursorclass=DictCursor,
                **sql_settings[conf_name])
        return ConnUtil.__pool[conf_name].connection()

    def close(self):
        if self._cursor:
            self._cursor.close()
        self._conn.close()

    def insert_one(self, sql, value):
        count = self._cursor.execute(sql, value)
        self._conn.commit()
        return count

    def insert_many(self, sql, values):
        count = self._cursor.execute(sql, values)
        self._conn.commit()
        return count

    def update(self, sql, param=None):
        count = self._cursor.execute(sql, param)
        self._conn.commit()
        return count

    def fetch_one(self, sql, param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            return self._cursor.fetchone()
        else:
            return False

    def fetch_many(self, sql, num, param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            return self._cursor.fetchmany(num)
        else:
            return False

    def fetch_all(self, sql, param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            return self._cursor.fetchall()
        else:
            return False


if __name__ == '__main__':
    conn = ConnUtil()
    result = conn.insert_one('insert into user_info(name) values(%s)', 'test')

    # result = conn.fetch_all("select * from user_info")
    print(result)











# 使用 cursor() 方法创建一个游标对象 cursor
# cursor = conn.cursor()

# 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据
# data = cursor.fetchone()

# print("Database Version : %s" % data)

# 关闭数据库连接
# conn.close()
