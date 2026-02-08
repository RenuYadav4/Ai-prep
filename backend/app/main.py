from fastapi import FastAPI #type: ignore
from sqlalchemy import text #type: ignore
from app.core.database import engine

app = FastAPI(title="AI prep Platform1")

@app.get("/")
def welcome():
    return {"status":"ok"}