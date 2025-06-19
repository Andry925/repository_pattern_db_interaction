from typing import Optional

from pydantic import BaseModel


class Note(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    priority: int

    class Config:
        orm_mode = True
