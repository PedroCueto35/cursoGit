import MySQLdb

db=MySQLdb.connect(host='localhost',user='admin', password='123abc...')

cursor=db.cursor()

cursor.execute("SELECT VERSION()")

datos=cursor.fetchone()

print("Data version: {0}".format(datos))

db.close()