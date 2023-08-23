from navigation.navigator import Navigator

navigator = Navigator()

if __name__ == '__main__':
    print('Приветствуем в приложении "Телефонный справочник". ')
    print('________________________________________________')
    while True:
        if navigator.next_handler:
            navigator.next_handler()
        else:
            navigator.get_menu()
