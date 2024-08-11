from contextlib import asynccontextmanager
from typing import AsyncContextManager

from S3.S3Client import S3Client
from config import config


@asynccontextmanager
async def s3_client_context() -> AsyncContextManager[S3Client]:
    yield S3Client(
        access_key=config.access_key,
        secret_key=config.secret_key,
        endpoint_url=config.endpoint_url,
        bucket_name=config.bucket_name,
    )
