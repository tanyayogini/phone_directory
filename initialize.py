from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from dao.dao import PhoneDAO
from dao.models import Base
from db_config import SQLALCHEMY_DATABASE_URI
from services.phone_service import PhoneService

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Base.metadata.create_all(engine)
engine.connect()
session = Session(bind=engine)

phone_dao = PhoneDAO(session=session)
phone_service = PhoneService(dao=phone_dao)
