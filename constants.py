
d = {
    'ru':{
        'test': ['Test.'],
        'er': ['Собщение с не выбранной функцией.'],
        'search': ['Поиск по заказам.'],
        'show_city':['Показать заказы из вашего города.'],
        'show_by_24':['Показать все заказы за последние 24 часа'],
        'show_by_urgent' :['Показать все срочные заказы'],
        'show_by_  id':[ 'Показать по номеру заказа'],
        'my_status':[ 'Мой статус'],
        'reg':['Регистрация'],
        'cancel':[ 'Отменено'],
        'setings': 'Нажал на кнопку смены языка'
    },
    'en': {
        'test': ['Test.'],
        'er': ['Message with no function selected.'],
        'search': ['Search by orders.'],
        'show_city': ['Show orders from your city.'],
        'show_by_24': ['Show all orders in the last 24 hours'],
        'show_by_urgent': ['Show all urgent orders'],
        'show_by_ id': ['Show by order number'],
        'my_status': ['My status'],
        'reg': ['Register'],
        'cancel': ['Canceled'],
        'setings': 'Нажал на кнопку смены языка'
    }
}
def_buttons = {
    'ru': {
        'search': ['🔍 Поиск заказа'],
		'status': ['👤 Мой статус'],
        'show_by_id': ['📤 Показать заказ по номеру'],
		'show_by_24': ['🕛 Показать все заказы за последние 24 часа'],
		'show_all_urgant': ['⚡️ Показать все срочные заказы'],
		'search_by_citi': ['📍 Показать все заказы из вашего города'],
		'setings': ['⚙️ Настройки языка'],
		'reg': ['📝 Зарегистрироваться']
	},
	'en': {
        'search': ['🔍 Order search'],
		'status': ['👤 My status'],
		'show_by_id': ['📤 Show order by number'],
		'show_by_24': ['🕛 Show all orders in the last 24 hours'],
		'show_all_urgant': ['⚡️ Show all urgent orders'],
		'search_by_citi': ['📍 Show all orders from your city'],
		'setings': ['⚙️ Language settings'],
		'reg': ['📝 Register']
	}
}
show_city_text = {
    'ru': {
        'country': 'Выберите интересующую Вас страну.',
        'country_error': 'Эта страна не обслуживается.',
        'state': 'Выберите интересующую Вас область.',
        'state_error': 'Этот область не обслуживается.',
        'city': 'Выберите город который Вас интересует.',
        '0': 'За последние 3 дня не было добавлено ни одного заказа из вашего города.',
        'no_0_1': 'За последние 3 дня было добавлено всего ',
        'no_0_2': ' заказов из вашего города. Показать их всех?',
        'er_big': 'Введите пожалуйста количества заказов которое хотели бы увидеть (меньше количества заказов за последние 3 дня).',
    },
    'en': {
        'country': 'Select the country you are interested in.',
        'country_error': 'This country is not served.',
        'state': 'Select the region you are interested in.',
        'state_error': 'This area is out of service.',
        'city': 'Select the city you are interested in.',
        '0': 'No orders from your city have been added in the last 3 days.',
        'no_0_1': 'Total has been added in the last 3 days',
        'no_0_2': ' orders from your city. Show them all?',
        'er_big': 'Please enter the number of orders you would like to see (less than the number of orders in the last 3 days).',
    }
}
register_text = {
    'ru':{
        'name-1': 'Ваше имя ',
        'name-2': '? Если нет то введите своё имя.',
        'f-name': 'Введите свою фамилию.',
        'patronymic': 'Введите отчество.',
        'phone': 'Введите свой номер телефона для связи с вами (например: +77777777777).',
        'end_1': 'Вас зовут:',
        'end_2': '\nВаш номер телефона: ',
    },
    'en':{
        'name-1': 'Your name',
        'name-2': '? If not, enter your name.',
        'f-name': 'Enter your last name.',
        'patronymic': 'Please enter a middle name.',
        'phone': 'Enter your phone number to contact you (for example: +77777777777).',
        'end_1': 'Your name is:',
        'end_2': '\nYour phone number: ',
    }
}
search_text = {
    'ru': {
        'country': 'Выберите страну, в которой вы находитесь.',
        'country_to': 'Выберите страну, в котором вы хотите поехать.',
        'country_error': 'Эта страна не обслуживается.',
        'state': 'Выберите область, в которой вы находитесь.',
        'state_to': 'Выберите область, в которую вы хотите поехать.',
        'state_error': 'Этот область не обслуживается.',
        'city': 'Выберите город, котором вы находитесь.',
        'city_to': 'Выберите город, в который вы хотите поехать.',
        'urgent_nourgent': 'Все',
        'urgent': 'Только срочные',
        'nourgent': 'Только не срочные',
        'urgent_text': 'Выберите тип интересующего вас заказа (из кнопок ниже).',
        'auto_type': 'Выберите тип вашего автомобиля.\nТак как это не обязательное поле, вы можете его пропустить',
        '0': 'За последние 7 дня не было добавлено заказов соответствующих вашим фильтрам.',
        'no_0_1': 'За последние 7 дня было добавлено всего ',
        'no_0_2': ' заказов подходящих по вашим фильтрам. Показать их всех?',
        'er_big': 'Введите пожалуйста количества заказов которое хотели бы увидеть (меньше количества заказов за последние 7 дней).',
	},
	'en': {
        'country': 'Select the country you are in.',
        'country_to': 'Select the country you want to travel to.',
        'country_error': 'This country is not served.',
        'state': 'Select the state you are in.',
        'state_to': 'Select the state you want to go to.',
        'state_error': 'This area is out of service.',
        'city': 'Select the city you are in.',
        'city_to': 'Select the city you want to go to.',
        'urgent_nourgent': 'All',
        'urgent': 'Urgent only',
        'nourgent': 'Not urgent',
        'urgent_text': 'Select the type of order you are interested in (from the buttons below).',
        'auto_type': 'Select your vehicle type.\nAs this is not a required field, you can skip it',
        '0': 'No orders matching your filters have been added in the last 7 days.',
        'no_0_1': 'Total has been added in the last 7 days',
        'no_0_2': ' orders matching your filters. Show them all?',
        'er_big': 'Please enter the number of orders you would like to see (less than the number of orders in the last 7 days).',
	}
}
select_from = {
    'ru': {
        'city': 'Теперь выберите город.\n',
        'list_cities': 'Теперь выберите город.\n',
        'country_sel': "Страна {!s} успешно выбрана.",
    },
    'en': {
        'city': 'Now select a city.',
        'list_cities': 'Now select a city.\n',
        'country_sel': "Country {!s} selected successfully.",
    },
}
show_by_24_text = {}
cancel_text = {}
show_by_id_text = {}
show_all_urgent = {}
type_finction = {}
token_text = '5241881960:AAGJcLipwIa8ymZp_QIQCWO7gg4OZhkdhyA'
text_yes = {'ru': 'Да', 'en' :'Yes' }
text_no = {'ru': 'Нет', 'en' :'No' }
text_next = {'ru': 'Пропустить', 'en': 'Skip' }
error_buttons = {'ru': 'Пожалуйста выберите одну из кнопок ниже.', 'en': 'Please select one of the buttons below'}
error_text = {'ru': 'Ошибка.\nОбратитесь в поддержку @Gram_support_bot.', 'en': 'Error.\nPlease contact @Gram_support_bot support.'}
error_text_0 = {'ru': 'Введите пожалуйста число больше 0.', 'en' :'Please enter a number greater than 0.' }
error_text_num = {'ru': 'Введите пожалуйста число.', 'en' :'Please enter a number.' }
count_orders_text = {'ru': 'Введите количества заказов, которые хотите увидеть.', 'en': 'Enter the number of orders you want to see.' }
function_edit_text = {'ru': 'Функция пока не доступна или находится в модификации.', 'en' :'The function is not yet available or is under modification.' }
test_text = {'ru': 'Привет Авазбек 1', 'en' :'Hello Avazbek 1' }
welcome_1 = {'ru': 'Здравствуйте ', 'en' :'Hello ' }
welcome_2 = {'ru': ' вы уже зарегистрированы.\n', 'en' :' you are already registered.\n' }
welcome1 = {'ru': 'Поздравляем вы успешно зарегистрировались.', 'en' :'Congratulations, you have successfully registered.' }
def_but_cli = 'Нажал на одну из кнопок по умолчанию'
switch_language_text = {}
switch_language_text['sel'] = {'ru': 'Выберите язык','en': 'Choose language'}
switch_language_text['lang'] = {'en': 'en: English','ru': 'ru: Русский'}
switch_language_text['true'] = {'en': 'You have successfully changed the language.','ru': 'Вы успешно сменили язык.'}
cancel_text['button'] = {'ru': 'Назад', 'en' :'Back' }
cancel_text['stop'] = {'ru': 'Вы остановили все процессы.', 'en' :'You have stopped all processes.' }
cancel_text['def_but'] = {'ru': 'Выберите одну из кнопок ниже.', 'en' :'Choose one of the buttons below.' }
cancel_text['state_null'] = {'ru': 'Ни один процесс не задействован.', 'en' :'No process is running.' }

