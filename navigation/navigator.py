from initialize import phone_service, session
from views import phones_view
from views.phones_view import get_pagination_data
from views.table_visualize_and_export import export_csv
from .menu import *
from datetime import datetime


class Navigator:

    def __init__(self):
        self.menu = {"1": self.get_step1,
                     "2": self.search_step1,
                     "3": self.create,
                     "4": self.update_step1,
                     "5": self.delete_step1,
                     "6": self.export_data,
                     "0": self.exit_app}
        self.next_handler = None
        self.state = None
        self.phones = None
        self.search = None

    def get_menu(self):
        self.get_handler(MENU, self.menu)

    def get_handler(self, menu: str, menu_dict: dict, **kwargs):
        print(menu)
        menu_dict = menu_dict
        choice = input()
        if choice in menu_dict:
            self.next_handler = menu_dict[choice]
            if self.next_handler:
                self.next_handler(**kwargs)
        else:
            self.command_not_found()

    def get_step1(self):
        if not self.phones:
            self.phones = phone_service.get_all()
        phone_pages = get_pagination_data(self.phones)
        print(f"Всего страниц: {phone_pages.page_count}")
        read_menu = {"1": self.get_step2,
                     "2": None}
        self.get_handler(READ_MENU, read_menu)

    def get_step2(self):
        self.next_handler = self.get_step1
        try:
            choice = input("Введите номер страницы: ")
            phones_view.get_all(self.phones, int(choice))
        except ValueError:
            print("Номер страницы должен быть числом!")

    def create(self):
        phone_service.create_phone()
        self.phones = None
        self.next_handler = None

    def search_step1(self):
        search_menu = {"1": self.search_by_surname,
                       "2": self.search_by_company,
                       "3": self.search_by_surname_and_company,
                       "4": None}
        self.get_handler(SEARCH_MENU, search_menu)

    def search_by_surname(self):
        surname = input("Введите полностью или частично фамилию для поиска\n")
        self.search = phone_service.get_by_surname(surname)
        self.search_next_handler()

    def search_by_company(self):
        company = input("Введите полностью или частично название организации для поиска\n")
        self.search = phone_service.get_by_company(company)
        self.search_next_handler()

    def search_by_surname_and_company(self):
        surname = input("Введите полностью или частично фамилию для поиска\n")
        company = input("Введите полностью или частично название организации для поиска\n")
        self.search = phone_service.get_by_surname_and_company(surname, company)
        self.search_next_handler()

    def search_next_handler(self):
        if self.search.count() == 0:
            self.next_handler = None
        else:
            if self.state == 'delete':
                self.next_handler = self.delete_step2
            elif self.state == 'update':
                self.next_handler = self.update_step2
            else:
                self.next_handler = self.export_search

    def update_step1(self):
        self.state = 'update'
        self.next_handler = self.update_delete_step1

    def delete_step1(self):
        self.state = 'delete'
        self.next_handler = self.update_delete_step1

    def update_delete_step1(self):
        update_delete_menu = {"1": self.update_delete_step2,
                              "2": self.search_step1,
                              "3": None}
        self.get_handler(UPDATE_DELETE_MENU, update_delete_menu)

    def update_delete_step2(self):
        if self.state == 'update':
            self.next_handler = self.update_step2
        else:
            self.next_handler = self.delete_step2
        self.phones = None

    def delete_step2(self):
        self.state = None
        delete_menu = {"1": phone_service.delete_phone,
                       "2": None}
        id = input("Введите id необходимой записи: ")
        phone = phone_service.get_by_id(id)
        print(f'Найдена запись: Фамилия {phone.surname}, Имя {phone.name}')
        self.get_handler(DELETE_MENU, delete_menu, id=id)
        self.phones = None
        self.next_handler = None

    def update_step2(self):
        self.state = None
        update_menu = {"1": phone_service.update_phone,
                       "2": None}
        id = input("Введите id необходимой записи: ")
        phone = phone_service.get_by_id(id)
        print(f'Найдена запись: Фамилия {phone.surname}, Имя {phone.name}')
        self.get_handler(UPDATE_MENU, update_menu, id=id)
        self.phones = None
        self.next_handler = None

    def command_not_found(self):
        print(COMMAND_NOT_FOUND)
        self.next_handler = None
        self.state = None

    def export_data(self):
        if not self.phones:
            self.phones = phone_service.get_all()
        export_csv(self.phones, 'phones.csv')
        self.next_handler = None
        self.search = None

    def export_search(self):
        export_search_menu = {"1": export_csv,
                              "2": None}
        self.get_handler(EXPORT_SEARCH_MENU, export_search_menu,
                         phones=self.search,
                         filename=f'search {datetime.now()}')
        self.next_handler = None

    def exit_app(self):
        self.export_data()
        session.close()
        exit()
