import pytest

from services.phone_service import PhoneService


class TestPhoneService:
    @pytest.fixture
    def phone_service(self, get_dao):
        return PhoneService(get_dao)

    def test_get_all(self, phone_service, create_phones):
        assert phone_service.get_all().count() == 2

    def test_get_by_surname(self, phone_service, create_phones):
        assert phone_service.get_by_surname('test').count() == 2
        assert phone_service.get_by_surname('2test').count() == 1

    def test_delete(self, phone_service, create_phones):
        phone_service.delete_phone(1)
        assert phone_service.get_all().count() == 1
