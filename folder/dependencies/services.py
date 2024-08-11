from fastapi import Depends

from file.dependencies.repositories import get_file_repo
from folder.FolderService import FolderService
from folder.dependencies.repositories import get_folder_repo, get_public_folder_repo


def get_folder_service() -> FolderService:
    return FolderService(files=Depends(get_file_repo),
                         folders=Depends(get_folder_repo),
                         public_folders=Depends(get_public_folder_repo))
