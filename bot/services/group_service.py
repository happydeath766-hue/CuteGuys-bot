from sqlalchemy import select

from bot.models.group import Group
from bot.database.session import SessionLocal


class GroupService:

    @staticmethod
    async def add_group(
        chat_id: int,
        title: str,
        username: str | None,
        invite_link: str | None,
    ):

        async with SessionLocal() as session:

            result = await session.execute(
                select(Group).where(Group.chat_id == chat_id)
            )

            group = result.scalar_one_or_none()

            if group:
                group.title = title
                group.username = username
                group.invite_link = invite_link
                group.active = True

            else:

                session.add(
                    Group(
                        chat_id=chat_id,
                        title=title,
                        username=username,
                        invite_link=invite_link,
                        approved=False,
                        active=True,
                    )
                )

            await session.commit()

    @staticmethod
    async def approve(chat_id: int):

        async with SessionLocal() as session:

            result = await session.execute(
                select(Group).where(Group.chat_id == chat_id)
            )

            group = result.scalar_one_or_none()

            if group:

                group.approved = True

                await session.commit()

    @staticmethod
    async def reject(chat_id: int):

        async with SessionLocal() as session:

            result = await session.execute(
                select(Group).where(Group.chat_id == chat_id)
            )

            group = result.scalar_one_or_none()

            if group:

                group.active = False

                await session.commit()
