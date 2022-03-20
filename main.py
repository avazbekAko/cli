from datetime import datetime, timedelta
import jsonpickle as jsonpickle
import requests
from flask import Flask, request, Response, escape
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import KeyboardMessage, RichMediaMessage
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.viber_requests import ViberMessageRequest, ViberSubscribedRequest, ViberFailedRequest
import MySQLdb
from constants import def_buttons, switch_language_text, error_text, show_by_id_text, function_edit_text, \
    show_by_24_text, text_yes, error_buttons, show_all_urgent, cancel_text

my_URL = 'https://api.gram.tj/api/'
app = Flask(__name__)
viber = Api(BotConfiguration(
    name='Грузоперевозки Gram',
    avatar='',
    auth_token='4edcc13b8be7de9a-e403bf8f1c922ca1-9ab3197a55341cde'
))

'''
*---===================--------------------===================--------------------===================--------------------===================--------------------*
for i in range(10):
    viber.send_messages('WlsA3IdYDPUMRlvswkOMlA==', [TextMessage(text=str('Hello' + str(i)))])
*---===================--------------------===================--------------------===================--------------------===================--------------------*
'''

language_user = ''
set_lang_boll = False
show_by_id_boll = False
show_by_24_boll = False
urgant_order_by_24_boll = False
t = True

work = True

def save(id, type_finction, m_text,re):
    global language_user
    mmm = ''
    name__ = ''
    for f in m_text:
        if f == "'":
            mmm += f"\\{f}"
        else:
            mmm += f
    for nem in str(re['sender']['name']):
        if nem == "'":
            name__ += f"\\{nem}"
        else:
            name__ += nem
    id_s = str(id)[:-2]
    sql = "INSERT INTO `message` (`chat_id`, `function_type`, `message`, `time`, `name_user`) VALUES ('" + str(id_s) + "', '" + type_finction + "', '" + mmm + "', '" + str(datetime.now())[
                                                                            0:-7] + "', '" + name__ + "');"
    try:
        print(sql)
        mydb = MySQLdb.connect(host='localhost', user='root', password='TeleBot@2022@ok', db='viber', )
        cur = mydb.cursor()
        cur.execute(sql)
        mydb.commit()
        cur.execute(f'SELECT `language` FROM users where chat_id = "{str(id_s)}";')
        results = cur.fetchall()
        print(results)
        if str(results) == "()":
            sql1 = "INSERT INTO `users` (`chat_id`, `name`, `time`) VALUES ('" + str(id_s) + "', '" + name__ + "', '" + str(datetime.now())[0:-7] + "');"
            cur.execute(sql1)
            mydb.commit()
            language_user = 'ru'
        else:
            language_user = str(results)[3:-5]
            print(language_user)
    except AssertionError as e:
        print(e)
def token_function():
        Data = {
            'phone': '+992557776484',
            'password': 'password',
        }
        response = requests.post(f'{my_URL}auth/login', data=Data)
        answer = jsonpickle.decode(response.text)
        token_ = str(answer['access_token'])
        ttt = "Bearer " + token_
        return ttt
