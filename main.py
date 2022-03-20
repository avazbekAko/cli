from flask import Flask, request, Response, escape
import MySQLdb

app = Flask(__name__)


@app.route('/t-logs')
def tlogs():
    mydb = MySQLdb.connect(host='localhost', user='root', password='TeleBot@2022@ok', db='logs', )
    cur = mydb.cursor()
    cur.execute(f'SELECT * FROM find;')
    results = cur.fetchall()
    id_ = {}
    chat_id_ = {}
    f_name_ = {}
    name_ = {}
    m_text = {}
    j = 0
    for res in results:
        id_[j] = res[0]
        chat_id_[j] = str(res[1])
        f_name_[j] = str(res[2])
        m_text[j] = str(res[3])
        name_[j] = str(res[5])
        j+=1
    answer = []
    for h in range(j):
        answer += {
            "id": id_[h],
            "chat_id": chat_id_[h],
            "name": name_[h],
            "function_name": f_name_[h],
            "text_messeg": m_text[h]
        },
    answer = str(answer).replace("'", '"')
    answer = str(answer).replace("None", 'null')
    return f'{answer}'
@app.route('/v-logs')
def vlogs():
    mydb = MySQLdb.connect(host='localhost', user='root', password='TeleBot@2022@ok', db='viber', )
    cur = mydb.cursor()
    cur.execute(f'SELECT * FROM message;')
    results = cur.fetchall()
    id_ = {}
    chat_id_ = {}
    f_name_ = {}
    name_ = {}
    m_text = {}
    j = 0
    for res in results:
        id_[j] = res[0]
        chat_id_[j] = str(res[1])
        f_name_[j] = str(res[2])
        m_text[j] = str(res[3])
        name_[j] = str(res[5])
        j+=1
    answer = []
    for h in range(j):
        answer += {
            "id": id_[h],
            "chat_id": chat_id_[h],
            "name": name_[h],
            "function_name": f_name_[h],
            "text_messeg": m_text[h]
        },
    answer = str(answer).replace("'", '"')
    answer = str(answer).replace("None", 'null')
    return f'{answer}'
@app.route('/t-users')
def tusers():
    mydb = MySQLdb.connect(host='localhost', user='root', password='TeleBot@2022@ok', db='logs', )
    cur = mydb.cursor()
    cur.execute(f'SELECT * FROM users;')
    results = cur.fetchall()
    id_ = {}
    chat_id_ = {}
    name_ = {}
    j = 0
    for res in results:
        id_[j] = res[0]
        chat_id_[j] = res[1]
        name_[j] = res[3]
        j+=1
    answer = []
    for h in range(j):
        answer += {
            "id": id_[h],
            "chat_id": chat_id_[h],
            "name": name_[h]
        },
    answer = str(answer).replace("'", '"')
    return f'{answer}'
@app.route('/v-users')
def vusers():
    mydb = MySQLdb.connect(host='localhost', user='root', password='TeleBot@2022@ok', db='viber', )
    cur = mydb.cursor()
    cur.execute(f'SELECT * FROM users;')
    results = cur.fetchall()
    id_ = {}
    chat_id_ = {}

    name_ = {}
    j = 0
    for res in results:
        id_[j] = res[0]
        chat_id_[j] = res[1]
        name_[j] = res[3]
        j+=1
    answer = []
    for h in range(j):
        answer += {
            "id": id_[h],
            "chat_id": chat_id_[h],
            "name": name_[h]
        },
    answer = str(answer).replace("'", '"')
    return f'{answer}'

if __name__ == "__main__":
    try:
        app.run(host="192.168.111.25", port=8008)
    except:
        print("Error app")