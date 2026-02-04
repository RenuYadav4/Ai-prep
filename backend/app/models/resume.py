from sqlalchemy import Column, Integer, Text, ForeignKey   #type: ignore
from sqlalchemy.orm import relationship  #type: ignore
from app.models.base import Base

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable = False)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete = "CASCADE"),
        unique = True,
    )

    user = relationship("User", back_populates = "resume")