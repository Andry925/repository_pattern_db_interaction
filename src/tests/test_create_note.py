import pytest

from repositories.in_memory_note_repository import InMemoryNoteRepository
from services.note_service import NoteService


@pytest.mark.asyncio
async def test_create_note():
    repo = InMemoryNoteRepository()
    service = NoteService(repo)

    note = await service.create_note("Super Note", "test sample", 2)

    assert note.id == 1
    assert note.title == "Super Note"
    assert note.content == "test sample"
    assert note.priority == 2

    assert len(repo._notes) == 1
