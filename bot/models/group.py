from sqlalchemy import BigInteger, Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from bot.database.base import Base


class Group(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(primary_key=True)

    chat_id: Mapped[int] = mapped_column(BigInteger, unique=True)

    title: Mapped[str] = mapped_column(String(255))

    username: Mapped[str | None]

    invite_link: Mapped[str | None]

    members: Mapped[int] = mapped_column(default=0)

    approved: Mapped[bool] = mapped_column(Boolean, default=False)

    active: Mapped[bool] = mapped_column(Boolean, default=True)
