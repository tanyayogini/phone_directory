def get_data() -> dict:
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    secondname = input("Введите отчество: ")
    company = input("Введите название организации: ")
    phone_work = input("Введите рабочий телефон (только цифры): +7")
    phone_private = (input("Введите рабочий телефон (только цифры): +7"))

    data = {'surname': surname,
            'name': name,
            'secondname': secondname,
            'company': company,
            'phone_work': phone_work,
            'phone_private': phone_private}

    return data


def get_data_for_update(data: dict) -> dict:
    data = {key: data[key] for key in data if data[key] != ''}
    return data


def add_phone_code(data: dict, key: str) -> dict:
    data[key] = '7' + data[key]
    return data
