from fastapi import FastAPI

from database import repo_dependency
from services.note_service import NoteService

app = FastAPI()


@app.get("/healthy")
async def healthy():
    return {"healthy": True}


@app.post("/create-note")
async def create_note(title: str, content: str, priority: int, repo: repo_dependency):
    service = NoteService(repo)
    note = await service.create_note(title, content, priority)
    return note.dict()
