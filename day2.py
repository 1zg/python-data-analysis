#链接数据库-》创建游标-》执行sql-》关闭游标

import pymysql
# con=pymysql.connect(
#     host='176.19.0.104',
#     port=3306,
#     user='root',
#     password='123456',
#     database='aidtn2605'
# )
# name=input('姓名：')
# password=input('密码：')
# mobile=input('电话：')
name='mark'
password='111111'
mobile='17258946978'
db=pymysql.connect(
	host='localhost',
	port=3306,
	user='root',
	password='123456',
	database='aidtn2605',
    autocommit=True
)
# db_cursor=db.cursor(pymysql.cursors.DictCursor)
sql_select=f"select * from users where username='{name}' or mobile='{mobile}';"
# print(db_cursor.execute(sql_select),db_cursor.fetchall())
# sql_insert=f"insert users values(null,'{name}','{password}','{mobile}');"
# db_cursor.execute(sql_insert)
# print(db_cursor.execute(sql_select),db_cursor.fetchall())
# db_cursor.close()
sql_insert=f'insert users values(null,"{name}","{password}","{mobile}")'

#上下文管理器 with as
with db.cursor(pymysql.cursors.DictCursor) as cursor:
    booolsele=cursor.execute(sql_select)
    # result=cursor.fetchall()
    # print(booolsele)
    # print(result)
    if booolsele:
        print('用户名或电话已存在')
    else:
        try:
            cursor.execute(sql_insert)
        except Exception as e:
            print("插入失败",e)
        else:
            print("插入成功，新纪录id为：",cursor.lastrowid)
print('-----------------')
#错误处理 判断语句 异常处理
# from . import zz
lst=[1,2,3]
dit={}
try:
    # print(dit['1'])
    print(lst[1])
except IndexError as e:
    print(e)
except KeyError as e:
    print(e,'keyerror')
except Exception as e:#兜底一场，写在最后
    print(e)
else:
    # print('看看是啥')
    print('try正常执行')
finally:
    print('异常与否，都会执行')
print('------------------')
#自定义异常 需要用raise手动触发,与if搭配使用
class zdyerror(Exception):
    def __init__(self,msg,code):
        self.msg=msg
        self.code=code
        super().__init__(msg,code)
try:
    i=1
    if i<2:
        raise zdyerror('error',1)
except zdyerror as e:
    print(e.code,e.msg)
#缓冲区
#delete
#