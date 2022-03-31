import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import telebot
from telebot import types

cred = credentials.Certificate('abay.json')
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://telega-abay-default-rtdb.firebaseio.com"})
ref = db.reference()

bot = telebot.TeleBot("1983541443:AAFrx6v0rfrihllanOgIETr4E6dli26mM6s")


@bot.message_handler(commands=['start'])
def start(message):
    start_menu = types.ReplyKeyboardMarkup(True)
    start_menu.row("заказать")
    start_menu.row('отслеживать')
    sent = bot.send_message(message.chat.id, """Здравствуйте, Это бот Абая. 
    Функции бота:
    - Заказать услуги принта колледжа
    - Отслеживать заказ""", reply_markup=start_menu)
    bot.register_next_step_handler(sent, message_bot)

@bot.message_handler(content_types=['text'])
def message_bot(message):
    if message.text == "заказать":
        bot_sent = bot.send_message(message.chat.id, 'срок')
        bot.register_next_step_handler(bot_sent, bot_sent2)
    if message.text == "отслеживать":
        idofuser = message.from_user.username
        print(idofuser)
        time = ref.child('zakaz').get()
        for key, value in time.items():
            if idofuser in time:
                bot.send_message(message.from_user.id, "Статус заказа "+idofuser +": "+value['статус'])
            else:
                print("oshibka")
def bot_sent2(message):
    bot_sent3 = bot.send_message(message.chat.id, 'ФИО')
    global b
    b = message.text
    bot.register_next_step_handler(bot_sent3, bot_sent4)
def bot_sent4(message):
    global d
    d = message.text
    key = types.InlineKeyboardMarkup()
    bt = types.InlineKeyboardButton(text='hoodie', callback_data='hoodie')
    bt1 = types.InlineKeyboardButton(text='shirt', callback_data='shirt')
    bt2 = types.InlineKeyboardButton(text='shopper', callback_data='shopper')
    key.add(bt, bt1, bt2)
    sent1 = bot.send_message(message.chat.id, 'Выберите что хотите заказать', reply_markup=key)
    bot.register_next_step_handler(sent1, inline)


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
        a = c.from_user.username
        ref.child('zakaz').child(a).update({'товар': c.data})
        ref.child('zakaz').child(a).update({'срок': b})
        ref.child('zakaz').child(a).update({'фио': d})
        ref.child('zakaz').child(a).update({'статус': "начался"})
        bot.send_message(c.message.chat.id, 'Заказ успешно принят')
bot.polling(none_stop=True)
