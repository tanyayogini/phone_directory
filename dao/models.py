from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Phone(Base):
    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True, index=True)
    surname = Column(String)
    name = Column(String)
    secondname = Column(String)
    company = Column(String)
    phone_work = Column(String)
    phone_private = Column(String)

