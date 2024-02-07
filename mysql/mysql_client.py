import pymysql

"""
参数说明：
    host : 数据库服务器地址
    user : 登录用户名
    password : 密码
    database : 数据库名称
    port : 数据库连接端口，默认为3306时可不填写。
    charset : 数据库编码，一般设置为utf8
"""
"""
连接数据库的流程 ：
1. 导包 ：import pymysql
2. 建立连接 ： connect(host,user,password,port,database,chaset)
3. 创建游标 ： cursor()
4. 执行SQL语句
    （1） 执行SQL ：execute(sql)
    (2) 查询一条数据 : fetchone()
    (3) 查询多条数据 ： fetchmany(number)  , number代表的是传入多条数据
    （4） 查询所有数据 ： fetchall()
5. 关闭游标 ： cursor.close()
6. 关闭连接 ： connect.close()
"""

# 数据库信息
config = {
    "host": "192.168.0.218",
    "port": 3306,
    "database": "zhengshiku",
    "charset": "utf8",
    "user": "root",
    "password": "!qaz2wsx"
}

class Mysqldb:
    # 初始化方法
    def __init__(self):
        # 初始化方法中调用连接数据库的方法
        self.conn = self.get_conn()
        # 调用获取游标的方法
        self.cursor = self.get_cursor()

    # 连接数据库的方法
    def get_conn(self):
        # **config代表不定长参数
        conn = pymysql.connect(**config)
        return conn

    # 获取游标
    def get_cursor(self):
        cursor = self.conn.cursor()
        return cursor

    # 查询sql语句返回的所有数据
    def select_all(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # 查询sql语句返回的一条数据
    def select_one(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    # 查询sql语句返回的几条数据
    def select_many(self, sql, num):
        self.cursor.execute(sql)
        return self.cursor.fetchmany(num)

    # 增删改除了SQL语句不一样其他都是一样的，都需要提交
    def commit_data(self, sql):
        try:
            # 执行语句
            self.cursor.execute(sql)
            # 提交
            self.conn.commit()
            # print('提交成功')
        except Exception as e:
            print('提交失败', e)
            # 失败后需要回滚
            self.conn.rollback()

    # 当对象被销毁时，游标要关闭,连接也要关闭
    # 创建时是先创建连接后创建游标，关闭时是先关闭游标后关闭连接
    def __del__(self):
        self.cursor.close()
        self.conn.close()











