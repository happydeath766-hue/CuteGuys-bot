from sqlalchemy import select

from bot.database.session import SessionLocal
from bot.models.group import Group


class ListService:

    @staticmethod
    async def generate():

        async with SessionLocal() as session:

            result = await session.execute(
                select(Group).where(
                    Group.approved == True,
                    Group.active == True
                ).order_by(Group.members.desc())
            )

            groups = result.scalars().all()

            text = "<b>📋 Lista de Grupos</b>\n\n"

            if not groups:
                text += "No hay grupos disponibles."

                return text

            for group in groups:

                if group.invite_link:

                    text += (
                        f'• <a href="{group.invite_link}">'
                        f'{group.title}</a>\n'
                    )

                elif group.username:

                    text += (
                        f'• <a href="https://t.me/{group.username}">'
                        f'{group.title}</a>\n'
                    )

                else:

                    text += f"• {group.title}\n"

            return text
