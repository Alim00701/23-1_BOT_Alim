from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

start_button = KeyboardButton('/start⚡️')
quiz_button = KeyboardButton('/quiz❔')
mem_button = KeyboardButton('/mem🤣')
reg_button = KeyboardButton('/reg📝')

share_location = KeyboardButton('Share location📍', request_location=True)
share_contact = KeyboardButton('Share contact☎️', request_contact=True)

start_markup.add(start_button,reg_button, quiz_button, mem_button, share_location, share_contact)

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton('Cancel')
)

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=3
).add(
    KeyboardButton('ДА'),
    KeyboardButton('НЕТ'),
    KeyboardButton('Cancel')
)

gender_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=3
).add(
    KeyboardButton('M'),
    KeyboardButton('W'),
    KeyboardButton('Не традиционный '),
    KeyboardButton('Cancel')
)
