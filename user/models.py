from datetime import datetime

from pydantic import EmailStr
from sqlalchemy import String, TIMESTAMP, Boolean, Integer, ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base

from file.models import File
from file.models import PublicFile


class User(Base, AsyncAttrs):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[EmailStr] = mapped_column(String, nullable=False, unique=True)
    username: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    registered_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    subscription_id: Mapped[int] = mapped_column(Integer, ForeignKey('subscription.id'), nullable=False, default=1)
    total_uploaded_size: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    files: Mapped[list['File']] = relationship(
        "File",
        back_populates="user"
    )
    public_files: Mapped[list['PublicFile']] = relationship(
        "PublicFile",
        back_populates="user"
    )
