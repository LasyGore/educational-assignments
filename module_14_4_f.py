import logging
import sqlite3
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)

api_token = "_______________"
bot = Bot(token=api_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()

async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()

async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])
    # Calculate BMR using Mifflin-St Jeor equation
    bmr = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f"Ваша норма калорий составляет {bmr} калорий в день.")
    await state.finish()

def get_all_products():
    conn = sqlite3.connect('products.db')  # Подключение к базе данных
    c = conn.cursor()
    c.execute("SELECT * FROM Products")
    products=c.fetchall()
#   print(products)
    conn.close()
    return products
def generate_inline_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button_calculate = types.InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
    button_formulas = types.InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
    button_buy = types.InlineKeyboardButton('Купить', callback_data='buy')
    return keyboard

async def main_menu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_calculate = types.KeyboardButton('Рассчитать')
    button_info = types.KeyboardButton('Информация')
    button_buy = types.KeyboardButton('Купить')
    keyboard.add(button_calculate, button_info)
    keyboard.add(button_buy)
    await message.answer("Выберите действие:", reply_markup=keyboard)

async def get_formulas(call):
    if call.data == 'formulas':
        formula_text = 'Формула Mifflin-St Jeor для мужчин: 10 * вес + 6.25 * рост - 5 * возраст + 5'
        await call.message.answer(formula_text)

#
def generate_inline_keyboard1():
    keyboard = types.InlineKeyboardMarkup()
    button_prod1 = types.InlineKeyboardButton('Product1', callback_data='product1_buying')
    button_prod2 = types.InlineKeyboardButton('Product2', callback_data='product2_buying')
    button_prod3 = types.InlineKeyboardButton('Product3', callback_data='product3_buying')
    button_prod4 = types.InlineKeyboardButton('Product4', callback_data='product4_buying')
    keyboard.add(button_prod1, button_prod2, button_prod3, button_prod4)
    return keyboard

#async def get_buying_list(message):
#    for number in range(1, 5):
#        product_info = f'Название: Продукт{number} | Описание: описание {number} | Цена: {number * 100}'
#        await message.answer_photo(photo=open(f'{number}.jpg','rb'), caption=product_info)
#    keyboard = generate_inline_keyboard1()
#    await message.answer("Выберите продукт для покупки:", reply_markup=keyboard)
async def get_buying_list(message):
    products = get_all_products()
    for product in products:
        product_info = f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}"
        photo_path = f"{product[0]}.jpg"  # Где product[0] - это номер записи
        await message.answer_photo(photo=open(photo_path, 'rb'), caption=product_info)
#        await message.answer(product_info)
        keyboard = generate_inline_keyboard1()
    await message.answer("Выберите продукт для покупки:", reply_markup=keyboard)

async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await main_menu(message)

@dp.message_handler(text="Рассчитать")
async def process_calculate(message: types.Message):
    keyboard = generate_inline_keyboard()
    await message.answer("Выберите опцию:", reply_markup=keyboard)

@dp.callback_query_handler(text='calories')
async def process_calculate_inline(call: types.CallbackQuery):
    await set_age(call)

@dp.message_handler(state=UserState.age)
async def process_growth(message: types.Message, state: UserState):
    await set_growth(message, state)

@dp.message_handler(state=UserState.growth)
async def process_weight(message: types.Message, state: UserState):
    await set_weight(message, state)

@dp.message_handler(state=UserState.weight)
async def process_send_calories(message: types.Message, state: UserState):
    await send_calories(message, state)

#
@dp.message_handler(text="Купить")
async def process_buy(message: types.Message):
    await get_buying_list(message)

@dp.callback_query_handler(text=['product1_buying', 'product2_buying', 'product3_buying', 'product4_buying'])
async def process_product_buying(call: types.CallbackQuery):
    await send_confirm_message(call)
#
@dp.callback_query_handler()
async def callback_handler(call: types.CallbackQuery):
    await get_formulas(call)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)