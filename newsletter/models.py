from sqlalchemy import Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class Newsletter(Base):
    __tablename__ = "newsletter"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    subject: Mapped[str] = mapped_column(String, nullable=False)
    recipients: Mapped[list[str]] = mapped_column(JSONB, nullable=False)
    body: Mapped[str] = mapped_column(String, nullable=False)
