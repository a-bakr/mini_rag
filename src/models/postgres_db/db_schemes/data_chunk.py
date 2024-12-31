from sqlalchemy import Index, Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from db_schemes import SQLAlchemyBase
from pydantic import BaseModel
import uuid
 
class DataChunk(SQLAlchemyBase):

    __tablename__ = 'chunks'

    chunk_id = Column(Integer, primary_key=True, autoincrement=True)
    chunk_uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)

    chunk_text = Column(String, nullable=False)
    chunk_metadata = Column(JSONB, nullable=True)
    chunk_order = Column(Integer, nullable=False)

    chunk_project_id = Column(Integer, ForeignKey('project.project_id'), nullable=False)
    chunk_asset_id = Column(Integer, ForeignKey('asset.asset_id'), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

    project = relationship('project', back_populates='chunks')
    asset = relationship('Asset', back_populates='chunks')

    __table_args__ = {
        Index('ix_chunk_project_id', chunk_project_id),
        Index('ix_chunk_asset_id', chunk_asset_id),
    }

    class RetrievedDocument(BaseModel):
        text: str
        score: float