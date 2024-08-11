from typing import Annotated

from fastapi import UploadFile

from file.schemas import FileCreate
from .S3Client import S3Client


class CommonService:
    def __init__(
            self,
            file_repo_context,
            s3_client: S3Client,
    ):
        self.files = file_repo_context
        self.s3_client = s3_client

    async def upload_file(
            self,
            image: UploadFile,
            file: FileCreate,
    ):
        async with self.files() as files:
            file = await files.create(schema=file)

        try:
            await self.s3_client.upload_file(
                key=str(file.id),
                file_path=file.file_path,
            )
        except Exception as e:
            async with self.files() as files:
                await files.delete(record_id=file.id)
            raise e

        return file

    async def get_file(
            self,
            key: str,
    ):
        filepath = await self._get_file_image(key=key)

        return filepath

    async def get_file_image(
            self,
            key: str,
    ) -> str:
        filepath = await self._get_file_image(key=key)
        return filepath

    async def _get_file_image(
            self,
            key: str,
    ) -> Annotated[str, "Path there the file is saved"]:

        filepath = self.s3_client.get_filepath(key=key)
        await self.s3_client.get_file(key=key, destination_path=filepath)

        return filepath

    async def delete_file(
            self,
            key: str
    ):
        await self.s3_client.delete_file(key=key)

        async with self.files() as files:
            await files.delete(record_id=int(key))
