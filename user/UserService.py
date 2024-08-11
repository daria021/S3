from dataclasses import dataclass

from user.models import User
from user.repository import UserRepo
from user.schemas import UserCreate, UserResponse, UserUpdate


@dataclass
class UserService:
    users: UserRepo

    async def create_user(
            self,
            user: UserCreate
    ) -> UserResponse:
        user = await self.users.create(schema=user)
        return user

    async def get_filter_users(
            self,
            clean_filters: dict,
    ) -> User:
        res = await self.users.get_filtered_by(**clean_filters)
        return res[0]

    async def get_one_user(
            self,
            user_id: int,
    ):
        res = await self.users.get(record_id=user_id)
        return res

    async def get_all_users(self
                            ) -> list[User]:
        res = await self.users.get_all()
        return res

    async def update_user(
            self,
            user_id: int,
            update: UserUpdate):
        user = await self.users.update(record_id=user_id, schema=update)
        return user

    async def delete_user(self,
                          user_id: int,
                          ) -> None:
        await self.users.delete(record_id=user_id)
        return

    async def get_user_files(self,
                             user_id: int,
                             ):
        res = await self.users.get(record_id=user_id)
        return res
