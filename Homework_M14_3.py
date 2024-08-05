from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Информация'),
            KeyboardButton(text='Рассчитать')
        ],
        [KeyboardButton(text='Купить')]
    ], resize_keyboard=True
)
ib = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
            InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
        ]
    ]
)
iBuyB = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Витамин A', callback_data='product_buying'),
            InlineKeyboardButton(text='Витамин B6', callback_data='product_buying'),
            InlineKeyboardButton(text='Витамин C', callback_data='product_buying'),
            InlineKeyboardButton(text='Витамин D3', callback_data='product_buying')
        ]
    ]
)


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


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    with open('A.png', "rb") as img:
        await message.answer_photo(img, 'Витамин А || Витамин А является одним из важнейших витаминов в нашем организме || Цена 100 руб.')
    with open('B.png', "rb") as img:
        await message.answer_photo(img, 'Витамин B6 || Витамин В6 (пиридоксин) участвует во многих биохимических реакциях, необходимых для поддержания жизни || Цена 200 руб.')
    with open('C.png', "rb") as img:
        await message.answer_photo(img, 'Витамин C || Витамин C — это незаменимое питательное вещество, имеющее огромное значение для работы иммунной системы || Цена 300 руб.')
    with open('D3.png', "rb") as img:
        await message.answer_photo(img, 'Витамин D3 || Витамин D3 — необходим для правильной работы иммунной, нервной, гармональной и кровеносной систем человека, он участвует в метаболизме кальция и фосфора || Цена 400 руб.')
    await message.answer('Выберите продукт для покупки:', reply_markup=iBuyB)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


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
    ccal = (int(data["weight"]) * 10) + (int(data["growth"]) * 6.25) - (int(data["age"]) * 5) + 5
    await message.answer(f'Ваша расчетное потребление калорий:{ccal}')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
