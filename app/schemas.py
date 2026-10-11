
from typing import Literal

from pydantic import BaseModel, Field


TaskStatus = Literal["pending", "in_progress", "completed"]
TaskPriority = Literal["low", "medium", "high"]


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=150)
    description: str = ""
    status: TaskStatus = "pending"
    priority: TaskPriority = "medium"


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=150)
    description: str | None = None
    status: TaskStatus | None = None
    priority: TaskPriority | None = None


class TaskRead(BaseModel):
    id: int
    title: str
    description: str
    status: TaskStatus
    priority: TaskPriority

    class Config:
        from_attributes = True
