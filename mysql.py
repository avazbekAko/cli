import pymysql.cursors
def getConnection():
    # Вы можете изменить параметры соединения.
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='TeleBot@2022@ok',
        db='find',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
connection = getConnection()
print ("Connect successful!")
sql = "Select * from message "
try :
    cursor = connection.cursor()
    # Выполнить sql и передать 1 параметр.
    cursor.execute(sql, ( 10 ) )
    print ("cursor.description: ", cursor.description)
    print()
    for row in cursor:
        print (" ----------- ")
        print("id: ", row['id'])
        print ("message: ", row["message"])
        print ("id_chat: ", row["id_chat"])
finally:
    # Закрыть соединение
    connection.close()