from app.database.database import engine
from app.base import Base
from app.models import *

# importing them here only created the table not connected yet, for that these will also imported when first db query happens
# because when api runs, init_db is not executed
# Models must be imported during app startup, not just during DB init
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
