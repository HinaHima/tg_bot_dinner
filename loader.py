from aiogram import  Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN

# Creating the RAM
storage = MemoryStorage()
# Creating the bot object
bot = Bot(token=TOKEN)
# Initializing the bot dispatcher
dp = Dispatcher(bot, storage=storage)