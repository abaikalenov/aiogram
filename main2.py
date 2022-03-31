import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

my_id = 850888379
TOKEN = "5192395375:AAEbaEvMY4yI7Nuo8KcW3qpZJOCd1XdviDY"

loop = asyncio.get_event_loop()
bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop = loop)

@dp.message_handler()
async def echo(message: Message):
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

async def sent_to_admin(dp):
    await bot.send_message(chat_id=my_id, text="Hi abay")

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=sent_to_admin)

