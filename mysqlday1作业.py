# 作业：
# 第一题：
# 通过MySQL客户端在aidtn2605数据库中创建如下结构的数据表 -- users：
# +-----------+----------------------------+------+-----+---------+----------------+
# | Field     | Type                       |Null | Key | Default | Extra          |
# +-----------+----------------------------+------+-----+---------+----------------+
# | id        | bigint(10) unsigned        | NO   | PRI |         | auto_increment |
# | username  | varchar(30)                | NO   | UNI |         |                |
# | password  | varchar(32)                | No   |     |         |                |
# | mobile    | varchar(11)                | No   | UNI |         |                |
# +-----------+----------------------------+------+-----+---------+----------------+
# 通过MySQL客户端至少写入5条记录
'''
create database aidtn2605;

create table users(
	id bigint(10) unsigned not null primary key auto_increment,
	username varchar(30) not null unique,
	password varchar(32) not null,
	mobile varchar(11) not null unique
);

insert users values(null,'bob','111','18258946988');
insert users values(null,'tom','1111','17258946978');
insert users values(null,'tony','11111','16258946968');
insert users values(null,'alice','111111','15258946958');
insert users values(null,'timi','1111111','14258946948');
'''

# 第二题：
# 通过Python将aidtn2605数据库中的users数据表读取成如下结构：
# 密码为6位(如ABCD12)，就显示6个星号(******)，8位就显示8个星号
# 电话为13800138000，则显示 138****8000
# [
# 	{'id':1,'username':'Tom','password':'******','mobile':'138****0000'},
# 	{'id':1,'username':'Tom','password':'******','mobile':'138****0000'},
# 	{'id':1,'username':'Tom','password':'******','mobile':'138****0000'},
# 	{'id':1,'username':'Tom','password':'******','mobile':'138****0000'},
# 	{'id':1,'username':'Tom','password':'******','mobile':'138****0000'}
# ]
import pymysql
db=pymysql.connect(
	host='localhost',
	port=3306,
	user='root',
	password='123456',
	database='aidtn2605'
)
cursor=db.cursor()
# cursor=db.cursor(pymysql.cursors.DictCursor)
sql='select * from users'
cursor.execute(sql)
results=cursor.fetchall()
# print(results)
lst=[]
for i in results:
	dit = {}
	dit['id']=i[0]
	dit['username']=i[1]
	dit['password']=i[2].replace(i[2],'*'*len(i[2]))
	dit['mobile']=i[3][0:3]+i[3][3:7].replace(i[3][3:7],'*'*len(i[3][3:7]))+i[3][7:]
	lst.append(dit)
	# print(dit)
	# print(lst)
print(lst)

