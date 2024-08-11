import os
from typing import Callable, AsyncContextManager

from .S3Client import S3Client
from file.schemas import FileResponse, FileCreate


class S3Service:
    def __init__(self, client_context: Callable[[], AsyncContextManager[S3Client]]):
        self.client_context = client_context

    async def get_file(
            self,
            key: str,
    ):
        filepath = f"temp/{key}"
        async with self.client_context() as client:
            await client.get_file(key=key, destination_path=filepath)
        return filepath

    async def upload_file(
            self,
            key: str,
            schema: FileCreate,
            filepath: str
    ):
        async with self.client_context() as client:
            await client.upload_file(key=key, file_path=filepath)
        os.remove(filepath)
        return key

    async def delete_file(
            self,
            key: str,
    ):
        async with self.client_context() as client:
            await client.delete_file(key=key)
