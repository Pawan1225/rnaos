from fastapi import FastAPI

from apps.backend.app.api.v1.health import router as health_router
from apps.backend.app.core import register_exception_handlers
from packages.config.settings import settings
from packages.core_logging import get_logger

logger = get_logger("rnaos")

logger.info("Starting RNAOS API...")

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="RNAOS Scientific Research Platform",
)

# Register global exception handlers
register_exception_handlers(app)

# Register routers
app.include_router(
    health_router,
    prefix=settings.API_PREFIX,
)


@app.get("/", tags=["Root"])
async def root():
    logger.info("Root endpoint accessed")

    return {
        "platform": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "status": "running",
    }
