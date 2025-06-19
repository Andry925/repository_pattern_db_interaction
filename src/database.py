from typing import Annotated

from fastapi import Depends
from repositories.in_memory_note_repository import InMemoryNoteRepository

from repositories.note_repository import NoteRepository


def get_repo() -> NoteRepository:
    return InMemoryNoteRepository()


repo_dependency = Annotated[NoteRepository, Depends(get_repo)]
