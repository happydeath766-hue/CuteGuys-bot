from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data.startswith("approve:"))
async def approve_group(callback: CallbackQuery):

    chat_id = int(callback.data.split(":")[1])

    # Aquí después guardaremos el grupo en PostgreSQL
    # approved=True

    await callback.message.edit_text(
        f"""
✅ Grupo aprobado

ID:
<code>{chat_id}</code>

Ya aparecerá en la lista pública.
"""
    )

    await callback.answer("Grupo aprobado")


@router.callback_query(F.data.startswith("reject:"))
async def reject_group(callback: CallbackQuery):

    chat_id = int(callback.data.split(":")[1])

    # Aquí después lo eliminaremos o lo marcaremos como rechazado

    await callback.message.edit_text(
        f"""
❌ Grupo rechazado

ID:
<code>{chat_id}</code>
"""
    )

    await callback.answer("Grupo rechazado")
