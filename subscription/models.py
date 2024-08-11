from sqlalchemy import Integer, String, BigInteger
from sqlalchemy.orm import mapped_column, Mapped

from db import Base


class Subscriprion(Base):
    __tablename__ = "subscription"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    type: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    disk_space: Mapped[int] = mapped_column(BigInteger, nullable=False)
