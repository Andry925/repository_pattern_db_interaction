# Overview

The Repository Pattern is a design pattern that acts as an intermediary between your application’s business logic and its data layer.  
It abstracts data access, making your code cleaner, more testable, and easier to maintain.

In my case, it allows business logic to be decoupled from SQLAlchemy’s `Session` or any database-specific implementation.  
This helps in:

- Switching to another database (e.g., MongoDB) without rewriting all business logic
- Writing unit tests without dealing with an actual database
- Improving modularity and separation of concerns

---

### Problem Without Repository Pattern

- Business logic depends directly on SQLAlchemy’s `Session`
- Switching to another backend requires rewriting service logic
- Unit testing requires mocking SQLAlchemy sessions — often complex

---

## Repository Design Pattern Components

### 1. `NoteRepository`  
Abstract base class defining the interface for all repositories. 
https://github.com/Andry925/repository_pattern_db_interaction/blob/main/src/repositories/note_repository.py


### 2. `InMemoryNoteRepository`  
Concrete implementation for testing. Stores notes in memory using a list.
https://github.com/Andry925/repository_pattern_db_interaction/blob/main/src/repositories/in_memory_note_repository.py

### 3. `NoteService`  
Contains application business logic and uses the repository to persist notes.
https://github.com/Andry925/repository_pattern_db_interaction/blob/main/src/services/note_service.py

### 4. `RepoDependency`  
FastAPI dependency that injects the repository into endpoints.
https://github.com/Andry925/repository_pattern_db_interaction/blob/main/src/database.py

### 5. `Endpoint - main.py`  
Exposes a `/create-note` endpoint using FastAPI.
https://github.com/Andry925/repository_pattern_db_interaction/blob/main/src/main.py

---

# How to Run

To build and run the Dockerized FastAPI app:

```bash
docker build -t fastapi-notes-app .
docker run -p 8000:8000 fastapi-notes-app
```

The app will be available at:

```
http://localhost:8000/docs
```

---

# Tests

To ensure the code works correctly, I used `pytest` for testing:

```bash
pip install pytest pytest-asyncio
pytest test_note_service.py
```

The test verifies that:

- A note is successfully created via `NoteService`
- It is stored correctly inside `InMemoryNoteRepository`
