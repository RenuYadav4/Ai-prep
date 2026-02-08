from app.database.database import engine
from app.base import Base

from app.models import(
    user,
    resume,
    answer_evaluation,
    company,
    job_description,
    PreparationSession,
    questions,
)

def init_db():
    print("Initializing databse...")
    Base.metadata.create_all(bind = engine)
    print("All tables are created successfully")

if __name__ == "__main__":
    init_db()
