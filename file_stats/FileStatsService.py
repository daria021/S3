from datetime import datetime

from fastapi import HTTPException

from file.dependencies.repositories import public_file_repo_context
from file_stats.dependencies.repositories import file_stats_repo_context
from file_stats.schemas import FileStatsResponse, FileStatsCreate, FileStatsUpdate


class FileStatsService:

    @staticmethod
    async def create_file_stats(
            key: str,
            user_id: int,
    ) -> FileStatsResponse:

        async with public_file_repo_context() as files:
            file = await files.get_by_file_key(key=key)

        if not file:
            raise HTTPException(status_code=404, detail="File not found")

        schema = FileStatsCreate(
            file_id=file.id,
            owner_id=user_id,
            views=0,
            created_at=datetime.now(),
        )

        async with file_stats_repo_context() as stats:
            stat = await stats.create(schema=schema)

        return stat

    @staticmethod
    async def update_file_stats(
            file_id: int,
            views: int,
    ) -> FileStatsResponse:

        async with file_stats_repo_context() as stats:
            old_stats = await stats.get_filtered_by(file_id=file_id)
        print("VIEWS=", views)
        schema = FileStatsUpdate(
            file_id=file_id,
            owner_id=old_stats[0].owner_id,
            views=views,
            created_at=old_stats[0].created_at,
            updated_at=datetime.now()
        )
        print(old_stats[0].id, schema.model_dump())
        async with file_stats_repo_context() as stats:
            return await stats.update(record_id=old_stats[0].id, schema=schema)

    @staticmethod
    async def get_file_stats(
            key: str,
    ) -> FileStatsResponse:

        async with public_file_repo_context() as files:
            file = await files.get_by_file_key(key=key)

        if not file:
            raise HTTPException(status_code=404, detail="File not found")

        async with file_stats_repo_context() as file_stats:
            return (await file_stats.get_filtered_by(file_id=file.id))[0]
