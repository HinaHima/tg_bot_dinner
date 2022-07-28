# This is the main file, we run the bot from there.

# Importing from the framework the bot executor.
from aiogram import executor
# Importing the logging module so we can track the errors
import logging
# The handlers help to 'catch' the users' messages and their inline keyboard choices
import casual_handlers
# Also handlers but for the admins
import admin
# Importing the variables to control the bot
from loader import dp, bot, storage

#turning on the logging
logging.basicConfig(level=logging.INFO)

#This says what to do when the bot has being turned off
#async def on_shutdown(dp):
    #await bot.close()
#on_shutdown=on_shutdown(dp)

if __name__ == "__main__":
    from loader import dp
    executor.start_polling(dp, skip_updates = True)