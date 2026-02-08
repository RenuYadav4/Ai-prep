from sqlalchemy import Column, Integer, String, ForeignKey   #type: ignore
from sqlalchemy.orm import relationship   #type: ignore
from app.base import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question_text = Column(String, nullable=False)

    preparation_session_id = Column(
        Integer, ForeignKey("preparation_sessions.id")
    )

    preparation_session = relationship(
        "PreparationSession", back_populates="questions"
    )

    answer = relationship(
        "AnswerEvaluation",
        back_populates="question",
        uselist=False
    )
