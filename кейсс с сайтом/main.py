from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6736335028:AAHnJxKqMkZai-kdEuI2l1725wdH9DUPei8')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='')))

executor.start_polling(dp)