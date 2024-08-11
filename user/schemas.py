from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    name: str
    email: str
    username: str
    hashed_password: str


class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]
    username: Optional[str]
    hashed_password: Optional[str]
    subscription_id: Optional[int]
    total_uploaded_size: Optional[int]

    model_config = ConfigDict(from_attributes=True)


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    username: str
    hashed_password: str
    registered_at: datetime
    files: list['FileResponse']
    subscription_id: int
    total_uploaded_size: int

    model_config = ConfigDict(from_attributes=True)


class UserFilter(BaseModel):
    id: Optional[int]
    name: Optional[str]
    email: Optional[str]
    username: Optional[str]
    hashed_password: Optional[str]
    registered_at: Optional[datetime]
    files: Optional[list['FileResponse']]
    subscription_id: int
    total_uploaded_size: int

    model_config = ConfigDict(from_attributes=True)


from file.schemas import FileResponse

UserResponse.model_rebuild()
