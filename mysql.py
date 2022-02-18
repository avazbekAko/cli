import MySQLdb

mydb = MySQLdb.connect(
    host='localhost',
    user='root',
    password='TeleBot@2022@ok',
    db='find',
)
cur = mydb.cursor()

sql = "INSERT INTO message (message, id_chat) VALUES ('Tesss12', '120932')"
cur.execute(sql)
mydb.commit()

command = cur.execute('SELECT * FROM message')
results = cur.fetchall()
print (results)