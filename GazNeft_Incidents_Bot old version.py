import telebot
from telebot import types

token=''
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    with open('incidents.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption='АВАРИЯ НА СКВАЖИНЕ. ОТКРЫТОЕ ФОНТАНИРОВАНИЕ')
    bot.send_message(message.chat.id, 'Сбор исходных данных об аварии, введите /step1 для продолжения')
@bot.message_handler(commands=['step1'])
def step1_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton('Наличие пострадавших')
    item2=types.KeyboardButton('Наличие завалов и обрушений')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'КАКАЯ ЧИСЛЕННОСТЬ СПАСАТЕЛЕЙ НЕОБХОДИМА?', reply_markup=markup)
    bot.send_message(message.chat.id, 'Базовая численность группы спасателей: 12 спасателей', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ['Наличие пострадавших', 'Наличие завалов и обрушений'])
def process_step1_reply(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Наличие пострадавших':
        bot.send_message(message.chat.id, '+ 4 спасателя = 16', reply_markup=markup)
    elif message.text == 'Наличие завалов и обрушений':
        bot.send_message(message.chat.id, '+ 12 спасателей = 24', reply_markup=markup)
    bot.send_message(message.chat.id, 'Введите /step2 для продолжения', reply_markup=markup)

@bot.message_handler(commands=['step2'])
def step2_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Горящее аварийно-выбрасываемое вещество')
    item2 = types.KeyboardButton('Присутствуют токсичные вещества')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'КАКИЕ СРЕДСТВА ИНДИВИДУАЛЬНОЙ ЗАЩИТЫ ТРЕБУЮТСЯ ДЛЯ СПАСАТЕЛЕЙ?', reply_markup=markup)
    bot.send_message(message.chat.id, 'Воздушно-дыхательные аппараты (по числу спасателей + резерв 4 шт.)', reply_markup=markup)
    bot.send_message(message.chat.id, 'Защитный шлем (по числу спасателей)', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ['Горящее аварийно-выбрасываемое вещество', 'Присутствуют токсичные вещества'])
