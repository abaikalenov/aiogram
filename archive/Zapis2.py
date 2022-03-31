import telebot
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from telebot import types

cred = credentials.Certificate('abay.json')
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://telega-abay-default-rtdb.firebaseio.com"
})
ref = db.reference()

bot = telebot.TeleBot('1983541443:AAFrx6v0rfrihllanOgIETr4E6dli26mM6s')

@bot.message_handler(commands=['start'])
def handle_start(message):
    time = ref.child('zapis').get()
    for key, value in time.items():
        if key == "10:00":
            bot.send_message(message.from_user.id, "10:00 " + value['name'])
        elif key == "11:00":
            bot.send_message(message.from_user.id, "11:00 " + value['name'])
        elif key == "12:00":
            bot.send_message(message.from_user.id, "12:00 " + value['name'])
        elif key == "13:00":
            bot.send_message(message.from_user.id, "13:00 " + value['name'])
        elif key == "14:00":
            bot.send_message(message.from_user.id, "14:00 " + value['name'])
        elif key == "15:00":
            bot.send_message(message.from_user.id, "15:00 " + value['name'])
        elif key == "16:00":
            bot.send_message(message.from_user.id, "16:00 " + value['name'])
        elif key == "17:00":
            bot.send_message(message.from_user.id, "17:00 " + value['name'])
        elif key == "18:00":
            bot.send_message(message.from_user.id, "19:00 " + value['name'])
        else:
            bot.send_message(message.from_user.id, "No one signed up for this time. \n"
                                                   "YOU CAN TAKE A REST")

bot.polling()
