from fastapi import Depends

from subscription.SubscriptionService import SubscriptionService
from subscription.dependencies.repositories import get_subscription_repo
from user.dependencies.repositories import get_user_repo


def get_subscription_service() -> SubscriptionService:
    return SubscriptionService(subscriptions=Depends(get_subscription_repo),
                               users=Depends(get_user_repo))
