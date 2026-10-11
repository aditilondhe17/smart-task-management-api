
from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False, index=True)
    description = Column(Text, nullable=True)
    status = Column(String(20), nullable=False, default="pending")
    priority = Column(String(20), nullable=False, default="medium")
