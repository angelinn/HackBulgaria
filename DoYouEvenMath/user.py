from sqlalchemy import Column, Integer, String
from connection import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    score = Column(Integer)
