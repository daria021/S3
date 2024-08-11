from fastapi import APIRouter, Depends

from .UserService import UserService
from .dependencies.repositories import get_user_repo
from .dependencies.services import get_user_service
from .repository import UserRepo
from .schemas import UserResponse, UserCreate, UserUpdate, UserFilter
from .models import User

router = APIRouter(
    prefix="/user",
    tags=["user/"]
)


@router.post("", response_model=UserResponse)
async def create_user(user: UserCreate,
                      users: UserService = Depends(get_user_service)):
    user = await users.create_user(user)

    return user


@router.get("/filter", response_model=list[UserResponse])
async def get_filter_users(filters: UserFilter = Depends(),
                           users: UserService = Depends(get_user_service)
                           ) -> User:
    clean_filters = {key: value for key, value in filters.model_dump().items() if value is not None}

    res = await users.get_filter_users(clean_filters)
    return res


@router.get("/{user_id}", response_model=UserResponse)
async def get_one_user(user_id: int,
                       users: UserService = Depends(get_user_service)):
    res = await users.get_one_user(user_id=user_id)
    return res


@router.get("", response_model=list[UserResponse])
async def get_all_users(users: UserService = Depends(get_user_service)
                        ) -> list[User]:
    res = await users.get_all_users()
    return res


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int,
                      users: UserService = Depends(get_user_service)):
    user = await users.update_user(user_id=user_id)
    return user


@router.delete("/{user_id}")
async def delete_user(user_id: int,
                      users: UserService = Depends(get_user_service)) -> None:
    await users.delete_user(user_id=user_id)
    return


@router.get("/keys/{user_id}")
async def get_user_files(user_id: int,
                         users: UserService = Depends(get_user_service)):
    res = await users.get_user_files(user_id=user_id)
    return res.files
