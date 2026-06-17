# 作业
# 请封装一个类，如ModelManager的类，
# 用于完成针于users表的CURD的操作！尽量有适应性。
import pymysql
class ModelManager:
    def __init__(self,host,port,user,password,db):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.db=db
        try:
            self.db_con = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.db,
                autocommit=True
            )
        except Exception as e:
            print(e)
        else:
            self.cur=self.db_con.cursor(pymysql.cursors.DictCursor)

    def inser(self,table_name,inser_data):
        try:
            sql=f'insert {table_name}(username,password,mobile) values(%s,%s,%s)'
            self.cur.execute(sql,inser_data)
        except Exception as e:
            print('插入失败',e)
        else:
            print(f"插入成功：")
            self.selec(table_name, 'id', self.cur.lastrowid)
    def dele(self,table_name,id):
        try:
            print(f"将要删除：")
            self.selec(table_name, 'id', id)
            sql=f'delete from {table_name} where id=%s'
            self.cur.execute(sql,id)
        except Exception as e:
            print('删除失败',e)
        else:
            print("删除成功")
    def updat(self,table_name,id,cname,new_data):
        try:
            print(f"更新前数据：")
            self.selec(table_name, 'id', id)
            sql=f'update {table_name} set {cname}="{new_data}" where id=%s'
            self.cur.execute(sql,id)
        except Exception as e:
            print('更新失败',e)
        else:
            print(f"更新成功：")
            self.selec(table_name, 'id', id)
    def selec(self,table_name,var_name,var_data):
        try:
            sql=f'select * from {table_name} where {var_name}="{var_data}"'
            self.cur.execute(sql)
        except Exception as e:
            print('查询失败',e)
        else:
            results=self.cur.fetchall()
            print(results)

aidtn2605_users=ModelManager('localhost',3306,'root','123456','aidtn2605')
ins_da=('ll','333','11858946988')
aidtn2605_users.inser('users',ins_da)
aidtn2605_users.dele('users',10)
aidtn2605_users.updat('users',9,'username','ntmd')
aidtn2605_users.selec('users','id',1)