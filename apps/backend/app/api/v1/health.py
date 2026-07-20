from fastapi import APIRouter

from packages.schemas import APIResponse

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/", response_model=APIResponse)
async def health():
    return APIResponse(
        message="RNAOS is healthy",
        data={
            "status": "healthy",
        },
    )
