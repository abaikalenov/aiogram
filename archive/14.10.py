import telebot
from telebot import types

TOKEN = "1983541443:AAFrx6v0rfrihllanOgIETr4E6dli26mM6s"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    h1 = types.InlineKeyboardButton(text="1", callback_data="1st")
    h2 = types.InlineKeyboardButton(text="2", callback_data="2nd")
    h3 = types.InlineKeyboardButton(text="3", callback_data="3rd")
    keyboard.add(h1, h2, h3)
    bot.send_message(message.chat.id, 'Please choose', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def call_in(call):
    if call.data == "1st":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        f1 = types.InlineKeyboardButton(text="1A", url="https://instagram.com/jihc.kz?utm_medium=copy_link")
        f2 = types.InlineKeyboardButton(text="1D", url="https://instagram.com/jihc.kz?utm_medium=copy_link")
        f3 = types.InlineKeyboardButton(text="1f1", url="https://instagram.com/jihc.kz?utm_medium=copy_link")
        f4 = types.InlineKeyboardButton(text="1f2", url="https://instagram.com/jihc.kz?utm_medium=copy_link")
        h5 = types.InlineKeyboardButton(text="Back", callback_data="5th")
        keyboard.add(f1, f2, f3, f4, h5)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Choose your class", reply_markup=keyboard)

    if call.data == "2nd":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        f1 = types.InlineKeyboardButton(text="2D", url="https://instagram.com/jihc.kz?utm_medium=copy_link")
        f2 = types.InlineKeyboardButton(text="2E", url="https://instagram.com/jihc.kz?utm_medium=copy_link")
        f3 = types.InlineKeyboardButton(text="2G", url="https://instagram.com/jihc.kz?utm_medium=copy_link")
        f4 = types.InlineKeyboardButton(text="2b1", url="https://instagram.com/jihc.kz?utm_medium=copy_link")
        f5 = types.InlineKeyboardButton(text="2b2", url="https://instagram.com/jihc.kz?utm_medium=copy_link")
        h5 = types.InlineKeyboardButton(text="Back", callback_data="5th")
        keyboard.add(f1, f2, f3, f4, f5, h5)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Choose your class", reply_markup=keyboard)
    if call.data == "3rd":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        f1 = types.InlineKeyboardButton(text="3I", url="https://instagram.com/ionedarxalayaqtar?utm_medium=copy_link")
        f2 = types.InlineKeyboardButton(text="3F", url="https://instagram.com/jic_fabulous.family?utm_medium=copy_link")
        f3 = types.InlineKeyboardButton(text="3G", url="https://instagram.com/jic_btmns?utm_medium=copy_link")
        f4 = types.InlineKeyboardButton(text="3H", url="https://instagram.com/3h_dontrush?utm_medium=copy_link")
        f5 = types.InlineKeyboardButton(text="3C", url="https://instagram.com/_29person?utm_medium=copy_link")
        h5 = types.InlineKeyboardButton(text="Back", callback_data="5th")
        keyboard.add(f1, f2, f3, f4, f5, h5)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Choose your class", reply_markup=keyboard)
    if call.data == "5th":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        h1 = types.InlineKeyboardButton(text="1", callback_data="1st")
        h2 = types.InlineKeyboardButton(text="2", callback_data="2nd")
        h3 = types.InlineKeyboardButton(text="3", callback_data="3rd")
        keyboard.add(h1, h2, h3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Menu", reply_markup=keyboard)


bot.polling(none_stop=True)