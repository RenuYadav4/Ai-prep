from sqlalchemy import Column, Integer,String   #type: ignore
from sqlalchemy.orm import relationship #type: ignore
from app.base import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    sessions = relationship("PreparationSession", back_populates="company")
