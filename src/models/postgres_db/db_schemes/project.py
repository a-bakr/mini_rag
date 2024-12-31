from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from db_schemes import SQLAlchemyBase
import uuid
 

class Project(SQLAlchemyBase):
    __tablename__ = 'project'

    project_id = Column(Integer, primary_key=True, autoincrement=True)
    project_uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

    chunks = relationship("DataChunk", back_populates='project')
    assets = relationship("Asset", back_populates='project')