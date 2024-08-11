from fastapi import APIRouter, Depends

from file_stats.dependencies.services import get_file_stats_service
from file_stats.schemas import FileStatsResponse

router = APIRouter(
    prefix="/file_stats",
    tags=["file_stats/"]
)


@router.get("/get_file_stats")
async def get_file_stats(
        key: str,
        stats_service=Depends(get_file_stats_service),
) -> FileStatsResponse:
    stats = await stats_service.get_file_stats(key=key)
    print("stats =", stats)
    return stats
