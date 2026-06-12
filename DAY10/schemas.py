from pydantic import BaseModel
from typing import Optional
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
class TaskUpdate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool
class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool