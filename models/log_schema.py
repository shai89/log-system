from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LogCreate(BaseModel):
    timestamp: datetime
    level: str
    service_name: str
    message: str
    trace_id: Optional[str] = None
    source: Optional[str] = None
