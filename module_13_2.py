#Хэндлеры обработки сообщений
#работаем в отдельном venv
#версия python 3.0.9
#версия  aiogram 2.25.1
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = "№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№ - Тут наш токен!"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_message(message):
    print('Start message !')
    await message.answer("Привет! Я бот помогающий твоему здоровью.!!!")

@dp.message_handler()
async def all_message(message):
    print("Мы получили сообщение!")
    await message.answer('Введите команду /start, чтобы начать общение.')



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
