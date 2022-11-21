import random
import sqlite3
from config import bot
from sqlite3 import Connection


def sql_create():
    global db, cursor
    db = sqlite3.connect('mentors.sqlite3')
    cursor = db.cursor()

    if db:
        print('База данных подключена:)')

    db.execute('CREATE TABLE IF NOT EXISTS anketa'
               '(id INTEGER PRIMARY KEY, username TEXT,'
               'name TEXT, age INTEGER, direction TEXT, group1 INTEGER, gender TEXT)')

    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO anketa VALUES'
                       '(?, ?, ?, ?, ?)', tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    result = cursor.execute('SELECT * FROM anketa').fetchall()
    random_user = random.choice(result)
    await bot.send_message(message.chat.id,
                           f"{random_user[2]}, {random_user[1]}, {random_user['0']}, "
                           f"{random_user[3]}, {random_user[4]}"
                           f"{random_user[5]}")


async def sql_command_all():
    return cursor.execute('SELECT * FROM anketa').fetchall()


async def sql_command_delete(user_id):
    cursor.execute('DELETE FROM anketa WHERE id = ?', (user_id, ))
    db.commit()


async def sql_command_get_all_ids():
    return cursor.execute('SELECT id FROM anketa').fetchall()
