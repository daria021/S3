from typing import Optional

from pydantic import BaseModel, ConfigDict


class SubscriptionCreate(BaseModel):
    type: str
    price: int
    disk_space: int


class SubscriptionUpdate(BaseModel):
    type: Optional[str]
    price: Optional[int]
    disk_space: Optional[int]

    model_config = ConfigDict(from_attributes=True)


class SubscriptionResponse(BaseModel):
    id: int
    type: str
    price: int
    disk_space: int

    model_config = ConfigDict(from_attributes=True)
