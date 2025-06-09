from fastapi import Depends
from sqlalchemy.orm import Session
from models.log_schema import LogCreate
from services.log_service import ingest_log_service
from config import get_db
from typing import Optional, List
from datetime import datetime
from models.log_db_model import Log

from services.log_service import get_logs_service


def ingest_log_controller(log, db):
    return ingest_log_service(log, db)

def get_logs_controller(
    level: Optional[str],
    service_name: Optional[str],
    from_ts: Optional[datetime],
    to_ts: Optional[datetime],
    limit: int,
    db: Session
):
    return get_logs_service(db, level, service_name, from_ts, to_ts, limit)
