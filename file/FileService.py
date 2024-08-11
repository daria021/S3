from dataclasses import dataclass

from fastapi import UploadFile, Depends, File

from S3.dependencies.key_service import generate_image_key
from file.dependencies.exceptions import NotEnoughtDiskSpaceException
from file.file_repository import FileRepo
from file.public_file_repository import PublicFileRepo
from file.schemas import FileUpdate, FileCreate, PublicFileCreate
from file_stats.dependencies.services import get_file_stats_service
from folder.folder_repository import FolderRepo
from newsletter.schemas import NewsletterCreate
from subscription.repository import SubscriptionRepo
from user.auth.routes import check_auth
from user.repository import UserRepo
from user.schemas import UserResponse, UserUpdate


@dataclass
class FileService:
    files: FileRepo
    folders: FolderRepo
    subscriptions: SubscriptionRepo
    users: UserRepo
    public_files: PublicFileRepo

    async def add_file_to_folder(self, folder_key: str, file_key: str):
        folder = await self.folders.get_by_key(folder_key)
        file = await self.files.get_by_file_key(file_key)
        update_schema = FileUpdate(**file.model_dump())
        update_schema.folder_id = folder.id
        await self.files.update(file.id, update_schema)

    async def delete_file_from_folder(self, file_key: str):
        file = await self.files.get_by_file_key(file_key)
        update_schema = FileUpdate(**file.model_dump())
        update_schema.folder_id = None
        await self.files.update(file.id, update_schema)

    async def check_subscription(self,
                                 user: UserResponse,
                                 image: UploadFile = File(...),
                                 ):
        file_size = len(image.file.read())
        image.file.seek(0)  # Сбрасываем указатель файла

        total_size = user.total_uploaded_size + file_size

        subscription_id = user.subscription_id
        subscription = await self.subscriptions.get(record_id=subscription_id)
        if total_size > subscription.disk_space:
            raise NotEnoughtDiskSpaceException
        return total_size

    async def write_file(self,
                         user: UserResponse,
                         filename: str,
                         image: UploadFile = File(...),
                         ):
        file = await self.files.get_filtered_by(filename=filename, user_id=user.id)

        if file:
            await self.files.delete(file[0].id)

        key = generate_image_key(extension=image.filename.split(".")[-1])

        file_path = f"temp/{key}"

        with open(file_path, "wb") as file:
            file.write(image.file.read())

        schema_file = FileCreate(
            user_id=user.id,
            key=key,
            file_path=file_path,
            filename=filename,
        )
        await self.files.create(schema=schema_file)

        total_size = await self.check_subscription(image=image, user=user)

        schema_user = UserUpdate(
            name=user.name,
            email=user.email,
            username=user.username,
            hashed_password=user.hashed_password,
            total_uploaded_size=total_size,
            subscription_id=user.subscription_id,
        )
        await self.users.update(record_id=user.id, schema=schema_user)

        return

    async def create_email(self,
                           key: str,
                           stats=Depends(get_file_stats_service),
                           ):

        file = await self.files.get_filtered_by(key=key)
        file_stats = await stats.get_file_stats(key=key)

        key = file[0].key
        filepath = f"temp/{key}"
        recipients = await self.users.get_filtered_by(id=file_stats.owner_id)
        recipients_email = recipients[0].email

        mail = NewsletterCreate(
            subject="Ваш публичный файл был скачан",
            recipients=[recipients_email],
            body=f"Добрый день, файл {file[0].filename} был скачан",
        )
        return [mail, filepath, file, file_stats]

    async def delete_file(self,
                          filename: str,
                          user: UserResponse = Depends(check_auth),
                          ):
        file = await self.files.get_filtered_by(filename=filename, user_id=user.id)
        await self.files.delete(record_id=file[0].id)
        return file

    async def create_public_key(self,
                                filename: str,
                                user: UserResponse,
                                ):
        file = await self.public_files.get_filtered_by(filename=filename, user_id=user.id)
        key = file[0].key
        file_path = file[0].file_path

        public_file = await self.public_files.get_filtered_by(filename=filename, user_id=user.id)
        if public_file:
            return key
        else:
            schema = PublicFileCreate(
                user_id=user.id,
                key=key,
                file_path=file_path,
                filename=filename,
            )
            await self.public_files.create(schema)
        return key
