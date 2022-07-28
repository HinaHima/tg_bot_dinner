# importing all we need to use the state machine
import states
from aiogram import types
# Importing the variables to control the bot
from loader import dp, bot
# Importing the database
import sqlite3
# Importing the inline keyboards needed
import markup
# Importing the RAM
from aiogram.dispatcher import FSMContext
# Importing the states needed
from states import Spam, NewDescription, Places

# The admin panel
@dp.message_handler(commands=["admin"])
async def admin(message: types.Message):
    db = sqlite3.connect("next.db")
    cursor = db.cursor()
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
    cursor.close()

# The spam button
@dp.callback_query_handler(text="btnSpam")
async def spam(message: types.Message):
    await bot.send_message(message.from_user.id, text="Введите текст рассылки")

    await Spam.spamText.set()

@dp.message_handler(state=states.Spam)
async def do_spam(message: types.Message, state: FSMContext):
    db = sqlite3.connect("next.db")
    cursor = db.cursor()
    cursor.execute("SELECT tgID from users")
    spam_list = []
    while True:
        each_user = cursor.fetchone()

        if each_user == None:
            break

        spam_list.append(each_user[0])

    for user in spam_list:
        await bot.send_message(user, text=f"{message.text}")

    await bot.send_message(message.from_user.id, text="Рассылка завершена")
    await state.reset_state()

    cursor.close()

# The button that changes the amount of places (one of the value in the db).
@dp.callback_query_handler(text="btnPlaces")
async def spam(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text="Вводите новое значение в формате 'x свободных'")

    await Places.places.set()

@dp.message_handler(state=states.Places)
async def places(message: types.Message, state: FSMContext):
    db = sqlite3.connect("next.db")
    cursor = db.cursor()
    places = message.text
    await state.update_data(
        {"places":places}
    )
    data = await state.get_data()
    places = data.get("places")
    cursor.execute("UPDATE next SET places = ?", [places])
    await state.reset_state()
    db.commit()

    await bot.send_message(message.from_user.id, text="Изменения внесены")
    cursor.close()

# The button that changes a whole line in a database.
@dp.callback_query_handler(text="btnDescription")
async def description(message: types.Message):
    await bot.send_message(message.from_user.id, text="Введите дату")

    await NewDescription.date.set()

@dp.message_handler(state=NewDescription.date)
async def variable_1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {"date":answer}
    )

    await bot.send_message(message.from_user.id,
                           text="Введите локацию, можно с адресом")
    await NewDescription.location.set()

@dp.message_handler(state=NewDescription.location)
async def variable_2(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {"location":answer}
    )

    await bot.send_message(message.from_user.id,
                           text="Введите количество свободных на данный момент мест")
    await NewDescription.places.set()

@dp.message_handler(state=NewDescription.places)
async def variable_3(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {"places":answer}
    )

    await bot.send_message(message.from_user.id,
                           text="Введите цены")
    await NewDescription.cost.set()

@dp.message_handler(state=NewDescription.cost)
async def variable_4(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {"cost":answer}
    )

    await bot.send_message(message.from_user.id,
                           text="Введите при необходимости название фильма. "
                                "Иначе - введите любой текст (например - 'секрет'). Ни в коем случае не оставлять поле пустым!")
    await NewDescription.film.set()

@dp.message_handler(state=NewDescription.film)
async def variable_5(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(
        {"film":answer}
    )

    await NewDescription.check.set()
    await bot.send_message(message.from_user.id, text="Введите любой символ")

@dp.message_handler(state=NewDescription.check)
async def variable_6(message: types.Message, state: FSMContext):
    db = sqlite3.connect("next.db")
    cursor = db.cursor()
    data = await state.get_data()
    date = data.get("date")
    location = data.get("location")
    places = data.get("places")
    cost = data.get("cost")
    film = data.get("film")

    cursor.execute("UPDATE next SET date = ?", [date])
    cursor.execute("UPDATE next SET location = ?", [location])
    cursor.execute("UPDATE next SET places = ?", [places])
    cursor.execute("UPDATE next SET cost = ?", [cost])
    cursor.execute("UPDATE next SET film = ?", [film])
    await state.reset_state()
    await bot.send_message(message.from_user.id, text="Изменения внесены")

    db.commit()
    cursor.close()
