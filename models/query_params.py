from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from db.enums import LogLevel

class LogQueryParams(BaseModel):
    level: Optional[LogLevel] = Field(None, description="Log level to filter")
    service_name: Optional[str] = Field(None, description="Service name to filter")
    from_ts: Optional[datetime] = Field(None, description="Start timestamp (ISO 8601)")
    to_ts: Optional[datetime] = Field(None, description="End timestamp (ISO 8601)")
    limit: int = Field(100, ge=1, le=1000, description="Max number of logs to return")
