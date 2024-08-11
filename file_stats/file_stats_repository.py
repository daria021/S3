from AbstractRepository import AbstractRepo
from file_stats.models import FileStats
from file_stats.schemas import FileStatsUpdate, FileStatsCreate, FileStatsResponse


class FileStatsRepo(AbstractRepo):
    model = FileStats
    update_schema = FileStatsUpdate
    create_schema = FileStatsCreate
    get_schema = FileStatsResponse

    @classmethod
    async def validate(cls, obj: FileStats):
        await obj.awaitable_attrs.file
        return cls.get_schema.model_validate(obj)

    async def get_by_file_key(self, key: str) -> FileStatsResponse:
        file = (await self.get_filtered_by(key=key))
        if file:
            return file[0]
