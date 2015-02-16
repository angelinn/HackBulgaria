from connection import Base
from sqlalchemy import Column, Integer, String, Float, Boolean


class Page(Base):
    __tablename__ = 'page'

    id = Column(Integer, primary_key=True)
    website = Column(String)
    url = Column(String)
    title = Column(String)
    description = Column(String)
    ads = Column(Integer)
    SSL = Column(Boolean)
    multi_lang = Column(Boolean)
    points = Column(Integer)
