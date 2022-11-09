from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from decouple import config
import logging

TOKEN = config('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f'Салам {message.from_user.first_name}')


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('Next question', callback_data='button_call_1')
    markup.add(button_call_1)

    question = 'Сколько звезд на гос флаге США?'
    answer = [
        '70',
        '45',
        '100',
        '50'
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='Учи историю двоечник',
        reply_markup=markup
    )


@dp.callback_query_handler(text='button_call_1')
async def quiz_2(call: types.CallbackQuery):
    markup_2 = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('Next question', callback_data='button_call_2')
    markup_2.add(button_call_2)
    question = 'Первым президентом США был?'
    answer = [
        'Владимир Путин',
        'Джордж Вашингтон',
        'Джеки Чан',
        'Джон Адамс'
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='Учи историю двоечник',
        reply_markup=markup_2
    )


@dp.message_handler(commands=['mem'])
async def mem(call: types.CallbackQuery):
    photo = open("media/MEMimages.jpg", 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)


@dp.message_handler()
async def echo(message: types.Message):
    try:
        z = message.text
        x = int(z)
        c = x ** 2
        await bot.send_message(message.from_user.id, str(c))
    except:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
