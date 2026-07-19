from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.services.list_service import ListService

router = Router()


@router.message(Command("lista"))
async def group_list(message: Message):

    text = await ListService.generate()

    await message.answer(
        text,
        disable_web_page_preview=True
    )
