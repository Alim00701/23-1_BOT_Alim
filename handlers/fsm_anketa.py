from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMINS
from keyboards.client_kb import submit_markup, cancel_markup, gender_markup
from database.bot_db import sql_command_insert


class FSMAdmin(StatesGroup):
    name = State()
    age = State()
    ID = State()
    group1 = State()
    direction = State()
    gender = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id not in ADMINS:
            await message.answer('Эта функция доступна только админам группы!')
        else:
            await FSMAdmin.name.set()
            await message.answer('Имя ментора', reply_markup=cancel_markup)
    else:
        await message.answer('Пиши в личку!')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['username'] = f'@{message.from_user.username}'
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Возраст ментора')


async def load_age(message: types.Message, state: FSMContext):
    try:
        if 10 < int(message.text) < 50:
            async with state.proxy() as data:
                data['age'] = int(message.text)
            await FSMAdmin.next()
            await message.answer('ID ментора')
        else:
            await message.answer('Доступ запрещен!', reply_markup=cancel_markup)
    except:
        await message.answer('Пишите корректно')


async def load_Id_mentor(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ID'] = message.text
    await FSMAdmin.next()
    await message.answer('Группа?')


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group1'] = message.text
    await FSMAdmin.next()
    await message.answer("Какое у вас направление?",)


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer('Пол ментора', reply_markup=gender_markup)


async def load_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
        await bot.send_message(message.chat.id,
                               f"{data['name']}, {data['age']}, {data['ID']}, {data['group1']}, {data['direction']}"
                               f"{data['gender']}")
    await FSMAdmin.next()
    await message.answer('Все правильно? да или нет?', reply_markup=submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await sql_command_insert(state)
        await state.finish()
        await message.answer('Регистрация завершена!')
    elif message.text.lower() == 'нет':
        await state.finish()
        await message.answer('Отмена')
    else:
        await message.answer('Пишите корректно (да или нет)')


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отмена')


def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['reg📝'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_Id_mentor, state=FSMAdmin.ID)
    dp.register_message_handler(load_group, state=FSMAdmin.group1)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_gender, state=FSMAdmin.gender)
    dp.register_message_handler(submit, state=FSMAdmin.submit)
