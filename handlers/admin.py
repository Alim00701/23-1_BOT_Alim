from aiogram import Dispatcher, types
from config import bot, dp, ADMINS
import random


async def ban(message: types.Message):
    if message.chat.type == 'group':
        if message.from_user.id not in ADMINS:
            await message.answer('Ты не мой БОСС!!!')
        elif not message.reply_to_message:
            await message.answer('Команда должна быть ответом на сообщение')
        else:
            await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            await message.answer(f'{message.from_user.first_name} Админ кикнул'
                                 f'{message.reply_to_message.from_user.full_name}')
    else:
        await message.answer('Пиши в группе!')


async def game(message: types.Message):
    emogi = random.choice(['🏀', '⚽️', '🎯', '🎲', '🎰', '🎳'])
    if message.text.startswith('game') and message.from_user.id in ADMINS:
        await bot.send_message(message.chat.id, text=emogi)


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(game)
