from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base


class Folder(Base, AsyncAttrs):
    __tablename__ = "folder"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), nullable=False)
    key: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    folder_name: Mapped[str] = mapped_column(String, nullable=False)
    files: Mapped[list["File"]] = relationship(
        "File",
        back_populates="folder",
        cascade="all, delete-orphan",
        primaryjoin="Folder.id == File.folder_id"
    )


class PublicFolder(Base, AsyncAttrs):
    __tablename__ = "public_folder"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), nullable=False)
    key: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    folder_name: Mapped[str] = mapped_column(String, nullable=False)
    files: Mapped[list["PublicFile"]] = relationship(
        "PublicFile",
        back_populates="folder",
        cascade="all, delete-orphan",
        primaryjoin="PublicFolder.id == PublicFile.folder_id"
    )
