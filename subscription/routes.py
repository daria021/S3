from fastapi import APIRouter, Depends

from subscription.SubscriptionService import SubscriptionService
from subscription.dependencies.services import get_subscription_service

router = APIRouter(
    prefix="/subscription",
    tags=["subscription/"]
)


@router.post("/add_subscirption")
async def add_subscription(type: str,
                           price: int,
                           disk_space: int,
                           subscriptions: SubscriptionService = Depends(get_subscription_service)):
    await subscriptions.add_subscription(type=type, price=price, disk_space=disk_space)
    return {"message": "Subscription added successfully"}


@router.post("/post")
async def buy_subscription(type: str,
                           subscriptions: SubscriptionService = Depends(get_subscription_service)):
    await subscriptions.buy_subscription(type=type)
    return {"message": "Subscription bought successfully"}
