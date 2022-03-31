import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import telebot

cred = credentials.Certificate('abay.json')
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://telega-abay-default-rtdb.firebaseio.com"})
ref = db.reference()

bot = telebot.TeleBot("1983541443:AAFrx6v0rfrihllanOgIETr4E6dli26mM6s")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Whats your name?')

@bot.message_handler(content_types=['text'])
def soz(message):
    if message =="Abay":
        bot.send_message(message.chat.id, "You are from best place")
    else:
        user = message.text
        print(user)
        contains = ref.child('Registration').child('name').get()
        cStr = "" + str(contains)
        if cStr == "None":
            user_ref = ref.child('Registration').child('name')
            user_ref.set(user)
            bot.reply_to(message, "Tnx")


bot.polling(none_stop=True)
