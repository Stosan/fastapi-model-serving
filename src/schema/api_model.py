from datetime import datetime
from typing import Any
from pydantic import BaseModel

class CustomAPIResponse(BaseModel):
    status: int = 200
    time: str = datetime.utcnow().isoformat()
    prediction_data: Any = None
    message: str = None

class CustomErrorResponse(BaseModel):
    status: int = 200
    time: str = datetime.utcnow().isoformat()
    error: str