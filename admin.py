import states
from aiogram import  types
from loader import dp, bot
from db import db, cursor
from aiogram import types
import markup
from aiogram.dispatcher import FSMContext
from states import Spam

@dp.message_handler(commands=["admin"])
async def admin(message: types.Message):
    admins = []
    cursor.execute("""SELECT tgID FROM admin""")
    while True:
        results = cursor.fetchone()
        if results == None:
            break
        admins.append(results[0])

    if message.from_user.id in admins:
        await bot.send_message(message.from_user.id, text="Админ-панель", reply_markup=markup.adminKB)
    else:
        await bot.send_message(message.from_user.id, text="Вы не имеете доступ к панели администратора.")



@dp.callback_query_handler(text="btnSpam")
async def spam(message: types.Message):
    await bot.send_message("Введите текст рассылки")
    await states.Spam.set()

@dp.message_handler(state=states.Spam)
async def do_spam(message: types.Message, state: FSMContext):
    cursor.execute("SELECT tgID from users")
    spam_list = []
    while True:
        each_user = cursor.fetchone()

        if each_user == None:
            break

        spam_list.append(each_user[0])

    for user in spam_list:
        await bot.send_message(user, text=f"{message.text}")
        await state.finish()