from app.database.database import SessionLocal
from sqlalchemy.orm import Session #type: ignore
from typing import Generator

def get_db() -> Generator[Generator,None,None]:
    db=SessionLocal()
    try:
        yield db
    finally: 
        db.close()
        