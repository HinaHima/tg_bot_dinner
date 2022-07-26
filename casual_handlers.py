from loader import dp, bot
from db import db, cursor
import markup
import text
from aiogram import types

@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):
    cursor.execute(f"SELECT * FROM users WHERE tgID = {message.from_user.id}")
    user = cursor.fetchone()
    if user:
        await bot.send_message(message.from_user.id, text="Здесь должно быть краткое описание мероприятия или приветственное сообщение.",
                               reply_markup=markup.mainMenu)
    else:
        new_user =  message.from_user.id
        cursor.execute(f"INSERT INTO users VALUES (?)", new_user)
        await bot.send_message(message.from_user.id,
                               text="Здесь должно быть краткое описание мероприятия или приветственное сообщение.",
                               reply_markup=markup.mainMenu)

@dp.callback_query_handler(text="btnInfo")
async def info(message: types.Message):
    await bot.send_message(message.from_user.id, text=f"{text.textInfo}")

@dp.callback_query_handler(text="btnNext")
async def info(message: types.Message):
    cursor.execute("SELECT * FROM next")
    date = cursor.fetchone()[0]
    cursor.execute("SELECT * FROM next")
    location = cursor.fetchone()[1]
    cursor.execute("SELECT * FROM next")
    places = cursor.fetchone()[2]
    cursor.execute("SELECT * FROM next")
    cost = cursor.fetchone()[3]
    cursor.execute("SELECT * FROM next")
    film = cursor.fetchone()[4]
    cursor.execute("SELECT * FROM next")
    await bot.send_message(message.from_user.id,
                           text=f"Дата - {date}, место - {location}, количество мест - {places}, стоймость - {cost}, фильм - {film}.",
                           reply_markup=markup.checkRegister)

@dp.callback_query_handler(text="btnMenu")
async def menu(message: types.Message):
    await bot.send_message(message.from_user.id, text='Возвращаем Вас в меню.',
                           reply_markup=markup.mainMenu)

@dp.callback_query_handler(text="btnRegister")
async def register(message: types.Message):
    cursor.execute("SELECT * FROM next")
    places = cursor.fetchone()[2]
    if places != '0 свободных':
        await bot.send_message(message.from_user.id,
                               text=f"{places} мест. Если хотите записаться, пожалуйста, напишите (тут данные/ссылка на социалки)")
    else:
        await bot.send_message(message.from_user.id, text="К сожалению, свободных мест нет. (Тут можно вставить необходимый текст)",
                               reply_markup=markup.mainMenu)
