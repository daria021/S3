from fastapi import Depends

from user.UserService import UserService
from user.dependencies.repositories import get_user_repo


def get_user_service() -> UserService:
    return UserService(users=Depends(get_user_repo))
