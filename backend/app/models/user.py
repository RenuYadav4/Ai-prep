from sqlalchemy import Column, Integer, String  #type: ignore
from sqlalchemy.orm import relationship   #type: ignore
from app.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index = True)
    email = Column(String, unique = True, nullable = False, index = True)
    password = Column(String, nullable = False)


    # one to one relationship
    resume = relationship(
        "Resume",
        back_populates = "user",
        uselist = False,
        cascade = "all, delete"
    )

    job_description = relationship(
        "JobDescription",
        back_populates = "user",
        uselist = False,
        cascade = "all, delete"
    )
  
    sessions = relationship ("PreparationSession", back_populates = "user")