import csv
from prettytable import PrettyTable
from sqlalchemy.orm import Query


FIELD_TITLE = [
        "id",
        "Фамилия",
        "Имя",
        "Отчество",
        "Название организации",
        "Рабочий телефон",
        "Личный телефон"]


def visualize_phone(phone: str) -> str:
    return f"+{phone[0]}({phone[1:4]}){phone[4:7]}-{phone[7:9]}-{phone[9:]}"


def get_table_rows(phones: Query) -> list[list]:
    result = []
    for phone in phones:
        result.append(
            [phone.id,
             phone.surname,
             phone.name,
             phone.secondname,
             phone.company,
             visualize_phone(phone.phone_work),
             visualize_phone(phone.phone_private)])
    return result


def create_prettytable(phones: Query) -> PrettyTable:
    phone_table = PrettyTable()
    phone_table.field_names = FIELD_TITLE

    phone_table.add_rows(get_table_rows(phones))
    return phone_table


def export_csv(phones: Query, filename: str) -> None:
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(FIELD_TITLE)
        writer.writerows(get_table_rows(phones))
    print("__________________________\n"
          "Файл успешно экспортирован.\n"
          "___________________________\n")


