from sqlalchemy.orm import Session
from models.log_schema import LogCreate
from dals.log_dal import create_log
from typing import Optional, List
from datetime import datetime
from models.log_db_model import Log
from dals.log_dal import get_logs


def ingest_log_service(log: LogCreate, db: Session):
    return create_log(log, db)

def get_logs_service(
    db: Session,
    level: Optional[str] = None,
    service_name: Optional[str] = None,
    from_ts: Optional[datetime] = None,
    to_ts: Optional[datetime] = None,
    limit: int = 100
) -> List[Log]:
    return get_logs(db, level, service_name, from_ts, to_ts, limit)
