from typing import Optional, List

from models.schemas.note import Note
from repositories.note_repository import NoteRepository


class InMemoryNoteRepository(NoteRepository):
    def __init__(self):
        self._notes: List[Note] = []
        self._id_counter = 1

    async def add_note(self, note: Note) -> Optional[Note]:
        note.id = self._id_counter
        self._id_counter += 1
        self._notes.append(note)
        return note
