from AbstractRepository import AbstractRepo
from folder.models import Folder
from folder.schemas import FolderUpdate, FolderCreate, FolderResponse


class FolderRepo(AbstractRepo):
    model = Folder
    update_schema = FolderUpdate
    create_schema = FolderCreate
    get_schema = FolderResponse

    @classmethod
    async def validate(cls, obj: Folder):
        await obj.awaitable_attrs.files
        return cls.get_schema.model_validate(obj)

    async def get_by_key(self, key: str) -> FolderResponse:
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