show_by_id_text['input_num'] = {'ru': 'Для получения подробной информации, ведите номер заказа', 'en' :'For more information, please enter your order number.' }
show_by_id_text['error'] = {'ru': 'Не верный номер заказа. Для получения подробной информации, ведите номер заказа', 'en' :'Invalid order number. For more information, please enter your order number.' }

show_by_24_text['0'] = {'ru': f'За последние 24 часа не было добавленно ни одного срочного заказа.', 'en': 'No rush orders have been added in the last 24 hours.'}
show_by_24_text['no_0_1'] = {'ru': 'За последние 24 часа было добавленно всего ', 'en': 'Total added in the last 24 hours '}
show_by_24_text['no_0_2'] = {'ru': '  заказов. Показать их всех? ', 'en': '  orders. Show them all?'}
show_by_24_text['er_big'] = {'ru': 'Введите пожалуйста число меньше количества заказов за последние 24 часа.', 'en': 'Enter the number of orders in the last 24 hours.'}
show_all_urgent['0'] = {'ru': f'За последние 24 часа не было добавленно ни одного срочного заказа.', 'en': 'No rush orders have been added in the last 24 hours.'}
show_all_urgent['no_0_1'] = {'ru': 'За последние 24 часа было добавленно всего ', 'en': 'Total added in the last 24 hours '}
show_all_urgent['no_0_2'] = {'ru': ' срочных заказов. Показать их всех? ', 'en': ' urgent orders. Show them all?'}
show_all_urgent['er_big'] = {'ru': 'Введите пожалуйста число меньше количества заказов за последние 24 часа.', 'en': 'Enter the number of orders in the last 24 hours.'}
type_finction['test'] = 'Test'
type_finction['er'] = 'Собщение с не выбранной функцией'
type_finction['search'] = 'Поиск по заказам'
type_finction['show_city'] = 'Показать заказы из вашего города'
type_finction['show_by_24'] = 'Показать все заказы за последние 24 часа'
type_finction['show_by_urgent'] = 'Показать все срочные заказы'
type_finction['show_by_id'] = 'Показать по номеру заказа'
type_finction['my_status'] = 'Мой статус'
type_finction['reg'] = 'Регистрация'
type_finction['setings'] = 'Нажал на кнопку смены языка'
type_finction['more'] = 'Нажал на кнопку подробнее'
type_finction['cancel'] = 'Отменено'
default_buttons_text = {}
default_buttons_text['search'] = '🔍 Поиск заказа'
default_buttons_text['status'] = '👤 Мой статус'
default_buttons_text['show_by_id'] = '📤 Показать заказ по номеру'
default_buttons_text['show_by_24'] = '🕛 Показать все заказы за последние 24 часа'
default_buttons_text['show_all_urgant'] = '⚡️ Показать все срочные заказы'
default_buttons_text['search_by_citi'] = '📍 Показать все заказы из вашего города'
default_buttons_text['setings'] = '⚙️ Настройки языка'
default_buttons_text['reg'] = '📝 Зарегистрироваться'


