from aiogram import executor
import logging
import casual_handlers
import admin
from loader import dp, bot, storage

async def on_shutdown(dp):
    await bot.close()
    await storage.close()


#turning on the logging
logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    from loader import dp
    executor.start_polling(dp, skip_updates = True, on_shutdown=on_shutdown)