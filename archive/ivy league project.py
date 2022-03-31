import telebot
from telebot import types

bot = telebot.TeleBot("2087712017:AAGfnPLs0UNq0SKufCGPee3VljS0oKyhsuQ")

@bot.message_handler(commands=['start'])
def start(message):
    start_menu = types.ReplyKeyboardMarkup(True, True)
    start_menu.row("О Лиге Плюща", 'Описание Университетов')
    start_menu.row('Стиль Лиги Плюща', 'Как поступить?')
    bot.send_message(message.chat.id, """ Здравствуйте! Я бот Абая!
    Здесь вы можете подробно узнать о Лиге плюща
    -Какая присхождения Лиги плюща
    -Как вы можете поступить
    -Описание каждого университета который входит в состав Лиги плюща""", reply_markup=start_menu)

def goback(message):
    start_menu = types.ReplyKeyboardMarkup(True, True)
    start_menu.row("О Лиге Плюща", 'Описание Университетов')
    start_menu.row('Стиль Лиги Плюща', "Как поступить?")
    bot.send_message(message.chat.id, "Menu", reply_markup=start_menu)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    chat_id = message.chat.id
    pic = 'https://s2.best-wallpaper.net/wallpaper/1920x1200/1806/Grape-fields-clouds-countryside_1920x1200.jpg'
    pic2 = 'https://vtorrevieje.com/wp-content/uploads/2018/12/vinnie-pogreba-ispanii.jpg'


    if message.text == 'О Лиге Плюща':
        second_menu = types.ReplyKeyboardMarkup(True)
        second_menu.row('Назад')
        bot.send_message(message.chat.id, """Их объединяет плющ как таковой. Он плотно покрывал стены университетов. Руководство вузов активно поддерживало это состояние. 
        Каждый год на празднике «День плюща» студенты торжественно высаживали ползучий кустарник.""", reply_markup=second_menu)

    elif message.text == 'Как поступить?':
        third_menu = types.ReplyKeyboardMarkup(True)
        third_menu.row('Назад')
        bot.send_message(message.chat.id, """Как поступить в университет Ivy League?
    У каждого вуза Лиги плюща своя процедура поступления, но пакет документов в целом одинаковый. Он включает в себя:
    Заявку абитуриента
    Аттестат об имеющемся образовании
    Рекомендательные письма от преподавателей
    Языковой сертификат TOEFL iBT (минимум 100 баллов из 120)
    Сертификат SAT (минимум 1400 баллов из 2400)
    Мотивационное письмо
    Свидетельства спортивных, научных и творческих достижений
    После рассмотрения заявки абитуриента могут пригласить на собеседование или предложить ему написать эссе.
    """, reply_markup=third_menu)

    elif message.text == 'Стиль Лиги Плюща':
        second_menu = types.ReplyKeyboardMarkup(True)
        second_menu.row('Назад')
        bot.send_message(message.chat.id, """Стиль Лиги плюща:
    Не последнее место в ассоциации занимала мода. С 1950-х годов стиль одежды Ivy League, получивший название преппи, 
    создавали J. Press и Brooks Brothers, чьи магазины были расположены в кампусах Гарварда, Принстона и Йеля. 
    Мода пришла из повседневной спортивной одежды британского и американского высшего класса 1920-х годов. Блейзеры на двух пуговицах, 
    рубашки из хлопка оксфорд с воротником button-down, бретонские полоски, поло и броги. Осенью студенты носили твидовые пиджаки, носки с узором аргайл, свитеры и джемперы.
    Сегодня стиль Лиги Плюща все еще отражает престиж: актуальными остаются топсайдеры, лоферы, брюки, джинсы, бейсбольные куртки, харрингтоны, рубашки, шорты чинос.""",
                             reply_markup=second_menu)

    elif message.text == 'Описание Университетов':
        second_menu = types.ReplyKeyboardMarkup(True, True, True)
        second_menu.row("Гарвард", "Йельский", "Пенсильвания ")
        second_menu.row("Принстон", "Колумбиский", "Браун")
        second_menu.row("Дармутский", "Корнельский ", "Назад")
        bot.send_message(message.chat.id, """Выберите университет:""",
                             reply_markup=second_menu)


    elif message.text == 'Обзор':
        bot.send_media_group(message.chat.id, [types.InputMediaPhoto(pic)])
        bot.send_media_group(message.chat.id, [types.InputMediaPhoto(pic2)])

    elif message.text == 'Назад':
        goback(message)

    elif message.text == 'Halyk Bank':
        bot.send_message(message.from_user.id, "*************")

    elif message.text == 'Kaspi bank':
        bot.send_message(message.from_user.id, "*************")

    elif message.text == 'Коллаборации':
        ft = types.ReplyKeyboardMarkup(True, True)
        ft.row('Gucci', 'Reto')
        ft.row('Ders', 'GYWQ')
        ft.row('Назад')
        bot.send_message(message.chat.id, "Коллаборации", reply_markup=ft)

    else:
        pass

bot.polling(none_stop=True)