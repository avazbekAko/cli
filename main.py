import logging
import aiogram.utils.markdown as md
import jsonpickle as jsonpickle
import requests as requests
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

my_URL = 'http://testapi.gram.tj/api/'
token = "5093577230:AAHFAG6U0U3AaGo1tgGC2eyRaxcjbQZbnS8"

bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

name = ''
phone = ''

phone_ = ''
dop_phone = ''
from_city_id_ = ''
to_city_id_ = ''
amount_ = ''
number = ''
cargo = ''
type_payment = ''
performer_count = ''
urgent = ''
comment = ''
auto_type_id = ''
pick_time = ''

class new_order(StatesGroup):
    phone_ = State()
    dop_phone = State()
    from_countries_id_ = State()
    from_city_id_ = State()
    to_countries_id_ = State()
    to_city_id_ = State()
    amount_ = State()
    weight = State()
    cargo = State()
    type_payment = State()
    performer_count = State()
    urgent = State()
    comment = State()
    auto_type_id = State()
    pick_time = State()
    error = State()


class reg(StatesGroup):
    name = State()
    number = State()
    error = State()

#----------------------------cancel----------------------------------------
@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    logging.info('Cancelling state %r', current_state)
    await state.finish()
    await message.reply('Вы остановили все процессы.',  reply_markup=types.ReplyKeyboardRemove())

#-----------------------------NEW-order--------------------------------------
@dp.message_handler(commands='new')
async def phone_(message: types.Message):
    global phone
    global name
    Data = {
        'phone': '+992557776484',
        'password': 'password',
    }
    response = requests.post(f'{my_URL}auth/login', data=Data)
    answer = jsonpickle.decode(response.text)
    token_ = str(answer['access_token'])
    ttt = "Bearer " + token_
    chat_id = message.chat.id
    Header = {
        'Authorization': ttt,
    }
    r = requests.get(f'{my_URL}t-bot/client-info/{chat_id}', headers=Header, data=Data)
    if str(r.text) == '{}':
        await reg.name.set()
        await message.reply(
            f"Здравствуйте {message.chat.first_name} вы ещё не зарегистрированы в нашем боте.\nДля продолжения вам нужно пройти небольшую регистрацию.",
            reply_markup=types.ReplyKeyboardRemove())
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Да"]
        keyboard.add(
            *buttons,
        )
        await message.answer(f"Вас зовут {message.chat.full_name}? Если нет то введите своё ФИО.",
                             reply_markup=keyboard)
    else:
        answer = jsonpickle.decode(r.text)
        name = answer['full_name']
        phone = answer['phone']
        await new_order.phone_.set()
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Да"]
        keyboard.add(
            *buttons,
        )
    await message.reply(
        f"Ваш номер телефона {phone}? Если нет введите свой номер телефона для связи с вами (например: +7**********).",
        reply_markup=keyboard)

@dp.message_handler(state=new_order.phone_)
async def new_order_1(message: types.Message):
    global phone
    global phone_
    if message.text == 'Да':
        phone_ = phone
    else:
        phone_ = message.text
    await new_order.next()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Пропустить"]
    keyboard.add(
        *buttons,
    )
    await message.reply(
        "Введите дополнительный номер телефона для связи с вами (например: +7**********).\nТак как это не обязательное поле вы можете его пропустить",
        reply_markup=keyboard)

@dp.message_handler(state=new_order.dop_phone)
async def new_order_2(message: types.Message):
    global dop_phone
    if message.text == 'Пропустить':
        dop_phone = 'null'
    else:
        dop_phone = message.text
    await new_order.next()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = []

    Data = {
        'phone': '+992557776484',
        'password': 'password',
    }
    response = requests.post(f'{my_URL}auth/login', data=Data)
    answer = jsonpickle.decode(response.text)
    token_ = str(answer['access_token'])
    ttt = "Bearer " + token_
    Header = {
        'Authorization': ttt,
    }
    r = requests.get(f'{my_URL}countries', headers=Header)
    re = jsonpickle.decode(r.text)
    for i in re:
        buttons += [f"{i['id']}: {i['name']}"]
    keyboard.add(
        *buttons,
    )
    await message.reply("Выберите страну отправителя", reply_markup=keyboard)

