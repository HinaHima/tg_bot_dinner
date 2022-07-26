from aiogram import  Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN

#creating the RAM
storage = MemoryStorage()
#creating the bot object
bot = Bot(token=TOKEN)
#initializing the bot dispatcher
dp = Dispatcher(bot, storage=storage)