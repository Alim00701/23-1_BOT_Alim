from aiogram import Dispatcher, types
from config import bot, dp


# @dp.message_handler()
async def echo(message: types.Message):
    try:
        z = message.text
        x = int(z)
        c = x ** 2
        await bot.send_message(message.from_user.id, str(c))
    except:
        await bot.send_message(message.from_user.id, message.text)

    bad_words = ['java', 'css', 'html', 'нигер', 'глупой']
    username = f'@{message.from_user.username}' if message.from_user.username is not None \
        else message.from_user.full_name

    for word in bad_words:
        if word in message.text.lower():
            await bot.send_message(
                message.chat.id,
                f'Не говори так @{username} '
                f'Сам ты {word}!'
            )
            await bot.delete_message(message.chat.id, message.message_id)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
