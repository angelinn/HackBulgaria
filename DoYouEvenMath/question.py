from connection import Base
from sqlalchemy import Column, Integer, String, Float


class Question(Base):
    __tablename__ = 'question'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(Float)