def keyboard(lang):
    KEYBOARD = {
        "Type": "keyboard",
        "Buttons": [
            {
                "Columns": 3,
                "Rows": 2,
                "BgColor": "#e6f5ff",
                "BgMedia": "http://link.to.button.image",
                "BgMediaType": "picture",
                "BgLoop": True,
                "ActionType": "reply",
                "ActionBody": "search",
                "ReplyType": "message",
                "Text": str(def_buttons[lang]['search'])[2:-2]
            },
            {
                "Columns": 3,
                "Rows": 2,
                "BgColor": "#e6f5ff",
                "BgMedia": "http://link.to.button.image",
                "BgMediaType": "picture",
                "BgLoop": True,
                "ActionType": "reply",
                "ActionBody": "my_status",
                "ReplyType": "message",
                "Text": str(def_buttons[lang]['status'])[2:-2]
            },
            {
                "Columns": 3,
                "Rows": 2,
                "BgColor": "#e6f5ff",
                "BgMedia": "http://link.to.button.image",
                "BgMediaType": "picture",
                "BgLoop": True,
                "ActionType": "reply",
                "ActionBody": "show_by_id",
                "ReplyType": "message",
                "Text": str(def_buttons[lang]['show_by_id'])[2:-2]
            },
            {
                "Columns": 3,
                "Rows": 2,
                "BgColor": "#e6f5ff",
                "BgMedia": "http://link.to.button.image",
                "BgMediaType": "picture",
                "BgLoop": True,
                "ActionType": "reply",
                "ActionBody": "show_by_24",
                "ReplyType": "message",
                "Text": str(def_buttons[lang]['show_by_24'])[2:-2]
            },
            {
                "Columns": 3,
                "Rows": 2,
                "BgColor": "#e6f5ff",
                "BgMedia": "http://link.to.button.image",
                "BgMediaType": "picture",
                "BgLoop": True,
                "ActionType": "reply",
                "ActionBody": "show_by_24_urgent",
                "ReplyType": "message",
                "Text": str(def_buttons[lang]['show_all_urgant'])[2:-2]
            },
            {
                "Columns": 3,
                "Rows": 2,
                "BgColor": "#e6f5ff",
                "BgMedia": "http://link.to.button.image",
                "BgMediaType": "picture",
                "BgLoop": True,
                "ActionType": "reply",
                "ActionBody": "show_by_city",
                "ReplyType": "message",
                "Text": str(def_buttons[lang]["search_by_citi"])[2:-2]
            },
            {
                "Columns": 3,
                "Rows": 2,
                "BgColor": "#e6f5ff",
                "BgMedia": "http://link.to.button.image",
                "BgMediaType": "picture",
                "BgLoop": True,
                "ActionType": "reply",
                "ActionBody": "setings",
                "ReplyType": "message",
                "Text": str(def_buttons[lang]["setings"])[2:-2]
            }
        ]
    }
    return KEYBOARD
def send(text, id, boll):
    if boll:
        viber.send_messages(id, [
            TextMessage(text=text),
            KeyboardMessage(tracking_data='tracking_data', keyboard=keyboard(language_user))
        ])
    else:
        viber.send_messages(id, [
            TextMessage(text=text),
        ])
def send_keyboard(text, id, key):
    viber.send_messages(id, [
        TextMessage(text=text),
        KeyboardMessage(tracking_data='tracking_data', keyboard=key)
    ])
def send_answer(i,id,boll):
        order_id = "Номер заказа: " + str(i['rnd_id'])
        phone = "☎️ " + str(i['phone'])
        answer = order_id + "\n" + \
                 phone + "\n"
        if (i['dop_phone'] != None):
            answer += "☎️ " + str(i['dop_phone']) + "\n"
        if (i['amount'] != None):
            answer += "💵 " + str(i['amount']) + "$" + "\n"
        if (i['cargo'] != None):
            answer += "📦 " + str(i['cargo']) + "\n"
        if (i['type_payment'] != None):
            answer += "💵 " + str(i['type_payment']) + "\n"
        if (i['performer_count'] != None):
            answer += "🚛 " + str(i['performer_count']) + " шт\n"
        if (i['urgent'] != None):
            answer += "⚡️ " + str(i['urgent']) + "\n"
        if (i['comment'] != None):
            answer += "💬 " + str(i['comment']) + "\n"
        if (i['pick_time'] != None):
            answer += "🕐 " + str(i['pick_time']) + "\n"
        if (i['auto_type'] != None):
            answer += "🚛 " + str(i['auto_type']) + "\n"
        from_city1 = str(i['from_city'])
        from_city1 = str(from_city1).replace(' ', "_")
        from_city1 = str(from_city1).replace('`', "_")
        from_city1 = str(from_city1).replace("'", "_")
        from_city1 = str(from_city1).replace('-', "_")
        fr = str(i['to_city'])
        fr = str(fr).replace(' ', "_")
        fr = str(fr).replace('`', "_")
        fr = str(fr).replace("'", "_")
        fr = str(fr).replace('-', "_")
#        from_iso2 = str(i['f_iso2'])
#        from_city1 = f"{data_flags[from_iso2]['emoji']} из #" + from_city1
        from_city1 = f" из #" + from_city1
