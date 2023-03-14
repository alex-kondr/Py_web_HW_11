from fastapi import FastAPI, Path, Query, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from db import get_db, Note


app = FastAPI()


@app.get("/api/healthchecker", name="Ababgalamaga")
async def healthchecker(db: Session = Depends(get_db)):
    
    try:
        result = db.execute(text("SELECT 1")).fetchone()
        
        if result is None:
            raise HTTPException(status_code=500, detail="DB not conf")
        
        return {"message": result[0]}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error {e}")


class NoteModel(BaseModel):
    name: str
    description: str
    done: bool
    

@app.post("/notes")
async def create_note(note: NoteModel, db: Session = Depends(get_db)):
    new_note = Note(name=note.name, description=note.description, done=note.done)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


