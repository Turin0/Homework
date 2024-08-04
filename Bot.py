from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

api = '7158361279:AAEWZQeDyYadhauevXQlForHeaOwOG9zNUM'
bot = Bot(token=api)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True)
buttonInf = KeyboardButton(text='Информация')
buttonCal = KeyboardButton(text='Рассчитать')
kb.row(buttonCal, buttonInf)
ib = InlineKeyboardMarkup()
iButtonCal = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
iButtonInf = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
ib.row(iButtonCal, iButtonInf)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=ib)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    ccal = (int(data["age"]) * 5) + (int(data["weight"]) * 10) + (int(data["growth"]) * 6.25) + 5
    await message.answer(f'Ваша расчетное потребление калорий:{ccal}')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    