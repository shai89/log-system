from sqlalchemy.orm import Session
from models.log_db_model import Log
from models.log_schema import LogCreate
from typing import List, Optional
from datetime import datetime


def create_log(log: LogCreate, db: Session):
    data = log.dict()
    if isinstance(data["timestamp"], str):
        from datetime import datetime
        data["timestamp"] = datetime.fromisoformat(data["timestamp"])
    db_log = Log(**data)

    # db_log = Log(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log


def get_logs(
    db: Session,
    level: Optional[str] = None,
    service_name: Optional[str] = None,
    from_ts: Optional[datetime] = None,
    to_ts: Optional[datetime] = None,
    limit: int = 100
) -> List[Log]:
    query = db.query(Log)

    if level:
        query = query.filter(Log.level == level)
    if service_name:
        query = query.filter(Log.service_name == service_name)
    if from_ts:
        query = query.filter(Log.timestamp >= from_ts)
    if to_ts:
        query = query.filter(Log.timestamp <= to_ts)

    return query.order_by(Log.timestamp.desc()).limit(limit).all()
