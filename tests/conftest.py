from unittest.mock import MagicMock

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from dao.dao import PhoneDAO
from dao.models import Base
from services.phone_service import PhoneService


@pytest.fixture
def get_session():
    engine = create_engine('sqlite:///test.db')
    Base.metadata.create_all(engine)
    engine.connect()
    session = Session(bind=engine)
    yield session
    session.close()
    Base.metadata.drop_all(engine)

@pytest.fixture
def get_dao(get_session):
    phone_dao = PhoneDAO(session=get_session)
    return phone_dao

@pytest.fixture
def get_service(get_dao):
    return PhoneService(dao=get_dao)

@pytest.fixture
def create_phones(get_dao):
    get_dao.create_phone(surname='test_sur',
              name='test_name',
              secondname='test',
              company='test_company',
              phone_work='79111111111',
              phone_private='79222222222')

    get_dao.create_phone(surname='2test_sur',
                         name='2test_name',
                         secondname='2test',
                         company='2test_company',
                         phone_work='79333333333',
                         phone_private='79444444444')
    return
