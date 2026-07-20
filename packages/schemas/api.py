from typing import Any

from pydantic import BaseModel


class APIResponse(BaseModel):
    success: bool = True
    message: str = "Success"
    data: Any | None = None


class APIError(BaseModel):
    success: bool = False
    error: str
