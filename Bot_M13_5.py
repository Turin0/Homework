from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True)
buttonInf = KeyboardButton(text='Информация')
buttonCal = KeyboardButton(text='Рассчитать')
kb.row(buttonCal, buttonInf)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст:')
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
    ccal = (int(data["weight"]) * 10) + (int(data["growth"]) * 6.25) - (int(data["age"]) * 5) + 5
    await message.answer(f'Ваша расчетное потребление калорий:{ccal}')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
