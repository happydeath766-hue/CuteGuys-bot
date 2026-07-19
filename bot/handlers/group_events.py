from aiogram import Router
from aiogram.filters import ChatMemberUpdatedFilter
from aiogram.types import ChatMemberUpdated
from aiogram.enums import ChatMemberStatus

router = Router()


@router.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=(
            ChatMemberStatus.LEFT >> ChatMemberStatus.MEMBER
        )
    )
)
async def bot_added(event: ChatMemberUpdated):
    chat = event.chat

    print(f"Nuevo grupo: {chat.title}")

    # Aquí después guardaremos el grupo en PostgreSQL
