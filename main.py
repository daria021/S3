from fastapi import FastAPI

from file.routes import router as file_router
from user.auth.routes import router as auth_router
from user.routes import router as user_router
from folder.routes import router as folder_router
from file_stats.routes import router as file_stats_router
from subscription.routes import router as subscription_router

app = FastAPI(
    title="s3"
)

app.include_router(
    user_router
)
app.include_router(
    file_router
)

app.include_router(
    auth_router
)

app.include_router(
    folder_router
)

app.include_router(
    file_stats_router
)

app.include_router(
    subscription_router
)
