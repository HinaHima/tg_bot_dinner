#importing aiogram and modules needed
from  aiogram import Bot, Dispatcher, executor, types
#importing the token
from config import TOKEN
#importing logging
import logging
#importing the database
import sqlite3
#importing the texts
import text
#importing the markups
import markup

#creating the bot object
bot = Bot(token=TOKEN)
#initializing the bot dispatcher
dp = Dispatcher(bot)
#turning on the logging
logging.basicConfig(level=logging.INFO)

db = sqlite3.connect("next.db")
cursor = db.cursor()

@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):
    await bot.send_message(message.from_user.id, text="Здесь должно быть краткое описание мероприятия или приветственное сообщение.", reply_markup=markup.mainMenu)

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
                           text=f"Дата - {date}, место - {location}, количество мест - {places}, стоймость - {cost}, фильм - {film}.", reply_markup=markup.checkRegister)

@dp.callback_query_handler(text="btnMenu")
async def menu(message: types.Message):
    await bot.send_message(message.from_user.id, text='Возвращаем Вас в меню.', reply_markup=markup.mainMenu)

@dp.callback_query_handler(text="btnRegister")
async def register(message: types.Message):
    cursor.execute("SELECT * FROM next")
    places = cursor.fetchone()[2]
    if places != '0 свободных':
        await bot.send_message(message.from_user.id, text=f"{places} мест. Если хотите записаться, пожалуйста, напишите (тут данные/ссылка на социалки)")
    else:
        await bot.send_message(message.from_user.id, text="К сожалению, свободных мест нет. (Тут можно вставить необходимый текст)", reply_markup=markup.mainMenu)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)