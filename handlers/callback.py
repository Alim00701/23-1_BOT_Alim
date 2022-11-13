from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp


# @dp.callback_query_handler(text='button_call_1')
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


async def quiz_3(call: types.CallbackQuery):
    markup_3 = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton('Next question', callback_data='button_call_3')
    markup_3.add(button_call_3)
    question = 'Первый космонавтом был?'
    answer = [
        'Юрий Гагарин',
        'Герман Титов',
        'Николаев Андриян',
        'Павел Романович'
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='Учи историю двоечник',
        reply_markup=markup_3
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text='button_call_1')
    dp.register_callback_query_handler(quiz_3, text='button_call_2')
