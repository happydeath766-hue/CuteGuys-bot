from aiogram import Router
from aiogram.filters import ChatMemberUpdatedFilter
from aiogram.enums import ChatMemberStatus
from aiogram.types import ChatMemberUpdated
from bot.config.config import settings
from bot.keyboards.admin import pending_group_keyboard
from bot.services.group_service import GroupService

router = Router()


@router.my_chat_member(ChatMemberUpdatedFilter())
async def group_update(event: ChatMemberUpdated):

    print("🔥 Evento my_chat_member recibido")

    old = event.old_chat_member.status
    new = event.new_chat_member.status

    print(f"Estado anterior: {old}")
    print(f"Estado nuevo: {new}")

    if (
        old == ChatMemberStatus.LEFT
        and new in (
            ChatMemberStatus.MEMBER,
            ChatMemberStatus.ADMINISTRATOR,
        )
    ):

        chat = event.chat

        print(f"✅ Bot agregado a: {chat.title}")

        await GroupService.add_group(
            chat.id,
            chat.title,
            chat.username,
            None
        )

        await event.bot.send_message(
            chat_id=settings.OWNER_ID,
            text=f"""
📥 Nuevo grupo detectado

📛 Nombre:
{chat.title}

🆔
<code>{chat.id}</code>

Estado:
⏳ Pendiente
""",
            reply_markup=pending_group_keyboard(chat.id),
        )

    elif (
        old in (
            ChatMemberStatus.MEMBER,
            ChatMemberStatus.ADMINISTRATOR,
        )
        and new == ChatMemberStatus.LEFT
    ):

        print(f"❌ Bot eliminado de: {event.chat.title}"){chat.title}

🆔
<code>{chat.id}</code>

Estado:
⏳ Pendiente
""",
            reply_markup=pending_group_keyboard(chat.id)
        )

    elif (
        old in (
            ChatMemberStatus.MEMBER,
            ChatMemberStatus.ADMINISTRATOR,
        )
        and new == ChatMemberStatus.LEFT
    ):

        print("Bot eliminado del grupo")
