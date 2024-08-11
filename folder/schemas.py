from typing import Optional

from pydantic import BaseModel, ConfigDict

from file.schemas import PublicFileResponse, FileResponse


class FolderCreate(BaseModel):
    user_id: int
    folder_name: str
    key: str


class FolderUpdate(BaseModel):
    key: str
    folder_name: str
    files: list[str]


class FolderResponse(BaseModel):
    id: int
    user_id: int
    key: str
    folder_name: str
    files: list[str]
    files: list[FileResponse]

    model_config = ConfigDict(from_attributes=True)


class FolderFilter(BaseModel):
    id: Optional[int]
    user_id: int
    key: Optional[str]
    folder_name: str

    model_config = ConfigDict(from_attributes=True)


class PublicFolderCreate(BaseModel):
    user_id: int
    key: str
    folder_name: str


class PublicFolderUpdate(BaseModel):
    ...


class PublicFolderResponse(BaseModel):
    id: int
    user_id: int
    key: str
    folder_name: str
    files: list[PublicFileResponse]

    model_config = ConfigDict(from_attributes=True)


class PublicFolderFilter(BaseModel):
    id: Optional[int]
    user_id: int
    key: Optional[str]
    folder_name: str

    model_config = ConfigDict(from_attributes=True)
