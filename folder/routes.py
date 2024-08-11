from fastapi import APIRouter, Depends

from file.dependencies.repositories import get_files_service
from folder.dependencies.services import get_folder_service
from user.auth.routes import check_auth
from user.schemas import UserResponse

router = APIRouter(
    prefix="/folder",
    tags=["folder/"]
)


@router.post("/create_a_folder")
async def create_a_folder(
        folder_name: str,
        folder_service=Depends(get_folder_service),
) -> str:
    key = await folder_service.create_a_folder(folder_name=folder_name)

    return key


@router.post("/create_a_public_folder")
async def create_a_public_folder(
        public_folder_name: str,
        folder_service=Depends(get_folder_service),
) -> str:
    key = await folder_service.create_a_public_folder(public_folder_name=public_folder_name)

    return key


@router.post("/add_file_to_folder")
async def add_file_to_folder(
        folder_key: str,
        file_key: str,
        folder_service=Depends(get_folder_service),
):
    await folder_service.add_file_to_folder(folder_key=folder_key, file_key=file_key)
    return "File was added to the folder"


@router.get("/get_folder")
async def get_folder(
        folder_key: str,
        folder_service=Depends(get_folder_service),
):
    folder = await folder_service.get_folder(folder_key=folder_key)

    return folder[0]


@router.get("/get_public_folder")
async def get_public_folder(
        folder_key: str,
        folder_service=Depends(get_folder_service),
):
    folder = await folder_service.get_public_folder(folder_key=folder_key)

    return folder


@router.post("/add_public_file_to_folder")
async def add_public_file_to_folder(
        public_file_key: str,
        public_folder_key: str,
        folder_service=Depends(get_folder_service),
):
    await folder_service.add_public_file_to_folder(public_file_key=public_file_key, public_folder_key=public_folder_key)

    return "File was added to the folder"


@router.delete("/delete_file_from_folder")
async def delete_file_from_folder(
        file_key: str,
        user: UserResponse = Depends(check_auth),
        files=Depends(get_files_service),
):
    await files.delete_file_from_folder(file_key=file_key)

    return "File was deleted from the folder"


@router.delete("/delete_public_file_from_folder")
async def delete_public_file_from_folder(
        public_file_key: str,
        files=Depends(get_files_service),
):
    await files.delete_public_file_from_folder(file_key=public_file_key)

    return "File was deleted from the folder"
