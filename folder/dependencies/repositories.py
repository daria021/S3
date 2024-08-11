from contextlib import asynccontextmanager

from db import get_async_session
from folder.folder_repository import FolderRepo
from folder.public_folder_repository import PublicFolderRepo


async def get_folder_repo() -> FolderRepo:
    async with get_async_session() as session:
        yield FolderRepo(session=session)


@asynccontextmanager
async def folder_repo_context() -> FolderRepo:
    async with get_async_session() as session:
        yield FolderRepo(session=session)


async def get_public_folder_repo() -> PublicFolderRepo:
    async with get_async_session() as session:
        yield PublicFolderRepo(session=session)


@asynccontextmanager
async def public_folder_repo_context() -> PublicFolderRepo:
    async with get_async_session() as session:
        yield PublicFolderRepo(session=session)
