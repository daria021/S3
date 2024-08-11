from contextlib import asynccontextmanager

from db import get_async_session
from file.file_repository import FileRepo


async def get_file_repo() -> FileRepo:
    async with get_async_session() as session:
        yield FileRepo(session=session)


@asynccontextmanager
async def file_repo_context() -> FileRepo:
    async with get_async_session() as session:
        yield FileRepo(session=session)
