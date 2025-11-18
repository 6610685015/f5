from database import Base
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE
from sqlalchemy import TIMESTAMP, Column, String
from sqlalchemy.sql import func


class Name(Base):
    __tablename__ = "names"
    id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    title = Column(String, nullable=True)
    first = Column(String, nullable=False)
    family = Column(String, nullable=True)
    other = Column(String, nullable=True)
    createdAt = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    updatedAt = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())
