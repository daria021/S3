from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class NewsletterUpdate(BaseModel):
    subject: Optional[str]
    recipients: Optional[list[EmailStr]]
    body: Optional[str]


class NewsletterCreate(NewsletterUpdate):
    subject: str
    recipients: list[EmailStr]
    body: str


class NewsletterResponse(BaseModel):
    id: int
    subject: str
    recipients: list[EmailStr]
    body: str

    model_config = ConfigDict(from_attributes=True)