#        to_iso2 = str(i['t_iso2'])
#        to_city1 = f"{data_flags[to_iso2]['emoji']} в #" + fr
        to_city1 = f" в #" + fr
        answer += from_city1 + ' ➡️ ' + to_city1
        send(answer, id, boll)
def yes_no_keyboard(language_user):
    yes_no_keyboard = {
        "Type": "keyboard",
        "Buttons": [
            {
                "Columns": 3,
                "Rows": 2,
                "BgColor": "#00aa00",
                "BgMedia": "http://link.to.button.image",
                "BgMediaType": "picture",
                "BgLoop": True,
                "ActionType": "reply",
                "ActionBody": "yes",
                "ReplyType": "message",
                "Text": str(text_yes[language_user])
            },
            {
                "Columns": 3,
                "Rows": 2,
                "BgColor": "#ff0000",
                "BgMedia": "http://link.to.button.image",
                "BgMediaType": "picture",
                "BgLoop": True,
                "ActionType": "reply",
                "ActionBody": "cancel",
                "ReplyType": "message",
                "Text": str(cancel_text['button'][language_user])
            }
        ]
    }
    return yes_no_keyboard


@app.route('/', methods=['GET'])
def hello():
    return f'Hello, Avazbek!'

@app.route('/', methods=['POST'])
def incoming():
    global language_user
    global language_user
    global set_lang_boll
    global show_by_id_boll
    global show_by_24_boll
    global urgant_order_by_24_boll
    global t

    global work
    if work:
        work = False
        #logger.debug("received request. post data: {0}".format(request.get_data()))
        if not viber.verify_signature(request.get_data(), request.headers.get('X-Viber-Content-Signature')):
            return Response(status=403)
        viber_request = viber.parse_request(request.get_data())
        if isinstance(viber_request, ViberMessageRequest):
            save(viber_request.sender.id, 'Test', request.get_json()['message']['text'], request.get_json())
            if str(request.get_json()['message']['text']) == 'cancel':
                print(request.get_json()['message']['text'] + "\n")
                print(viber_request.sender.id)
                set_lang_boll = False
                show_by_id_boll = False
                show_by_24_boll = False
                urgant_order_by_24_boll = False
                t = True
                send(str(cancel_text['stop'][language_user]),viber_request.sender.id,False)
                send(str(cancel_text['def_but'][language_user]),viber_request.sender.id,True)
            elif str(request.get_json()['message']['text']) == 'Привет':
                print(request.get_json()['message']['text'] + "\n")
                print(viber_request.sender.id)
                text_by_send = f"Привет {request.get_json()['sender']['name']} "
                viber.send_messages(viber_request.sender.id, [
                    TextMessage(text=str(text_by_send)),
                    KeyboardMessage(tracking_data='tracking_data', keyboard=keyboard(language_user))
                ])
            elif str(request.get_json()['message']['text']) == 'test':
                print(request.get_json()['message']['text'])
                print(viber_request.sender.id)
                text_by_send = function_edit_text[language_user]
                viber.send_messages(
                    viber_request.sender.id, [
                        TextMessage(text=text_by_send),
                        KeyboardMessage(tracking_data='tracking_data', keyboard=keyboard(language_user))
                    ]
                )
            elif str(request.get_json()['message']['text']) == 'search':
                print(request.get_json()['message']['text'] + "\n")
                print(viber_request.sender.id)
                text_by_send = function_edit_text[language_user]
                viber.send_messages(viber_request.sender.id, [
                    TextMessage(text=str(text_by_send)),
                    KeyboardMessage(tracking_data='tracking_data', keyboard=keyboard(language_user))
                ])
            elif str(request.get_json()['message']['text']) == 'my_status':
                print(request.get_json()['message']['text'] + "\n")
                print(viber_request.sender.id)
                text_by_send = function_edit_text[language_user]
                viber.send_messages(viber_request.sender.id, [
                    TextMessage(text=str(text_by_send)),
                    KeyboardMessage(tracking_data='tracking_data', keyboard=keyboard(language_user))
                ])
            elif str(request.get_json()['message']['text']) == 'show_by_id':
                print(request.get_json()['message']['text'] + "\n")
                print(viber_request.sender.id)
                key = {
                    "Type": "keyboard",
                    "Buttons": [
                        {
                            "Columns": 3,
                            "Rows": 2,
                            "BgColor": "#ff0000",
                            "BgMedia": "http://link.to.button.image",
                            "BgMediaType": "picture",
                            "BgLoop": True,
                            "ActionType": "reply",
                            "ActionBody": "cancel",
                            "ReplyType": "message",
                            "Text": str(cancel_text['button'][language_user])
                        }
                    ]
                }
                send_keyboard(str(show_by_id_text['input_num'][language_user]), viber_request.sender.id, key)
                show_by_id_boll = True
            elif str(request.get_json()['message']['text']) == 'show_by_24':
                print(request.get_json()['message']['text'])
                print(viber_request.sender.id)
                ttt = token_function()
                Header = {
                    'Authorization': ttt,
                    'Content-Type': 'application/json',
                }
                if urgant_order_by_24_boll:
                    Data = {
                        'to_datetime': str(datetime.now())[0:-10],
                        'from_datetime': str(datetime.now() - timedelta(days=1))[0:-10],
                        'urgent': '1'
                    }
                else:
                    Data = {
                        'to_datetime': str(datetime.now())[0:-10],
                        'from_datetime': str(datetime.now() - timedelta(days=1))[0:-10],
                    }
                Url_ = f'{my_URL}t-bot/market-orders/'
                Data = str(Data).replace("'", '"')
                r = requests.get(Url_, headers=Header, data=Data)
                global dd
                dd = 0
                r = jsonpickle.decode(r.text)
                for ss in r:
                    dd += 1
                if dd == 0:
                    send(show_by_24_text['0'][language_user], viber_request.sender.id, True)
                else:
                    show_by_24_boll = True
                    key = yes_no_keyboard(language_user)
                    send_keyboard(show_by_24_text['no_0_1'][language_user] + str(dd) + show_by_24_text['no_0_2'][language_user], viber_request.sender.id, key)
            elif str(request.get_json()['message']['text']) == 'show_by_24_urgent':
                urgant_order_by_24_boll = True
                print(request.get_json()['message']['text'])
                print(viber_request.sender.id)
                ttt = token_function()
                Header = {
                    'Authorization': ttt,
                    'Content-Type': 'application/json',
                }
                if urgant_order_by_24_boll:
                    Data = {
                        'to_datetime': str(datetime.now())[0:-10],
                        'from_datetime': str(datetime.now() - timedelta(days=1))[0:-10],
                        'urgent': '1'
                    }
                else:
                    Data = {
                        'to_datetime': str(datetime.now())[0:-10],
                        'from_datetime': str(datetime.now() - timedelta(days=1))[0:-10],
                    }
                Url_ = f'{my_URL}t-bot/market-orders/'
                Data = str(Data).replace("'", '"')
                r = requests.get(Url_, headers=Header, data=Data)
                dd = 0
                r = jsonpickle.decode(r.text)
                for ss in r:
                    dd += 1
                if dd == 0:
                    send(show_all_urgent['0'][language_user], viber_request.sender.id, True)
                else:
                    show_by_24_boll = True
                    key = yes_no_keyboard(language_user)
                    send_keyboard(
                        show_all_urgent['no_0_1'][language_user] + str(dd) + show_all_urgent['no_0_2'][language_user],
                        viber_request.sender.id, key)
            elif str(request.get_json()['message']['text']) == 'show_by_city':
                print(request.get_json()['message']['text'] + "\n")
                print(viber_request.sender.id)

                text_by_send = function_edit_text[language_user]
                viber.send_messages(viber_request.sender.id, [
                    TextMessage(text=str(text_by_send)),
                    KeyboardMessage(tracking_data='tracking_data', keyboard=keyboard(language_user))
                ])
            elif str(request.get_json()['message']['text']) == 'setings':
                print(request.get_json()['message']['text'] + "\n")
                print(viber_request.sender.id)
                text_by_send = switch_language_text['sel'][language_user]
                key = {
                        "Type": "keyboard",
                        "Buttons": [
                            {
                                "Columns": 3,
                                "Rows": 2,
                                "BgColor": "#e6f5ff",
                                "BgMedia": "http://link.to.button.image",
                                "BgMediaType": "picture",
                                "BgLoop": True,
                                "ActionType": "reply",
                                "ActionBody": "ru",
                                "ReplyType": "message",
                                "Text": str(switch_language_text['lang']['ru'])
                            },
                            {

                                "Columns": 3,
                                "Rows": 2,
                                "BgColor": "#e6f5ff",
                                "BgMedia": "http://link.to.button.image",
                                "BgMediaType": "picture",
                                "BgLoop": True,
                                "ActionType": "reply",
                                "ActionBody": "en",
                                "ReplyType": "message",
                                "Text": str(switch_language_text['lang']['en'])

                            },
                        ]
                    }
                set_lang_boll = True
                send_keyboard(text_by_send, viber_request.sender.id, key)
            elif set_lang_boll:
                f = request.get_json()['message']['text']
                if f == 'ru' or f == 'en':
                    sql = "UPDATE users SET language = '" + f + f"' WHERE  chat_id = '{str(viber_request.sender.id)[:-2]}';"
                    try:
                        print(sql)
                        mydb = MySQLdb.connect(host='localhost', user='root', password='TeleBot@2022@ok', db='viber', )
                        cur = mydb.cursor()
                        cur.execute(sql)
                        mydb.commit()
                        language_user = f
                        text_by_send = switch_language_text['true'][language_user]
                        viber.send_messages(viber_request.sender.id, [
                            TextMessage(text=str(text_by_send)),
                            KeyboardMessage(tracking_data='tracking_data', keyboard=keyboard(language_user))
                        ])
                        set_lang_boll = False
                    except:
                        send(str(error_text[language_user]), viber_request.sender.id, True)
                        viber.send_messages(viber_request.sender.id, [
                            TextMessage(text=str(error_text[language_user])),
                            KeyboardMessage(tracking_data='tracking_data', keyboard=keyboard(language_user))
                        ])
            elif show_by_id_boll:
                f = request.get_json()['message']['text']
                ttt = token_function()
                Header = {
                    'Authorization': ttt,
                }
                r = requests.get(f'{my_URL}t-bot/market-orders/{f}/find', headers=Header)
                try:
                    i = jsonpickle.decode(r.text)
                    send_answer(i, viber_request.sender.id, True)
                    show_by_id_boll = False
                except:
                    send(show_by_id_text['error'][language_user], viber_request.sender.id, False)
            elif show_by_24_boll:
                f = request.get_json()['message']['text']
                if f == 'yes':
                    ttt = token_function()
                    Header = {
                        'Authorization': ttt,
                        'Content-Type': 'application/json',
                    }
                    if urgant_order_by_24_boll:
                        Data = {
                            'to_datetime': str(datetime.now())[0:-10],
                            'from_datetime': str(datetime.now() - timedelta(days=1))[0:-10],
                            'urgent': '1'
                        }
                    else:
                        Data = {
                            'to_datetime': str(datetime.now())[0:-10],
                            'from_datetime': str(datetime.now() - timedelta(days=1))[0:-10],
                        }
                    Url_ = f'{my_URL}t-bot/market-orders/'
                    Data = str(Data).replace("'", '"')
                    r = requests.get(Url_, headers=Header, data=Data)
                    r = jsonpickle.decode(r.text)
                    hhhh = 0
                    for i in r:
                        if hhhh == 50:
                            key = yes_no_keyboard(language_user)
                            send("Пока что я могу показать вам только 50 заказов.", viber_request.sender.id, True)
                            hhhh = 0
                            print("t" + str(hhhh))
                            t = False
                            break
                        hhhh+=1
                        try:
                            send_answer(i, viber_request.sender.id, False)
                        except:
                            print(str(hhhh) + "dsf")
                    if t:
                        send(str(cancel_text['def_but'][language_user]), viber_request.sender.id, True)
            else:
                print(request.get_json()['message']['text'] + "\n")
                print(viber_request.sender.id)
                send(str(error_buttons[language_user]),viber_request.sender.id,True)
        work = True
        return Response(status=200)
    else:
        return Response(status=202)

if __name__ == "__main__":
    try:
        app.run(host="192.168.111.25", port=8008)
    except:
        print("Error app")