@dp.message_handler(state=new_order.from_countries_id_)
async def new_order_3(message: types.Message):
    from_countries = ''
    from_city_id = message.text
    for r in from_city_id:
        if r == ':':
            break
        else:
            from_countries += r
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = []

    Data = {
        'phone': '+992557776484',
        'password': 'password',
    }
    response = requests.post(f'{my_URL}auth/login', data=Data)
    answer = jsonpickle.decode(response.text)
    token_ = str(answer['access_token'])
    ttt = "Bearer " + token_
    Header = {
        'Authorization': ttt,
    }
    r = requests.get(f'{my_URL}cities', headers=Header)
    re = jsonpickle.decode(r.text)
    for i in re:
        buttons += [f"{i['id']}: {i['name']}"]
    keyboard.add(
        *buttons,
    )
    await new_order.next()
    await message.reply("Выберите город отправителя", reply_markup=keyboard)

@dp.message_handler(state=new_order.from_city_id_)
async def new_order_3(message: types.Message):
    global from_city_id_
    from_city_id_ = ''
    from_city_id = message.text
    for r in from_city_id:
        if r == ':':
            break
        else:
            from_city_id_ += r
    await new_order.next()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = []

    Data = {
        'phone': '+992557776484',
        'password': 'password',
    }
    response = requests.post(f'{my_URL}auth/login', data=Data)
    answer = jsonpickle.decode(response.text)
    token_ = str(answer['access_token'])
    ttt = "Bearer " + token_
    Header = {
        'Authorization': ttt,
    }
    r = requests.get(f'{my_URL}countries', headers=Header)
    re = jsonpickle.decode(r.text)
    for i in re:
        buttons += [f"{i['id']}: {i['name']}"]
    keyboard.add(
        *buttons,
    )
    await message.reply(f"Выберите страну получателя.", reply_markup=keyboard)

@dp.message_handler(state=new_order.to_countries_id_)
async def new_order_4(message: types.Message):
    to_countries_ = message.text
    to_countries = ''
    for r in to_countries_:
        if r == ':':
            break
        else:
            to_countries += r
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = []

    Data = {
        'phone': '+992557776484',
        'password': 'password',
    }
    response = requests.post(f'{my_URL}auth/login', data=Data)
    answer = jsonpickle.decode(response.text)
    token_ = str(answer['access_token'])
    ttt = "Bearer " + token_
    Header = {
        'Authorization': ttt,
    }
    r = requests.get(f'{my_URL}cities', headers=Header)
    re = jsonpickle.decode(r.text)
    for i in re:
        buttons += [f"{i['id']}: {i['name']}"]
    keyboard.add(
        *buttons,
    )
    await new_order.next()
    await message.reply("Выберите город получателя.", reply_markup=keyboard)

