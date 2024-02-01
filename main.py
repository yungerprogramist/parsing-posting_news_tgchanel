from aiogram import Bot, Dispatcher
from dotenv import load_dotenv 
import os  
import asyncio
import schedule
import pytz

from bot.routers import main_router, session_router

from script.main_script import app
from DataBase.google_sheet import clear_google_data_DB



def run_miling():
    asyncio.create_task(clear_google_data_DB())
    
async def job_schedule():
    schedule.every().monday.at("00:00").do(run_miling)
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

async def on_startup(): 
    asyncio.create_task(job_schedule())




load_dotenv()

async def main():
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher()
    dp.include_routers(
            main_router.router,
            session_router.router
        )

    await app.start()

    dp.startup.register(on_startup)
         
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    app.run(main())



