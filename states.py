from aiogram.dispatcher.filters.state import StatesGroup, State

class Spam(StatesGroup):
    spamText = State()

class NewDescription(StatesGroup):
    date = State()
    location = State()
    places = State()
    cost = State()
    film = State()
    update = State()

class Places(StatesGroup):
    places = State()