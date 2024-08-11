from typing import Optional

from pydantic import BaseModel, ConfigDict


class FileCreate(BaseModel):
    user_id: int
    key: str
    file_path: str
    filename: str


class FileUpdate(BaseModel):
    id: Optional[int]
    user_id: Optional[int]
    key: Optional[str]
    file_path: Optional[str]
    filename: Optional[str]
    folder_id: Optional[int]


class FileResponse(BaseModel):
    id: int
    user_id: int
    key: str
    file_path: str
    filename: str
    folder_id: Optional[int]

    model_config = ConfigDict(from_attributes=True)


class FileFilter(BaseModel):
    id: Optional[int]
    user_id: int
    key: Optional[str]
    file_path: Optional[str]
    filename: str
    folder_id: Optional[int]

    model_config = ConfigDict(from_attributes=True)


class PublicFileCreate(BaseModel):
    user_id: int
    key: str
    file_path: str
    filename: str


class PublicFileUpdate(BaseModel):
    ...


class PublicFileResponse(BaseModel):
    id: int
    user_id: int
    key: str
    file_path: str
    filename: str
    folder_id: Optional[int]

    model_config = ConfigDict(from_attributes=True)


class PublicFileFilter(BaseModel):
    id: Optional[int]
    user_id: int
    key: Optional[str]
    file_path: Optional[str]
    filename: str
    folder_id: Optional[int]

    model_config = ConfigDict(from_attributes=True)
