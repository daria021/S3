from contextlib import asynccontextmanager

from db import get_async_session
from file.FileService import FileService
from file.file_repository import FileRepo
from file.public_file_repository import PublicFileRepo
from folder.dependencies.repositories import folder_repo_context


async def get_file_repo() -> FileRepo:
    async with get_async_session() as session:
        yield FileRepo(session=session)


@asynccontextmanager
async def file_repo_context() -> FileRepo:
    async with get_async_session() as session:
        yield FileRepo(session=session)


async def get_public_file_repo() -> PublicFileRepo:
    async with get_async_session() as session:
        yield PublicFileRepo(session=session)


@asynccontextmanager
async def public_file_repo_context() -> PublicFileRepo:
    async with get_async_session() as session:
        yield PublicFileRepo(session=session)


async def get_files_service() -> FileService:
    async with file_repo_context() as files:
        async with folder_repo_context() as folders:
            yield FileService(files=files, folders=folders)
