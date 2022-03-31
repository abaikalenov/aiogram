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
    hideBoard = types.ReplyKeyboardRemove()
    re = bot.send_message(message.chat.id, 'изменить состояние заказа. введите юзернейм', reply_markup=hideBoard)
    bot.register_next_step_handler(re, idofuser)

def idofuser(message):
    global a
    a = message.text
    print(a)
    time = ref.child('zakaz').get()
    for key, value in time.items():
        if a in time:
            bot.send_message(message.from_user.id, "Статус заказа " + a + ": " + value['статус'])
            key = types.InlineKeyboardMarkup()
            bt = types.InlineKeyboardButton(text='изменить на готово', callback_data='готово')
            key.add(bt)
            sent4 = bot.send_message(message.chat.id, 'нажмите на кнопку что бы изменить', reply_markup=key)
            bot.register_next_step_handler(sent4, inline)
        else:
            bot.send_message(message.chat.id, "ошибка")

@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    ref.child('zakaz').child(a).update({'статус': c.data})
    bot.send_message(c.message.chat.id, 'изменено на готово')

bot.polling(none_stop=True)
