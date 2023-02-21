import time
import logging

from aiogram import Bot, Dispatcher,executor,types

TOKEN = "6105985545:AAE8i7G-Gr_bH4R5knKIUcS6LSAyaUqpb5Q"
MSG = 'Привет, {}'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message:types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    
    for i in range(999):
        time.sleep(1)

        await bot.send_message(user_id, MSG.format(user_name))




if __name__ == '__main__':
    executor.start_polling(dp)