from fastapi import Depends

from S3.S3Service import S3Service
from file.FileService import FileService
from file.dependencies.clients import s3_client_context
from file.dependencies.repositories import get_file_repo, get_public_file_repo
from folder.dependencies.repositories import get_folder_repo
from subscription.dependencies.repositories import get_subscription_repo
from user.dependencies.repositories import get_user_repo


def get_s3_service() -> S3Service:
    return S3Service(client_context=s3_client_context)


def get_file_service() -> FileService:
    return FileService(files=Depends(get_file_repo),
                       folders=Depends(get_folder_repo),
                       subscriptions=Depends(get_subscription_repo),
                       users=Depends(get_user_repo),
                       public_files=Depends(get_public_file_repo))
