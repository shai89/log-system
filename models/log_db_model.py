from sqlalchemy import Column, String, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from db.base import Base

class Log(Base):
    __tablename__ = "logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    timestamp = Column(TIMESTAMP(timezone=True), nullable=False)
    level = Column(Text, nullable=False)
    service_name = Column(Text, nullable=False)
    message = Column(Text, nullable=False)
    trace_id = Column(Text, nullable=True)
    source = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())