import telebot
from telebot import types

token=''
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    with open('incidents.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption='АВАРИЯ НА СКВАЖИНЕ. ОТКРЫТОЕ ФОНТАНИРОВАНИЕ')
    bot.send_message(message.chat.id, 'Сбор исходных данных об аварии')
    step1_message(message)

def step1_message(message):
    markup=types.InlineKeyboardMarkup()
    item1=types.InlineKeyboardButton('Наличие пострадавших', callback_data='step1_postra')
    item2=types.InlineKeyboardButton('Наличие завалов и обрушений', callback_data='step1_zaval')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'КАКАЯ ЧИСЛЕННОСТЬ СПАСАТЕЛЕЙ НЕОБХОДИМА?', reply_markup=markup)
    bot.send_message(message.chat.id, 'Базовая численность группы спасателей: 12 спасателей')

@bot.callback_query_handler(func=lambda call: call.data.startswith('step1'))
def process_step1_reply(call):
    if call.data=='step1_postra':
        bot.send_message(call.message.chat.id, '+ 4 спасателя = 16')
    elif call.data=='step1_zaval':
        bot.send_message(call.message.chat.id, '+ 12 спасателей = 24')
    step2_message(call.message)

def step2_message(message):
    markup=types.InlineKeyboardMarkup()
    item1=types.InlineKeyboardButton('Горящее вещество', callback_data='step2_fire')
    item2=types.InlineKeyboardButton('Токсичные вещества', callback_data='step2_toxic')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'КАКИЕ СРЕДСТВА ИНДИВИДУАЛЬНОЙ ЗАЩИТЫ ТРЕБУЮТСЯ ДЛЯ СПАСАТЕЛЕЙ?', reply_markup=markup)
    bot.send_message(message.chat.id, 'Воздушно-дыхательные аппараты (по числу спасателей + резерв 4 шт.)')
    bot.send_message(message.chat.id, 'Защитный шлем (по числу спасателей)')

@bot.callback_query_handler(func=lambda call: call.data.startswith('step2'))
def process_step2_reply(call):
    if call.data=='step2_fire':
        bot.send_message(call.message.chat.id, 'теплоотражающий костюм')
        bot.send_message(call.message.chat.id, 'теплоотражающие щиты (4шт.)')
    elif call.data=='step2_toxic':
        bot.send_message(call.message.chat.id, 'костюм химзащиты')
    step3_message(call.message)

def step3_message(message):
    markup=types.InlineKeyboardMarkup()
    items=[
        types.InlineKeyboardButton('Пострадавшие', callback_data='step3_postra'),
        types.InlineKeyboardButton('Завалы и обрушения', callback_data='step3_zaval'),
        types.InlineKeyboardButton('Повреждено оборудование', callback_data='step3_equip'),
        types.InlineKeyboardButton('Горящее вещество', callback_data='step3_fire'),
        types.InlineKeyboardButton('Токсичные вещества', callback_data='step3_toxic'),
        types.InlineKeyboardButton('Разливы пожароопасных веществ', callback_data='step3_spill')
    ]
    markup.add(*items)
    bot.send_message(message.chat.id, 'КАКОЕ ОБОРУДОВАНИЕ ТРЕБУЕТСЯ ДЛЯ ЛИКВИДАЦИИ АВАРИИ?', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('step3'))
def process_step3_reply(call):
    responses={
        'step3_postra': 'тепловизор, носилки, спасательное устройство, мешок Амбу, кровоостанавливающие и перевязочные материалы',
        'step3_zaval': 'оборудование и оснастка для расчистки места аварии от металлоконструкций',
        'step3_equip': '1) оборудование для создания фланцевой базы\n2) комплект оборудования дистанционной резки металлоконструкций\n3) запорно-устьевое устройство\n4) оборудование и техническая оснастка для наведения запорно-установочного устройства на устье скважины\n5) роботизированный многофункциональный комплекс фонтанирующих скважин\n6) гидравлическая станция высокого давления\n7) тяговая лебёдка',
        'step3_fire': 'пламеподавитель - 2шт., оборудование для создания водяных завес',
        'step3_toxic': 'устройства для дистанционного поджига фонтанирующей скважины',
        'step3_spill': 'оборудование для ликвидации аварийных разливов пожароопасных веществ'
    }
    bot.send_message(call.message.chat.id, responses[call.data])
    step4_message(call.message)

def step4_message(message):
    markup=types.InlineKeyboardMarkup()
    item1=types.InlineKeyboardButton('Неисправно оборудование', callback_data='step4_equip')
    item2=types.InlineKeyboardButton('Разливы пожароопасных веществ', callback_data='step4_spill')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'КАКОЙ АВТОТРАНСПОРТ И СПЕЦТЕХНИКА ТРЕБУЮТСЯ ДЛЯ ЛИКВИДАЦИИ АВАРИИ?', reply_markup=markup)
    bot.send_message(message.chat.id, 'Специальная техника:\n1) аварийно-спасательный автомобиль\n2) штабной автомобиль\n3) грузовой автомобиль для перевозки аварийно-спасательного оборудования\n4) пожарный автомобиль - 2шт.\n5) автомобиль скорой медицинской помощи\n6) передвижной насосный агрегат')

@bot.callback_query_handler(func=lambda call: call.data.startswith('step4'))
def process_step4_reply(call):
    if call.data=='step4_equip':
        bot.send_message(call.message.chat.id, '1) кран прицепной\n2) кран автомобильный\n3) бульдозер')
    elif call.data=='step4_spill':
        bot.send_message(call.message.chat.id, '1) экскаватор\n2) автоцистерна')
    step5_message(call.message)

def step5_message(message):
    markup=types.InlineKeyboardMarkup()
    item1=types.InlineKeyboardButton('Отсутствуют токсичные вещества', callback_data='step5_notoxic')
    item2=types.InlineKeyboardButton('Имеются токсичные вещества', callback_data='step5_toxic')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'ПРЕДЛАГАЕМЫЙ ПЛАН ЛИКВИДАЦИИ АВАРИИ:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('step5'))
def process_step5_reply(call):
    if call.data=='step5_notoxic':
        bot.send_message(call.message.chat.id, '1) разведка места аварии и поиск пострадавших\n2) эвакуация пострадавших из опасной зоны и оказание первой помощи\n3) создание штаба по ликвидации аварии\n4) расчистка завалов металлоконструкций\n5) тушение горящего фонтана\n6) демонтаж повреждённого оборудования\n7) подготовка устья скважины к наведению запорного устройства\n8) наведение устьевого запорного устройства\n9) закрытие устьевого запорного устройства\n10) глушение скважины')
    elif call.data=='step5_toxic':
        bot.send_message(call.message.chat.id, '1) разведка места аварии и поиск пострадавших\n2) эвакуация пострадавших из опасной зоны и оказание первой помощи\n3) поджиг фонтанирующей среды\n4) создание штаба по ликвидации аварии\n5) расчистка завалов металлоконструкций\n6) демонтаж повреждённого оборудования\n7) подготовка устья\n8) наведение устьевого запорного устройства\n9) закрытие устьевого запорного устройства\n10) глушение скважины')
    bot.send_message(call.message.chat.id, 'Введите /start для перезапуска')

@bot.message_handler(commands=['step1', 'step2', 'step3', 'step4', 'step5'])
def menu_handler(message):
    if message.text=='/step1':
        step1_message(message)
    elif message.text=='/step2':
        step2_message(message)
    elif message.text=='/step3':
        step3_message(message)
    elif message.text=='/step4':
        step4_message(message)
    elif message.text=='/step5':
        step5_message(message)

bot.infinity_polling()