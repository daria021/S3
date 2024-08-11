from AbstractRepository import AbstractRepo
from .schemas import FileUpdate, FileCreate, FileResponse
from .models import File


class FileRepo(AbstractRepo):
    model = File
    update_schema = FileUpdate
    create_schema = FileCreate
    get_schema = FileResponse

    @classmethod
    async def validate(cls, obj: File):
        await obj.awaitable_attrs.user
        await obj.awaitable_attrs.folder
        return cls.get_schema.model_validate(obj)

    async def get_by_file_key(self, key: str) -> FileResponse:
        file = (await self.get_filtered_by(key=key))
        if file:
            return file[0]
