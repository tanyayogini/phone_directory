import pytest

from dao.dao import PhoneDAO
from tests.conftest import get_session


class TestPhoneDAO:
    @pytest.fixture
    def phone_dao(self, get_session):
        phone_dao = PhoneDAO(get_session)
        phone_dao.create_phone(surname='test_sur',
                               name='test_name',
                               secondname='test',
                               company='test_company',
                               phone_work='79111111111',
                               phone_private='79222222222')
        phone_dao.create_phone(surname='2test_sur',
                               name='2test_name',
                               secondname='2test',
                               company='2test_company',
                               phone_work='793333333333',
                               phone_private='79444444444')
        return phone_dao

    def test_get_all(self, phone_dao):
        assert phone_dao.get_all().count() == 2

    def test_get_by_id(self, phone_dao):
        assert phone_dao.get_by_id(1).surname == 'test_sur'

    def test_get_by_surname(self, phone_dao):
        assert phone_dao.get_by_surname('2').count() == 1
        assert phone_dao.get_by_surname('2').first().company == '2test_company'
        assert phone_dao.get_by_surname('test').count() == 2
        assert phone_dao.get_by_surname('Test').count() == 2

    def test_create_phone(self, phone_dao):
        phone_dao.create_phone(surname='3test_sur',
                               name='3test_name',
                               secondname='3test',
                               company='3test_company',
                               phone_work='79555555555',
                               phone_private='79666666666')

        assert phone_dao.get_all().count() == 3
        assert phone_dao.get_by_id(3).surname == '3test_sur'
        assert phone_dao.get_by_id(3).phone_work == '79555555555'

    def test_phone_update(self, phone_dao):
        phone_dao.update_phone(id=2, surname='2update_surname')
        assert phone_dao.get_by_id(2).surname == '2update_surname'
        assert phone_dao.get_by_id(2).name == '2test_name'

    def test_phone_delete(self, phone_dao):
        phone_dao.delete_phone(2)
        assert phone_dao.get_all().count() == 1
