from paginate_sqlalchemy import SqlalchemyOrmPage
from sqlalchemy.orm import Query

from views.table_visualize_and_export import create_prettytable


def get_pagination_data(phones: Query) -> SqlalchemyOrmPage:
    phones_page = SqlalchemyOrmPage(phones, page=1, items_per_page=5)
    return phones_page


def get_all(phones: Query, page: int = 1) -> None:
    page_count = get_pagination_data(phones).page_count
    if page <= page_count:
        page = SqlalchemyOrmPage(phones, page=page, items_per_page=5)
        print(create_prettytable(page))
        print(f"_____________________________\n"
              f"Показана страница {page.page}\n"
              f"______________________________")
    else:
        print("____________________\n"
              "Страница не найдена!\n"
              "____________________")


def view_by_search(phones: Query) -> None:
    if phones.count() > 0:
        print(create_prettytable(phones))
    else:
        print("___________________________________\n"
              "По Вашему запросу ничего не найдено\n"
              "_____________________________________")


def create_success() -> None:
    print("______________________\n"
          "Запись успешно создана\n"
          "______________________")
def update_success() -> None:
    print("________________\n"
          "Запись обновлена\n"
          "________________\n")

def delete_success() -> None:
    print("________________\n"
          "Запись удалена\n"
          "________________\n")


def phone_not_found() -> None:
    print("____________________________\n"
          "Запись с таким id не найдена\n"
          "____________________________")
