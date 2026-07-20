from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from packages.core_logging import get_logger

logger = get_logger("rnaos.exceptions")


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Request,
        exc: Exception,
    ):
        logger.exception("Unhandled exception occurred")

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": {
                    "type": exc.__class__.__name__,
                    "message": str(exc),
                },
            },
        )
