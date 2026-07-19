from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start(message: Message):

    await message.answer(
        """
Bienvenido a <b>Cute Guys Bot</b>

Usa el menú para navegar.
"""
    )
