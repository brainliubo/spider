import pymysql

db = pymysql.connect(host = "localhost",user = "root",
                      password= "mysql858040508", port = 3306,database = "mysql_study")
cursor = db.cursor()

sql_cmd = "show databases"

cursor.execute(sql_cmd)
print(cursor.fetchall())
print(type(cursor.fetchall()))
print(cursor.fetchall())
