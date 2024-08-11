from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict

from file import FileResponse


class FileStatsCreate(BaseModel):
    file_id: int
    owner_id: int
    views: int
    created_at: datetime
    updated_at: Optional[datetime] = None


class FileStatsResponse(BaseModel):
    id: int
    file_id: int
    owner_id: int
    file: FileResponse
    views: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class FileStatsUpdate(BaseModel):
    file_id: Optional[int]
    owner_id: Optional[int]
    views: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)
