from models.schemas.note import Note
from repositories.note_repository import NoteRepository


class NoteService:
    def __init__(self, repo: NoteRepository):
        self.repo = repo

    async def create_note(self, title: str, content: str, priority: int) -> Note:
        note = Note(title=title, content=content, priority=priority)
        return await self.repo.add_note(note)
