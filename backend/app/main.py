from fastapi import FastAPI #type: ignore
from sqlalchemy import text #type: ignore
from app.database.database import engine
from app.routes.auth import router as auth_router

app = FastAPI(title="AI prep Platform1")

app.include_router(auth_router)

@app.get("/")
def welcome():
    return {"status":"ok"}