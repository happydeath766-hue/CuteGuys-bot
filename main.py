from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from dotenv import load_dotenv
from bot.handlers.admin_callbacks import router as admin_callbacks_router
from bot.handlers.list import router as list_router
import asyncio
import logging
import os
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)

dp = Dispatcher()


async def set_commands():
    commands = [
        BotCommand(command="start", description="Iniciar bot"),
        BotCommand(command="admin", description="Panel de administración"),
    ]
    await bot.set_my_commands(commands)


async def main():
    logging.basicConfig(level=logging.INFO)

    await set_commands()

    print("✅ Cute Guys Bot iniciado correctamente")

    await dp.start_polling(bot)

from bot.handlers.start import router as start_router
from bot.handlers.admin import router as admin_router
from bot.handlers.group_events import router as group_router

dp.include_router(start_router)
dp.include_router(admin_router)
dp.include_router(group_router)
dp.include_router(admin_callbacks_router)
dp.include_router(list_router)

if __name__ == "__main__":
    asyncio.run(main())
