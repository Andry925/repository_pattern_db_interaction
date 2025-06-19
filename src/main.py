from fastapi import FastAPI

from database import init_db

app = FastAPI()


@app.get("/healthy")
async def healthy():
    return {"healthy": True}


@app.on_event("startup")
async def on_startup():
    await init_db()
