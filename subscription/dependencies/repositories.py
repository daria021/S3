from contextlib import asynccontextmanager

from db import get_async_session
from subscription.repository import SubscriptionRepo


async def get_subscription_repo() -> SubscriptionRepo:
    async with get_async_session() as session:
        yield SubscriptionRepo(session=session)


@asynccontextmanager
async def subscription_repo_context() -> SubscriptionRepo:
    async with get_async_session() as session:
        yield SubscriptionRepo(session=session)
