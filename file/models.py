from typing import Optional

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base


class File(Base, AsyncAttrs):
    __tablename__ = "file"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    key: Mapped[str] = mapped_column(String, nullable=False)
    filename: Mapped[str] = mapped_column(String, nullable=False)
    file_path: Mapped[str] = mapped_column(String, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), nullable=False)
    user: Mapped['User'] = relationship("User", back_populates="files")
    folder_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey('folder.id'))
    folder: Mapped['Folder'] = relationship(
        "Folder",
        back_populates="files"
    )


class PublicFile(Base, AsyncAttrs):
    __tablename__ = "public_file"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    key: Mapped[str] = mapped_column(String, nullable=False)
    filename: Mapped[str] = mapped_column(String, nullable=False)
    file_path: Mapped[str] = mapped_column(String, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), nullable=False)
    user: Mapped['User'] = relationship("User", back_populates="public_files")
    folder_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey('public_folder.id'))
    folder: Mapped['PublicFolder'] = relationship(
        "PublicFolder",
        back_populates="files"
    )
    stats: Mapped['FileStats'] = relationship(
        "FileStats",
        cascade="all, delete-orphan",
        back_populates="file",
        primaryjoin="PublicFile.id == FileStats.file_id"
    )