def process_step2_reply(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Горящее аварийно-выбрасываемое вещество':
        bot.send_message(message.chat.id, 'теплоотражающий костюм')
        bot.send_message(message.chat.id, 'теплоотражающие щиты (4шт.)')
    elif message.text == 'Присутствуют токсичные вещества':
        bot.send_message(message.chat.id, 'костюм химзащиты')
    bot.send_message(message.chat.id, 'Введите /step3 для продолжения', reply_markup=markup)

@bot.message_handler(commands=['step3'])
def step3_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Наличие пострадавших на месте аварии')
    item2 = types.KeyboardButton('Завалы и обрушения')
    item3 = types.KeyboardButton('Повреждено оборудование на устье скважины')
    item4 = types.KeyboardButton('Горящее состояние аварийно-выбрасываемого вещества')
    item5 = types.KeyboardButton('Присутствуют токсичные вещества на месте аварии')
    item6 = types.KeyboardButton('Присутствуют разливы пожароопасных веществ')
    markup.add(item1, item2, item3, item4, item5, item6)
    bot.send_message(message.chat.id, 'КАКОЕ ОБОРУДОВАНИЕ ТРЕБУЕТСЯ ДЛЯ ЛИКВИДАЦИИ АВАРИИ?', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ['Наличие пострадавших на месте аварии', 'Завалы и обрушения', 'Повреждено оборудование на устье скважины','Горящее состояние аварийно-выбрасываемого вещества', 'Присутствуют токсичные вещества на месте аварии', 'Присутствуют разливы пожароопасных веществ'])
def process_step3_reply(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Наличие пострадавших на месте аварии':
        bot.send_message(message.chat.id, 'тепловизор, носилки, спасательное устройство, мешок Амбу, кровоостнавливающие и перевязочные материалы')
    elif message.text == 'Завалы и обрушения':
        bot.send_message(message.chat.id, 'оборудование и оснастка для расчистки места аварии от металлокунструкций')
    elif message.text == 'Повреждено оборудование на устье скважины':
        bot.send_message(message.chat.id, '1) оборудование для создания фланцевой базы\n2) комплект оборудования дистанционной резки металлоконструкций\n3) запорно-устьевое устройство\n4) оборудование и техническая оснастка для наведения запорно-установочного устройства на устье скважины\n5) роботизированный многофункцианальный комплекс фонтанирующих скважин\n6) гидравлическая станция высокого давления\n7) тяговая лебёдка')
    elif message.text == 'Горящее состояние аварийно-выбрасываемого вещества':
        bot.send_message(message.chat.id, 'пламеподавитель - 2шт., оборудование для создания водяных завес')
    elif message.text == 'Присутствуют токсичные вещества на месте аварии':
        bot.send_message(message.chat.id, 'устройства для дистанционного поджига фонтанирующей скважины')
    elif message.text == 'Присутствуют разливы пожароопасных веществ':
        bot.send_message(message.chat.id, 'оборудование для ликвидации аварийных разливов')
    bot.send_message(message.chat.id, 'Введите /step4 для продолжения', reply_markup=markup)

@bot.message_handler(commands=['step4'])
def step4_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Неисправно оборудование на устье скважины')
    item2 = types.KeyboardButton('Имеются разливы пожароопасных веществ')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'КАКОЙ АВТОТРАНСПОРТ И СПЕЦТЕХНИКА ТРЕБУЮТСЯ ДЛЯ ЛИКВИДАЦИИ АВАРИИ?', reply_markup=markup)
    bot.send_message(message.chat.id, 'Специальная техника:\n1) аварийно-спасательный автомобиль\n2) штабной автомобиль\n3) грузовой автомобиль для перевозки аварийно-спасательного оборудования\n4) пожарный автомобиль - 2шт.\n5) автомобиль скорой медецинской помощи\n6) передвижной насосный агрегат', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ['Неисправно оборудование на устье скважины','Имеются разливы пожароопасных веществ'])
def process_step4_reply(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Неисправно оборудование на устье скважины':
        bot.send_message(message.chat.id, '1) кран прицепной\n2) кран автомобильный\n3) бульдозер')
    elif message.text == 'Имеются разливы пожароопасных веществ':
        bot.send_message(message.chat.id, '1) экскаватор\n2) автоцистерна')
    bot.send_message(message.chat.id,'Введите /step5 для продолжения', reply_markup=markup)

@bot.message_handler(commands=['step5'])
def step5_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Отсутствуют токсичные вещества на месте аварии')
    item2 = types.KeyboardButton('Имеются токсичные вещества на месте аварии')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'ПРЕДЛАГАЕМЫЙ ПЛАН ЛИКВИДАЦИИ АВАРИИ:', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ['Отсутствуют токсичные вещества на месте аварии','Имеются токсичные вещества на месте аварии'])
def process_step5_reply(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Отсутствуют токсичные вещества на месте аварии':
        bot.send_message(message.chat.id, '1) разведка места аварии и поиск пострадавших\n2) эвакуация пострадавших из опасной зоны и оказание первой помощи\n3) создание штаба по ликвидации аварии\n4) расчистка завалов металлоконструкций\n5) тушение горящего фонтана\n6) демонтаж повреждённого оборудования\n7) подготовка устья скважины к наведению запорного устройства\n8) наведение устьевого запорного устройства\n9) закрытие устьевого запорного устройства\n10) глушение скважины')
    elif message.text == 'Имеются токсичные вещества на месте аварии':
        bot.send_message(message.chat.id, '1) разведка места аварии и поиск пострадавших\n2) эвакуация пострадавших из опасной зоны и оказание первой помощи\n3) поджиг фонтанирующей среды\n4) создание штаба по ликвидации аварии\n5) расчистка завалов металлоконструкций\n6) демонтаж повреждённого оборудования\n7) подготовка устья\n8) наведение устьевого запорного устройства\n9) закрытие устьевого запорного устройства\n10) глушение скважины')
    bot.send_message(message.chat.id,'Введите /start для перезапуска', reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def catch_all(message):
    bot.send_message(message.chat.id, 'Неизвестная команда, введите /start для начала')

bot.infinity_polling()