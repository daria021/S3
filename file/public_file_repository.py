from AbstractRepository import AbstractRepo
from .schemas import PublicFileUpdate, PublicFileCreate, PublicFileResponse
from .models import PublicFile


class PublicFileRepo(AbstractRepo):
    model = PublicFile
    update_schema = PublicFileUpdate
    create_schema = PublicFileCreate
    get_schema = PublicFileResponse

    @classmethod
    async def validate(cls, obj: PublicFile):
        await obj.awaitable_attrs.user
        await obj.awaitable_attrs.folder
        return cls.get_schema.model_validate(obj)

    async def get_by_file_key(self, key: str) -> PublicFileResponse:
        file = (await self.get_filtered_by(key=key))
        if file:
            return file[0]
