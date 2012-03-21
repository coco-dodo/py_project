#!/home/qiaoyi/python/bin/python
#--*-- encoding:utf-8 --*--

import MySQLdb

def mysql_connect(_host, _port, _user, _passwd, _db):
	'''
		创建数据库连接，connect参数一定要使用keyword argumnets
		'''
	conn = MySQLdb.connect(host=_host,port=_port,user=_user,passwd=_passwd,db=_db)
	return conn

def mysql_close(conn):
	conn.close()

def mysql_query(conn, query, args):
	'''
		执行单条sql语句,接收的参数为sql语句本身和使用的参数列表,返回值为受影响的行数
		'''
	cursor = conn.cursor()
	rowcount = cursor.execute(query, args)	
	records = cursor.fetchall()
	cursor.close() 
	return records

def mysql_insert(conn, query, args):
	cursor = conn.cursor()
	cont = cursor.execute(query, args)
	cursor.close()
	return cont

def mysql_insert_batch(conn, query, args):
	'''
		sql="insert into cdinfo values(0,%s,%s,%s,%s,%s)"
		param=((title,singer,imgurl,url,alpha),(title2,singer2,imgurl2,url2,alpha2))
		n=cursor.executemany(sql,param) 批量插入
		'''
	cursor = conn.cursor()
	cont = cursor.executemany(query, args)
	cursor.close()
	return cont


def mysql_update(conn, query, args):
	cursor = conn.cursor()
	cont = cursor.execute(query, args)
	cursor.close()
	return cont


def test():
	conn = mysql_connect("10.20.150.83",3307,"pca","pca","clipper")
	records = mysql_query(conn, "select * from task where name = 'haha'",None)
	for record in records:
		print record
	cont = mysql_insert_batch(conn, "insert into task(name) values(%s)",(("haha"),("haha")))
	records = mysql_query(conn, "select * from task where name = 'haha'",None)
	for record in records:
		print record
	cont = mysql_insert(conn, "insert into task(name) values(%s)",("xixihaha"))
	records = mysql_query(conn, "select * from task where name = 'xixihaha'",None)
	for record in records:
		print record
	cont = mysql_update(conn, "update task set name=%s where name=%s",("hoho","xixihaha"))	
	records = mysql_query(conn, "select * from task where name = 'hoho'",None)
	for record in records:
		print record
	mysql_close(conn)


if __name__ == "__main__":
	test()
