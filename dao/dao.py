from sqlalchemy.orm import Session, Query

from dao.models import Phone


class PhoneDAO:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> Query:
        phones = self.session.query(Phone).order_by('surname')
        return phones

    def get_by_id(self, id: int) -> Phone:
        phone = self.session.query(Phone).get(id)
        return phone

    def get_by_surname(self, surname: str, phones: list[Phone] = None) -> Query:
        if not phones:
            phones = self.session.query(Phone).filter(Phone.surname.ilike(f'%{surname}%')).order_by('surname')
        else:
            phones = phones.filter(Phone.surname.ilike(f'%{surname}%'))
        return phones

    def get_by_company(self, company: str, phones: list[Phone] = None) -> Query:
        if not phones:
            phones = self.session.query(Phone).filter(Phone.company.ilike(f'%{company}%')).order_by('surname')
        else:
            phones = phones.filter(Phone.company.ilike(f'%{company}%'))
        return phones

    def create_phone(self, **kwargs) -> None:
        phone = Phone(**kwargs)
        self.session.add(phone)
        self.session.commit()

    def update_phone(self, **kwargs) -> None:
        phone = self.get_by_id(kwargs['id'])
        if 'surname' in kwargs:
            phone.surname = kwargs['surname']
        if 'name' in kwargs:
            phone.name = kwargs['name']
        if 'secondname' in kwargs:
            phone.secondname = kwargs['secondname']
        if 'company' in kwargs:
            phone.company = kwargs['company']
        if 'phone_work' in kwargs:
            phone.phone_work = kwargs['phone_work']
        if 'phone_private' in kwargs:
            phone.phone_private = kwargs['phone_private']
        self.session.add(phone)
        self.session.commit()

    def delete_phone(self, id: int) -> None:
        phone = self.get_by_id(id)
        self.session.delete(phone)
        self.session.commit()
