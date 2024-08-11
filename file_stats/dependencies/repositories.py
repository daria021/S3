from contextlib import asynccontextmanager

from db import get_async_session
from file_stats.file_stats_repository import FileStatsRepo


async def get_file_stats_repo() -> FileStatsRepo:
    async with get_async_session() as session:
        yield FileStatsRepo(session=session)


@asynccontextmanager
async def file_stats_repo_context() -> FileStatsRepo:
    async with get_async_session() as session:
        yield FileStatsRepo(session=session)
