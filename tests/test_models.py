import pytest
from dao.models import Phone

phone = Phone(surname='test_sur',
              name='test_name',
              secondname='test',
              company='test_company',
              phone_work='79111111111',
              phone_private='79222222222')


def test_phone_model():
    assert phone.surname == 'test_sur'
    assert phone.name == 'test_name'
    assert phone.company == 'test_company'
    assert phone.phone_private == '79222222222'
