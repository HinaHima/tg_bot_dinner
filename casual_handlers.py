# Importing the variables to control the bot
from loader import dp, bot
# Importing the inline keyboards needed
import markup
# The description used in one of the inline keyboard variant, it's static
import text
from aiogram import types
# Importing the database
import sqlite3

# Different start depending on wether the user is new or not. If not, the new user's id is stored in the database
# For the spam feature.
@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):
    db = sqlite3.connect("next.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM users WHERE tgID = {message.from_user.id}")
    user = cursor.fetchone()
    if user:
        await bot.send_message(message.from_user.id, text="Здесь должно быть краткое описание мероприятия или приветственное сообщение.",
                               reply_markup=markup.mainMenu)
    else:
        new_user =  int(message.from_user.id)
        cursor.execute(f"INSERT INTO users (tgID) VALUES (?)", tuple(new_user))
        db.commit()
        await bot.send_message(message.from_user.id,
                               text="Здесь должно быть краткое описание мероприятия или приветственное сообщение.",
                               reply_markup=markup.mainMenu)

    cursor.close()

# The info about the whole event
@dp.callback_query_handler(text="btnInfo")
async def info(message: types.Message):
    await bot.send_message(message.from_user.id, text=f"{text.textInfo}")

# The info about the next event
@dp.callback_query_handler(text="btnNext")
async def info(message: types.Message):
    db = sqlite3.connect("next.db")
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM next WHERE rowid = 1""")
    data = cursor.fetchone()
    cursor.close()
    list = []

    for entry in data:
        list.append(entry)

    await bot.send_message(message.from_user.id,
    text=f"Дата - {list[0]}, место - {list[1]}, количество мест - {list[2]}, стоймость - {list[3]}, фильм - {list[4]}.",
    reply_markup=markup.checkRegister)

# Going back to the main menu
@dp.callback_query_handler(text="btnMenu")
async def menu(message: types.Message):
    await bot.send_message(message.from_user.id, text='Возвращаем Вас в меню.',
                           reply_markup=markup.mainMenu)

# The info about how to register to the next event
@dp.callback_query_handler(text="btnRegister")
async def register(message: types.Message):
    db = sqlite3.connect("next.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM next")
    places = cursor.fetchone()[2]
    cursor.close()
    if places != '0 свободных':
        await bot.send_message(message.from_user.id,
                               text=f"Если хотите записаться, пожалуйста, напишите (тут данные/ссылка на социалки)")
    else:
        await bot.send_message(message.from_user.id, text="К сожалению, свободных мест нет. (Тут можно вставить необходимый текст)",
                               reply_markup=markup.mainMenu)

