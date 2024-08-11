from AbstractRepository import AbstractRepo
from folder.models import PublicFolder
from folder.schemas import PublicFolderUpdate, PublicFolderCreate, PublicFolderResponse


class PublicFolderRepo(AbstractRepo):
    model = PublicFolder
    update_schema = PublicFolderUpdate
    create_schema = PublicFolderCreate
    get_schema = PublicFolderResponse

    @classmethod
    async def validate(cls, obj: PublicFolder):
        await obj.awaitable_attrs.files
        return cls.get_schema.model_validate(obj)

    async def get_by_key(self, key: str) -> PublicFolderResponse:
        folder = (await self.get_filtered_by(key=key))
        if folder:
            return folder[0]

    async def add_file_to_folder(self, folder_key: str, file_key: str):
        folder = (await self.get_filtered_by(key=folder_key))[0]
        folder.files.append(file_key)
        await self.session.commit()

    async def delete_file_from_folder(self, folder_key: str, file_key: str):
        folder = (await self.get_filtered_by(key=folder_key))[0]
        file = (await self.get_filtered_by(key=file_key))
        folder.files.remove(file)
        await self.session.commit()
