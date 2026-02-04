from sqlalchemy import create_engine  #type: ignore
from sqlalchemy.orm import sessionmaker, declarative_base   #type: ignore
from app.core.config import serrings


# create engine
engine = create_engine(
    settings.DATABASE_URL,     #type: ignore
    pool_pre_ping = True

)

# create session
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush =False,
    bind = engine 
)

# Base class for models (this is the database model not pydantic)
# Base = declarative_base()



