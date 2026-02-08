from sqlalchemy import Column, Integer, ForeignKey, DateTime, String  #type: ignore
from sqlalchemy.orm import relationship #type: ignore
from datetime import datetime  #type: ignore
from app.base import Base 

class PreparationSession(Base):
    __tablename__ = "preparation_sessions"

    id =  Column(Integer, primary_key = True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    resume_id = Column(Integer, ForeignKey("resumes.id"), nullable=True)
    jd_id = Column(Integer, ForeignKey("job_descriptions.id"), nullable=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=True)

    created_at = Column(DateTime, default = datetime.utcnow)

    user = relationship("User", back_populates = "preparation_sessions")
    company = relationship("Company", back_populates="preparation_sessions")

    questions = relationship(
        "Question",
        back_populates="preparation_session",
        cascade="all, delete"
    )