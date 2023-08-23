from unittest.mock import Mock

from services.utils import get_data, get_data_for_update, add_phone_code


def test_get_data_for_update():
    data = {'surname': 'test_sur',
            'name': 'test_name',
            'secondname': 'test',
            'company': 'test_company',
            'phone_work': '79111111111',
            'phone_private': '79222222222'}

    data2 = {'surname': 'test_sur',
            'secondname': 'test',
            'company': 'test_company',
            'phone_private': '79222222222'}

    assert len(get_data_for_update(data).keys()) == 6
    assert len(get_data_for_update(data2).keys()) == 4

def test_add_phone_code():
    data = {'surname': 'test_sur',
            'name': 'test_name',
            'secondname': 'test',
            'company': 'test_company',
            'phone_work': '9111111111',
            'phone_private': '9222222222'}
    assert add_phone_code(data, 'phone_work')['phone_work'] == '79111111111'




