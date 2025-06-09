from fastapi import APIRouter, status, Query, Depends
from sqlalchemy.orm import Session
from typing import Optional, List
from datetime import datetime
from models.log_schema import LogCreate
from models.query_params import LogQueryParams
from controllers import log_controller
from config import get_db

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
async def ingest_log(log: LogCreate, db: Session = Depends(get_db)):
    return log_controller.ingest_log_controller(log, db)


@router.get("/", response_model=List[LogCreate], summary="Fetch logs", description="Filter logs with optional query parameters")
def fetch_logs(
    params: LogQueryParams = Depends(),
    db: Session = Depends(get_db)
):
    return log_controller.get_logs_controller(
        level=params.level,
        service_name=params.service_name,
        from_ts=params.from_ts,
        to_ts=params.to_ts,
        limit=params.limit,
        db=db
    )
