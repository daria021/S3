import os

from fastapi import APIRouter, UploadFile, File, BackgroundTasks, Depends
from fastapi.responses import FileResponse

from S3.S3Service import S3Service
from file.FileService import FileService
from file.dependencies.services import get_s3_service, get_file_service
from file_stats.FileStatsService import FileStatsService
from file_stats.dependencies.services import get_file_stats_service
from newsletter.dependencies.services import get_mail_service
from user.auth.routes import check_auth
from user.schemas import UserResponse

router = APIRouter(
    prefix="/file",
    tags=["file/"]
)


@router.post("/upload")
async def upload_file(
        filename: str,
        s3_service: S3Service = Depends(get_s3_service),
        image: UploadFile = File(...),
        user: UserResponse = Depends(check_auth),
        file_service: FileService = Depends(get_file_service),
):
    schema_file = await file_service.write_file(user=user, filename=filename, image=image)

    await s3_service.upload_file(key=schema_file.key, schema=schema_file, filepath=schema_file.file_path)

    return schema_file.key


@router.delete("/delete")
async def delete_file(
        filename: str,
        s3_service: S3Service = Depends(get_s3_service),
        file_service: FileService = Depends(get_file_service),
):
    file = await file_service.delete_file(filename=filename)
    await s3_service.delete_file(key=file[0].key)


@router.get("/get")
async def get_file(
        filename: str,
        background_tasks: BackgroundTasks,
        s3_service: S3Service = Depends(get_s3_service),
) -> FileResponse:
    Fileresponse = await s3_service.get_file(filename)
    background_tasks.add_task(os.remove)
    return Fileresponse


@router.get("/get_public_file")
async def get_public_file(
        key: str,
        background_tasks: BackgroundTasks,
        s3_service: S3Service = Depends(get_s3_service),
        stats=Depends(get_file_stats_service),
        mails=Depends(get_mail_service),
        file_service: FileService = Depends(get_file_service),

) -> FileResponse:
    mail, filepath, file, file_stats = await file_service.create_email(key=key)

    await s3_service.get_file(key=key)

    background_tasks.add_task(os.remove, filepath)

    await stats.update_file_stats(file_id=file[0].id, views=file_stats.views + 1)

    await mails.send_mail(mail=mail)

    return FileResponse(path=filepath, filename=key, media_type="multipart/form-data")


@router.get("/get_public_key")
async def create_public_key(
        filename: str,
        user: UserResponse = Depends(check_auth),
        file_stats: FileStatsService = Depends(get_file_stats_service),
        file_service: FileService = Depends(get_file_service)
) -> str:
    key = await file_service.create_public_key(filename=filename, user=user)
    await file_stats.create_file_stats(key=key, user_id=user.id)
    return key
