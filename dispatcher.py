from main import bot, dp

from aiogram.types import Message
from config import my_id

async def sent_to_admin(dp):
    await bot.send_message(chat_id=my_id, text="hello!")

@dp.message_handler()
async def echo(message: Message):
    n = f"Privet ti napisal: {message.text}"
    if message.text == "hello":
        await bot.send_message(chat_id=message.from_user.id, text="Hello. This is abays aiogram bot")
    elif message.text == "weather":
        await bot.send_message(chat_id= message.from_user.id, text="Today is a little cold")
    elif message.text == "ocenka":
        await bot.send_message(chat_id= message.from_user.id, text="Vashi ocenky:4, 5, 5")
    elif message.text == "poseshayemost":
        await bot.send_message(chat_id= message.from_user.id, text="Vy ne bili v 1 uroke")
    else:
        await bot.send_message(chat_id=message.from_user.id, text= "Netu otveta")