@dp.message_handler(state=new_order.to_city_id_)
async def new_order_4(message: types.Message):
    global to_city_id_
    to_city_id_ = ''
    to_city = message.text
    for r in to_city:
        if r == ':':
            break
        else:
            to_city_id_ += r
    await new_order.next()
    await message.reply("Стоимость заказа.\nНапример 123.45", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(state=new_order.amount_)
async def new_order_5(message: types.Message):
    global amount_
    amount_ = message.text
    await new_order.next()
    await message.reply("Введите объём вашего груза.", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(state=new_order.weight)
async def new_order_6(message: types.Message):
    global weight
    if message.text == 'Пропустить':
        weight = 'null'
    else:
        weight = message.text
    await new_order.next()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Пропустить"]
    keyboard.add(
        *buttons,
    )
    await message.reply("Введите тип вашего груза.\nТак как это не обязательное поле вы можете его пропустить",
                        reply_markup=keyboard)

@dp.message_handler(state=new_order.cargo)
async def new_order_7(message: types.Message):
    global cargo
    if message.text == 'Пропустить':
        cargo = 'null'
    else:
        cargo = message.text
    await new_order.next()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Пропустить"]
    keyboard.add(
        *buttons,
    )
    await message.reply(
        "Введите тип оплаты вашего заказа.\nТак как это не обязательное поле вы можете его пропустить",
        reply_markup=keyboard)

@dp.message_handler(state=new_order.type_payment)
async def new_order_8(message: types.Message):
    global type_payment
    if message.text == 'Пропустить':
        type_payment = 'null'
    else:
        type_payment = message.text
    await new_order.next()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Пропустить"]
    keyboard.add(
        *buttons,
    )
    await message.reply(
        "Введите колличество водителей нужных для выполнения вашего заказа.\nТак как это не обязательное поле вы можете его пропустить",
        reply_markup=keyboard)

@dp.message_handler(state=new_order.performer_count)
async def new_order_9(message: types.Message):
    global performer_count
    if message.text == 'Пропустить':
        performer_count = 'null'
    else:
        performer_count = message.text
    await new_order.next()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Да", 'Нет']
    keyboard.add(
        *buttons,
    )
    await message.reply("Ваш заказ срочный?.",
                        reply_markup=keyboard)

@dp.message_handler(state=new_order.urgent)
async def new_order_10(message: types.Message):
    global urgent
    if message.text == 'Нет':
        urgent = 'null'
    else:
        urgent = 'null'
    await new_order.next()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Пропустить"]
    keyboard.add(
        *buttons,
    )
    await message.reply(
        "Введите коментарий к вашему заказу.\nТак как это не обязательное поле вы можете его пропустить",
        reply_markup=keyboard)

@dp.message_handler(state=new_order.comment)
async def new_order_11(message: types.Message):
    global comment
    if message.text == 'Пропустить':
        comment = 'null'
    else:
        comment = message.text
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = []

    Data = {
        'phone': '+992557776484',
        'password': 'password',
    }
    response = requests.post(f'{my_URL}auth/login', data=Data)
    answer = jsonpickle.decode(response.text)
    token_ = str(answer['access_token'])
    ttt = "Bearer " + token_
    Header = {
        'Authorization': ttt,
    }
    r = requests.get(f'{my_URL}cities', headers=Header)
    re = jsonpickle.decode(r.text)
    for i in re:
        buttons += [f"{i['id']}: {i['name']}"]
    await new_order.next()
    buttons += ["Пропустить"]
    keyboard.add(
        *buttons,
    )
    await message.reply("Выберите вид автомобиля нужного для перевлзки вашего заказа.\nТак как это не обязательное поле вы можете его пропустить",
                        reply_markup=keyboard)

@dp.message_handler(state=new_order.auto_type_id)
async def new_order_12(message: types.Message):
    global auto_type_id
    if message.text == 'Пропустить':
        auto_type_id = 'null'
    else:
        auto_type_id = message.text
    await new_order.next()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Пропустить"]
    keyboard.add(
        *buttons,
    )
    await message.reply(
        "Введите крайний срок отправки груза (например: 2022-01-12 15:15 ).\nТак как это не обязательное поле вы можете его пропустить",
        reply_markup=keyboard)

@dp.message_handler(state=new_order.pick_time)
async def new_order_13(message: types.Message):
    global pick_time
    if message.text == 'Пропустить':
        pick_time = 'null'
    else:
        pick_time = message.text
    await new_order.next()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Да", 'Нет']
    keyboard.add(
        *buttons,
    )
    Data = {
        'phone': phone_,
        'dop_phone': dop_phone,
        'from_city_id': from_city_id_,
        'to_city_id': to_city_id_,
        'amount': amount_,
        'weight': weight,
        'cargo': cargo,
        'type_payment': type_payment,
        'performer_count': performer_count,
        'urgent': urgent,
        'comment': comment,
        'auto_type_id': auto_type_id,
        'pick_time': pick_time,
    }
    Data = str(Data).replace("'null'", 'null')
    Data = str(Data).replace("'", '"')
    Data = str(Data).replace('", "amount": "', ', Цена = ')
    Data = str(Data).replace('", "weight": "', ', Объём = ')
    Data = str(Data).replace('"dop_phone": null, ', "")
    Data = str(Data).replace('"cargo": null, ', "")
    Data = str(Data).replace('"type_payment": null, ', "")
    Data = str(Data).replace('"performer_count": null, ', "")
    Data = str(Data).replace('"urgent": null, ', "")
    Data = str(Data).replace('"comment": null, ', "")
    Data = str(Data).replace('"auto_type_id": null, ', "")
    Data = str(Data).replace(', "pick_time": null', "")
    Data = str(Data).replace('", "cargo":', ', Тип вашего груза: ')
    Data = str(Data).replace(',', '\n')
    Data = str(Data).replace('{"phone": "', 'Ваш номер телефона: ')
    Data = str(Data).replace('", "to_city_id": "', ', Город получателя: ')
    Data = str(Data).replace('"from_city_id": "', 'Город отправителя: ')
    Data = str(Data).replace('"}', '')
    await message.reply(f"{ Data }")
    await message.reply("Так выглядит ваш заказ.\nВсё верно?", reply_markup=keyboard)


@dp.message_handler(state=new_order.error)
async def new_order_14(message: types.Message):
    global my_URL
    if message.text == 'Да':
        Data = {
            'phone': '+992557776484',
            'password': 'password',
        }
        response = requests.post(f'{my_URL}auth/login', data=Data)
        answer = jsonpickle.decode(response.text)
        token_ = str(answer['access_token'])
        ttt = "Bearer " + token_
        Data = {
            'phone': phone_,
            'dop_phone': dop_phone,
            'from_city_id': from_city_id_,
            'to_city_id': to_city_id_,
            'amount': amount_,
            'weight': weight,
            'cargo': cargo,
            'type_payment': type_payment,
            'performer_count': performer_count,
            'urgent': urgent,
            'comment': comment,
            'auto_type_id': auto_type_id,
            'pick_time': pick_time,
        }
        Data = str(Data).replace("'null'", 'null')
        Data = str(Data).replace("'", '"')
        Data = str(Data).replace(', "amount": "', ', "amount": ')
        Data = str(Data).replace('", "weight": "', ', "weight": ')
        Data = str(Data).replace('", "cargo":', ', "cargo":')
        Data = str(Data).replace('"dop_phone": null, ', "")
        Data = str(Data).replace('"cargo": null, ', "")
        Data = str(Data).replace('"type_payment": null, ', "")
        Data = str(Data).replace('"performer_count": null, ', "")
        Data = str(Data).replace('"urgent": null, ', "")
        Data = str(Data).replace('"comment": null, ', "")
        Data = str(Data).replace('"auto_type_id": null, ', "")
        Data = str(Data).replace(', "pick_time": null', "")
        Header = {
            'Authorization': ttt,
            'Content-Type': 'application/json',
        }
        r = requests.post(f'{my_URL}t-bot/market-orders', headers=Header, data=Data)
        r = jsonpickle.decode(r.text)
        for i in r:
            if str(i) == 'errors':
                await message.answer(f"Произошла ошибка. Проверьте свои данные и повторите попытку")
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                buttons = ["Да"]
                keyboard.add(
                    *buttons,
                )
                await message.reply(
                    f"Ваш номер телефона {phone}? Если нет введите свой номер телефона для связи с вами (например: +7**********).",
                    reply_markup=keyboard)
                await new_order.phone_.set()
            else:
                await message.reply(
                    f"{r['message']}",
                    reply_markup=types.ReplyKeyboardRemove())
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Да"]
        keyboard.add(
            *buttons,
        )
        await message.reply(
            f"Ваш номер телефона {phone}? Если нет введите свой номер телефона для связи с вами (например: +7**********).",
            reply_markup=keyboard)
        await new_order.phone_.set()

#--------------------------------------------------------------------
@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    global my_URL
    global name
    global phone
    Data = {
        'phone': '+992557776484',
        'password': 'password',
    }
    response = requests.post(f'{my_URL}auth/login', data=Data)
    answer = jsonpickle.decode(response.text)
    token_ = str(answer['access_token'])
    ttt = "Bearer " + token_
    chat_id = message.chat.id
    Header = {
        'Authorization': ttt,
    }
    r = requests.get(f'{my_URL}t-bot/client-info/{chat_id}', headers=Header, data=Data)
    if str(r.text) == '{}':
        await reg.name.set()
        await message.reply(
            f"Здравствуйте {message.chat.first_name} рады видеть вас в нашем боте.\nДля продолжения вам нужно пройти небольшую регистрацию.",
            reply_markup=types.ReplyKeyboardRemove())
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Да"]
        keyboard.add(
            *buttons,
        )
        await message.answer(f"Вас зовут {message.chat.full_name}? Если нет то введите своё ФИО.",
                             reply_markup=keyboard)
    else:
        answer = jsonpickle.decode(r.text)
        name = answer['full_name']
        phone = answer['phone']
        await message.reply(
            f"Здравствуйте {name} вы уже зарегистрированы.\nДля оформления новых заказов введите /new",
            reply_markup=types.ReplyKeyboardRemove()
        )
@dp.message_handler(state=reg.name)
async def register_1(message: types.Message):
    global name
    if message.text == 'Да':
        name = message.chat.full_name
    else:
        name = message.text
    await reg.next()
    await message.reply("Введите свой номер телефона для связи с вами (например: +7**********).",  reply_markup=types.ReplyKeyboardRemove())
@dp.message_handler(state=reg.number)
async def register_2(message, state: FSMContext):
    global phone
    phone = message.text
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Да", "Нет"]
    keyboard.add(
        *buttons,
    )
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text('Вас зовут: ', (name)),
            md.text('Ваш номер телефона: ', (phone)),
            sep='\n',
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )
    await bot.send_message(
        message.chat.id,
        "Всё верно?"
    )
    await reg.next()
@dp.message_handler(state=reg.error)
async def register_3(message: types.Message):
    global my_URL
    if message.text == 'Да':
        Data = {
            'phone': '+992557776484',
            'password': 'password',
        }
        response = requests.post(f'{my_URL}auth/login', data=Data)
        answer = jsonpickle.decode(response.text)
        token_ = str(answer['access_token'])
        ttt = "Bearer " + token_
        chat_id = message.chat.id
        Data = {
            'phone': phone,
            'full_name': name,
            'telegram_chat_id': chat_id
        }
        Header = {
            'Authorization': ttt,
        }
        r = requests.post(f'{my_URL}t-bot/register-client', headers = Header, data = Data)
        if r.status_code == 200:
            await message.answer(f"Поздравляем вы зарегистрировались.\nТеперь введите /new для оформления новых заказов.")
        r = jsonpickle.decode(r.text)
        for i in r:
            if str(i) == 'errors':
                await message.answer(f"Произошла ошибка. Проверьте свои данные и повторите попытку")
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                buttons = ["Да"]
                keyboard.add(
                    *buttons,
                )
                await message.answer(f"Вас зовут {message.chat.full_name}? Если нет то введите своё ФИО.",
                                     reply_markup=keyboard)
                await reg.name.set()
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Да"]
        keyboard.add(
            *buttons,
        )
        await message.answer(f"Вас зовут {message.chat.full_name}? Если нет то введите своё ФИО.",
                             reply_markup=keyboard)
        await reg.name.set()



#---------------------error-----------------------------------------------------
@dp.message_handler()
async def error(message: types.Message, state: FSMContext):
    await message.reply("error",  reply_markup=types.ReplyKeyboardRemove())

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
