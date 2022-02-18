import MySQLdb

mydb = MySQLdb.connect(
    host='localhost',
    user='root',
    password='TeleBot@2022@ok',
    db='find',
)
cur = mydb.cursor()
command = cur.execute('SELECT * FROM message')
results = cur.fetchall()
print (results)