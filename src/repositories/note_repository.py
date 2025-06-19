from abc import ABC, abstractmethod
from typing import Optional

from models.schemas.note import Note


class NoteRepository(ABC):

    @abstractmethod
    async def add_note(self, note: Note) -> Optional[Note]:
        pass
