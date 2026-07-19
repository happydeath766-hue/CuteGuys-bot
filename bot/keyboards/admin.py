from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def pending_group_keyboard(chat_id: int):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✅ Aprobar",
                    callback_data=f"approve:{chat_id}"
                ),
                InlineKeyboardButton(
                    text="❌ Rechazar",
                    callback_data=f"reject:{chat_id}"
                )
            ]
        ]
    )
