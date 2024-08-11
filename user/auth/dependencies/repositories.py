from ..repository import AuthorizationRepo
from db import get_async_session


async def get_auth_repo() -> AuthorizationRepo:
    async with get_async_session() as session:
        yield AuthorizationRepo(session=session)
