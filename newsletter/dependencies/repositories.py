from contextlib import asynccontextmanager

from db import get_async_session
from newsletter.repository import NewsletterRepo


async def get_mail_repo() -> NewsletterRepo:
    async with get_async_session() as session:
        yield NewsletterRepo(session=session)


@asynccontextmanager
async def mail_repo_context() -> NewsletterRepo:
    async with get_async_session() as session:
        yield NewsletterRepo(session=session)
