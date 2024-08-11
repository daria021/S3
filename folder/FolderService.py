from dataclasses import dataclass

from fastapi import Depends

from S3.dependencies.key_service import generate_folder_key
from file.file_repository import FileRepo
from folder.folder_repository import FolderRepo
from folder.public_folder_repository import PublicFolderRepo
from folder.schemas import FolderCreate
from user.auth.routes import check_auth
from user.schemas import UserResponse


@dataclass
class FolderService:
    folders: FolderRepo
    files: FileRepo
    public_folders: PublicFolderRepo

    async def create_a_folder(self,
                              folder_name: str,
                              user: UserResponse = Depends(check_auth),
                              ):
        key = generate_folder_key(folder_name=folder_name)
        await self.folders.create(schema=FolderCreate(folder_name=folder_name, user_id=user.id, key=key))
        return key

    async def create_a_public_folder(self,
                                     public_folder_name: str,
                                     user: UserResponse = Depends(check_auth),
                                     ):
        key = generate_folder_key(folder_name=public_folder_name)
        await self.folders.create(schema=FolderCreate(folder_name=public_folder_name, user_id=user.id, key=key))
        return key

    async def add_file_to_folder(self,
                                 folder_key: str,
                                 file_key: str,
                                 ):
        await self.folders.add_file_to_folder(folder_key=folder_key, file_key=file_key)

    async def get_folder(
            self,
            folder_key: str,
            user: UserResponse = Depends(check_auth),
    ):
        folder = await self.folders.get_filtered_by(key=folder_key, user_id=user.id)

        return folder[0]

    async def get_public_folder(
            self,
            folder_key: str,
    ):
        folder = await self.public_folders.get_by_key(key=folder_key)

        return folder

    async def add_public_file_to_folder(
            self,
            public_file_key: str,
            public_folder_key: str,
            user: UserResponse = Depends(check_auth),
    ):
        await self.public_folders.add_file_to_folder(folder_key=public_folder_key, file_key=public_file_key)

        return "File was added to the folder"

    async def delete_public_file_from_folder(
            self,
            public_file_key: str,
            user: UserResponse = Depends(check_auth),
    ):
        await self.public_folders.delete_file_from_folder(file_key=public_file_key)

        return "File was deleted from the folder"
