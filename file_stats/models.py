from datetime import datetime
from typing import Optional

from sqlalchemy import Integer, TIMESTAMP, ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base


class FileStats(Base, AsyncAttrs):
    __tablename__ = "file_stats"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    file_id: Mapped[int] = mapped_column(Integer, ForeignKey('public_file.id'), nullable=False)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), nullable=False)
    file: Mapped['File'] = relationship("PublicFile")
    views: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)
    updated_at: Mapped[Optional[datetime]] = mapped_column(TIMESTAMP, default=datetime.utcnow)
