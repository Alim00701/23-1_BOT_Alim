from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
from keyboards.client_kb import start_markup
from database.bot_db import sql_command_random


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start⚡️'])
    dp.register_message_handler(quiz_1, commands=['quiz❔'])
    dp.register_message_handler(mem, commands=['mem🤣'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='/!')
    dp.register_message_handler(get_random_user, command=['get'])


# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'Салам {message.from_user.first_name}',
                           reply_markup=start_markup)


# @dp.message_handler(commands=['quiz'])
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


# @dp.message_handler(commands=['mem'])
async def mem(call: types.CallbackQuery):
    photo = open("media/MEMimages.jpg", 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)


async def pin(message: types.Message):
    if message.from_user.id != message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.message_id, message.reply_to_message.from_user.id)
    elif not message.reply_to_message:
        await message.answer('Команда должна быть ответом на сообщение!')


async def get_random_user(message: types.Message):
    await sql_command_random(message)
