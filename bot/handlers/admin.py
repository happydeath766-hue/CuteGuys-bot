from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.config.config import settings

router = Router()


@router.message(Command("admin"))
async def admin(message: Message):

    if message.from_user.id != settings.OWNER_ID:
        return

    await message.answer(
        """
👑 PANEL ADMIN

1. Grupos pendientes

2. Grupos aprobados

3. Enviar anuncio

4. Enviar lista

5. Configuración
"""
    )
