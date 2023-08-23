from sqlalchemy.orm import exc, Query
from dao.dao import PhoneDAO
from dao.models import Phone
from services.utils import get_data, get_data_for_update, add_phone_code
from views.phones_view import view_by_search, update_success, phone_not_found, delete_success, create_success


class PhoneService:
    def __init__(self, dao: PhoneDAO):
        self.dao = dao

    def get_all(self) -> Query:
        phones = self.dao.get_all()
        return phones

    def get_by_id(self, id: int) -> Phone:
        return self.dao.get_by_id(id)

    def get_by_surname(self, surname: str) -> Query:
        phones = self.dao.get_by_surname(surname)
        view_by_search(phones)
        return phones

    def get_by_company(self, company: str) -> Query:
        phones = self.dao.get_by_company(company)
        view_by_search(phones)
        return phones

    def get_by_surname_and_company(self, surname: str, company: str) -> Query:
        phones = self.dao.get_by_surname(surname)
        phones = self.dao.get_by_company(company=company, phones=phones)
        view_by_search(phones)
        return phones

    def create_phone(self) -> None:
        data = get_data()
        add_phone_code(data, 'phone_work')
        add_phone_code(data, 'phone_private')
        self.dao.create_phone(**data)
        create_success()

    def update_phone(self, id: int) -> None:
        data = get_data_for_update(get_data())
        if 'phone_work' in data:
            add_phone_code(data, 'phone_work')
        if 'phone_private' in data:
            add_phone_code(data, 'phone_private')
        try:
            self.dao.update_phone(id=id, **data)
            update_success()
        except exc.UnmappedInstanceError:
            phone_not_found()

    def delete_phone(self, id: int) -> None:
        try:
            self.dao.delete_phone(id)
            delete_success()
        except exc.UnmappedInstanceError:
            phone_not_found()
