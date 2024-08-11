from dataclasses import dataclass

from fastapi import Depends

from subscription.repository import SubscriptionRepo
from subscription.schemas import SubscriptionCreate
from user.auth.routes import check_auth
from user.repository import UserRepo
from user.schemas import UserResponse, UserUpdate


@dataclass
class SubscriptionService:
    subscriptions: SubscriptionRepo
    users: UserRepo

    async def add_subscription(
            self, type: str,
            price: int,
            disk_space: int,
    ):
        schema = SubscriptionCreate(
            type=type,
            price=price,
            disk_space=disk_space
        )
        await self.subscriptions.create(schema=schema)

    async def buy_subscription(self,
                               type: str,
                               user: UserResponse = Depends(check_auth)):
        subscription = await self.subscriptions.get_filtered_by(type=type)

        schema_user = UserUpdate(
            name=user.name,
            email=user.email,
            username=user.username,
            hashed_password=user.hashed_password,
            subscription_id=subscription[0].id,
            total_uploaded_size=user.total_uploaded_size
        )
        await self.users.update(record_id=user.id, schema=schema_user)
