from connection import Base
from sqlalchemy import Column, Integer, String, Float


class Website(Base):
    __tablename__ = 'website'

    id = Column(Integer, primary_key=True)
    url = Column(String)
    title = Column(String)
    domain = Column(String)
    pages_count = Column(Integer)
    HTML_version = Column(Float)
