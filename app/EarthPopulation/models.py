from sqlalchemy import Column, Integer, String, BigInteger

from .db import Base

class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    population = Column(Integer, nullable=False)
    region = Column(String, nullable=False)