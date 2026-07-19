from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from dotenv import load_dotenv
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


if __name__ == "__main__":
    asyncio.run(main())
