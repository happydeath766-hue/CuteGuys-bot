from sqlalchemy import BigInteger, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from bot.database.base import Base


class Admin(Base):
    __tablename__ = "admins"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(BigInteger, unique=True)

    owner: Mapped[bool] = mapped_column(Boolean, default=False)
