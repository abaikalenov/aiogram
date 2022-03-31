import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import telebot
from telebot import types

cred = credentials.Certificate('abay.json')
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://telega-abay-default-rtdb.firebaseio.com"})
ref = db.reference()

bot = telebot.TeleBot("1983541443:AAFrx6v0rfrihllanOgIETr4E6dli26mM6s")


@bot.message_handler(commands=['start'])
def start(message):
    users_database = {
        "1274981264": {
            "username": "user_1",
            "last_activity": 161921259
        },
        "4254785765": {
            "username": "user_2",
            "last_activity": 1603212638
        }
    }
    db.reference("/users_database/").update(users_database)


bot.polling(none_stop=True)
